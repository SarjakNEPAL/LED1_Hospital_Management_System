from tkinter import*
from tkinter import PhotoImage
from tkinter import messagebox
from datamethods import *
import admin_panel

def render():
    def signin():
        username=user.get()
        password=code.get()
        if username!="" and password!="":
            a=login(username,password)
            if a=="admin":
                root.destroy()
                admin_panel.render(username)
            if a=="recpt":
                root.destroy()
                import enter_phone_number
                enter_phone_number.render(username)
            else:
            
                messagebox.showerror("Login Failed","Incorrect User ID or Password \n Please try again")
    
        else:
            messagebox.showwarning("Incomplete Fields","Please fill all the fields!")
            root.deiconify()
                    
    root=Tk()
    root.title("Hospital Management System | Login Page")
    root.geometry("925x500+300+200")
    root.resizable(False,False)
    root.iconbitmap("logo.ico")
    image_path =PhotoImage(file=r"bkg.png")  
    bg_image=Label(root,image=image_path)
    bg_image.place(relheight=1,relwidth=1.8)

    frame0=Frame(root, width=400,height=50,bg='grey')
    frame0.place(x=430,y=10)
    topic=Label(frame0,text='Hospital Management System',fg='#57a1f8',bg='white',font=('microsoft YaHei UI Light',23,'bold'))
    topic.pack()
    
    frame=Frame(root,width=350,height=300,bg="white")
    frame.place(x=480,y=100)

    heading=Label(frame,text='LOGIN',fg='#57a1f8',bg='white',font=('microsoft YaHei UI Light',23,'bold'))
    heading.place(x=100,y=5)

    def on_enter(e):
        user.delete(0,'end')

    def on_leave(e):
        name= user.get()
        if name=='':
            user.insert(0,'Username')

    user=Entry(frame,width=25,fg='black',border=0,bg="white",font=('microsoft YaHei UI Light',11))
    user.place(x=30,y=80)
    user.insert(0,'User ID')
    user.bind('<FocusIn>',on_enter)
    user.bind('<FocusOut>',on_leave)

    Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)

    def on_enter(e):
        code.delete(0,'end')

    def on_leave(e):
        name= code.get()
        if name=='':
            code.insert(0,'password')

    code=Entry(frame,width=25,fg='black',border=0,bg="white",font=('microsoft YaHei UI Light',11))
    code.place(x=30,y=150)
    code.insert(0,'password')
    code.bind('<FocusIn>',on_enter)
    code.bind('<FocusOut>',on_leave)

    Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)

    Button(frame,width=39,pady=7,text='Login',bg='#57a1f8',fg='white',border=0,command=signin).place(x=35,y=204)
    root.mainloop()
