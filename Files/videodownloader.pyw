import os
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from yt_dlp import YoutubeDL
import re
import json
import urllib.request
from PIL import Image, ImageTk
from io import BytesIO
import threading
import time

class VideoDownloaderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Youtube & X Video Downloader")
        self.root.geometry("800x600")
        self.root.configure(bg="#1E1E1E")
        
        # Set minimum window size
        self.root.minsize(800, 600)
        
        # Initialize download directory
        self.download_dir = os.path.join(os.path.expanduser("~"), "Desktop", "Video Downloader")
        
        # Create main container
        self.main_frame = tk.Frame(self.root, bg="#1E1E1E")
        self.main_frame.pack(expand=True, fill='both', padx=20, pady=20)
        
        # Create separate frames for different sections
        self.input_frame = tk.Frame(self.main_frame, bg="#1E1E1E")
        self.input_frame.pack(fill='x', pady=(0, 10))
        
        self.directory_frame = tk.Frame(self.main_frame, bg="#1E1E1E")
        self.directory_frame.pack(fill='x', pady=(0, 10))
        
        self.preview_frame = tk.Frame(self.main_frame, bg="#1E1E1E")
        self.preview_frame.pack(fill='both', expand=True, pady=(0, 10))
        
        self.control_frame = tk.Frame(self.main_frame, bg="#1E1E1E")
        self.control_frame.pack(fill='x', side='bottom', pady=(10, 0))
        
        # Initialize image references
        self.current_photo = None
        self.thumbnail_label = None
        
        self.setup_styles()
        self.create_widgets()
        self.reset_preview()

    def setup_styles(self):
        style = ttk.Style()
        style.theme_use("clam")
        
        style.configure(
            "Custom.TButton",
            foreground="white",
            background="#007AFF",
            font=("Helvetica", 12, "bold"),
            borderwidth=0,
            padding=10
        )
        style.map(
            "Custom.TButton",
            background=[("active", "#0051FF")],
            foreground=[("active", "white")]
        )
        
        style.configure(
            "Custom.Horizontal.TProgressbar",
            troughcolor="#2D2D2D",
            bordercolor="#2D2D2D",
            background="#007AFF",
            lightcolor="#007AFF",
            darkcolor="#007AFF",
            thickness=15
        )

    def create_widgets(self):
        # Input Section
        url_label = tk.Label(
            self.input_frame,
            text="Enter Video URL:",
            fg="white",
            bg="#1E1E1E",
            font=("Helvetica", 14)
        )
        url_label.pack(anchor='w', pady=(0, 5))
        
        entry_frame = tk.Frame(self.input_frame, bg="#1E1E1E")
        entry_frame.pack(fill='x')
        
        self.url_entry = tk.Entry(
            entry_frame,
            font=("Helvetica", 12),
            bg="#2D2D2D",
            fg="white",
            insertbackground="white",
            relief='flat',
            bd=10
        )
        self.url_entry.pack(side='left', fill='x', expand=True)
        
        self.download_button = ttk.Button(
            entry_frame,
            text="Download",
            style="Custom.TButton",
            command=self.start_process
        )
        self.download_button.pack(side='right', padx=(10, 0))
        
        # Directory Selection Section
        dir_label = tk.Label(
            self.directory_frame,
            text="Download Location:",
            fg="white",
            bg="#1E1E1E",
            font=("Helvetica", 12)
        )
        dir_label.pack(side='left', padx=(0, 10))
        
        self.dir_display = tk.Label(
            self.directory_frame,
            text=self.download_dir,
            fg="#007AFF",
            bg="#1E1E1E",
            font=("Helvetica", 12)
        )
        self.dir_display.pack(side='left', expand=True, fill='x')
        
        self.change_dir_button = ttk.Button(
            self.directory_frame,
            text="Change",
            style="Custom.TButton",
            command=self.change_directory
        )
        self.change_dir_button.pack(side='right', padx=(10, 0))
        
        # Preview Section (initially empty)
        self.preview_container = tk.Frame(self.preview_frame, bg="#1E1E1E")
        self.preview_container.pack(expand=True)
        
        # Progress Section
        self.progress_bar = ttk.Progressbar(
            self.control_frame,
            orient="horizontal",
            mode="determinate",
            style="Custom.Horizontal.TProgressbar"
        )
        self.progress_bar.pack(fill='x', pady=(0, 10))
        
        self.status_label = tk.Label(
            self.control_frame,
            text="Ready",
            fg="white",
            bg="#1E1E1E",
            font=("Helvetica", 12)
        )
        self.status_label.pack(pady=5)

    def reset_preview(self):
        """Clear and reset the preview area"""
        for widget in self.preview_frame.winfo_children():
            widget.destroy()
        
        self.preview_container = tk.Frame(self.preview_frame, bg="#1E1E1E")
        self.preview_container.pack(expand=True)
        
        self.preview_label = tk.Label(
            self.preview_container,
            text="Enter a URL and click Download",
            fg="#666666",
            bg="#1E1E1E",
            font=("Helvetica", 12)
        )
        self.preview_label.pack(expand=True)

    def change_directory(self):
        new_dir = filedialog.askdirectory(
            initialdir=self.download_dir,
            title="Select Download Location"
        )
        if new_dir:
            self.download_dir = new_dir
            self.dir_display.config(text=self.download_dir)

    def start_process(self):
        url = self.url_entry.get().strip()
        if not url:
            messagebox.showerror("Error", "Please enter a video URL")
            return
        
        self.status_label.config(text="Processing...")
        self.download_button.config(state='disabled')
        self.progress_bar["value"] = 0
        
        # Clear existing preview
        self.reset_preview()
        self.preview_label.config(text="⌛ Loading...", fg="#007AFF")
        
        # Start processing in separate thread
        threading.Thread(target=self._process_video, args=(url,), daemon=True).start()

    def _process_video(self, url):
        try:
            # Basic info extraction with minimal options (from working version)
            ydl_opts = {
                'quiet': True,
                'extract_flat': True,
                'force_generic_extractor': False
            }
            
            with YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False, process=False)
                
                if not info:
                    raise Exception("Could not fetch video information")
                
                thumbnail_url = info.get('thumbnail')
                title = info.get('title', 'Unknown Title')
                
                # Load thumbnail first
                self._load_thumbnail(thumbnail_url, title)
                
                # Then start download
                self._start_download(url)
                
        except Exception as e:
            self.root.after(0, lambda: self._handle_error(str(e)))
            self.root.after(0, self._reset_state)

    def _load_thumbnail(self, thumbnail_url, title):
        try:
            # Use a shorter timeout for thumbnail
            with urllib.request.urlopen(thumbnail_url, timeout=5) as response:
                image_data = response.read()
                image = Image.open(BytesIO(image_data))
                
                # Calculate sizes
                preview_width = min(600, self.root.winfo_width() - 100)
                preview_height = 300
                
                # Maintain aspect ratio
                aspect_ratio = image.width / image.height
                if aspect_ratio > (preview_width / preview_height):
                    new_width = preview_width
                    new_height = int(preview_width / aspect_ratio)
                else:
                    new_height = preview_height
                    new_width = int(preview_height * aspect_ratio)
                
                image = image.resize((new_width, new_height), Image.Resampling.LANCZOS)
                
                # Update UI in main thread
                self.root.after(0, lambda: self._update_thumbnail_ui(image, title))
                
        except Exception as e:
            print(f"Thumbnail error: {str(e)}")  # For debugging
            # Continue with download even if thumbnail fails
            pass

    def _update_thumbnail_ui(self, image, title):
        try:
            self.current_photo = ImageTk.PhotoImage(image)
            
            # Clear preview frame
            for widget in self.preview_frame.winfo_children():
                widget.destroy()
            
            self.preview_container = tk.Frame(self.preview_frame, bg="#1E1E1E")
            self.preview_container.pack(expand=True)
            
            self.thumbnail_label = tk.Label(
                self.preview_container,
                image=self.current_photo,
                bg="#1E1E1E"
            )
            self.thumbnail_label.pack(pady=(0, 10))
            
            title_label = tk.Label(
                self.preview_container,
                text=title,
                fg="white",
                bg="#1E1E1E",
                font=("Helvetica", 12, "bold"),
                wraplength=image.width
            )
            title_label.pack()
            
            # Update window size
            self.root.update_idletasks()
            required_height = (
                self.input_frame.winfo_reqheight() +
                self.directory_frame.winfo_reqheight() +
                self.preview_container.winfo_reqheight() +
                self.control_frame.winfo_reqheight() +
                60
            )
            
            screen_height = self.root.winfo_screenheight()
            new_height = min(required_height, screen_height - 100)
            self.root.geometry(f"800x{int(new_height)}")
            
        except Exception as e:
            print(f"UI update error: {str(e)}")  # For debugging
            pass

    def _start_download(self, url):
        if not os.path.exists(self.download_dir):
            os.makedirs(self.download_dir)
        
        try:
            # Download options (from working version)
            ydl_opts = {
                'format': 'bestvideo[ext=mp4][vcodec^=avc1]+bestaudio[ext=m4a]/best[ext=mp4]/best',
                'outtmpl': os.path.join(self.download_dir, '%(title)s.%(ext)s'),
                'merge_output_format': 'mp4',
                'progress_hooks': [self._progress_hook],
                'quiet': True
            }
            
            with YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
                
            self.root.after(0, self._download_complete)
            
        except Exception as e:
            self.root.after(0, lambda: self._handle_error(str(e)))
        finally:
            self.root.after(0, self._reset_state)

    def _progress_hook(self, d):
        if d['status'] == 'downloading':
            try:
                percentage = float(d.get('_percent_str', '0%').replace('%', ''))
                speed = d.get('speed', 0)
                eta = d.get('eta', 0)
                
                self.root.after(0, lambda: self._update_progress(percentage, speed, eta))
                
            except (ValueError, AttributeError):
                pass
                
        elif d['status'] == 'finished':
            self.root.after(0, lambda: self.status_label.config(text="Finalizing download..."))

    def _update_progress(self, percentage, speed, eta):
        self.progress_bar["value"] = percentage
        if speed and eta:
            speed_mb = speed / 1024 / 1024
            self.status_label.config(text=f"Downloading: {percentage:.1f}% ({speed_mb:.1f} MB/s, ETA: {eta}s)")

    def _download_complete(self):
        self.status_label.config(text="Download completed!")
        messagebox.showinfo("Success", f"Video downloaded successfully to {self.download_dir}")
        self.progress_bar["value"] = 0

    def _handle_error(self, error_message):
        messagebox.showerror("Error", error_message)
        self.status_label.config(text="Error occurred")
        self.progress_bar["value"] = 0

    def _reset_state(self):
        self.download_button.config(state='normal')

def main():
    root = tk.Tk()
    app = VideoDownloaderApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()