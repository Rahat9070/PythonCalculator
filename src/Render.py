from tkinter import *
from tkinter import ttk
from .Calculator import Calculator

class Render():
    def __init__(self, master=None, **kwargs):
        self.root = Tk()
        self.frm = ttk.Frame(self.root, padding=10)
        self.frm.grid()
        self.calculator = Calculator()
        self.create_textbox()
        self.create_buttons()
        self.root.title("Calculator")
    
    def render(self):
        self.root.mainloop()
    
    def create_textbox(self):
        self.txt_var = StringVar()
        self.txt = ttk.Entry(self.frm, textvariable=self.txt_var, width=20, font=("Comic Sans MS", 16), justify="right", state="readonly")
        self.txt.grid(column=1, row=0, columnspan=5)
        self.txt_operator_var = StringVar()
        self.txt_operator = ttk.Entry(self.frm, textvariable=self.txt_operator_var, width=2, font=("Comic Sans MS", 15), justify="center", state="readonly")
        self.txt_operator.grid(column=0, row=0, columnspan=1)
        self.txt_operator_var.set("")
        self.txt_var.set("0")

    def create_buttons(self):
        ttk.Button(self.frm, text="1", command=lambda: self.update_values(1)).grid(column=0, row=1)
        ttk.Button(self.frm, text="2", command=lambda: self.update_values(2)).grid(column=1, row=1)
        ttk.Button(self.frm, text="3", command=lambda: self.update_values(3)).grid(column=2, row=1)
        ttk.Button(self.frm, text="+", command=lambda: self.update_operator("+")).grid(column=3, row=1)
        ttk.Button(self.frm, text="-", command=lambda: self.update_operator("-")).grid(column=4, row=1)
        ttk.Button(self.frm, text="4", command=lambda: self.update_values(4)).grid(column=0, row=2)
        ttk.Button(self.frm, text="5", command=lambda: self.update_values(5)).grid(column=1, row=2)
        ttk.Button(self.frm, text="6", command=lambda: self.update_values(6)).grid(column=2, row=2)
        ttk.Button(self.frm, text="x", command=lambda: self.update_operator("x")).grid(column=3, row=2)
        ttk.Button(self.frm, text="÷", command=lambda: self.update_operator("÷")).grid(column=4, row=2)
        ttk.Button(self.frm, text="7", command=lambda: self.update_values(7)).grid(column=0, row=3)
        ttk.Button(self.frm, text="8", command=lambda: self.update_values(8)).grid(column=1, row=3)
        ttk.Button(self.frm, text="9", command=lambda: self.update_values(9)).grid(column=2, row=3)
        ttk.Button(self.frm, text="0", command=lambda: self.update_values(0)).grid(column=1, row=4)
        ttk.Button(self.frm, text="^", command=lambda: self.update_operator("^")).grid(column=3, row=3)
        ttk.Button(self.frm, text="√", command=lambda: self.update_operator("√")).grid(column=4, row=3)
        ttk.Button(self.frm, text="%", command=lambda: self.update_operator("%")).grid(column=2, row=4)
        ttk.Button(self.frm, text="C", command=lambda: self.clear()).grid(column=0, row=4)
        ttk.Button(self.frm, text=".", command=lambda: self.update_values(".")).grid(column=3, row=4)
        ttk.Button(self.frm, text="=", command=lambda: self.show_answer()).grid(column=4, row=4)
    
    def update_values(self, num):
        self.calculator.add_to_num(num) 
        num = self.calculator.return_num()
        if num == 0:
            self.txt_var.set("0")
        else:
            self.txt_var.set(str(num))
    
    def update_operator(self, operator):
        if operator == '-' and not self.calculator.num:
            self.calculator.set_subtract_flag(True)
            self.txt_var.set("-")
        else:
            self.txt_operator_var.set(operator)
            self.calculator.set_operator(operator)

    
    def show_answer(self):
        result = 0
        try:
            result = self.calculator.calculate()
        except ValueError as e:
            self.txt_var.set(str(e))
            return
        if result is not None:
            self.txt_var.set(str(result))
        else:
            self.txt_var.set("Error")
        self.calculator.clear_num()
    
    def clear(self):
        self.calculator.clear_function()
        self.txt_var.set("0")
        self.txt_operator_var.set("")