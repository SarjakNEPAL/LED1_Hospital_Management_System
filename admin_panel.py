import os
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3

search_entry = None
terminal_treeview = None

def search(): #functio
    '''Used to search dat'''
    global search_entry,terminal_treeview
    k= search_entry.get()

    if not k:
        messagebox.showwarning("Warning! ", "Search is  empty")
        return False
    
    conn=sqlite3.connect('database.db')
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM Patients WHERE phone_number=?", (k,))
    patient_data=cursor.fetchone()

    if patient_data: #if the searched number exists in database  show it on tree view
        name, address, gender,phone_number=patient_data

        for row in terminal_treeview.get_children(): #removes all  children  of the tree view widget
            terminal_treeview.delete(row) #deleting each  child one by one

        terminal_treeview.insert("", "end", values=(name, address, gender,phone_number)) # insearch
    else: #comment
        messagebox.showinfo("Info", "No data found for the provided phone number! ")
    conn.close() #closing  connection

def render(user):
    global search_entry, terminal_treeview
    def on_double_click(event):
        item = terminal_treeview.selection()[0]
        name = terminal_treeview.item(item, "values")[3]
        root.destroy()
        import patients_all_appointments
        patients_all_appointments.render(name,'admin')
    def staffinfo():
        root.destroy()
        import staff_information
        if staff_information.render():
            render("admin")
    def appoint(user): #appoint scene switch        
        k = search_entry.get() #getting value from entry box
        if not k: #check whether empty or not
            messagebox.showwarning("Warning!", "Search is empty ") 
            return #return to previous window

        conn = sqlite3.connect('database.db') #connect database
        cursor = conn.cursor() #starting cursor
        cursor.execute("SELECT phone_number FROM Patients WHERE phone_number=?", (k,))
        a= cursor.fetchone() #fetching result
        if a==None: #if no such user exist then
            messagebox.showerror("Oops!","No patient available with number, redirecting to account creation") # display error message
            root.destroy() 
            import patientadd #import patient registration panel
            patientadd.render("admin") #opens the window
        else: #otherwise
            root.destroy() #window close
            import patients_all_appointments 
            patients_all_appointments.render(k,'admin')

    def patientinfo():
        root.destroy()
        import patients_panel
        patients_panel.render()

    def change_password_func():
        root.destroy()
        import admin_passchage
        admin_passchage.render()

    def logout():
        root.destroy()
        import main

    NAVBAR_COLOR = "#1a237e"
    SEARCH_BUTTON_COLOR = "#4caf50"

    root = tk.Tk()
    root.title("Admin Panel")
    root.geometry("800x600")
    root.iconbitmap("logo.ico")
    font_style = ("Roboto", 10)

    navbar = tk.Frame(root, bg=NAVBAR_COLOR, height=50)
    navbar.pack(fill="x", padx=5, pady=5)
    navbar_shadow = tk.Label(navbar, bg=NAVBAR_COLOR, bd=1, relief="raised")
    navbar_shadow.pack(fill="both", expand=True)

    navbar_title = tk.Label(navbar, text="Admin Panel", fg="white", font=("Open Sans", 12, "bold"), bg=NAVBAR_COLOR)
    navbar_title.pack(pady=10)

    search_frame = tk.Frame(root)
    search_frame.pack(pady=10)
    search_entry = ttk.Entry(search_frame, font=font_style)
    search_entry.grid(row=0, column=0, padx=(10, 0))
    search_button = ttk.Button(search_frame, text="Search", style="Search.TButton", command=search)
    search_button.grid(row=0, column=1, padx=(5, 10))

    sidebar = tk.Frame(root, bg="#f4f4f4", width=200, padx=10, pady=10)
    sidebar.pack(side="left", fill="y")

    a_button = ttk.Button(sidebar, text="Add Appointment", style="Sidebar.TButton", command=lambda:appoint(user))
    a_button.pack(pady=5)
    staff_info_button = ttk.Button(sidebar, text="Staff Info", style="Sidebar.TButton", command=staffinfo)
    staff_info_button.pack(pady=5)
    patients_button = ttk.Button(sidebar, text="Patients", style="Sidebar.TButton", command=patientinfo)
    patients_button.pack(pady=5)
    change_password_button = ttk.Button(sidebar, text="Change Password", style="Sidebar.TButton",
                                        command=change_password_func)
    change_password_button.pack(pady=5)
    logout_button = ttk.Button(sidebar, text="Logout", style="Sidebar.TButton", command=logout)
    logout_button.pack(pady=5)

    terminal_frame = tk.Frame(root, bg="white", padx=10, pady=10)
    terminal_frame.pack(fill="both", expand=True)

    scrollbar = ttk.Scrollbar(terminal_frame, orient="vertical")
    scrollbar.pack(side="right", fill="y")

    terminal_treeview = ttk.Treeview(terminal_frame, columns=("name", "address", "gender","phone_number"),
                                     show="headings", yscrollcommand=scrollbar.set)
    terminal_treeview.heading("name", text="name")
    terminal_treeview.heading("address", text="address")
    terminal_treeview.heading( "gender", text= "gender")
    terminal_treeview.heading("phone_number", text="Phone Number")
    terminal_treeview.pack(fill="both", expand=True)

    terminal_treeview.bind("<Double-1>", on_double_click)  # Bind double-click event

    style = ttk.Style()
    style.configure("Search.TButton", background=SEARCH_BUTTON_COLOR)
    style.configure("Sidebar.TButton", font=font_style, width=15)

    root.mainloop()

if __name__ == "__main__":
    render("admin")
