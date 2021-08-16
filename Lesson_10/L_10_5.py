from tkinter import Tk, Label, Button, Entry


class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        self.counter = 0
        master.title('First GUI')

        self.label = Label(master, text="Hello")
        self.label.pack()

        self.button = Button(master, text='BUTTON', command=self.greet)
        self.button.pack()

        self.text = Entry(master)
        self.text.pack()

    def greet(self):
        self.counter += 1
        self.label.configure(text=self.text.get())


root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()
