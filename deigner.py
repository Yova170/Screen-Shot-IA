from tkinter import *
from tkinter import ttk
from tkinter import filedialog

config_file = "config.ini"


ventana = Tk()
ventana.wm_title("IA CUT")

ventana.geometry('500x300')
ventana.iconbitmap('source/ico.ico')
ventana.wm_iconbitmap('source/ico.ico')
ventana.resizable(width=False, height=False)
folder = filedialog.askdirectory()




print(folder)

ventana.mainloop()
