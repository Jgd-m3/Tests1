#test guardar usuario en archivo .txt
import os.path as path
import login 

file_string = r'usuarios1.txt'

if not path.exists(file_string):
	nana = login.login(file_string)
	nana.register_user()

data =[]

with open(file_string, 'r') as file_input:

	for i, line in enumerate(file_input):
		if i == 0:
			print('la cabecera es: {}'.format(line))
		if i == 1:
			data.append(int(line))
		if i == 2 or i == 3:
			data.append(str(line).strip())



print('user:{}\nuser:{}\npass:{}'.format(data[0],data[1],data[2]))
	