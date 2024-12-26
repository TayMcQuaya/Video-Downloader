# Video Downloader Program

## Overview
This program provides a simple graphical user interface (GUI) for downloading videos from YouTube and X/Twitter. It uses `yt-dlp` for video downloading and allows users to select a video URL, download it in the best available quality, and save it as an MP4 file. The program also ensures compatibility by forcing H.264 encoding.

## Features
- Download videos from YouTube and X/Twitter.
- Saves videos in MP4 format with H.264 encoding.
- Automatically merges video and audio streams.
- User-friendly GUI built with `tkinter`.
- Progress bar to show download progress.

## How to Use
1. Run the program by double-clicking the `video_downloader.pyw` file.
2. Enter the video URL (YouTube or X/Twitter) in the text box.
3. Click the **Download** button.
4. The video will be saved in a folder named `Video Downloader` on your Desktop.

## Requirements
This program requires Python and the following dependencies:

1. [Python 3.8+](https://www.python.org/downloads/): Ensure Python is installed on your system.
2. Required Python libraries:
   - `yt-dlp`: For video downloading and merging.
   - `tkinter`: For building the GUI (comes pre-installed with Python on most platforms).
   - `Pillow`: For handling image formats like `.ico` (optional for the icon).

### Install Dependencies
Install the required libraries using the following commands:
```bash
pip install yt-dlp pillow
```

For Windows, you may also need `ffmpeg`:
- [Download ffmpeg](https://ffmpeg.org/download.html)
- Add `ffmpeg` to your system PATH for proper merging of video and audio streams.

## Running the Program
1. Place the program file (`video_downloader.pyw`) and the `video_downloader_icon.ico` in the same directory.
2. Ensure Python is installed on your system and all dependencies are installed.
3. Double-click the `video_downloader.pyw` file to launch the program.
4. Follow the steps in the **How to Use** section to download your videos.

## Troubleshooting
- If the program doesn't open, ensure Python is properly installed and associated with `.pyw` files.
- If video downloads fail or produce unsupported formats:
  - Check your internet connection.
  - Ensure `ffmpeg` is installed and configured.
  - Verify that the video URL is valid.
- For AV1 codec issues, ensure you are using the updated version of the script to force H.264 encoding.

## Icon
The program includes a custom `.ico` icon for the GUI. You can use the provided `video_downloader_icon.ico` file as the application icon for a better visual experience.

## Links
- [Python Download](https://www.python.org/downloads/)
- [yt-dlp Documentation](https://github.com/yt-dlp/yt-dlp)
- [Pillow Documentation](https://pillow.readthedocs.io/)
- [FFmpeg Download](https://ffmpeg.org/download.html)

## License
This program is open source and free to use for personal projects. If you modify or distribute it, please retain the credits.

---

Enjoy downloading videos with ease!

