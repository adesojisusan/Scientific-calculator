import tkinter


root = tkinter.Tk()
root.title('Calculator')

def add():
    pass

root_label= tkinter.Label(root, text='42')
root_label.grid(row=0, column=0)

button_1 = tkinter.Button(root, text='1', command=add())
button_1.grid(row= 1, column = 0)

button_2 = tkinter.Button(root, text ='2', command = add())
button_2.grid(row=1, column = 1)

button_3 = tkinter.Button(root, text ='3', command = add())
button_3.grid(row=1, column = 2)




root.mainloop()