from tkinter import *
from pytube import YouTube    #pip install pytube

root = Tk()
root.geometry('500x300')
root.resizable(0,0)
root.title("Youtube video downloader by Aditya Rana")

link = StringVar()

Label(root, text = 'Paste Link Here:', font = 'arial 15 bold').place(x= 160 , y = 60)
link_enter = Entry(root, width = 70,textvariable = link).place(x = 32, y = 90)

def Downloader():     
    url =YouTube(str(link.get())) #paste link of YouTube video in get("Here!")
    video = url.streams.first()
    video.download()
    Label(root, text = 'DOWNLOADED', font = 'arial 15').place(x= 180 , y = 210)  

Button(root,text = 'DOWNLOAD', font = 'arial 15 bold' ,bg = 'green', padx = 2, command = Downloader).place(x=180 ,y = 150)

root.mainloop()
