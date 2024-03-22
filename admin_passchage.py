from tkinter import*
from tkinter import PhotoImage
from tkinter import messagebox
import datamethods

def render():
    window=Tk()
    window.title("Admin Password Change")
    window.geometry("1020x500+300+200")
    window.resizable(False,False)
    window.iconbitmap("logo.ico")

    def signup():
        o_pass=user.get()
        password=code.get()
        conform_password=conform_code.get()
        if password==conform_password:
            if o_pass!=conform_password:
                if datamethods.admchgpass(f"{o_pass}",f"{conform_password}"):
                    messagebox.showinfo("Yehh!",f"Password updated successfully.\n new password: {conform_password}")
                    goback()
                else:
                    messagebox.showerror("Opps!","old password is wrong")
            else:
                messagebox.showwarning("Opps!","old password and new password cannot be same")
                user.delete(0,END)
                code.delete(0,END)
                conform_code.delete(0,END)
        else:
                messagebox.showwarning("Opps!","password doesn't match")
                code.delete(0,END)
                conform_code.delete(0,END)
    
    image_path =PhotoImage(file=r"regg.png")
    bg_image=Label(window,image=image_path)
    bg_image.place(relheight=1,relwidth=1.5)

    frame=Frame(window,width=350,height=390,bg="white")
    frame.place(x=480,y=50)

    heading=Label(frame,text='admin\nChange Password',fg='#57a1f8',bg='white',font=('microsoft YaHei UI Light',15,'bold'))
    heading.place(x=100,y=5)

    def on_enter(e):
        user.delete(0,'end')

    def on_leave(e):
        if user.get()=='':
            user.insert(0,'Old Password')

    user=Entry(frame,width=25,fg='black',border=0,bg="white",font=('microsoft YaHei UI Light',11))
    user.place(x=30,y=80)
    user.insert(0,'old password')
    user.bind('<FocusIn>',on_enter)
    user.bind('<FocusOut>',on_leave)

    Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)

    def on_enter(e):
        code.delete(0,'end')

    def on_leave(e):
        if code.get()=='':
            code.insert(0,'confirm password')

    code=Entry(frame,width=25,fg='black',border=0,bg="white",font=('microsoft YaHei UI Light',11))
    code.place(x=30,y=220)
    code.insert(0,'confirm password')
    code.bind('<FocusIn>',on_enter)
    code.bind('<FocusOut>',on_leave)

    Frame(frame,width=295,height=2,bg='black').place(x=25,y=247)

    def on_enter(e):
        conform_code.delete(0,'end')

    def on_leave(e):
        if conform_code.get()=='':
            conform_code.insert(0,'new password')

    conform_code=Entry(frame,width=25,fg='black',border=0,bg="white",font=('microsoft YaHei UI Light',11))
    conform_code.place(x=30,y=150)
    conform_code.insert(0,'new password')
    conform_code.bind('<FocusIn>',on_enter)
    conform_code.bind('<FocusOut>',on_leave)

    Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)

    Button(frame,width=39,pady=7,text='Update Password',bg='#57a1f8',fg='white',border=0,command=signup).place(x=35,y=280)

    def goback():
        window.destroy()
        import admin_panel
        admin_panel.render("admin")

    sign_up=Button(frame,width=6,text='Go back',border=0,bg='#57a1f8',cursor='hand2',fg='white',command=goback)
    sign_up.place(x=210,y=340)

    window.mainloop()
