from tkinter import *
import pytube
import _thread
from tkinter import messagebox as mb
import os


dwnlded = False


def d_thread():
    global dwnlded
    while True:
        if dwnlded:            
            dwnlded = False
            r = mb.askquestion('Done','Video Downloaded Successfully.\nOpen Destination Folder?')            
            if r == 'yes':
                os.startfile('Videos')
            dlod.destroy()
            break
        else:
            continue



def download_vid(res):
    res.download('Videos')
    global dwnlded
    dwnlded = True 


def load_down_func():
    global dlod
    dlod = Tk()
    dlod.geometry('+350+350')
    dlod.title('Loading...')
    Label(dlod,text='Downloading The Video ... ',font=('',13)).pack()
    dlod.mainloop()


def download_func():    
    s = int(l_box.get(ACTIVE).split('.')[0])
    res_s.destroy()
    res = res_list[s-1]
    _thread.start_new_thread(load_down_func,())
    _thread.start_new_thread(download_vid,(res,))


def loading_func():
    global lod
    lod = Tk()
    lod.geometry('+350+350')
    lod.title('Loading...')
    Label(lod,text='Searching For The Given Url ... ',font=('',13)).pack()
    lod.mainloop()

def load_des():
    lod.destroy()

def youtube_func(url):
    global res_list
    res_list = []
    yt = pytube.YouTube(url)
    video = yt.streams.all()        
    for res in video:
        res_list.append(res)


    _thread.start_new_thread(load_des,()) 

    global res_s
    res_s = Tk()
    res_s.title('Select The Resolution.')

    title = yt.title

    Label(res_s, text='Title - '+ title,font=('',10)).pack()

    Label(res_s, text='Select The Resolution.',font=('',15)).pack()

    global l_box
    l_box = Listbox(res_s,width=100,height=len(res_list))
    l_box.pack()
    s = 1
    for i in res_list:
        i = str(s)+'. '+str(i)
        l_box.insert(END,i)
        s+=1
        
    Label(res_s,text='').pack()
    
    Button(res_s, text='Select',font=('',15),command=download_func).pack()    
    res_s.mainloop()
    

def set_res():
    global url_entry
    string = url_entry.get()
    url_entry.set('')
    print(string)
    try:
        _thread.start_new_thread(loading_func,())
        _thread.start_new_thread(youtube_func,(string,))        
    except pytube.exceptions.RegexMatchError:
        mb.showerror('error','No Video Found At Given Url.')
        

win = Tk()
win.geometry('350x350')
win.title('DeeTube')
win.configure(bg='white')

logo = PhotoImage(file='resources/logo.png')
Label(win, image=logo,bg='white').pack()

Label(win, text='\n',bg='white').pack()

Label(win, text='Paste The URL Here Of The Video You Want To Download.',font=('',10)).pack()
Label(win, text='Press CTRL+V To Paste',font=('',10)).pack()

Label(win, text='\n',bg='white').pack()

global url_entry
url_entry = StringVar()

Entry(win, textvariable=url_entry,width=35,bd=5,font=('',10)).pack()

Label(win, text='\n',bg='white').pack()

download_img = PhotoImage(file='resources/download.png')
Button(win, image=download_img,bg='white',bd=0,command=set_res).pack()

_thread.start_new_thread(d_thread,())

win.mainloop()
