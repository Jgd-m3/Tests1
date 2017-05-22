from tkinter import *
from tkinter import messagebox

root = Tk()
root.withdraw()
ask = messagebox.askyesno('hola', 'dime si o no')
root.deiconify()
print(ask)