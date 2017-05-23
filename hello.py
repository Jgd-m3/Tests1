""" 
from tkinter import *
from tkinter import messagebox

root = Tk()
root.withdraw()
ask = messagebox.askyesno('hola', 'dime si o no')
root.deiconify()
print(ask)

"""
import Connection


conn = Connection.DataBase()
try:
	print('connecting')

	conn.get_connection()

	print('connected')

	conn.close_connection()

	print('Disconnected')


except Exception:
	print(Exception.text())

print('none: ' + str(None.__sizeof__()))
print('0: ' + str(int("0").__sizeof__()))
print( True.__sizeof__())