from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import sqlite3
import os
import email_pass
import smtplib
import time
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
    



class Login_System:
    def __init__(self,root):
        self.root=root
        self.root.title("Login System | Developed By Huzaif")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#fafafa")
        self.root.resizable(0,0)
        self.otp=''
        ##IMAGES##
        self.phone_image=ImageTk.PhotoImage(file="imglogin/phone.png")
        self.lbl_Phone_image=Label(self.root,image=self.phone_image,bd=0).place(x=150,y=40)
        
        
    
    ##LOGIN FRAME## 
        self.employee_id=StringVar()
        self.password=StringVar()

        login_frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        login_frame.place(x=790,y=70,width=350,height=460)
        title=Label(login_frame,text="Login Form",font=("Elephant",30,"bold"),bg="white").place(x=0,y=30,relwidth=1)
        lbl_user=Label(login_frame,text="Employee ID",font=("Andalus",15),bg="white",fg="#767171").place(x=50,y=100)
        txt_username=Entry(login_frame,textvariable=self.employee_id,font=("times new roman",15),bg="#ECECEC").place(x=50,y=140,width=250)
        
        lbl_pass=Label(login_frame,text="Password",font=("Andalus",15),bg="white",fg="#767171").place(x=50,y=200)
        txt_pass=Entry(login_frame,textvariable=self.password,show="*",font=("times new roman",15),bg="#ECECEC").place(x=50,y=240,width=250)
        
        log_btn=Button(login_frame,text="Log In",comman=self.login,font=("Arial Rounded MT Bold",15),bg="#00B0F0",activebackground="#00B0F0",fg="white",activeforeground="white",cursor='hand2').place(x=50,y=300,width=250,height=35)

        hr=Label(login_frame,bg="lightgray").place(x=50,y=370,width=250,height=2)
        or_=Label(login_frame,text="OR",bg="white",fg="lightgray",font=("times new roman",15,"bold")).place(x=150,y=355)
        
        btn_forget=Button(login_frame,text="Forget Password?",command=self.forget_window,bd=0,font=("times new roman",13),bg="white",activebackground="white",fg="#00759E",activeforeground="#00759E").place(x=105,y=390)
       ##FRAME 2##
       
        
        register_frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        register_frame.place(x=790,y=570,width=350,height=60)        
        
        lbl_reg=Label(register_frame,text="HAVE A GOOD DAY!",font=("times new roman",13),bg="white").place(x=0,y=15,relwidth=1)
        # sign_btn=Button(register_frame,text="Sign Up",font=("times new roman",13,"bold"),bg="white",activebackground="white",fg="#00759E",activeforeground="#00759E",bd=0,cursor='hand2').place(x=230,y=14)
        
        
    
   
        
        
        
    def login(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()        
        try:
            if self.employee_id.get()=="" or self.password.get()=="":
                messagebox.showerror("Error","All Fields are required",parent=self.root)
            else:    
                cur.execute("select utype from employee where eid=? AND pass=?",(self.employee_id.get(),self.password.get()))
                user=cur.fetchone()
                if user==None:
                    messagebox.showerror("Error","Invalid Username or Password",parent=self.root)
                else:
                    if user[0]=="ADMIN":
                        self.root.destroy()
                        os.system("python dashboard.py")
                    else:
                        self.root.destroy()
                        os.system("python billing.py")                        
                    
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)         
            
       
            
    def forget_window(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()        
        try:
            if self.employee_id.get()=="":
                messagebox.showerror("Error","Employee ID must be required",parent=self.root)
            else:              
                cur.execute("select email from employee where eid=?",(self.employee_id.get(),))
                email=cur.fetchone()
                if email==None:
                    messagebox.showerror("Error","Invalid Employee id, try again",parent=self.root)
                else:          
                    #####FORGET WINDOW####
                    self.var_otp=StringVar()
                    self.var_newpass=StringVar()
                    self.var_confpass=StringVar()
                    # call send_email_function.
                    chk=self.send_email(email[0])
                    if chk=='f':
                        messagebox.showerror('Error','Connection Error, Try Again',parent=self.root)
                    else:
                    
                        self.forget_win=Toplevel(self.root)
                        self.forget_win.title("RESET PASSWORD")
                        self.forget_win.geometry('400x350+500+100')
                        self.forget_win.focus_force()      
                        
                        title=Label(self.forget_win,text='Reset Password',font=("goudy old style",15,'bold'),bg="#3f51b5",fg="white").pack(side=TOP,fill=X)
                        lbl_reset=Label(self.forget_win,text="Enter OTP Send on Registered Email",font=("times new roman",15)).place(x=20,y=60)
                        txt_reset=Entry(self.forget_win,textvariable=self.var_otp,font=("times new roman",15),bg='lightyellow').place(x=20,y=100,width=250,height=30)
                        self.btn_reset=Button(self.forget_win,text="SUBMIT",command=self.validate_otp,font=("times new roman",15),bg="lightblue")
                        self.btn_reset.place(x=280,y=100,width=100,height=30)
                        
                        
                        lbl_new_pass=Label(self.forget_win,text="NEW PASSWORD",font=("times new roman",15)).place(x=20,y=160)
                        txt_new_pass=Entry(self.forget_win,textvariable=self.var_newpass,font=("times new roman",15),bg='lightyellow').place(x=20,y=190,width=250,height=30)
                        
                        lbl_c_pass=Label(self.forget_win,text="CONFIRM PASSWORD",font=("times new roman",15)).place(x=20,y=225)
                        txt_c_pass=Entry(self.forget_win,textvariable=self.var_confpass,font=("times new roman",15),bg='lightyellow').place(x=20,y=255,width=250,height=30)                    
                        self.btn_update=Button(self.forget_win,text="UPDATE",command=self.update_password,state=DISABLED,font=("times new roman",15),bg="lightblue")
                        self.btn_update.place(x=150,y=300,width=100,height=30)            

        
                    
                                      
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)  
    
    def update_password(self):
        if self.var_newpass.get()=="" or self.var_confpass.get()=="":
            messagebox.showerror("Error","Password is Required",parent=self.forget_win)

        elif self.var_newpass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","New Password & confirm password should be same",parent=self.forget_win)
        else:
            con=sqlite3.connect(database=r'ims.db')
            cur=con.cursor()        
            try:
                cur.execute("Update employee SET pass=? where eid=?",(self.var_newpass.get(),self.employee_id.get()))
                con.commit()
                messagebox.showinfo("Success","Password Updated Successfully",parent=self.forget_win)
                self.forget_win.destroy()
            except Exception as ex:
                messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)                  
    def validate_otp(self):
        if int(self.otp)==int(self.var_otp.get()):
            self.btn_update.config(state=NORMAL)
            self.btn_reset.config(state=DISABLED)
        else:
            messagebox.showerror("Error","Invalid OTP Try Again",parent=self.forget_win)
    def send_email(self,to_):
        s=smtplib.SMTP('smtp.gmail.com',587)
        s.starttls()
        email_=email_pass.email_
        pass_=email_pass.pass_
        
        s.login(email_,pass_)
        
        self.otp=int(time.strftime("%H%S%M"))+int(time.strftime("%S"))
        
        
        subj='IMS-Reset Password OTP'
        msg=f'Dear Sir/Madam,\n\nYour Reset OTP is {str(self.otp)}.\n\nWith Regards,\nIMS Team.'
        msg="Subject:{}\n\n{}".format(subj,msg)
        s.sendmail(email_,to_,msg)
        chk=s.ehlo()
        if chk[0]==250:
            return 's'
        else:
            return 'f'

    # def first_reg(self):       
    #     con=sqlite3.connect(database=r'ims.db')
    #     cur=con.cursor() 
    #     try:
    #         cur.execute("select * from employee")
    #         cons=cur.fetchall()
    #         if len(cons)==0:         
    #             subprocess.call("firsttime_reg.py", shell=True)
                      
    #         else:
    #             print("ITS HAVE LEN")                                                    
    #     except Exception as ex:
    #         messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)        
                
                


                       
root = Tk() 
obj=Login_System(root)
root.mainloop()