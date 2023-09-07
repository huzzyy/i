from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3

class repairclass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1150x550+300+130")
        self.root.title("Inventory Management System | Developed By Huzaif")
        self.root.config(bg='white')    
        self.root.focus_force() 
        self.root.resizable(0,0)
        
              ##ALL VARIABLE##
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()        
        self.var_repair_invoice=StringVar() 
        self.var_name=StringVar()       
        self.var_mobile_model=StringVar()
        self.var_quantity=StringVar()       
      
      
      
      
        ##SERACH FRAME###
    
        
        ##OPTINONS##
        lbl_search=Label(self.root,text="Invoice No.",bg='white',font=("goudy old style",15))
        lbl_search.place(x=750,y=80)
        

        
        txt_search=Entry(self.root,textvariable=self.var_searchtxt,font=("goudy old style",15),bg="lightyellow").place(x=850,y=80, width=165)
        btn_search=Button(self.root,text="Search",command=self.search,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=1030,y=80,width=90,height=26)      
      
      
        
        ##TITLE###########
        lbl_title=Label(self.root,text="Repairing Mobile Details",font=("goudy old style",30),bg="#184a45",fg='white',bd=3,relief=RIDGE).pack(side=TOP,fill=X,padx=10,pady=20)
     
        
    
        
        ##CONTANT##
        lbl_repair_invoice=Label(self.root,text="Invoice No.",font=("goudy old style",15),bg="white").place(x=50,y=105)                       
        txt_repair_invoice=Entry(self.root,textvariable=self.var_repair_invoice,font=("goudy old style",15),bg="lightyellow").place(x=180,y=105,width=180)

        ##RROW  2###
        lbl_name=Label(self.root,text="Name",font=("goudy old style",15),bg="white").place(x=50,y=145)                  
        txt_name=Entry(self.root,textvariable=self.var_name,font=("goudy old style",15),bg="lightyellow").place(x=180,y=148,width=180)   
        
        
        ##RROW  2###
        lbl_name=Label(self.root,text="Mobile Model",font=("goudy old style",15),bg="white").place(x=49,y=185)                  
        txt_name=Entry(self.root,textvariable=self.var_mobile_model,font=("goudy old style",15),bg="lightyellow").place(x=180,y=188,width=180)
        
        ##RROW  3###
        lbl_name=Label(self.root,text="Quantity",font=("goudy old style",15),bg="white").place(x=50,y=220)                  
        txt_name=Entry(self.root,textvariable=self.var_quantity,font=("goudy old style",15),bg="lightyellow").place(x=180,y=225,width=180)
        
        ##ROW 4##
        lbl_desc=Label(self.root,text="Description",font=("goudy old style",15),bg="white").place(x=50,y=260)                                 
        self.txt_desc=Text(self.root,font=("goudy old style",15),bg="lightyellow")
        self.txt_desc.place(x=180,y=265,width=470,height=100)    
        
        
        ##BUTTON###
        btn_add=Button(self.root,text="Save",command=self.add,font=("goudy old style",15),bg="#2196f3",fg="white",cursor="hand2").place(x=180,y=400,width=110,height=35)
        btn_update=Button(self.root,text="Update",command=self.update,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=300,y=400,width=110,height=35)
        btn_delete=Button(self.root,text="Delete",command=self.delete,font=("goudy old style",15),bg="#f44336",fg="white",cursor="hand2").place(x=420,y=400,width=110,height=35)
        btn_clear=Button(self.root,text="Clear",command=self.clear,font=("goudy old style",15),bg="#607d8b",fg="white",cursor="hand2").place(x=540,y=400,width=110,height=35)   
        
        
        
  ##REPAIRER DETAISL#@###
        rep_frame=Frame(self.root,bd=3,relief=RIDGE)
        rep_frame.place(x=750,y=120,width=380,height=350)
        
        scrolly=Scrollbar(rep_frame,orient=VERTICAL)
        scrollx=Scrollbar(rep_frame,orient=HORIZONTAL)
        
        
        self.repairTable=ttk.Treeview(rep_frame,columns=("invoice","name","model","quantity","desc"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.repairTable.xview)
        scrolly.config(command=self.repairTable.yview)
        self.repairTable.heading("invoice",text="Invoice No.")
        self.repairTable.heading("name",text="Name")
        self.repairTable.heading("model",text="Mobile Model")
        self.repairTable.heading("quantity",text="Quantity")
        self.repairTable.heading("desc",text="Description")

        
        self.repairTable["show"]="headings"
        
        self.repairTable.column("invoice",width=90)
        self.repairTable.column("name",width=100)
        self.repairTable.column("model",width=100)
        self.repairTable.column("quantity",width=100)
        self.repairTable.column("desc",width=100)       
        self.repairTable.pack(fill=BOTH,expand=1)
        self.repairTable.bind("<ButtonRelease-1>",self.get_data)             
        
        self.show()


#######################################################################


    def add(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_repair_invoice.get()=="":
                messagebox.showerror("Error","Invoice  must be required",parent=self.root)
            
            else:
                cur.execute("Select * from repair where invoice=?",(self.var_repair_invoice.get(),))    
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Invoice number is already assigned, try different",parent=self.root)
                else:   
                    cur.execute("Insert into repair(invoice,name,model,quantity,desc)values(?,?,?,?,?)",(
                                        self.var_repair_invoice.get(),
                                        self.var_name.get(),                                        
                                        self.var_mobile_model.get(),
                                        self.var_quantity.get(),                                                                         
                                        self.txt_desc.get('1.0',END),
                                        
               
                    ))    
                    con.commit()
                    messagebox.showinfo("Success","Repairer Added Successfully",parent=self.root)
                    self.show()
            
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)
            
            
    def show(self):
         con=sqlite3.connect(database=r'ims.db')
         cur=con.cursor()
         try:
             cur.execute("select * from repair")
             rows=cur.fetchall()
             self.repairTable.delete(*self.repairTable.get_children())
             for row in rows:
                 self.repairTable.insert('',END,values=row)
             
         
         
         except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)    
    
    def get_data(self,ev):
        f=self.repairTable.focus()
        content=(self.repairTable.item(f))       
        row=content['values']
               
        self.var_repair_invoice.set(row[0])
        self.var_name.set(row[1])     
        self.var_mobile_model.set(row[2])
        self.var_quantity.set(row[3])                                            
        self.txt_desc.delete('1.0',END)
        self.txt_desc.insert(END,row[4])
   
      
      
      #############################################         
    def update(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_repair_invoice.get()=="":
                messagebox.showerror("Error","Invoice No. Must be required",parent=self.root)
            
            else:
                cur.execute("Select * from repair where invoice=?",(self.var_repair_invoice.get(),))    
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Invoice No.",parent=self.root)
                else:
                    cur.execute("Update  repair set name=?,model=?,quantity=?,desc=? where invoice=?",(

                                        self.var_name.get(),                                     
                                        self.var_mobile_model.get(),  
                                        self.var_quantity.get(),                                                                             
                                        self.txt_desc.get('1.0',END),                                       
                                        self.var_repair_invoice.get(),
               
                    ))    
                    con.commit()
                    messagebox.showinfo("Success","Repairer Updated Successfully",parent=self.root)
                    self.show()
            
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)     
                        
    def delete(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_repair_invoice.get()=="":
                messagebox.showerror("Error","Invoice No. Must be required",parent=self.root)
            
            else:
                cur.execute("Select * from repair where invoice=?",(self.var_repair_invoice.get(),))    
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Invoice No.",parent=self.root)
                else:
                     op=messagebox.askyesno("Confrim","Do you really want to delete?",parent=self.root)
                     if op == True:
                         cur.execute("delete from repair where invoice=?",(self.var_repair_invoice.get(),))
                         con.commit()
                                                                  
                     messagebox.showinfo("Delete","Repairer Deleted Successfully",parent=self.root)                    
                     self.clear()
                   
        
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)         
    def clear(self):
        self.var_repair_invoice.set("")
        self.var_name.set("")     
        self.var_mobile_model.set("")   
        self.var_quantity.set("")                                          
        self.txt_desc.delete('1.0',END)
        self.var_searchtxt.set("")        
        self.show()
        
        
        
    def search(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:            
            if self.var_searchtxt.get()=="": 
                messagebox.showerror("Error","Invoice No. should be required",parent=self.root)                   
            else:
                cur.execute("select * from repair where invoice=? ",(self.var_searchtxt.get(),))                                       
                row=cur.fetchone()
                if row!=None:                    
                    self.repairTable.delete(*self.repairTable.get_children())                 
                    self.repairTable.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No record found!!!!",parent=self.root)        
                    
            
            
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)          
        
if __name__=="__main__":
    root =Tk()
    obj=repairclass(root)  
    root.mainloop()     