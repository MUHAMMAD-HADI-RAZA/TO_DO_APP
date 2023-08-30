import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import DateEntry

class TO_DO_APP:
    def __init__(self, root):
        self.root = root
        self.root.title("T0-D0 LIST APP")

        self.root.configure(bg="#aef2ed")

        self.Tasks = []

        self.Task_Label = ttk.Label(root, text="TASK:", font=("Times New Roman", 14, "bold"))
        self.Task_Label.pack(pady=(20, 5), padx=10, anchor="w")

        self.Task_Entry = ttk.Entry(root, font=("Times New Roman", 12))
        self.Task_Entry.pack(pady=(0, 10), padx=10, fill="x")

        self.Due_Date_Label = ttk.Label(root, text="DUE DATE:", font=("Times New Roman", 14, "bold"))
        self.Due_Date_Label.pack(pady=(5, 5), padx=10, anchor="w")

        self.Selected_Date = tk.StringVar()

        self.Due_Date_Entry = DateEntry(root, Date_Pattern="dd-MM-yyyy", textvariable=self.Selected_Date, font=("Xenara", 12))
        self.Due_Date_Entry.pack(pady=(0,20), padx=10, fill="x")

        self.Add_Button = ttk.Button(root, text="ADD TASK", command=self.Add_Task, style="Custom.TButton")
        self.Add_Button.pack(pady=(0, 5), padx=10, fill="x")

        self.Task_TreeView = ttk.Treeview(root, columns=("Task", "Due Date"), show="headings")
        self.Task_TreeView.heading("Task", text="TASK")
        self.Task_TreeView.heading("Due Date", text="DUE DATE")
        self.Task_TreeView.pack(pady=(10, 0),padx=10, fill="both", expand=True)

        self.Complete_Button = ttk.Button(root, text="MARK AS COMPLETED", command=self.Complete_Task, style="Custom.TButton")
        self.Complete_Button.pack(pady=(0, 5), padx=10, fill="x")

        self.Delete_Button = ttk.Button(root, text="DELETE TASK", command=self.Delete_Task, style="Custom.TButton")
        self.Delete_Button.pack(pady=(0, 20), padx=10, fill="x")

        self.custom_button_style = ttk.Style()
        self.custom_button_style.configure("Custom.TButton", font=("Times New Roman", 12), background="#009688")

    def Add_Task(self):
        Task = self.Task_Entry.get()
        Due_Date = self.Selected_Date.get()

        if Task and Due_Date:
            self.Tasks.append({"Title": Task, "Completed": False, "Due_Date":Due_Date})
            self.Update_Task_TreeView()
            self.Task_Entry.delete(0, tk.END)
            self.Selected_Date.set("")
        else:
            messagebox.showwarning("Warning", "Please Write a Task..\nSelect a Due Date..")
    
    def Complete_Task(self):
        Selected_Index = self.Task_TreeView.selection()
        if Selected_Index:
            Index = int(Selected_Index[0][1])
            self.Tasks[Index]["Completed"] = True
            self.Update_Task_TreeView() 

    def Delete_Task(self):
        Selected_Index = self.Task_TreeView.selection()
        if Selected_Index:
            Index = int(Selected_Index[0][1])
            del self.Tasks[Index]
            self.Update_Task_TreeView()

    def Update_Task_TreeView(self):
        self.Task_TreeView.delete(*self.Task_TreeView.get_children())
        for idx, task in enumerate(self.Tasks):
            Status = "[✓]" if task["Completed"] else "[ ]"
            Due_Date = task["Due_Date"] if task.get("Due_Date") else "Not Set"
            self.Task_TreeView.insert("", "end", values=(f"{Status} {task['Title']}", Due_Date), tags=idx)

root = tk.Tk()
root.title("TO-DO LIST APP")
root.geometry("500x600")
app = TO_DO_APP(root)
root.mainloop()
