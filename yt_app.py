import tkinter as tk
from tkinter import messagebox
import yt_dlp

def start_download():
    link = url_entry.get().strip() # .strip() se extra space hat jayega
    
    # Check karein ki link sahi hai ya nahi
    if not link.startswith("http"):
        messagebox.showwarning("Input Error", "Bhai, pehle sahi YouTube link dalo!")
        return
    
    try:
        status_label.config(text="Downloading... Please wait.", fg="blue")
        root.update()
        
        ydl_opts = {'format': 'best'}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
            
        status_label.config(text="Download Complete! ✅", fg="green")
        messagebox.showinfo("Success", "Video download ho gayi hai!")
    except Exception as e:
        status_label.config(text="Download Failed ❌", fg="red")
        messagebox.showerror("Error", f"Kuch gadbad hui: {e}")

# --- UI Setup ---
root = tk.Tk()
root.title("My Python Downloader")
root.geometry("450x250")

tk.Label(root, text="YouTube Downloader", font=("Arial", 16, "bold")).pack(pady=10)
tk.Label(root, text="Paste YouTube Link Below:").pack()

url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=10)

status_label = tk.Label(root, text="Ready", font=("Arial", 10))
status_label.pack()

btn = tk.Button(root, text="Download Now", command=start_download, bg="red", fg="white", font=("Arial", 10, "bold"))
btn.pack(pady=20)

root.mainloop()