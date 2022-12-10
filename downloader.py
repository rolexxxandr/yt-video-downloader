from pytube import YouTube
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
from tkinter.ttk import Progressbar

def download_highest():
    bar = Progressbar(window, length=50)
    bar["value"] = 70
    yt = YouTube(str(link.get()))
    video = yt.streams.get_highest_resolution()
    video.download()
    Label(window, text = f"Video downloaded successfully", font = ('Arial', 10)).grid(column=0, row=3)
    messagebox.showinfo("File downloaded",f"Author: {yt.author}\nVideo: {yt.title}\nViews: {yt.views}")

def download_lowest():
    yt = YouTube(str(link.get()))
    video = yt.streams.get_lowest_resolution()
    video.download()
    Label(window, text = "Video downloaded successfully", font = ("Arial", 10)).grid(column=0, row=3)
    messagebox.showinfo("File downloaded",f"Author: {yt.author}\nVideo: {yt.title}\nViews: {yt.views}")

def download_auido():
    yt = YouTube(str(link.get()))
    audio = yt.streams.get_audio_only()
    audio.download(filename_prefix="audio_")
    Label(window, text = "Audio downloaded successfully", font = ("Arial", 10)).grid(column=0, row=3)
    messagebox.showinfo("File downloaded",f"Author: {yt.author}\nVideo: {yt.title}\nViews: {yt.views}")

def download_file():
    if combo.current() == 0:
        download_highest()
    elif combo.current() == 1:
        download_lowest()
    elif combo.current() == 2:
        download_auido()

# window settings
window = Tk()
window.title("Downloader")
window.geometry("300x100")
window.resizable(True, True)

link = StringVar()

# input area
txt = Entry(window, width=50, textvariable=link)
txt.grid(column=0, row=0)
txt.focus()

# combobox
current_variable  = StringVar()
combo = Combobox(window, state="readonly")
combo["values"] = ["highest", "lowest", "audio"]
combo.grid(column=0, row=2)
combo.current(0)

# download button
btn = Button(window, text="Download", bg="green", command=download_file)
btn.grid(column=0, row=1)

window.mainloop()
