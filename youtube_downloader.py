import ttkbootstrap as ttkb
from ttkbootstrap.constants import *
from tkinter import filedialog, messagebox
import yt_dlp
import subprocess
import os
import re
import threading

last_folder = None
last_downloaded_file = None

def fetch_video_qualities(url):
    try:
        with yt_dlp.YoutubeDL({'quiet': True}) as ydl:
            info = ydl.extract_info(url, download=False)
            formats = info.get('formats', [])
            video_qualities = sorted({f['height'] for f in formats if f.get('vcodec') != 'none' and f.get('height')})
            return [f"{q}p" for q in video_qualities]
    except Exception as e:
        messagebox.showerror("Lỗi", f"Không lấy được độ phân giải từ URL:\n{str(e)}")
        return []

def update_quality_options(*args):
    url = url_var.get().strip()
    if type_var.get() == "MP3":
        quality_menu['values'] = ['128', '192']
        quality_var.set('192')
    elif url:
        qualities = fetch_video_qualities(url)
        if qualities:
            quality_menu['values'] = qualities
            quality_var.set(qualities[-1])

def progress_hook(d):
    if d['status'] == 'downloading':
        percent_str = d.get('_percent_str', '0')
        percent_clean = re.sub(r'[^\d.]', '', percent_str)
        try:
            p = float(percent_clean)
            progress_var.set(p)
        except:
            pass
    elif d['status'] == 'finished':
        progress_var.set(100)

def start_download():
    global last_folder, last_downloaded_file
    try:
        url = url_var.get().strip()
        kind = type_var.get()
        quality = quality_var.get()

        if not url:
            messagebox.showerror("Lỗi", "Vui lòng nhập URL.")
            return

        folder = filedialog.askdirectory(initialdir=last_folder or os.getcwd())
        if not folder:
            return
        last_folder = folder
        progress_var.set(0)

        ydl_opts = {
            'outtmpl': os.path.join(folder, '%(title)s.%(ext)s'),
            'progress_hooks': [progress_hook],
            'quiet': True,
        }

        if kind == "MP3":
            ydl_opts.update({
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': quality
                }]
            })
        else:
            res_number = ''.join(filter(str.isdigit, quality))
            ydl_opts['format'] = f"bestvideo[height<={res_number}]+bestaudio/best/best"

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            file_path = ydl.prepare_filename(info)
            if kind == 'MP3':
                file_path = os.path.splitext(file_path)[0] + ".mp3"
            last_downloaded_file = file_path

        messagebox.showinfo("✅ Thành công", f"Đã tải {kind} xong!")

    except Exception as e:
        messagebox.showerror("❌ Lỗi", f"Lỗi khi tải: {e}")
        progress_var.set(0)

def start_download_thread():
    threading.Thread(target=start_download, daemon=True).start()

def open_download_folder():
    if last_downloaded_file and os.path.exists(last_downloaded_file):
        subprocess.Popen(f'explorer /select,"{last_downloaded_file}"')
    else:
        messagebox.showinfo("Thông báo", "Chưa có file nào hoặc file đã bị xóa.")

# Giao diện
app = ttkb.Window(themename="flatly")
app.title("🎬 YouTube Downloader")
app.geometry("650x500")

ttkb.Label(app, text="🎬 YouTube Downloader", font=("Segoe UI", 18, "bold")).pack(pady=20)

url_var = ttkb.StringVar()
ttkb.Entry(app, textvariable=url_var, font=("Segoe UI", 11), width=60, bootstyle="info").pack(pady=10, ipady=6)

# Chọn loại file
type_frame = ttkb.Frame(app)
type_frame.pack(pady=10)
type_var = ttkb.StringVar(value="MP3")
ttkb.Label(type_frame, text="Loại tệp:", font=("Segoe UI", 11)).pack(side=LEFT, padx=5)

type_menu = ttkb.Combobox(type_frame, textvariable=type_var, values=["MP3", "MP4"], state="readonly", width=10, bootstyle="secondary")
type_menu.pack(side=LEFT)

# Chọn chất lượng
quality_frame = ttkb.Frame(app)
quality_frame.pack(pady=10)
quality_var = ttkb.StringVar()
ttkb.Label(quality_frame, text="Chất lượng:", font=("Segoe UI", 11)).pack(side=LEFT, padx=5)
quality_menu = ttkb.Combobox(quality_frame, textvariable=quality_var, values=[], state="readonly", width=10, bootstyle="secondary")
quality_menu.pack(side=LEFT)

# Progress bar
progress_var = ttkb.DoubleVar(value=0)
ttkb.Progressbar(app, variable=progress_var, maximum=100, length=500, bootstyle="info-striped").pack(pady=20)

# Nút tải
btn_frame = ttkb.Frame(app)
btn_frame.pack(pady=10)
ttkb.Button(btn_frame, text="⬇️ Tải ngay", command=start_download_thread, bootstyle="success").pack(side=LEFT, padx=10, ipadx=10, ipady=5)
ttkb.Button(btn_frame, text="📂 Mở thư mục đã tải", command=open_download_folder, bootstyle="primary-outline").pack(side=LEFT, padx=10, ipadx=10, ipady=5)

# Gắn sự kiện cập nhật chất lượng khi nhập URL hoặc đổi loại file
url_var.trace_add("write", update_quality_options)
type_var.trace_add("write", update_quality_options)

app.mainloop()
