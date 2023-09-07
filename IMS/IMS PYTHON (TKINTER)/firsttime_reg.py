from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3


class femployeClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1150x550+300+130")
        self.root.title("Inventory Management System | Developed By Huzaif")
        self.root.config(bg='white')    
        self.root.focus_force() 
        self.root.resizable(0,0)
        ###################
        ##ALL VARIABLE##
        
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()
        
        self.var_emp_id=StringVar()
        self.var_gender=StringVar()
        self.var_contact=StringVar()
        self.var_name=StringVar()
        self.var_dob=StringVar()
        self.var_doj=StringVar()
        self.var_email=StringVar()
        self.var_pass=StringVar()
        self.var_utype=StringVar()
        self.var_salary=StringVar()
        
        ########LABELS######
        title=Label(self.root,text="Welcome to IMS- INVENTORY MANAGEMENT SYSTEM \n One Time Registration",font=("Times New Roman",15),bg="#0f4d7d",fg="white").place(x=0,y=100,width=1150)
        
        lbl_empid=Label(self.root,text="Unique ID",font=("goudy old style",15),bg="white").place(x=50,y=170)
        lbl_gender=Label(self.root,text="Gender",font=("goudy old style",15),bg="white").place(x=400,y=170)
        lbl_contact=Label(self.root,text="Contact",font=("goudy old style",15),bg="white").place(x=750,y=170)
        txt_empid=Entry(self.root,textvariable=self.var_emp_id,font=("goudy old style",15),bg="lightyellow").place(x=150,y=170,width=180)
        cmb_gender=ttk.Combobox(self.root,textvariable=self.var_gender,values=("Select","MALE","FEMALE","OTHER"),state='readonly',justify=CENTER,font=("goudy old style",15))
        cmb_gender.place(x=500,y=170,width=180)
        cmb_gender.current(0)
        txt_contact=Entry(self.root,textvariable=self.var_contact,font=("goudy old style",15),bg="lightyellow").place(x=850,y=170,width=180)
        
        ##ROW 2##
        lbl_name=Label(self.root,text="Name",font=("goudy old style",15),bg="white").place(x=50,y=220)
        lbl_dob=Label(self.root,text="D.O.B",font=("goudy old style",15),bg="white").place(x=400,y=220)
        lbl_doj=Label(self.root,text="D.O.J",font=("goudy old style",15),bg="white").place(x=750,y=220)
        
        
        txt_name=Entry(self.root,textvariable=self.var_name,font=("goudy old style",15),bg="lightyellow").place(x=150,y=220,width=180)
        txt_dob=Entry(self.root,textvariable=self.var_dob,font=("goudy old style",15),bg="lightyellow").place(x=500,y=220,width=180)        
        txt_doj=Entry(self.root,textvariable=self.var_doj,font=("goudy old style",15),bg="lightyellow").place(x=850,y=220,width=180)
        
        
        ##ROW 3###
        lbl_email=Label(self.root,text="Email",font=("goudy old style",15),bg="white").place(x=50,y=260)
        lbl_pass=Label(self.root,text="Password",font=("goudy old style",15),bg="white").place(x=400,y=260)
        lbl_utype=Label(self.root,text="User Type",font=("goudy old style",15),bg="white").place(x=750,y=260)
        
        
        
        txt_email=Entry(self.root,textvariable=self.var_email,font=("goudy old style",15),bg="lightyellow").place(x=150,y=260,width=180)
        txt_pass=Entry(self.root,textvariable=self.var_pass,font=("goudy old style",15),bg="lightyellow").place(x=500,y=260,width=180)        
        # txt_utype=Entry(self.root,textvariable=self.var_utype,text="Contact",font=("goudy old style",15),bg="lightyellow").place(x=850,y=230,width=180)
        cmb_utype=ttk.Combobox(self.root,textvariable=self.var_utype,values=("ADMIN","EMPLOYEE"),state=DISABLED,justify=CENTER,font=("goudy old style",15))
        cmb_utype.place(x=850,y=260,width=180)
        cmb_utype.current(0)

        ##ROW 4##
        lbl_Address=Label(self.root,text="Address",font=("goudy old style",15),bg="white").place(x=50,y=300)
        lbl_Salary=Label(self.root,text="Salary",font=("goudy old style",15),bg="white").place(x=500,y=300)
        self.txt_Address=Text(self.root,font=("goudy old style",15),bg="lightyellow")
        self.txt_Address.place(x=150,y=300,width=300,height=60)       
        txt_Salary=Label(self.root,text='NA',font=("goudy old style",15),state=DISABLED).place(x=600,y=300,width=180)
        
        btn_register=Button(self.root,text="Register",command=self.register,font=("goudy old style",15),bg="#2196f3",fg="white",cursor="hand2").place(x=400,y=380,width=160,height=28)
        
        btn_clear=Button(self.root,text="Clear",command=self.clear,font=("goudy old style",15),bg="#607d8b",fg="white",cursor="hand2").place(x=610,y=380,width=160,height=28)

        
        lbl_Address=Label(self.root,text="Note:\tEmail Address should be correct, It will help to recover the Password",font=("goudy old style",15),fg="red").place(x=270,y=500)
        
        
            ##IMAGAESSS##            
        self.bill_photo=Image.open("images/menu_im.png")
        self.bill_photo=self.bill_photo.resize((120,100), resample=Image.BILINEAR)
        self.bill_photo=ImageTk.PhotoImage(self.bill_photo)
        
        lbl_image =Label(self.root,image=self.bill_photo,bd=0,bg='white')
        lbl_image.place(x=550,y=0)
        
        self.bill2_photo=Image.open("images/cat2.jpg")
        self.bill2_photo=self.bill2_photo.resize((140,100), resample=Image.BILINEAR)
        self.bill2_photo=ImageTk.PhotoImage(self.bill2_photo)
        
        lbl_image2 =Label(self.root,image=self.bill2_photo,bd=0,bg='white')
        lbl_image2.place(x=750,y=0)
        
        self.im2=Image.open("images/bg.png")
        self.im2=self.im2.resize((120,90), resample=Image.BILINEAR)
        self.im2=ImageTk.PhotoImage(self.im2)
        self.lbl_im2=Label(self.root,image=self.im2,bd=0,relief=RAISED ,bg='white')
        self.lbl_im2.place(x=350,y=0)
        self.first()

#######################################################################

    def register(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_emp_id.get()=="":
                messagebox.showerror("Error","Employee ID Must be required",parent=self.root)
            elif self.var_name.get()=="" and self.var_pass.get()=="":
                messagebox.showerror("Error","Name And Password Must be required",parent=self.root)
            
            else:
                cur.execute("Select * from employee where eid=?",(self.var_emp_id.get(),))    
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","This Employee Id already assigned, try different",parent=self.root)
                else:
                    cur.execute("Insert into employee (eid,name,email,gender,contact,dob,doj,pass,utype,address,salary)values(?,?,?,?,?,?,?,?,?,?,?)",(
                                        self.var_emp_id.get(),
                                        self.var_name.get(),
                                        self.var_email.get(),
                                        self.var_gender.get(),
                                        self.var_contact.get(),                                     
                                        self.var_dob.get(),
                                        self.var_doj.get(),                                        
                                        self.var_pass.get(),
                                        self.var_utype.get(),
                                        self.txt_Address.get('1.0',END),
                                        self.var_salary.get(),
               
                    ))    
                    con.commit()
                    messagebox.showinfo("Success","Register  Successfully",parent=self.root)
                    self.root.destroy()
                    import login

                    
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)

        
    def clear(self):
        self.var_emp_id.set("")
        self.var_name.set("")
        self.var_email.set("")
        self.var_gender.set("Select")
        self.var_contact.set("")                                     
        self.var_dob.set("")
        self.var_doj.set("")                                        
        self.var_pass.set("")
        self.var_utype.set("Admin")
        self.txt_Address.delete('1.0',END)
        self.var_salary.set("")
        self.var_searchtxt.set("")
        self.var_searchby.set("Select")
    
    def first(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor() 
        try:
            cur.execute("select * from employee")
            cons=cur.fetchall()
            if len(cons)==0:
                pass

                
                      
            else:
                print("ITS HAVE LEN")                                                    
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)            
        

root =Tk()
obj=femployeClass(root)  
root.mainloop()   