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
            'format': 'bestvideo[ext=mp4][vcodec^=avc1]+bestaudio[ext=m4a]/mp4',  # Force H.264 (AVC1)
            'outtmpl': os.path.join(download_dir, '%(title)s.%(ext)s'),
            'merge_output_format': 'mp4',  # Ensure output is in MP4
            'progress_hooks': [progress_hook],
            'retries': 5,  # Retry in case of failure
            'timeout': 60,  # Timeout for requests
        }

        # Update the status label to indicate the start of the download
        status_label.config(text="")
        root.update()
        status_label.config(text="Starting download...")
        root.update()

        progress_bar["value"] = 0

        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        # Update the status label to indicate completion
        status_label.config(text="")
        root.update()
        status_label.config(text="Download Completed!")
        root.update()

        messagebox.showinfo("Success", f"Video downloaded successfully to {download_dir}")

    except Exception as e:
        # Handle exceptions and update the status label
        messagebox.showerror("Error", f"An error occurred: {e}")
        status_label.config(text="")
        root.update()
        status_label.config(text="Error occurred during download.")
        root.update()
    finally:
        progress_bar.stop()

def progress_hook(d):
    """Hook to update progress bar and status label during download."""
    if d['status'] == 'downloading':
        percentage_str = d.get('_percent_str', '0.0%')
        # Remove any ANSI color codes
        percentage_clean = re.sub(r'\x1b\[[0-9;]*m', '', percentage_str).strip('%')

        try:
            percentage = float(percentage_clean)
            progress_bar["value"] = percentage
        except ValueError:
            pass

        root.update()

    elif d['status'] == 'finished':
        status_label.config(text="")
        root.update()
        status_label.config(text="Download finished. Finalizing...")
        root.update()

# ------------------ GUI Setup ------------------

root = tk.Tk()
root.title("Video Downloader")
root.geometry("500x250")
root.resizable(False, False)

# Set the overall GUI background to black
root.configure(bg="black")

# Create a style for ttk widgets
style = ttk.Style()
style.theme_use("clam")

# Style for the Download Button
style.configure(
    "Custom.TButton",
    foreground="white",
    background="#444444",  # Dark gray button
    font=("Arial", 14, "bold"),
    borderwidth=0
)
# Change button color on hover/active
style.map(
    "Custom.TButton",
    background=[("active", "#666666")]
)

# Style for the Progress Bar
style.configure(
    "Custom.Horizontal.TProgressbar",
    troughcolor="#333333",   # Dark gray trough
    bordercolor="#333333",
    background="#00FF00",    # Bright green progress
    lightcolor="#00FF00",
    darkcolor="#00FF00",
    thickness=20
)

# ------------------ GUI Widgets ------------------

# URL Label
url_label = tk.Label(
    root,
    text="Video URL:",
    fg="white",
    bg="black",
    font=("Arial", 14)
)
url_label.pack(pady=5)

# URL Entry
url_entry = tk.Entry(
    root,
    width=50,
    font=("Arial", 12),
    bg="#222222",
    fg="white",
    insertbackground="white"  # Cursor color
)
url_entry.pack(pady=5)

# Download Button (using custom style)
download_button = ttk.Button(
    root,
    text="Download",
    style="Custom.TButton",
    command=download_video
)
download_button.pack(pady=10)

# Progress Bar (using custom style)
progress_bar = ttk.Progressbar(
    root,
    orient="horizontal",
    mode="determinate",
    length=400,
    style="Custom.Horizontal.TProgressbar"
)
progress_bar.pack(pady=10)

# Status Label
status_label = tk.Label(
    root,
    text="Enter a video URL and press 'Download'",
    fg="white",
    bg="black",
    font=("Arial", 14)
)
status_label.pack(pady=5)

# ------------------ Mainloop ------------------
root.mainloop()
