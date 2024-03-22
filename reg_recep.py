from tkinter import*
from tkinter import PhotoImage
from tkinter import messagebox
from datamethods import add_receptionist


window=Tk()
window.title("add staff page")
window.geometry("925x500+300+200")
window.resizable(False,False)
window.iconbitmap("logo.ico")
def goback():
    window.destroy()
    import staff_information
    staff_information.render()
    
def signup():
    username=user.get()
    password=code.get()
    conform_password=conform_code.get()
    if username!="username" and password!="password" and conform_password!="confirm_password":
        if password==conform_password:
            if len(password)>8:
                aaa=add_receptionist(username,password)
                if aaa[1]:
                    messagebox.showinfo("Success",f"Successfully added profile for:\n Username:{username}\n with userid:{aaa[0]}  \n password: {password}")
                else:
                    messagebox.showerror("Failure","Data already exist")
            else:
                messagebox.showwarning("OOPS!","password must be longer than 8 characters")
        else:
            messagebox.showwarning("OOPS!","Password do not match")
    else:
        messagebox.showwarning("OOPS!","All fields are mandatory to fill")
     




                






image_path =PhotoImage(file=r"regg.png")
bg_image=Label(window,image=image_path)
bg_image.place(relheight=1,relwidth=1.7)


###creating_regggistrationnbox####$$$%^&*(_______________________________----------___++++++++++++)

frame=Frame(window,width=350,height=390,bg="white")
frame.place(x=480,y=50)

heading=Label(frame,text='Add Staff',fg='#57a1f8',bg='white',font=('microsoft YaHei UI Light',23,'bold'))
heading.place(x=100,y=5)

##############################################################################################################################

def on_enter(e):
    user.delete(0,'end')

def on_leave(e):
    if user.get()=='':
        user.insert(0,'Username')

user=Entry(frame,width=25,fg='black',border=0,bg="white",font=('microsoft YaHei UI Light',11))
user.place(x=30,y=80)
user.insert(0,'username')
user.bind('<FocusIn>',on_enter)
user.bind('<FocusOut>',on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=20,y=107)

####################################################################_______________________________________________________---

def on_enter(e):
    code.delete(0,'end')

def on_leave(e):
    if code.get()=='':
         code.insert(0,'password')

code=Entry(frame,width=25,fg='black',border=0,bg="white",font=('microsoft YaHei UI Light',11))
code.place(x=30,y=150)
code.insert(0,'password')
code.bind('<FocusIn>',on_enter)
code.bind('<FocusOut>',on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)

####################################################################_______________________________________________________---

def on_enter(e):
    conform_code.delete(0,'end')

def on_leave(e):
    if conform_code.get()=='':
        conform_code.insert(0,'confirm password')

conform_code=Entry(frame,width=25,fg='black',border=0,bg="white",font=('microsoft YaHei UI Light',11))
conform_code.place(x=30,y=220)
conform_code.insert(0,'confirm password')
conform_code.bind('<FocusIn>',on_enter)
conform_code.bind('<FocusOut>',on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=247)

####################################################################_______________________________________________________---

Button(frame,width=39,pady=7,text='Add ',bg='#57a1f8',fg='white',border=0,command=signup).place(x=35,y=280)

Label=Label(frame,fg='black',bg='white',font=('microsoft YaHei UI Light',9))


sign_up=Button(frame,width=6,text='Go back',border=0,bg='#57a1f8',cursor='hand2',fg='white',command=goback)
sign_up.place(x=150,y=340)
            





window.mainloop()