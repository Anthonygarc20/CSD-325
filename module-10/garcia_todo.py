import tkinter as tk
from tkinter import messagebox

class TodoApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Garcia-ToDo")
        self.geometry("400x500")
        
        self.COLOR_PRIMARY = "#10AEE8"
        self.COLOR_ACCENT = "#EE840B"
        self.COLOR_TEXT = "#080101"
        self.COLOR_BG = "#E2E6E9"

        self.configure(bg=self.COLOR_BG)

        self.create_menu()

        self.main_frame = tk.Frame(self, bg=self.COLOR_BG)
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.instructions_label = tk.Label(
            self.main_frame, 
            text="Added --- ** Right Click Item to Delete **", 
            font=("Arial", 11, "bold"),
            bg=self.COLOR_ACCENT, 
            fg=self.COLOR_TEXT,
            pady=6
        )
        self.instructions_label.pack(fill=tk.X, pady=(0, 10))

        self.canvas = tk.Canvas(self.main_frame, bg=self.COLOR_BG, highlightthickness=0)
        self.scrollbar = tk.Scrollbar(self.main_frame, orient="vertical", command=self.canvas.yview)
        
        self.task_frame = tk.Frame(self.canvas, bg=self.COLOR_BG)
        self.task_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )

        self.canvas_window = self.canvas.create_window((0, 0), window=self.task_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.bind("<Configure>", lambda e: self.canvas.itemconfig(self.canvas_window, width=e.width))

        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        self.input_frame = tk.Frame(self, bg=self.COLOR_BG, pady=10)
        self.input_frame.pack(fill=tk.X, padx=10)

        self.task_entry = tk.Entry(self.input_frame, font=("Arial", 12))
        self.task_entry.pack(side="left", fill=tk.X, expand=True, padx=(0, 5))
        self.task_entry.bind("<Return>", lambda event: self.add_task())

        self.add_button = tk.Button(
            self.input_frame, 
            text="Add Task", 
            command=self.add_task,
            bg=self.COLOR_PRIMARY,
            fg=self.COLOR_TEXT,
            font=("Arial", 10, "bold"),
            relief=tk.FLAT
        )
        self.add_button.pack(side="right")

    def create_menu(self):
        menubar = tk.Menu(self, bg=self.COLOR_PRIMARY, fg=self.COLOR_TEXT)
        file_menu = tk.Menu(menubar, tearoff=0, bg=self.COLOR_PRIMARY, fg=self.COLOR_TEXT, activebackground=self.COLOR_ACCENT)
        file_menu.add_command(label="Exit", command=self.quit_program)
        menubar.add_cascade(label="File", menu=file_menu)
        self.config(menu=menubar)

    def add_task(self):
        task_text = self.task_entry.get().strip()
        if task_text:
            row_frame = tk.Frame(self.task_frame, bg=self.COLOR_PRIMARY, pady=6, padx=8)
            row_frame.pack(fill=tk.X, pady=4, expand=True)

            task_label = tk.Label(
                row_frame, 
                text=task_text, 
                bg=self.COLOR_PRIMARY, 
                fg=self.COLOR_TEXT,
                font=("Arial", 11),
                anchor="w"
            )
            task_label.pack(side="left", fill=tk.X, expand=True)

            row_frame.bind("<Button-3>", lambda event, target=row_frame: self.delete_task(target))
            task_label.bind("<Button-3>", lambda event, target=row_frame: self.delete_task(target))
            
            self.task_entry.delete(0, tk.END)
            self.canvas.update_idletasks()
            self.canvas.yview_moveto(1.0)

    def delete_task(self, target):
        target.destroy()
        self.canvas.update_idletasks()
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def quit_program(self):
        self.destroy()

if __name__ == "__main__":
    app = TodoApp()
    app.mainloop()