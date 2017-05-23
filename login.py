import window
from tkinter import Tk, messagebox
#parte grafica de la app que pide registro o login

class login():


	def __init__(self, path):
		self.path = path
		self.usr = None
		self.pwd = None
		self.id = None


	def select_user(self,usr, pwd, id):
		#TO-DO select to the DB to see if the user exists or you could insert it
		return id if usr and pwd and id else None


	def register_user(self):

		while True:
			root = Tk()
			root.withdraw()
			answer = messagebox.askyesno('Question?', 'Have you got an Account??')
			root.destroy()
			window.My_window(self, login = answer)

			idd = self.select_user(self.usr, self.pwd, self.id)
			if idd:
				break

		self._save_data(idd, self.usr, self.pwd)
		


	def _save_data(self, id, usr, pwd):
		with open(self.path, 'w') as file_output:
			file_output.write('[cabecera cabezona]\n')
			file_output.write('{}\n'.format(id))
			file_output.write('{}\n'.format(usr))
			file_output.write('{}\n'.format(pwd))


	def set_user_info(self, usr, pwd, id):
		self.usr = usr
		self.pwd = pwd
		self.id = id