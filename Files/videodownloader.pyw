import os
import tkinter as tk
from tkinter import ttk, messagebox
from yt_dlp import YoutubeDL
import re

def download_video():
    url = url_entry.get().strip()
    if not url:
        messagebox.showerror("Error", "Please enter a video URL.")
        return

    # Set up the download directory
    desktop = os.path.join(os.path.expanduser("~"), "Desktop")
    download_dir = os.path.join(desktop, "Video Downloader")
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)

    try:
        # Configure yt-dlp with forced H.264 encoding
        ydl_opts = {
            'format': 'bestvideo[ext=mp4][vcodec^=avc1]+bestaudio[ext=m4a]/mp4',  # Force H.264 (AVC1) codec
            'outtmpl': os.path.join(download_dir, '%(title)s.%(ext)s'),
            'merge_output_format': 'mp4',  # Ensure output is in MP4
            'progress_hooks': [progress_hook],
            'retries': 5,  # Retry in case of failure
            'timeout': 60,  # Timeout for requests
        }

        # Update the status label to indicate the start of the download
        status_label.config(text="Starting download...")
        progress_bar["value"] = 0
        root.update_idletasks()

        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        # Update the status label to indicate completion
        status_label.config(text="Download Completed!")
        messagebox.showinfo("Success", f"Video downloaded successfully to {download_dir}")
    except Exception as e:
        # Handle exceptions and update the status label
        messagebox.showerror("Error", f"An error occurred: {e}")
        status_label.config(text="Error occurred during download.")
    finally:
        progress_bar.stop()

def progress_hook(d):
    if d['status'] == 'downloading':
        # Extract and clean the percentage string
        percentage_str = d.get('_percent_str', '0.0%')
        percentage_clean = re.sub(r'\x1b\[[0-9;]*m', '', percentage_str).strip('%')
        
        try:
            percentage = float(percentage_clean)
            progress_bar["value"] = percentage
        except ValueError:
            pass

        root.update_idletasks()
    elif d['status'] == 'finished':
        status_label.config(text="Download finished. Finalizing...")

# GUI Setup
root = tk.Tk()
root.title("Video Downloader")
root.geometry("500x200")
root.resizable(False, False)

# URL Entry
url_label = tk.Label(root, text="Video URL:")
url_label.pack(pady=5)
url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

# Download Button
download_button = tk.Button(root, text="Download", command=download_video)
download_button.pack(pady=10)

# Progress Bar
progress_bar = ttk.Progressbar(root, orient="horizontal", mode="determinate", length=400)
progress_bar.pack(pady=10)

# Status Label
status_label = tk.Label(root, text="Enter a video URL and press 'Download'")
status_label.pack(pady=5)

# Run the GUI
root.mainloop()
