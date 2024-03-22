from tkinter import *
from tkinter import PhotoImage, messagebox

def render(user):
    global a
    a=user
    def back():
        window.destroy()
        global a
        if a=="admin":
            import patients_panel
            patients_panel.render()
        else:
            import enter_phone_number
            enter_phone_number.render(a)
    isok = False
    def signup():
        global a
        Patient_name = user.get()
        Phone_number = code.get()
        Address = address.get()
        Gender = gender.get()
        if (Patient_name != "Patient_name") and (Phone_number != "Phone_number") and (Address != "Address") and (Gender != 0):
            if Phone_number.isnumeric():
                from datamethods import add_patient as sign
                if sign(Patient_name, Address, Gender, Phone_number):
                    messagebox.showinfo("Successful", "Successfully registered!\n \
                                        Please re-enter patient phone number to interact")
                    back()
                else:
                    messagebox.showerror("OOPS!", "The number already registered to the account!\nTry \
                                          again with another phone number or re-enter the number in search")
            else:
                messagebox.showwarning("OOPS!", "Phone number must be numeric")
                code.delete(0, END)
        else:
            messagebox.showwarning("OOPS!", "All the fields must be filled!")

    window = Tk()
    window.title("Registration page")
    window.geometry("1025x500+300+200")
    window.resizable(False, False)
    window.iconbitmap("logo.ico")
    image_path = PhotoImage(file="patient.png")
    bg_image = Label(window, image=image_path)
    bg_image.place(relheight=1, relwidth=1.6)

    frame = Frame(window, width=350, height=490, bg="white")
    frame.place(x=680, y=50)

    heading = Label(frame, text='Add patient', fg='#57a1f8', bg='white', font=('microsoft YaHei UI Light', 23, 'bold'))
    heading.place(x=100, y=5)

    user = Entry(frame, width=25, fg='black', border=0, bg="white", font=('microsoft YaHei UI Light', 11))
    user.place(x=30, y=80)
    user.insert(0, 'Patient_name')

    code = Entry(frame, width=25, fg='black', border=0, bg="white", font=('microsoft YaHei UI Light', 11))
    code.place(x=30, y=150)
    code.insert(0, ' Phone_number')

    address = Entry(frame, width=25, fg='black', border=0, bg="white", font=('microsoft YaHei UI Light', 11))
    address.place(x=30, y=210)
    address.insert(0, ' Address')

    Label(frame, fg='black', bg="white", font=('microsoft YaHei UI Light', 11), text="Gender: ").place(x=30, y=270)

    gender = StringVar()
    gender.set(0)
    gender_male = Radiobutton(frame, fg='black', bg="white", font=('microsoft YaHei UI Light', 11), text="Male |", value="M", variable=gender)
    gender_male.place(x=90, y=270)
    gender_female = Radiobutton(frame, fg='black', bg="white", font=('microsoft YaHei UI Light', 11), text="Female |", value="F", variable=gender)
    gender_female.place(x=160, y=270)
    gender_other = Radiobutton(frame, fg='black', bg="white", font=('microsoft YaHei UI Light', 11), text="Other", value="O", variable=gender)
    gender_other.place(x=250, y=270)
    Button(frame, width=39, pady=7, text='Add patient', bg='#57a1f8', fg='white', border=0, command=signup).place(x=35, y=340)

    Button(frame, width=6, text='Go back', border=0, bg='#57a1f8', cursor='hand2', fg='white',command=back).place(x=150, y=390)

    window.mainloop()
  

if __name__ == "__main__":
    render("repct")
