from tkinter import *
from PIL import Image, ImageTk, ImageFilter
from category import categoryClass
from employe import employeClass
from supplier import supplierclass
from category import categoryClass
from product import productClass
from repair import repairclass
from sales import salesClass
import sqlite3
from tkinter import messagebox
import os
import time
class IMS:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1600x800+0+0")
        self.root.title("Inventory Management System || Developed By Huzaif")
        self.root.config(bg='white')
        self.root.resizable(0,0)
    
 # titlee#########
 
        self.icon_title=PhotoImage(file="images/logo1.png")
        title=Label(self.root,text="Inventory Management System",image=self.icon_title,compound=LEFT,font=("times new roman",40,"bold"),bg="#010c48",fg="white",anchor="w",padx=20).place(x=0,y=0,relwidth=1,height=70)

#LOGOUT BTN##
        btn_logout=Button(self.root,text="Logout",command=self.logout,font=("times new roman",15,"bold"),bg="yellow",cursor="hand2").place(x=1400,y=10,height=50,width=150)

#CLOCKK##
        self.lbl_clock=Label(self.root,text="Welcome To Cell Store | Inventory Management System\t\t Date:DD-MM-YYYY\t\t Time:HH:MM:SS",font=("times new roman",15),bg="#4d636d",fg="white")
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)
        
#LEFT MENU######
        self.menulogo=Image.open("images/menu_im.png")
        self.menulogo = self.menulogo.resize((200, 200), resample=Image.BILINEAR)

        self.menulogo=ImageTk.PhotoImage(self.menulogo)
        
        LeftMenu=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        LeftMenu.place(x=0,y=102,width=200,height=690)
        
        lbl_menuLogo=Label(LeftMenu,image=self.menulogo)
        lbl_menuLogo.pack(side=TOP,fill=X) 
        
#MENU BUTTON###
        self.icon_side=PhotoImage(file="images/side.png")
        lbl_menu=Label(LeftMenu,text="Menu",font=("times new roman",20),bg="#009688").pack(side=TOP,fill=X)        
        btn_employee=Button(LeftMenu,text="Employee",command=self.employee,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",18,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X) 
        btn_supplier=Button(LeftMenu,text="Supplier",command=self.supplier,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",18,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)     
        btn_category=Button(LeftMenu,text="Category",command=self.category,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",18,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X) 
        btn_products=Button(LeftMenu,text="Products",command=self.product,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",18,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_sales=Button(LeftMenu,text="Sales",command=self.sales,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",18,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X) 
        btn_repair=Button(LeftMenu,text="Repairing",command=self.repair,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",18,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_expense=Button(LeftMenu,text="Expense",image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",18,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X) 
        btn_urgentcash=Button(LeftMenu,text="Urgent Cash",image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",18,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X) 
        btn_exit=Button(LeftMenu,text="Exit",command=self.exit,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",18,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X) 
        
##__CONTENCT##
        self.lbl_employee=Label(self.root,text="Total Employee\n[ 0 ]",bd=5,relief=RIDGE,bg="#33bbf9",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_employee.place(x=300,y=120,height=150,width=300)    
        
        self.lbl_supplier=Label(self.root,text="Total Supplier\n[ 0 ]",bd=5,relief=RIDGE,bg="#ff5722",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_supplier.place(x=650,y=120,height=150,width=300) 
        
        self.lbl_category=Label(self.root,text="Total Category\n[ 0 ]",bd=5,relief=RIDGE,bg="#009688",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_category.place(x=1000,y=120,height=150,width=300)    
       
        self.lbl_Product=Label(self.root,text="Total Product\n[ 0 ]",bd=5,relief=RIDGE,bg="#607d8b",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_Product.place(x=300,y=300,height=150,width=300) 
        
        self.lbl_sales=Label(self.root,text="Total Sales\n[ 0 ]",bd=5,relief=RIDGE,bg="#ffc107",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_sales.place(x=650,y=300,height=150,width=300) 
        
        self.lbl_repair=Label(self.root,text="Total Repairing Mobiles\n[ 0 ]",bd=5,relief=RIDGE,bg="#53868B",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_repair.place(x=1000,y=300,height=150,width=300) 
        
        self.lbl_expense=Label(self.root,text="Total Expense\n[ 0 ]",bd=5,relief=RIDGE,bg="#68228B",fg="white", font=("goudy old style",20,"bold"))
        self.lbl_expense.place(x=300,y=485,height=150,width=300) 
        
        self.lbl_cash=Label(self.root,text="Total Urgent Cash\n[ 0 ]",bd=5,relief=RIDGE,bg="#33bbf9",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_cash.place(x=650,y=485,height=150,width=300)      
        
#FOOTER##
        lbl_Footer=Label(self.root,text="IMS-Inventory Management System || Developer by Huzaif \n For Any Techinal Issue Contact: +923215485899",font=("times new roman",12),bg="#4d636d",fg="white").pack(side=BOTTOM,fill=X)
        
        self.update_content()      
        
        
##____________________##
       
    def employee(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=employeClass(self.new_win)  
    
    def supplier(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=supplierclass(self.new_win)       
        
    def category(self):
        self.new_win=Toplevel(self.root) 
        self.new_obj=categoryClass(self.new_win)   
    
    def product(self):
        self.new_win=Toplevel(self.root) 
        self.new_obj=productClass(self.new_win)
        
        
    def repair(self):
        self.new_win=Toplevel(self.root) 
        self.new_obj=repairclass(self.new_win)
    def sales(self):
        self.new_win=Toplevel(self.root) 
        self.new_obj=salesClass(self.new_win)     
    
    def update_content(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()        
        try:
            cur.execute("select * from product")
            product=cur.fetchall()
            self.lbl_Product.config(text=f'Total Product\n[ {str(len(product))} ]')

            cur.execute("select * from supplier")
            supplier=cur.fetchall()
            self.lbl_supplier.config(text=f'Total Supplier\n[ {str(len(supplier))} ]')

            cur.execute("select * from employee")
            employee=cur.fetchall()
            self.lbl_employee.config(text=f'Total Employee\n[ {str(len(employee))} ]')

            cur.execute("select * from repair")
            repair=cur.fetchall()
            self.lbl_repair.config(text=f'Total Repairing Mobile\n[ {str(len(repair))} ]')
            
            cur.execute("select * from category")
            category=cur.fetchall()
            self.lbl_category.config(text=f'Total Category\n[ {str(len(category))} ]')
            bill=len(os.listdir('bill'))
            self.lbl_sales.config(text=f'Total Sales\n[{str(bill)}]')
            time_=time.strftime("%I:%M:%S")
            date_=time.strftime("%d-%m-%Y")
            self.lbl_clock.config(text=f"Welcome To Cell Store | Inventory Management System\t\t Date:{str(date_)}\t\t Time:{str(time_)}") 
            self.lbl_clock.after(200,self.update_content)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)        
    def logout(self):
        self.root.destroy()
        os.system("python login.py")   
    def exit(self):
        self.root.destroy()     
        
if __name__=="__main__":
    root =Tk()
    obj=IMS(root)  
    root.mainloop()     
            