# 🎬 YouTube Downloader (Python + GUI)

# 🎬 run the software file in the dist folder

A simple yet powerful desktop app to download YouTube videos or audio in your preferred quality. Built with a modern GUI using `ttkbootstrap`, it supports real-time progress display, MP3/MP4 conversion, and can be compiled into a standalone `.exe` file for Windows.

---

## 📌 Features

- ✅ Modern GUI with `ttkbootstrap`
- ✅ Download MP3 (audio) with 128kbps or 192kbps
- ✅ Download MP4 (video) with selectable resolutions (e.g., 360p, 720p, 1080p)
- ✅ Live download progress bar
- ✅ Open download folder after completion
- ✅ Can be bundled into a standalone `.exe` (no Python required)

---

## 🛠️ System Requirements

- **Python**: 3.9.x (recommended for PyInstaller compatibility)
- **pip**: ≥ 21.0
- **OS**: Windows 10/11 (64-bit)
- **FFmpeg**: No need to install separately; handled by `yt-dlp`

---

## 📦 Setup Instructions

```bash
# Step 1: Create project folder
mkdir youtube_downloader
cd youtube_downloader

# Step 2: Create and activate virtual environment
py -3.9 -m venv yt-env
yt-env\Scripts\activate

# Step 3: Install required libraries
pip install yt-dlp ttkbootstrap
```

---

## 🧩 Libraries Used

| Library        | Purpose                           |
|----------------|------------------------------------|
| `yt-dlp`       | Download YouTube videos/audio     |
| `ttkbootstrap` | Modern UI based on tkinter        |
| `tkinter`      | Built-in Python GUI toolkit       |

---

## ▶️ How to Run the App

```bash
# Activate virtual environment
yt-env\Scripts\activate

# Run the app
python youtube_downloader.py
```

After launch:
1. Paste a YouTube URL
2. Select format: MP3 or MP4
3. Choose quality
4. Click "⬇️ Download"

---

## 📁 Project Structure

```
youtube_downloader/
│
├── icon.ico                # Icon for .exe file
├── youtube_downloader.py   # Main Python source file
├── README.md
└── yt-env/                 # Virtual environment folder
```

---

## 💾 Build Standalone `.exe` (Windows)

### 🔧 Step 1: Install PyInstaller

```bash
pip install pyinstaller
```

### 🏗️ Step 2: Build the Executable

```bash
python -m PyInstaller --noconfirm --onefile --windowed --icon=icon.ico youtube_downloader.py
```

### ✅ Output:

- Final executable: `dist/youtube_downloader.exe`
- You can run or share it without needing Python installed

---

## ⚠️ Tips for `.exe` Build

- Ensure `icon.ico` is a valid `.ico` file (not just `.png` renamed)
- Place `icon.ico` in the same folder as `youtube_downloader.py`
- If build fails: delete `build/`, `dist/`, and `.spec` file, then rebuild

---

## 💡 Ideas for Future Improvements

- Playlist or channel downloads
- Clipboard auto-paste for copied links
- Support additional formats (.wav, .m4a, .webm)
- Light/dark theme toggle

---

## 🧑‍💻 Author

- **Name**: [DuOzeNg]
- **GitHub**: [github.com/DangTruongDuong]
- **Contact**: [DangTruongDuong2102@gmail.com] (optional)

---
