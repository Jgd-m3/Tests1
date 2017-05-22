#probando PyQt

import sys
from tkinter import *
from tkinter import messagebox




class My_window:

	#definir la funcion que llamaremos
	def login(self):
		#TO-DO EVERYTHING TO LOGIN THE USR
		messagebox.showinfo('holis', 'Has logeao HDP > {} < *{}*'.format(self.entrada_usr.get(), self.entrada_pwd.get()))
		self.parent.set_user_info(self.entrada_usr.get(), self.entrada_pwd.get(), 1)
		self.window.destroy()

	def __init__(self, parent, login = False):
		#creamos ventana
		self.window = Tk()
		self.parent = parent
		self.mode = login
		#tamanyo('ancho x alto + posx + posy')
		self.window.geometry('500x300+100+100')
		str_mode = 'Login' if self.mode else 'Sign Up'
		self.window.title(str_mode)

		#etiqueta grid(fila y columna)
		lbl_usr = Label(self.window, text='Usuario: ').grid(row= 2, column =2, sticky=W)
		lbl_pwd = Label(self.window, text='Password: ').grid(row=4, column=2, sticky=W)


		#txtfield
		self.entrada_usr = StringVar()
		self.entrada_pwd = StringVar()
		txt_usr = Entry(self.window, textvariable = self.entrada_usr).grid(row =2, column =3)
		txt_pwd = Entry(self.window, show = '*', textvariable = self.entrada_pwd).grid(row =4, column =3)



		bnt_login = Button(self.window, text=str_mode, width=10, command=self.login).grid(row=10, column=2)










		#inicializamos el procesamiento - solo windows
		self.window.mainloop()

#end window