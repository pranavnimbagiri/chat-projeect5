import socket
import sys
from threading import Thread
import select
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import ftplib
import os
import ntpath
import time
from ftplib import FTP
from pathlib import Path
from playsound import playsound
import pygame
from pygame import mixer


PORT  = 8050
IP_ADDRESS = '127.0.0.1'
SERVER = None
BUFFER_SIZE = 4096

name= None
listbox= None
filepathlabel= None

global song_counter
song_counter=0

for file in os.listfir('shared_files'):
    filename=os.fsdecode(file)
    listbox.insert(song_counter,filename)
    song_counter=song_counter+1

def play():
    global song_selected
    song_selected=listbox.get(ANCHOR)

    pygame
    mixer.init()
    mixer.init()
    mixer.music.load('shared_files/'+song_selected)
    mixer.music.play()
    if(song_selected!=""):
        infolabel.configure(text="Now Playing:"+song_selected)
    else:
        infolabel.configure(text="")

def stop():
    global song_selected
    pygamemixer.init()
    mixer.music.load('shared_files/'+song_selected)
    mixer.music.pause()
    infolabel.configure(text="")

def resume():
    global song_selected
    mixer.init()
    mixer.music.load('shared_files/'+song_selected)
    mixer.music.play()

def pause():
    global song_selected
    pygame
    mixer.init()
    mixer.music.load("shared_files/"+song_selected)
    mixer.music.pause()

def browsefile():
    global listbox
    global song_counter
    global filepathlabel

    try:
        filename=filedialog.askopenfilename()
        HOSTENAME="127.0.0.1"
        USERNAME="lftpd"
        PASSWORD="hi"

        ftp_server=FTP(HOSTENAME,USERNAME,PASSWORD)
        ftp_server.encoding="utf=8"
        ftp_server.cwd("shared_files")
        fname=ntpath.basename(filename)
        with open(filename,"rb") as file:
            ftp_server.storbinary(f"STOR{fname}",file)

        ftp_server.dir()
        ftp_server.quit()

        listbox.insert(song_counter,fname)
        song_counter=song_counter+1
    
    except FoleNotFounderror:
        print("cancel button pressed")

def dowwnload():

    song_to_download=listbox.get(ANCHOR)
    infolabel.configure(text="downloading"+song_to_download)
    HOSTENAME="127.0.0.1"
    USERNAME="lftpd"
    PASSWORD="hi"
    home=str(Path.home())
    download_path=home+"/Downloads"
    ftp_server=ftplib.FTP(HOSTNAME,USERNAME,PASSWORD)
    ftp_server.encoding="utf-8"
    ftp_server.cwd('shared_files')
    local_filename=os.path.join(download_path,song_to_download)
    file=open(local_filename,'wb')
    ftp_server.retrbinary('RETR'+song_to_download,file.write)
    ftp_server.dir()
    file.close()
    ftp_server.quit()
    infolabel.configure(text="Download Complete")
    time.sleep(1)
    if(song_selected!=""):
        infolabel.configure(text="Now Playing"+song_slected)
    else:
        infolabel.configure(text="")
        


def musicWindow():

    print("\n\t\t\t\tMUSIC window")

    #Client GUI starts here
    window=Tk()

    window.title('Music Window')
    window.geometry("300x300")
    window.configure(bg='lightskyblue')

    selectlabel = label(window,text="select song",bg='lightskyblue',font=("calibri",10))
    selectlabel.place(x=2,y=1)

    listbox=listbox(window,height=10,width=19,activestyle="dotbox",bg="lightskyblue",borderwidth=2,font=("calibri",10))
    listbox.place(x=10,y=10)

    scrollbar1=Scrollbar(listbox)
    scrollbar1.place(relheight=1,relx=1)
    scrollbar1.config(command=listbox.yview)

    playbutton=Button(window,text="play",width=10,bd=1,bg="skyblue",font=("Calibri,10"))
    playbutton.place(x=30,y=200)

    stop=Button(window,text="Stop",bd=1,width=10,bg="skyblue",font=("Calibri",10))
    stop.place(x=200,y=200)

    upload=Button(window,text="Upload",width=10,bd=1,bg="skyblue",font=("Calibri",10))
    upload.place(x=30,y=250)

    ResummeButton=Button(window,text="Resume",width=10,bd=1,bg="SkyBlue",font=("Calibri",10))
    ResummeButton.place(x=200,y=250)

    pausebutton=Button(window,text="Pause",width=10,bd=1,bg='skyblue',font=("Calibri",10))
    pausebutton.place(x=200,y=250)

    dowwnload=Button(window,text-"Download",width=10,bd=1,bg="skyblue",font=("Calibri",10))
    download.place(x=200,y=250)

    infolabel = label(window,text="",fg="blue",font=("Calibri",8))
    infolabel.place(x=4,y=280)

    window.mainloop()

def setup():
    global SERVER
    global PORT
    global IP_ADDRESS

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS, PORT))

    receive_thread = Thread(target=receiveMessage)               #receiving multiple messages
    receive_thread.start()

    musicWindow()

setup()