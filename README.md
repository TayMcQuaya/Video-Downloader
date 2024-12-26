# Video Downloader Program

## Overview
This program provides a simple graphical user interface (GUI) for downloading videos from YouTube and X/Twitter. It uses [yt-dlp](https://github.com/yt-dlp/yt-dlp) for video downloading and allows users to select a video URL, download it in the best available quality, and save it as an MP4 file. The program also ensures compatibility by forcing H.264 encoding for better playback support across most devices.

## Features
- **Download videos** from YouTube and X/Twitter.
- **Forces H.264** (AVC) encoding for broad compatibility.
- Automatically **merges video and audio streams**.
- **User-friendly GUI** built with `tkinter`:
  - **Black background** and **large white text** for readability.
  - **Custom-styled button** for a more modern look.
  - **Bright green progress bar** showing download progress.
- Videos are **saved as MP4** files by default.
- Progress bar and status messages provide real-time feedback.

## How to Use
1. **Launch** the program by double-clicking the `video_downloader.pyw` file.
2. **Enter** the video URL (YouTube or X/Twitter) in the text box.
3. Click the **Download** button.
4. A progress bar will indicate the **download progress**.
5. Once completed, the video will be **saved in a folder named** `Video Downloader` on your Desktop.

## Requirements
1. [**Python 3.8+**](https://www.python.org/downloads/): Ensure Python is installed on your system.
2. Required Python libraries:
   - **yt-dlp**: For downloading and merging video/audio.
   - **tkinter**: For building the GUI (comes pre-installed with most Python distributions).
   - **pillow**: Optional if you wish to use a custom icon (`.ico` file).
3. [**FFmpeg**](https://ffmpeg.org/download.html) (especially on Windows):
   - Needed to **merge video and audio streams** properly.
   - Make sure it is **added to your system PATH** so `yt-dlp` can find and use it.

### Install Dependencies
Install the required libraries using the following commands:
```bash
pip install yt-dlp pillow
```
> **Note:** `tkinter` typically ships with Python on Windows and macOS. On some Linux distros, it might need separate installation (e.g., `sudo apt-get install python3-tk`).

## Running the Program
1. Place the `video_downloader.pyw` file (and optionally, the `video_downloader_icon.ico`) in the same directory.
2. Ensure **Python** is installed and the **dependencies** listed above are installed.
3. Double-click the `video_downloader.pyw` to launch the GUI.
4. Follow the instructions in the **How to Use** section to download your videos.

## Custom UI Notes
- The main window **background** is set to **black**.
- All **text** is displayed in **white** with larger fonts for better visibility.
- The **Download** button is styled with a **dark-gray background** and **white** text, becoming lighter when hovered.
- The **progress bar** is a **thick green bar** over a dark-gray trough, making it more visible.
- You can easily **modify colors and fonts** in the code to match your preferences by adjusting the `ttk.Style` configurations.

## Troubleshooting
- If the program doesn't open, ensure **Python** is installed and properly associated with `.pyw` files.
- If video downloads fail or produce unsupported formats:
  - Check your **internet connection**.
  - Ensure **FFmpeg** is installed and configured in your PATH.
  - Verify that the **video URL** is valid.
- If you encounter any **visual display issues** (like text not updating), try installing an updated version of Python and using the included `root.update()` calls or separate threads to handle lengthy downloads.
- For **AV1 codec issues** (or if you specifically need older H.264 compatibility), verify you have the latest script version that **forces H.264** encoding.

## Icon
The program can include a custom `.ico` file (e.g., `video_downloader_icon.ico`) as the application icon for a more polished look. Place this file in the same directory as the main `.pyw` script and update the Tkinter icon reference in the code if desired.

## Links
- [Python Download](https://www.python.org/downloads/)
- [yt-dlp Documentation](https://github.com/yt-dlp/yt-dlp)
- [Pillow Documentation](https://pillow.readthedocs.io/)
- [FFmpeg Download](https://ffmpeg.org/download.html)

## License
This program is open source and free to use for personal projects. If you modify or distribute it, please retain the original credits.

---

Enjoy your video downloader with ease!