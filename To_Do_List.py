import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class TO_DO_APP:
    def __init__(self, root):
        self.root = root
        self.root.title("T0-D0 LIST APP")

        self.root.configure(bg="#e0f2f1")

        self.Tasks = []

        self.Task_Label = ttk.Label(root, text="Task:")
        self.Task_Label.pack(pady=(10, 0))

        self.Task_Entry = ttk.Entry(root)
        self.Task_Entry.pack(pady=(0, 10))

        self.Due_Date_Label = ttk.Label(root, text="Due Date (DD-MM-YYYY):")
        self.Due_Date_Label.pack()

        self.Due_Date_Entry = ttk.Entry(root)
        self.Due_Date_Entry.pack()

        self.Add_Button = ttk.Button(root, text="Add Task", command=self.Add_Task, style="Custom.TButton")
        self.Add_Button.pack()

        self.Task_ListBox = tk.Listbox(root, selectbackground="royalblue1")
        self.Task_ListBox.pack(pady=(10, 0))

        self.Complete_Button = ttk.Button(root, text="Mark as Completed", command=self.Complete_Task, style="Custom.TButton")
        self.Complete_Button.pack()

        self.Delete_Button = ttk.Button(root, text="Delete Task", command=self.Delete_Task, style="Custom.TButton")
        self.Delete_Button.pack()

        self.custom_button_style = ttk.Style()
        self.custom_button_style.configure("Custom.TButton", font=("Xenara", 10), background="#009688")

    def Add_Task(self):
        Task = self.Task_Entry.get()
        Due_Date = self.Due_Date_Entry.get()

        if Task:
            self.Tasks.append({"Title": Task, "Completed": False, "Due_Date":Due_Date})
            self.Update_Task_Listbox()
            self.Task_Entry.delete(0, tk.END)
            self.Due_Date_Entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please Write a Task..")
    def Complete_Task(self):
        Selected_Index = self.Task_ListBox.curselection()
        if Selected_Index:
            Index = Selected_Index[0]
            self.Tasks[Index]["Completed"] = True
            self.Update_Task_Listbox() 

    def Delete_Task(self):
        Selected_Index = self.Task_ListBox.curselection()
        if Selected_Index:
            Index = Selected_Index[0]
            del self.Tasks[Index]
            self.Update_Task_Listbox()

    def Update_Task_Listbox(self):
        self.Task_ListBox.delete(0, tk.END)
        for task in self.Tasks:
            Status = "[✓]" if task["Completed"] else "[ ]"
            Due_Date = f" (Due: {task['Due_Date']})" if task.get("Due_Date") else ""
            self.Task_ListBox.insert(tk.END, f"{Status} {task['Title']}{Due_Date}")

root = tk.Tk()
root.title("TO-DO LIST APP")
root.geometry("400x500")
app = TO_DO_APP(root)
root.mainloop()
