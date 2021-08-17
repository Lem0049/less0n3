import os
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *


class Notepad:
    __root = Tk()
    __thiTextArea = Text(__root, font=('Georgia', 30))
    __thisMenu = Menu(__root)
    __thisFileMenu = Menu(__thisMenu, tearoff=0)
    __thisEditMenu = Menu(__thisMenu, tearoff=0)
    __thisHelpMenu = Menu(__thisMenu, tearoff=0)
    __thisScrollBar = Scrollbar(__thiTextArea)
    __file = None

    def __init__(self, **kwargs):
        self.__width = kwargs['width']
        self.__height = kwargs['height']
        self.__root.geometry(f'{self.__width}x{self.__height}+50+50')
        self.__root.title('Untitled - notepad')
        self.__root.grid_rowconfigure(0, weight=1)
        self.__root.grid_columnconfigure(0, weight=1)
        self.__thiTextArea.grid(sticky=N + E + S + W)

        self.__root.config(menu=self.__thisMenu)
        self.__thisMenu.add_cascade(label="Файл", menu=self.__thisFileMenu)
        self.__thisMenu.add_command(label="Новый", command=self.__newFile)
        self.__thisFileMenu.add_command(label="Open", command=self.__openFile)
        self.__thisFileMenu.add_command(label="Save", command=self.__saveFile)
        self.__thisFileMenu.add_command(label="Exit", command=self.__quit)
        self.__thisScrollBar.pack(side=RIGHT, fill=Y)

    def __newFile(self):
        self.__root.title("Untitled - Notepad")
        self.__file = None
        self.__thiTextArea.delete(1.0, END)

    def __openFile(self):
        self.__file = askopenfilename(filetypes=[("All Files", "*.*")])
        if self.__file == "":
            self.__file = None
        else:
            self.__root.title(os.path.basename(self.__file) + " - Notepad")
            self.__thiTextArea.delete(1.0, END)
            file = open(self.__file, 'r', encoding='utf-8')
            self.__thiTextArea.insert(1.0, file.read())
            file.close()

    def __saveFile(self):
        if self.__file is None:
            self.__file = asksaveasfilename(initialfile='Untitled.txt', defaultextension='.txt',
                                        filetypes=[("All Files", "*.*")])
            if self.__file == "":
                self.__file = None
            else:
                file = open(self.__file, "w")
                file.write(self.__thiTextArea.get(1.0, END))
                file.close()

    def __quit(self):
        self.__root.destroy()

    def run(self):
        self.__root.mainloop()


note = Notepad(width=100, height=800)
note.run()
