import tkinter as tk
from tkinter import messagebox
from tkcalendar import DateEntry
from tkinter import ttk
import subprocess
import sqlite3

def render(phone_number,u):
    global a
    global b
    b= u
    a = phone_number

    def add_appointment(u):
        global a
        root.destroy()
        import name_of_patient
        name_of_patient.render(a,u)

    def delete_appointment(): #delete the selected appointment from the database and refresh the
        selected_item = tree.selection() #get the index of the selected item in the list
        if selected_item: # if there is an item selected
            item_values = tree.item(selected_item, 'values') #   get the values of the selected item
            bookedby_id = item_values[0] #   take the first value which is the id of the
            conn = sqlite3.connect('database.db') # open the database
            c = conn.cursor() #  create a cursor object to interact with the database
            c.execute("DELETE FROM Appointments WHERE bookedby_id=?", (bookedby_id,)) #  execute SQL command
            conn.commit() #  commit the changes to the database
            conn.close() #   close the connection to the database
            # Remove the item  from the treeview
            tree.delete(selected_item) #     remove the selected item
        else: # if nothing is selected display error message
            # Show a message if no item is  selected
            tk.messagebox.showinfo("No Selection", "Please select an appointment to delete.") #  show info dialog box

    def update_appointment():
        selected_item = tree.selection()
        if selected_item:
            # Get the selected appointment details
            item_values = tree.item(selected_item, 'values')
            bookedby_id = item_values[0]

            # Open a popup window for updating appointment
            popup = tk.Toplevel()
            popup.title("Update Appointment")
            popup.geometry("300x200")

            # Create a frame to hold the fields
            frame = tk.Frame(popup)
            frame.pack(expand=True, fill="both", padx=20, pady=20)

            # Date entry
            ttk.Label(frame, text="Date:").grid(row=0, column=0, sticky="w")
            date_entry = ttk.Entry(frame)
            date_entry.grid(row=0, column=1, padx=5, pady=5)

            # Time selection
            ttk.Label(frame, text="Time:").grid(row=1, column=0, sticky="w")
            time_combobox = ttk.Combobox(frame, values=["10:00 AM", "12:00 PM", "02:00 PM", "04:00 PM"])
            time_combobox.grid(row=1, column=1, padx=5, pady=5)

            # Function to handle updating the appointments
            def update(): #  define function
                # Get the new date & time
                new_date = date_entry.get() #    get the value of the Entry widget as string
                new_time = time_combobox.get()  #    get the selected value in the Combobox

                # Update the appointments in the database
                conn = sqlite3.connect('database.db') #  connect to the SQLite database
                c = conn.cursor() #  create cursor object
                c.execute("UPDATE Appointments SET date=?, time=? WHERE bookedby_id=?", (new_date, new_time, bookedby_id))
                conn.commit()   # commit changes after each command
                conn.close() #close connection when done with it

                # Update the treeview with new datas
                display_appointments() # refresh the listbox content
                # Close the popup windows
                popup.destroy() # destroy the current Tkinter window

            # Button to update appointment
            update_button = ttk.Button(frame, text="Update", command=update)
            update_button.grid(row=2, columnspan=2, pady=10)

        else:
            # Show a message if no item is selected
            tk.messagebox.showinfo("No Selection", "Please select an appointment to update.")

    def display_appointments(search_phone_number=None): #     define function
        global a # make variable available outside this function
        if search_phone_number: #    If there's a phone number provided for searching
            # Check if the phone number exists in the  database
            conn = sqlite3.connect('database.db') #  Connect to the SQLite database
            c = conn.cursor() #  Create a Cursor object
            c.execute("SELECT * FROM Appointments WHERE phone_number=?", (search_phone_number,)) # Execute SQL query
            result = c.fetchone() #  Fetch one row from the query result (if
            conn.close() # close   

            if not result: #        No match found
                tk.messagebox.showinfo("Phone Number Not Found", "The entered phone number does not exist in the database.")
                return #     Exit the function

        # Connect to the database.
        conn = sqlite3.connect('database.db') #  Open a connection to the database
        c = conn.cursor() #       Create a Cursor object

        # SQL query to fetch appointments.
        if search_phone_number: #       If we are looking for something specific
            c.execute("SELECT bookedby_id, date, time, doctor, phone_number FROM Appointments WHERE phone_number=?", (search_phone_number,))
            gk.config(text=f"{search_phone_number}")
        else: # Otherwise show all data
            c.execute("SELECT bookedby_id, date, time, doctor, phone_number FROM Appointments WHERE phone_number=?",(a,))

        appointments = c.fetchall() #Get all rows from the query result

        # Clear existing items in the treeview.
        for item in tree.get_children(): #For each item in the treeview 
            tree.delete(item) # Delete it

        # Display appointments in the treeview.
        for appointment in appointments: #   For each appointment
            tree.insert('', 'end', values=appointment) # Add it to the treeview

        # Close the connection.
        conn.close() #close

    def search_appointments():
        search_phone_number = search_entry.get()
        if search_phone_number:
            display_appointments(search_phone_number)
        else:
            tk.messagebox.showinfo("Empty Field", "Please enter a phone number to search.")

    def back(u):
        root.destroy()
        if u=="admin":
            import admin_panel
            admin_panel.render('admin')
        else:
            import enter_phone_number
            enter_phone_number.render(u)

    root = tk.Tk()
    root.title("Patient All Appointments")
    root.geometry("800x600")
    root.iconbitmap("logo.ico")
    style = ttk.Style()
    style.configure("Navbar.TFrame", background="#1a237e")
    style.configure("Navbar.TLabel", background="#1a237e", foreground="white")

    navbar = ttk.Frame(root, height=50, style="Navbar.TFrame")
    navbar.grid(row=0, column=0, columnspan=2, sticky="ew")

    ttk.Label(navbar, text="Appointments", font=("Arial", 18), style="Navbar.TLabel").pack(side=tk.LEFT, padx=10)
    gk=ttk.Label(navbar, text=f"{phone_number}", font=("Arial", 18), style="Navbar.TLabel")
    gk.pack(side=tk.RIGHT, padx=10)

    separator = ttk.Separator(root, orient="horizontal")
    separator.grid(row=1, column=0, columnspan=2, sticky="ew")

    tree = ttk.Treeview(root, columns=('Booked by', 'Date', 'Time', 'Doctor', 'Phone Number'), show='headings')
    tree.heading('Booked by', text='Booked by')
    tree.heading('Date', text='Date')
    tree.heading('Time', text='Time')
    tree.heading('Doctor', text='Doctor')
    tree.heading('Phone Number', text='Phone Number')
    tree.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

    separator_below_terminal = ttk.Separator(root, orient="horizontal")
    separator_below_terminal.grid(row=3, column=0, columnspan=2, sticky="ew")

    root.rowconfigure(2, weight=1)
    root.columnconfigure(0, weight=1)

    button_frame = ttk.Frame(root)
    button_frame.grid(row=4, column=0, columnspan=2, pady=10)

    ttk.Button(button_frame, text="Add Appointment", command=lambda:add_appointment(u)).pack(side=tk.LEFT, padx=10, pady=10)
    ttk.Button(button_frame, text="Delete", command=delete_appointment).pack(side=tk.LEFT, padx=10, pady=10)
    ttk.Button(button_frame, text="Update Appointment", command=update_appointment).pack(side=tk.LEFT, padx=10, pady=10)
    ttk.Button(button_frame, text="Back", command=lambda:back(u)).pack(side=tk.RIGHT, padx=10, pady=10)

    search_entry = ttk.Entry(button_frame)
    search_entry.pack(side=tk.RIGHT, padx=10, pady=10)
    search_button = ttk.Button(button_frame, text="Search", command=search_appointments)
    search_button.pack(side=tk.RIGHT, padx=10, pady=10)

    # Display all appointments initially
    display_appointments()

    root.mainloop()

if __name__ == "__main__":
    render("9876543210",'admin')
