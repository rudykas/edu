
from tkinter import *
from functools import partial
import tictactoe as ttt

window = Tk()

field = [
['_','_','_'],
['_','_','_'],
['x','_','0']]

#todo убрать отладочную печать из другого файла и изменить цвет кнопок или текста 

# погуглить hello world на c и как его скомпилировать 
# погуглить про вим, базовый синтаксис C 
# занятие в вим 


# после mainloop выполняется только эта штука 
def click(i,j):
	global field
	field[i][j]='x'
	draw_new_turn(field)
	field = ttt.next_turn(field, '0')
	draw_new_turn(field)

	print(ttt.state(field))



# drawing field
buttons_list = []
for i in range(3):
    buttons_list.append([])
    for j in range(3):
        button = Button(master=window, text=field[i][j], 
        	command = partial(click, i, j), 
        	highlightbackground = 'white',
        	state = DISABLED if (field[i][j] == 'x' or field[i][j] == '0') else NORMAL)
        button.grid(row=i, column=j)
        buttons_list[i].append(button)

print(buttons_list)
def draw_new_turn(field):
	for i in range(3):
		for j in range(3):
			buttons_list[i][j]['text']=field[i][j]
			buttons_list[i][j]['state']= DISABLED if (field[i][j] == 'x' or field[i][j] == '0') else NORMAL





# отрисовка новой кнопки после нажатия 
# draw_new_turn([
# ['x','x','0'],
# ['0','x','_'],
# ['x','_','0']])



        

# def click(i,j):
# 	def indexes():
# 		print('indexes', i, j)
# 	return indexes


# # drawing field
# for i in range(3):
#     for j in range(3):
#         button = Button(master=window, text=field[i][j], command = click(i,j))
#         button.grid(row=i, column=j)


# 
def handle_click(event): # here should be indexes
	pass

# button = tk.Button(text="Click me!")

# button.bind("<Button-1>", handle_click)

new_field = None 
# changing element of field according indexes of pushed button


window.mainloop()


# for i in range(3):
#     for j in range(3):
#         frame = Frame( 
#             master=window,
#             #relief = 'groove',
#             borderwidth=1,
#             # height = 4
#         )
#         frame.grid(row=i, column=j)
#         button = Button(master=frame, text=f"Row {i}\nColumn {j}")
#         button.pack()


# btn2 = Button()
# btn2.pack


# field = Label(text = 'Tic Tac Toe',  
# 	fg="white",
#     bg="black",
#     width=60,
#     height=60)

# # frame1 = Frame(master=window, width=100, height=100, bg="red")
# # frame1.pack()

# button = Button(
#     text="Click me!",
#     width=25,
#     height=5,
#     bg='black',
#     fg="white",
# )

# field.pack()
# button.pack()




# b=Button(t,text="hello")

# window = t.mainloop()

