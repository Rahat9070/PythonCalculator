from tkinter import *
from tkinter import ttk
from .Calculator import Calculator

class Render():
    def __init__(self, master=None, **kwargs):
        self.root = Tk()
        self.frm = ttk.Frame(self.root, padding=10)
        self.frm.grid()
        self.calculator = Calculator()
        self.create_buttons()
        self.root.title("Calculator")
    
    def render(self):
        self.root.mainloop()
    
    def create_buttons(self):
        ttk.Button(self.frm, text="1", command=lambda: self.calculator.add_to_num(1)).grid(column=0, row=0)
        ttk.Button(self.frm, text="2", command=lambda: self.calculator.add_to_num(2)).grid(column=1, row=0)
        ttk.Button(self.frm, text="3", command=lambda: self.calculator.add_to_num(3)).grid(column=2, row=0)
        ttk.Button(self.frm, text="+", command=self.calculator.add_to_num(3)).grid(column=3, row=0)
        ttk.Button(self.frm, text="-", command=self.calculator.add_to_num(3)).grid(column=4, row=0)
        ttk.Button(self.frm, text="4", command=lambda: self.calculator.add_to_num(4)).grid(column=0, row=1)
        ttk.Button(self.frm, text="5", command=lambda: self.calculator.add_to_num(5)).grid(column=1, row=1)
        ttk.Button(self.frm, text="6", command=lambda: self.calculator.add_to_num(6)).grid(column=2, row=1)
        ttk.Button(self.frm, text="x", command=self.calculator.add_to_num(3)).grid(column=3, row=1)
        ttk.Button(self.frm, text="/", command=self.calculator.add_to_num(3)).grid(column=4, row=1)
        ttk.Button(self.frm, text="7", command=lambda: self.calculator.add_to_num(7)).grid(column=0, row=2)
        ttk.Button(self.frm, text="8", command=lambda: self.calculator.add_to_num(8)).grid(column=1, row=2)
        ttk.Button(self.frm, text="9", command=lambda: self.calculator.add_to_num(9)).grid(column=2, row=2)
        ttk.Button(self.frm, text="0", command=lambda: self.calculator.add_to_num(0)).grid(column=1, row=3)

        ttk.Button(self.frm, text="=", command=self.root.destroy).grid(column=4, row=3)
        ttk.Button(self.frm, text="Quit", command=self.root.destroy).grid(column=4, row=3)