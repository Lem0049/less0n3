from tkinter import *

root = Tk()
data = ["что кликаешь?", "Go for a work", "fuck you", "go to hell"]

i = 0


def change(event):
    global i
    if i == len(data):
        i = 0
    b['text'] = data[i]
    b['activeforeground'] = 'red'
    i += 1


b = Button(text='common', width=20, height=2, font=('Veranda',30))
b.bind('<Button>', change)
# b.pack()
# b = Button(text='ok')
# b.pack()
b.grid(row=3, column=3)
root.geometry('600x400')

root.mainloop()
