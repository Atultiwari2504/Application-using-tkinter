import tkinter as tk
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("350x430")
        #To-do List
        self.tasks = []
        self.width = 20
        self.height = 2
        self.title("To-Do List App")
        self.tasksnumber = len(self.tasks)
        self.task()
    def task(self):
        self.label = tk.Label(self, text="To-Do List Application", font=("Arial", 20))
        self.label.pack(pady=10)
        if self.tasksnumber>0:
            for task in self.tasks:
                frame = tk.Frame(self, height=50, bg="lightgrey")
                frame.pack(fill=tk.X, pady=2)
                task_label = tk.Label(frame, text=task, font=("Arial", 14), bg="white", width=self.width, height=1)
                task_label.pack(side=tk.LEFT,pady=2)
                task_button = tk.Button(frame, text="Delete", command=lambda t=task: self.delete_task(t), width=self.width, height=2)
                task_button.pack(side=tk.LEFT,pady=2)
        frame1 = tk.Frame(self, height=50, bg="lightgrey")
        frame1.pack(fill=tk.X, pady=10)
        self.entry = tk.Entry(frame1, font=("Arial", 14), width=self.width)
        self.entry.pack(side=tk.LEFT,pady=2)
        self.add_button = tk.Button(frame1, text="Add Task", command=lambda: self.add_task(self.entry), width=self.width, height=self.height)
        self.add_button.pack(side=tk.LEFT,pady=2)
    def add_task(self, entry):
        new_task = entry.get()
        if new_task:
            self.tasks.append(new_task)
            self.tasksnumber += 1
            self.entry.delete(0, tk.END)
        for widget in self.winfo_children():
            widget.destroy()
        self.task()
    def delete_task(self, task):
        self.tasks.remove(task)
        self.tasksnumber -= 1
        for widget in self.winfo_children():
            widget.destroy()
        self.task()
if __name__ == "__main__":
    app = App()
    app.config(bg="white")
    app.mainloop()