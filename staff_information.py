import tkinter as tk
from tkinter import ttk
import sqlite3

def render():
    def add_staff():
        root.destroy()
        import reg_recep

    def delete_staff():
        selected_item = tree.focus()
        if selected_item:
            item_data = tree.item(selected_item)['values']
            user_id = item_data[0]

            conn = sqlite3.connect('database.db')
            c = conn.cursor()

            c.execute("DELETE FROM Users WHERE user_id=?", (user_id,))
            conn.commit()

            conn.close()

            populate_tree()

    def back():
        root.destroy()
        import admin_panel
        admin_panel.render("admin")

    def resize(event):
        terminal.config(width=600, height=400)

    def populate_tree():
        for row in tree.get_children():
            tree.delete(row)

        conn = sqlite3.connect('database.db')
        c = conn.cursor()

        c.execute("SELECT user_id, username, password FROM Users WHERE user_type='recpt'")
        rows = c.fetchall()

        for row in rows:
            tree.insert('', 'end', values=row)

        conn.close()

    root = tk.Tk()
    root.title("Staff Information and Admin Panel")
    root.geometry("800x600")
    root.resizable(False, False)
    root.iconbitmap("logo.ico")
    style = ttk.Style()
    style.configure("Navbar.TFrame", background="#1a237e")
    style.configure("Navbar.TLabel", background="#1a237e", foreground="white")

    navbar = ttk.Frame(root, height=50, style="Navbar.TFrame")
    navbar.grid(row=0, column=0, columnspan=2, sticky="ew")

    ttk.Label(navbar, text="Staff Information", font=("Arial", 18), style="Navbar.TLabel").pack(side=tk.LEFT, padx=10)
    ttk.Label(navbar, text="Admin Panel", font=("Arial", 18), style="Navbar.TLabel").pack(side=tk.RIGHT, padx=10)

    terminal = tk.Frame(root, width=600, height=400)
    terminal.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

    tree = ttk.Treeview(terminal, columns=('user_id', 'username', 'password'), show='headings')
    tree.heading('user_id', text='User ID')
    tree.heading('username', text='Username')
    tree.heading('password', text='password')
    tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    scrollbar = ttk.Scrollbar(terminal, orient='vertical', command=tree.yview)
    scrollbar.pack(side=tk.RIGHT, fill='y')

    tree.configure(yscrollcommand=scrollbar.set)

    populate_tree()

    navbar_below_text = ttk.Frame(root, height=50, style="")
    navbar_below_text.grid(row=2, column=0, columnspan=2, sticky="ew")

    ttk.Button(navbar_below_text, text="Add Staff", command=add_staff).pack(side=tk.LEFT, padx=10, pady=10)
    ttk.Button(navbar_below_text, text="Delete Staff", command=delete_staff).pack(side=tk.LEFT, padx=10, pady=10)
    ttk.Button(navbar_below_text, text="Back", command=back).pack(side=tk.RIGHT, padx=10, pady=10)

    root.rowconfigure(1, weight=1)
    root.columnconfigure(0, weight=1)

    root.mainloop()
    return True
