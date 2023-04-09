import tkinter as tk

class Calculator(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.entry = tk.Entry(self, width=60)
        self.entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        buttons = ['7', '8', '9', '/', '4', '5', '6', '*', '1', '2', '3', '-', '0', '.', '=', '+']

        row = 1
        col = 0
        for button in buttons:
            if col == 4:
                row += 1
                col = 0
            tk.Button(self, text=button, width=5, height=2, command=lambda x=button:self.button_click(x)).grid(row=row, column=col, padx=5, pady=5)
            col += 1

    def button_click(self, text):
        if text == 'C':
            self.entry.delete(0, tk.END)
        elif text == '=':
            try:
                result = eval(self.entry.get())
                self.entry.delete(0, tk.END)
                self.entry.insert(0, result)
            except:
                self.entry.delete(0, tk.END)
                self.entry.insert(0, "Error")
        else:
            self.entry.insert(tk.END, text)

root = tk.Tk()
root.title("Calculator")
app = Calculator(master=root)
app.mainloop()
