from tkinter import *
from tkcalendar import DateEntry
import sqlite3
from tkinter import messagebox

# Establish connection and create a cursor
conn = sqlite3.connect('database.db')
c = conn.cursor()

# Create Appointments table if it doesn't exist
import datamethods
datamethods.dbmkr()


def render(phone_number,user):
    u=user
    def back(u):
        root.destroy()
        import patients_all_appointments
        patients_all_appointments.render(phone_number,user)

    def book_appointment(u): #   Function to add an appointment to the database
        date = date_entry.get_date().strftime("%m/%d/%Y") #  Get selected date in "MM/DD/YY" format
        time = time_var.get() #  Get selected time
        department = department_var.get() #   Get selected department


        # Check if all fields are filled or not
        if date and time and department != "Choose Doctor": 
            # Insert data into database.
            c.execute("INSERT INTO Appointments (bookedby_id,date, time, doctor, phone_number) VALUES (?,?, ?, ?, ?)", 
                      (u,date,time, department, phone_number)) #parameters
            conn.commit() #  Save changes

            messagebox.showinfo("oops",f"Appointment booked for {phone_number} on {date} at {time} with {department}.")
            clear_entries() #Clear entries for next use
            back(u) #Go back to previous window
        else: #  If any field is empty then show error message
            messagebox.showwarning("oops","Please fill out all the fields." )

    def cancel_appointment(u):
        back(u)

    def clear_entries():
        name_entry.delete(0, END)
        date_entry.set_date("02/26/2024")
        time_var.set("10:00 AM")
        department_var.set("Choose Doctor")

    def next_user(u):
        root.destroy()
        if u=="admin":
            import admin_panel
            admin_panel.render("admin")
        else:
            import enter_phone_number
            enter_phone_number.render(u)

    root = Tk()
    root.title("Book Appointment")
    root.configure(bg="#f0f0f0")
    root.geometry("800x600")
    root.iconbitmap("logo.ico")
    navbar = Frame(root, bg="#1a237e", height=30)
    navbar.pack(side=TOP, fill=X)

    patient_name_label = Label(navbar, text=f"{phone_number}", fg="white", bg="#1a237e", font=("Arial", 10))
    patient_name_label.pack(side=RIGHT, padx=10)

    card_frame = Frame(root, bg="white", bd=2, relief="groove")
    card_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

    labels_font = ("Arial", 12)
    labels_fg = "black"
    labels_bg = "white"
    name_label = Label(card_frame, text="Name:", font=labels_font, fg=labels_fg, bg=labels_bg)
    date_label = Label(card_frame, text="Date:", font=labels_font, fg=labels_fg, bg=labels_bg)
    time_label = Label(card_frame, text="Time:", font=labels_font, fg=labels_fg, bg=labels_bg)
    department_label = Label(card_frame, text="Doctor:", font=labels_font, fg=labels_fg, bg=labels_bg)

    entry_bg = "#f8f8f8"
    name_entry = Entry(card_frame, bg=entry_bg)
    date_entry = DateEntry(card_frame, bg=entry_bg, date_pattern="MM/dd/yyyy", date_format="mm/dd/y", width=12)
    time_var = StringVar(root)
    time_var.set("10:00 AM")
    time_dropdown = OptionMenu(card_frame, time_var, "10:00 AM", "12:00 PM", "02:00 PM", "04:00 PM")
    department_var = StringVar(root)
    department_var.set("Choose Doctor")
    doctors = ["Dr. Yudip Upreti", "Dr. Sarjak Bhandari", "Dr. Anisha Shah", "Dr. Ravi Bhattarai"]
    department_dropdown = OptionMenu(card_frame, department_var, *doctors)

    button_bg = "#1a237e"
    button_fg = "white"
    book_button = Button(card_frame, text="Book Appointment", command=lambda:book_appointment(user), bg=button_bg, fg=button_fg)
    cancel_button = Button(card_frame, text="Cancel Appointment", command=lambda:cancel_appointment(user), bg=button_bg, fg=button_fg)
    next_button = Button(card_frame, text="Next User", command=lambda:next_user(user), bg=button_bg, fg=button_fg)

    labels_padx = 10
    labels_pady = 5
    entry_padx = 10
    entry_pady = 5
    labels_sticky = "e"
    labels_columnspan = 2

    date_label.grid(row=1, column=0, padx=labels_padx, pady=labels_pady, sticky=labels_sticky)
    date_entry.grid(row=1, column=1, padx=entry_padx, pady=entry_pady)
    time_label.grid(row=2, column=0, padx=labels_padx, pady=labels_pady, sticky=labels_sticky)
    time_dropdown.grid(row=2, column=1, padx=entry_padx, pady=entry_pady)
    department_label.grid(row=3, column=0, padx=labels_padx, pady=labels_pady, sticky=labels_sticky)
    department_dropdown.grid(row=3, column=1, padx=entry_padx, pady=entry_pady)
    book_button.grid(row=4, columnspan=labels_columnspan, padx=10, pady=10)
    cancel_button.grid(row=5, columnspan=labels_columnspan, padx=10, pady=10)
    next_button.grid(row=6, columnspan=labels_columnspan, padx=10, pady=10)

    root.mainloop()


if __name__ == "__main__":
    render("9876543210","recpt")
