from pytube import YouTube
import os
import tkinter as tk
window = tk.Tk()
link = tk.Entry()
dir_path = os.path.dirname(os.path.realpath(__file__))
j = 3
for f in os.listdir(dir_path+"/videos/"):
    videodisplay = tk.Button(text=f)
    videodisplay.grid(column=1, row=j)
    j = j+1
def download():
    global j
    YouTube(link.get()).streams.first().download(output_path=dir_path+"/videos/")
    videoname = YouTube(link.get()).title
    videodisplay = tk.Button(text = videoname)
    videodisplay.grid(column = 1, row = j)
    j = j+1
download = tk.Button(text = "Download", command= download)
link.grid(column = 1, row = 1)
download.grid(column=2, row=1)
videod = tk.Label(text="Downloaded Videos")
videod.grid(column = 1, row = 2)
window.mainloop()