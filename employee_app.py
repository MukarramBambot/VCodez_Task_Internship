# Task 19: Creating an Tkinter + MySQL Employee Database app

import tkinter as tk
from tkinter import ttk, messagebox
import db_backend

class EmployeeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🏢 Employee Management System")
        self.root.geometry("1100x650")
        self.root.minsize(900, 550)
        self.root.configure(bg="#eaf2f8")
        
        self.vars = {v: tk.StringVar() for v in ["id", "name", "age", "gender", "dept"]}
        tk.Label(root, text="Employee Management System", font=("Segoe UI", 20, "bold"),
                 bg="#2471A3", fg="white", pady=10).pack(fill="x")
        main = tk.Frame(root, bg="#eaf2f8", padx=20, pady=20)
        main.pack(expand=True, fill="both")

        form = tk.LabelFrame(main, text="Employee Details", font=("Arial", 12, "bold"),
                             bg="#f8f9f9", padx=20, pady=10)
        form.pack(side="left", fill="both", expand=True, padx=10, pady=10)

        fields = [("Name", "name"), ("Age", "age"), ("Gender", "gender"), ("Department", "dept")]
        for i, (lbl, var) in enumerate(fields):
            tk.Label(form, text=f"{lbl}:", bg="#f8f9f9").grid(row=i, column=0, sticky="w", pady=5)
            if var == "gender":
                ttk.Combobox(form, textvariable=self.vars[var],
                             values=["Male", "Female", "Other"], width=22).grid(row=i, column=1)
            else:
                tk.Entry(form, textvariable=self.vars[var], width=25).grid(row=i, column=1)

        btns = [("Add", "#00cc66", self.add), ("Update", "#0099cc", self.update),
                ("Delete", "#ff3333", self.delete), ("Clear", "#ffcc00", self.clear)]
        for i, (txt, color, cmd) in enumerate(btns):
            tk.Button(form, text=txt, bg=color, fg="white" if txt != "Clear" else "black",
                      width=8, command=cmd).grid(row=5, column=i, padx=5, pady=15)

        # ---- Right: Table ----
        table = tk.LabelFrame(main, text="Employee Records", font=("Arial", 12, "bold"),
                              bg="#f8f9f9", padx=20, pady=10)
        table.pack(side="right", fill="both", expand=True, padx=10, pady=10)

        self.tree = ttk.Treeview(table, columns=("id", "name", "age", "gender", "dept"), show="headings")
        for c in ["id", "name", "age", "gender", "dept"]:
            self.tree.heading(c, text=c.title())
        self.tree.column("id", width=40)
        self.tree.pack(fill="both", expand=True)
        self.tree.bind("<ButtonRelease-1>", self.select)
        self.refresh()

    # ---- CRUD Methods ----
    def add(self):
        data = [self.vars[v].get() for v in ["name", "age", "gender", "dept"]]
        if not all(data):
            return messagebox.showwarning("Error", "Fill all fields!")
        db_backend.insert_employee(*data)
        messagebox.showinfo("Success", "Employee Added!")
        self.refresh(), self.clear()

    def update(self):
        if not self.vars["id"].get():
            return messagebox.showwarning("Error", "Select a record!")
        db_backend.update_employee(self.vars["id"].get(), *[self.vars[v].get() for v in ["name", "age", "gender", "dept"]])
        messagebox.showinfo("Updated", "Record Updated!")
        self.refresh(), self.clear()

    def delete(self):
        if not self.vars["id"].get():
            return messagebox.showwarning("Error", "Select a record!")
        db_backend.delete_employee(self.vars["id"].get())
        messagebox.showinfo("Deleted", "Employee Removed!")
        self.refresh(), self.clear()

    def clear(self):
        for v in self.vars.values(): v.set("")

    def refresh(self):
        for i in self.tree.get_children(): self.tree.delete(i)
        for row in db_backend.fetch_all(): self.tree.insert("", "end", values=row)

    def select(self, e):
        item = self.tree.focus()
        if not item: return
        vals = self.tree.item(item)["values"]
        for i, k in enumerate(self.vars.keys()): self.vars[k].set(vals[i])

if __name__ == "__main__":
    root = tk.Tk()
    EmployeeApp(root)
    root.mainloop()
