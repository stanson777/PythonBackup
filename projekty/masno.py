import tkinter as tk

class Kalkulator:
    def __init__(self, master):
        self.master = master
        master.title("Kalkulator")

        self.ekran = tk.Entry(master, width=16, font=('Arial', 20), justify='right')
        self.ekran.grid(row=0, column=0, columnspan=4)

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/',
             1, 3), ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*',
             2, 3), ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-',
             3, 3), ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+',
             4, 3)
        ]

        for (text, row, col) in buttons:
            button = tk.Button(master, text=text, command=lambda t=text: self.handle_button_click(t))
            button.grid(row=row, column=col)

    def handle_button_click(self, value):
        if value == '=':
            try:
                result = eval(self.ekran.get())
                self.ekran.delete(0, tk.END)
                self.ekran.insert(tk.END, str(result))
            except:
                self.ekran.delete(0, tk.END)
                self.ekran.insert(tk.END, "Błąd")
        elif value == 'C':
            self.ekran.delete(0, tk.END)
        else:
            current_text = self.ekran.get()
            self.ekran.delete(0, tk.END)
            self.ekran.insert(tk.END, current_text + value)

        przycisk=tk.Button(self.master,text='silnia',command=self.silnia)
        przycisk.grid(row=5,)

    def silnia(self):
        new_window=self.master.Toplevel(self)
        new_window.title("Silnia")

        tk.
if __name__ == "__main__":
    root = tk.Tk()
    kalkulator = Kalkulator(root)
    root.mainloop()
