# Youtube and X Video Downloader

## Overview
This program provides a modern, user-friendly graphical interface (GUI) for downloading videos from YouTube and X/Twitter. It uses yt-dlp for video downloading and features a sleek dark theme interface with video preview capabilities. The program downloads videos in the best available quality and saves them as MP4 files.
Features

Video Preview: Shows thumbnail and title before downloading
Modern Dark Theme Interface: Sleek design with blue accents
Flexible Download Location: Choose where to save your videos
Real-time Progress Tracking: Shows download speed and ETA
Smart Window Sizing: Automatically adjusts to content
Error Handling: Clear error messages and recovery
Downloads from multiple platforms including YouTube and X/Twitter
Automatically merges video and audio streams
Saves videos in MP4 format by default

## How to Use

Launch the program with python video_downloader.py
Enter the video URL in the text box
Click "Download" to fetch video info and start download
Video thumbnail and title will appear
Progress bar shows download status with speed and ETA
Videos are saved in the selected download location (default is Desktop/Video Downloader)

## Requirements

Python 3.6+: Required to run the application
Required Python packages:

yt-dlp: For video downloading
Pillow: For image handling (thumbnails)
tkinter: For the GUI (usually comes with Python)


FFmpeg: Required for merging video and audio streams

Installation

Install Python from python.org
Install required packages:

bashCopypip install yt-dlp pillow

Install FFmpeg:

Windows: Download from ffmpeg.org and add to PATH
Mac: brew install ffmpeg
Linux: sudo apt-get install ffmpeg or equivalent



## Download Options

Custom Save Location: Change download directory anytime
High Quality: Downloads best available quality automatically
Progress Tracking: Shows percentage, speed, and time remaining
Error Recovery: Handles network issues and invalid URLs gracefully

## Troubleshooting
Common Issues

"Loading" stuck:

Check your internet connection
Verify the URL is valid
Try restarting the application


Download fails:

Ensure FFmpeg is properly installed
Check write permissions in download directory
Verify URL is accessible


Window sizing issues:

The window will automatically resize for content
Minimum window size is 800x600
Maximum height is screen height minus 100px



Error Messages

The application provides specific error messages for common issues
Network errors are handled gracefully
Invalid URLs are detected early

## Technical Details
Built with Python's tkinter for GUI
Uses threading for responsive UI during downloads
Implements proper error handling and recovery
Features automatic window management
Uses PIL for image processing

## Icon
The program can include a custom `.ico` file (e.g., `video_downloader_icon.ico`) as the application icon for a more polished look. Place this file in the same directory as the main `.pyw` script and update the Tkinter icon reference in the code if desired.

## Links
- [Python Download](https://www.python.org/downloads/)
- [yt-dlp Documentation](https://github.com/yt-dlp/yt-dlp)
- [Pillow Documentation](https://pillow.readthedocs.io/)
- [FFmpeg Download](https://ffmpeg.org/download.html)

## Contributing
Feel free to submit issues and enhancement requests!

## License
This program is open source and free to use. Please retain credits when modifying or distributing.

Created with ♥ for easy video downloads
---
