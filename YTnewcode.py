import tkinter as tk
from tkinter import messagebox, filedialog
import yt_dlp
import os

# Folder chun-ne ka function
def select_folder():
    folder = filedialog.askdirectory()
    if folder:
        folder_path.set(folder)

def start_download():
    link = url_entry.get().strip()
    save_dir = folder_path.get()
    
    if not link.startswith("http"):
        messagebox.showwarning("Input Error", "Pehle sahi YouTube link dalo!")
        return
    if not save_dir:
        messagebox.showwarning("Input Error", "Pehle folder chuno!")
        return
    
    try:
        status_label.config(text="Downloading... Please wait.", fg="blue")
        root.update()
        
        # Folder ke saath download settings
        ydl_opts = {
            'format': 'best',
            'outtmpl': f'{save_dir}/%(title)s.%(ext)s',
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
            
        status_label.config(text="Download Complete! ✅", fg="green")
        messagebox.showinfo("Success", f"Video '{save_dir}' mein save ho gayi!")
    except Exception as e:
        status_label.config(text="Failed ❌", fg="red")
        messagebox.showerror("Error", f"Error: {e}")

# --- UI Setup ---
root = tk.Tk()
root.title("My Smart Downloader")
root.geometry("500x350")

# Folder path store karne ke liye variable
folder_path = tk.StringVar()

tk.Label(root, text="Raj YT Vid Downloader", font=("Arial", 16, "bold")).pack(pady=10)

# Link Input
tk.Label(root, text="Paste Link Here:").pack()
url_entry = tk.Entry(root, width=55)
url_entry.pack(pady=5)

# Folder Selection
tk.Label(root, text="Save Location:").pack(pady=5)
folder_display = tk.Entry(root, textvariable=folder_path, width=40)
folder_display.pack(side=tk.TOP, pady=2)
tk.Button(root, text="Browse Folder", command=select_folder).pack(pady=5)

# Status
status_label = tk.Label(root, text="Ready", font=("Arial", 10))
status_label.pack(pady=10)

# Download Button
btn = tk.Button(root, text="START DOWNLOAD", command=start_download, bg="green", fg="white", font=("Arial", 10, "bold"), padx=20)
btn.pack(pady=20)

root.mainloop()