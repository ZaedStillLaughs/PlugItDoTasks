import tkinter as tk
import os

class PlugTasks:
    def __init__(self, root):
        self.root = root
        self.root.title("PLUG-TASKS PRO")
        self.root.geometry("400x500")
        self.root.configure(bg="#121212")
        self.filename = "tasks.txt"

        tk.Label(root, text="PLUG-TASKS", font=("Impact", 24), bg="#121212", fg="#00FF41").pack(pady=10)

        self.entry = tk.Entry(root, font=("Arial", 14), bg="#222", fg="white", insertbackground="white")
        self.entry.pack(pady=10, padx=20, fill='x')
        self.entry.bind('<Return>', lambda e: self.add_task())

        tk.Button(root, text="ADD TASK", command=self.add_task, bg="#00FF41", fg="black", font=("Arial", 10, "bold")).pack()

        self.list = tk.Listbox(root, font=("Arial", 12), bg="#1e1e1e", fg="white", selectbackground="#333", bd=0)
        self.list.pack(pady=20, padx=20, fill='both', expand=True)

        btn_frame = tk.Frame(root, bg="#121212")
        btn_frame.pack(pady=10)
        tk.Button(btn_frame, text="CHECK", command=self.toggle_task, bg="#2196F3", fg="white", width=10).grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="DELETE", command=self.delete_task, bg="#F44336", fg="white", width=10).grid(row=0, column=1, padx=5)

        if os.path.exists(self.filename):
            with open(self.filename, "r") as f:
                for line in f: self.list.insert("end", line.strip())

    def add_task(self):
        t = self.entry.get()
        if t:
            self.list.insert("end", f"[ ] {t}")
            self.entry.delete(0, "end")
            self.save()

    def toggle_task(self):
        try:
            i = self.list.curselection()[0]
            val = self.list.get(i)
            new = val.replace("[ ]", "[x]") if "[ ]" in val else val.replace("[x]", "[ ]")
            self.list.delete(i)
            self.list.insert(i, new)
            self.save()
        except: pass

    def delete_task(self):
        try:
            self.list.delete(self.list.curselection()[0])
            self.save()
        except: pass

    def save(self):
        with open(self.filename, "w") as f:
            for t in self.list.get(0, "end"): f.write(t + "\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = PlugTasks(root)
    root.mainloop()