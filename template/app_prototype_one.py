import tkinter
from tkinter import messagebox
from tkinter import filedialog
import webbrowser
import visualization_backedend


def clicked():
    file_path = filedialog.askopenfilename()
    visualization_backedend.backend(file_path)
    webbrowser.open('file:///home/coder/Downloads/neo4jtest.html')
    #messagebox.showinfo('alert', "Opened file "+ file_path)
def action_performed():
    messagebox.showinfo('alert', "action performed")
def exit_function():
    exit()

def file_operation(file_path):
    f = open(file_path,'r')
    

window = tkinter.Tk()
window.geometry('800x600')


menubar = tkinter.Menu(window)
filemenu = tkinter.Menu(menubar, tearoff=0)
actionmenu = tkinter.Menu(menubar,tearoff=0)

filemenu.add_command(label="csv", command=clicked)
filemenu.add_command(label="txt", command=clicked)
filemenu.add_command(label="xlsv", command=clicked)
filemenu.add_command(label="exit", command=exit_function)
menubar.add_cascade(label="file",menu=filemenu)

actionmenu.add_command(label="graph",command=action_performed)
actionmenu.add_command(label="Pie chart",command=action_performed)
actionmenu.add_command(label="Nodes",command=action_performed)
menubar.add_cascade(label = "action",menu=actionmenu)

window.config(menu=menubar)
window.mainloop()
