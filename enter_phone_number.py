<<<<<<< HEAD
from tkinter import *
import datamethods
import sqlite3
from tkinter import messagebox

def render(u):
    root = Tk()
    root.title("Phone Number Input")
    root.geometry("800x600")
    root.configure(bg="#f0f0f0")
    root.iconbitmap("logo.ico")

    def continue_clicked(u): 
        def patient_here(a): #patient varify
            if str(a).isnumeric()==True: #string and numerics
                datamethods.dbmkr() #make db
                link=sqlite3.connect("database.db") #db
                cursor=link.cursor() #consor
                cursor.execute(F"SELECT phone_number FROM Patients WHERE phone_number={a}") #db
                gg=cursor.fetchone() #consor
                link.close() #colsed from here
                if gg!=None: #condition
                    return True #check
                else: #condition
                    return False #check
            else: #condition
                messagebox.showwarning("Oops","Enter Number in Phone number") #check
        
        phone_number = phone_number_entry.get() #patience phone number
        if  phone_number!="": #if empty then
            if patient_here(phone_number): #calling the function
                root.destroy() #closing window
                import patients_all_appointments #  going to next page
                patients_all_appointments.render(phone_number,u) #  passing value
            else: # else condition
                
                messagebox.showerror("Oops!","No user found Redirecting to New account creation") # error msg
                root.destroy() #     closing window
                import patientadd # going to new account page
                patientadd.render(u) #  passing values
        else: # else condition
            messagebox.showwarning("Oops","Phone number cannot be empty") #  warning msg
        
    def bhk():
        root.destroy()
        import main
        
    frame = Frame(root, bg="#ffffff", bd=2, relief=SOLID)
    frame.place(relx=0.5, rely=0.5, anchor=CENTER)

    phone_number_label = Label(frame, text=f"Hi {u}!,Enter Patient's phone number:", font=("Arial", 24), bg="#ffffff")
    phone_number_label.pack(pady=10)

    phone_number_entry = Entry(frame, font=("Arial", 24), bd=2, relief=SOLID)
    phone_number_entry.pack(pady=10, padx=20, ipady=5, fill=X)

    continue_button = Button(frame, text="Continue", font=("Arial", 24), command=lambda:continue_clicked(u), bg="#1a237e", fg="white", bd=2, relief=RAISED)
    continue_button.pack(pady=20, padx=20, ipadx=10, ipady=5, fill=X)
    logout_button = Button(frame, text="Log Out", font=("Arial", 24), command=bhk, bg="grey", fg="blue", bd=2, relief=RAISED)
    logout_button.pack(pady=20, padx=20, ipadx=10, ipady=5, fill=X)
    root.mainloop()
=======
from tkinter import *
import datamethods
import sqlite3
from tkinter import messagebox

def render(u):
    root = Tk()
    root.title("Phone Number Input")
    root.geometry("800x600")
    root.configure(bg="#f0f0f0")
    root.iconbitmap("logo.ico")
    def continue_clicked(u):
        def patient_here(a):
            if str(a).isnumeric()==True:    
                datamethods.dbmkr()
                link=sqlite3.connect("database.db")
                cursor=link.cursor()
                cursor.execute(F"SELECT phone_number FROM Patients WHERE phone_number={a}")
                gg=cursor.fetchone()
                link.close()
                if gg!=None:
                    return True
                else:
                    return False
            else:
                messagebox.showwarning("Oops","Enter Number in Phone number")
        
        phone_number = phone_number_entry.get()
        if  phone_number!="":
            cond=patient_here(phone_number)
            if cond:
                root.destroy()
                import patients_all_appointments
                patients_all_appointments.render(phone_number,u)
            elif cond==False:
                
                messagebox.showerror("Oops!","No user found Redirecting to New account creation")
                root.destroy()
                import patientadd
                patientadd.render(u)
        else:
            messagebox.showwarning("Oops","Phone number cannot be empty")
        
    def bhk():
        root.destroy()
        import main
    frame = Frame(root, bg="#ffffff", bd=2, relief=SOLID)
    frame.place(relx=0.5, rely=0.5, anchor=CENTER)

    phone_number_label = Label(frame, text=f"Hi {u}!,Enter Patient's phone number:", font=("Arial", 24), bg="#ffffff")
    phone_number_label.pack(pady=10)

    phone_number_entry = Entry(frame, font=("Arial", 24), bd=2, relief=SOLID)
    phone_number_entry.pack(pady=10, padx=20, ipady=5, fill=X)

    continue_button = Button(frame, text="Continue", font=("Arial", 24), command=lambda:continue_clicked(u), bg="#1a237e", fg="white", bd=2, relief=RAISED)
    continue_button.pack(pady=20, padx=20, ipadx=10, ipady=5, fill=X)
    logout_button = Button(frame, text="Log Out", font=("Arial", 24), command=bhk, bg="grey", fg="blue", bd=2, relief=RAISED)
    logout_button.pack(pady=20, padx=20, ipadx=10, ipady=5, fill=X)
    root.mainloop()
>>>>>>> sarjak
