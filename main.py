from pytube import YouTube
from tkinter import *

def download_highest():
    url = YouTube(str(link.get()))
    video = url.streams.get_highest_resolution()
    video.download()
    Label(window, text = 'Video downloaded successfully', font = ('Arial', 10)).grid(column=0, row=2)

window = Tk()
window.title("Downloader")
window.geometry("300x100")
window.resizable(False, False)

link = StringVar()

txt = Entry(window, width=50, textvariable=link)
txt.grid(column=0, row=0)
txt.focus()

btn = Button(window, text="Download", bg="green", command=download_highest)
btn.grid(column=0, row=1)

window.mainloop()