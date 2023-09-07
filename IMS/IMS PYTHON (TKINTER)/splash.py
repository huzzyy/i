from tkinter import *
from tkinter import ttk,messagebox
import sqlite3
import pyttsx3 
import speech_recognition as sr 
import sys 



engine = pyttsx3.init('sapi5')  
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)
engine.setProperty('rate',170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
    

splash_win= Tk()
splash_win.title("Splash Screen")
splash_win.geometry("780x400+420+200")
splash_win.config(bg="#1a1a1a")    

splash_win.overrideredirect(True)

splash_label = Label(splash_win,text="Welcome To The IMS SYSTEM",bg="#1a1a1a",fg="white",
                     font=("times new roman",30)).place(x=0,y=40,relwidth=1)    
splash_label = Label(splash_win,text="Redefining Possibilites....",bg="#1a1a1a",fg="#e6e6e6",
                     font=("times new roman",30)).place(x=280,y=100) 

splash_label = Label(splash_win,text="Note:Two Admin Cannot be register from this splash screen because for security purpose.",bg="#1a1a1a",fg="#f44336",
                     font=("times new roman",15)).place(x=25,y=360) 



def task():
    speak("Hey Sir, Welcome To The IMS-INVENTORY MANAGEMENT SYSTEM")
    speak('If you using this application first time and want to register as Admin to control , Please Click on Register As Admin')
    speak('If you already have account then click on login button')
    speak('Please wait we creating an interface for you.')

def firsttime():
    con=sqlite3.connect(database=r'ims.db')
    cur=con.cursor()
    try:
        cur.execute("select * from employee") 
        cons=cur.fetchall()
        if len(cons)==0:
            
            loading = Label(splash_win,text="Loading...",bg="#1a1a1a",fg="#e6e6e6",
            font=("vardana",15)).place(x=50,y=270)
            labels2=Label(splash_win,text="Please Being Patient untill we redirect you to login page",bg="#1a1a1a",fg="white",font=("times new roman",15))            
            # progress=ttk.Progressbar(splash_win,orient=HORIZONTAL,length=520)
            labels2.place(x=50,y=300)
            # progress.config(mode='indeterminate')
            # progress.start()
            splash_win.after(4000,calling_mainwin)
        else:
            messagebox.showerror("Error","Admin Already Registered,You need to login now!!")
    except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=splash_win)          
            
            
def login():
    loading = Label(splash_win,text="Loading...",bg="#1a1a1a",fg="#e6e6e6",
    font=("vardana",15)).place(x=50,y=270)
    labels=Label(splash_win,text="Please Being Patient untill we redirect you to login page",bg="#1a1a1a",fg="white",font=("times new roman",15))
    
    # progress=ttk.Progressbar(splash_win,orient=HORIZONTAL,length=520)
    labels.place(x=50,y=300)
    # progress.config(mode='determinate')
    # progress.start()
    splash_win.after(4000,calling_mainwin2)
    
def close():
    splash_win.destroy()
    
    
Btn_firsttime=Button(splash_win,text="Already Registered?",font=("vardana",12),fg='white',bg="#008000",bd=0,command=login,width=20)
Btn_firsttime.place(x=40,y=210)

Btn_login=Button(splash_win,text="Register As Admin",font=("vardana",12),fg='white',bg="#008000",bd=0,command=firsttime,width=20)
Btn_login.place(x=270,y=210)

Btn_close=Button(splash_win,text="Close This Window",font=("vardana",12),fg='white',bg="#008000",bd=0,command=close,width=20)
Btn_close.place(x=490,y=210)

def calling_mainwin():
    splash_win.destroy()
    import firsttime_reg
    
def calling_mainwin2():
    splash_win.destroy()
    import login
    

if __name__=="__main__": 
    task()      
    mainloop()
