import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

def render():
    def add_patient():
        root.destroy()
        import patientadd
        patientadd.render("admin")

    def delete_patient():
        selected_item = terminal.selection()
        if selected_item:
            phone_number = terminal.item(selected_item)['values'][3]

            connection = sqlite3.connect("database.db")
            cursor = connection.cursor()

            cursor.execute("DELETE FROM Patients WHERE phone_number=?", (phone_number,))
            connection.commit()

            connection.close()

            terminal.delete(selected_item)

    def search_patient():
        search_phone_number = search_entry.get()

        if not search_phone_number:
            messagebox.showinfo("Empty Search", "Please input your phone number.")
            return

        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()

        cursor.execute("SELECT name, address, gender, phone_number FROM Patients WHERE phone_number=?",
                       (search_phone_number,))
        rows = cursor.fetchall()

        if not rows:
            messagebox.showerror("Invalid Phone Number", "Please input a valid phone number.")
        else:
            terminal.delete(*terminal.get_children())

            for row in rows:
                terminal.insert("", "end", values=row)

        connection.close()

    def back():
        root.destroy()
        import admin_panel
        admin_panel.render("admin")

    def resize(event):
        try:
            terminal["width"] = event.width - 20
            terminal["height"] = event.height - 320
        except tk.TclError as e:
            print("TclError:", e)

    def populate_treeview():
        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()

        cursor.execute("SELECT name, address, gender, phone_number FROM Patients")
        rows = cursor.fetchall()

        for row in rows:
            terminal.insert("", "end", values=row)

        connection.close()

    root = tk.Tk()
    root.title("Patient Information and Admin Panel")
    root.geometry("800x600")
    root.resizable(False, False)
    root.iconbitmap("logo.ico")
    style = ttk.Style()
    style.configure("Navbar.TFrame", background="#1a237e")
    style.configure("Navbar.TLabel", background="#1a237e", foreground="white")

    navbar = ttk.Frame(root, height=50, style="Navbar.TFrame")
    navbar.grid(row=0, column=0, columnspan=2, sticky="ew")

    ttk.Label(navbar, text="Patient Information", font=("Arial", 18), style="Navbar.TLabel").pack(side=tk.LEFT, padx=10)
    ttk.Label(navbar, text="Admin Panel", font=("Arial", 18), style="Navbar.TLabel").pack(side=tk.RIGHT, padx=10)

    separator = ttk.Separator(root, orient="horizontal")
    separator.grid(row=1, column=0, columnspan=2, sticky="ew")

    terminal = ttk.Treeview(root, columns=("Name", "Address", "Gender", "Phone Number"), show="headings")
    terminal.heading("Name", text="Name")
    terminal.heading("Address", text="Address")
    terminal.heading("Gender", text="Gender")
    terminal.heading("Phone Number", text="Phone Number")
    terminal.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")
    terminal.bind("<Configure>", resize)

    separator_below_terminal = ttk.Separator(root, orient="horizontal")
    separator_below_terminal.grid(row=3, column=0, columnspan=2, sticky="ew")

    root.rowconfigure(2, weight=1)
    root.columnconfigure(0, weight=1)

    button_frame = ttk.Frame(root)
    button_frame.grid(row=4, column=0, columnspan=2, pady=10)

    ttk.Button(button_frame, text="Add Patient", command=add_patient).pack(side=tk.LEFT, padx=10, pady=10)
    ttk.Button(button_frame, text="Delete Patient", command=delete_patient).pack(side=tk.LEFT, padx=10, pady=10)
    ttk.Button(button_frame, text="Back", command=back).pack(side=tk.RIGHT, padx=10, pady=10)

    search_entry = ttk.Entry(button_frame)
    search_entry.pack(side=tk.RIGHT, padx=10, pady=10)
    search_button = ttk.Button(button_frame, text="Search", command=search_patient)
    search_button.pack(side=tk.RIGHT, padx=10, pady=10)

    populate_treeview()

    root.mainloop()

if __name__=="__main__":
    render()
