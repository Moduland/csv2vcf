# -*- coding: utf-8 -*-
import time
from .VCF import *
from tkinter.filedialog import askopenfilename
from tkinter import *
import os

filename=""

if __name__=="__main__":
    root = Tk()
    root.overrideredirect(True)
    w = 400  # width for the Tk root
    h = 430  # height for the Tk root
    ws = root.winfo_screenwidth()  # width of the screen
    hs = root.winfo_screenheight()  # height of the screen
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    def open_folder(address):
        '''
        This function open file directory
        :param address: address of file
        :type address:str
        :return: None
        '''
        try:
            os.system("start "+address)
        except Exception:
            print("Error In Opening Final File")
    def openfile():
        '''
        This function ask for opening file with tkinter
        :return: filename as str
        '''
        global filename
        filename = askopenfilename(filetypes=(("CSV File", "*.csv")
                                              , ("Text File", "*.txt")
                                              ))
        folder=os.path.dirname(filename)
        time_1 = time.perf_counter()
        counter = csv_reader(filename)
        time_2 = time.perf_counter()
        delta_time = time_2 - time_1
        if counter!=None:
            print(str(counter) + " VCF File Generated In " + time_convert(delta_time))
            messagebox.showinfo("CSV2VCF",str(counter) + " VCF File Generated In " + time_convert(delta_time))
            open_folder(folder)
        return filename

    def tkinter_exit():
        '''
        This function quit tkinter windows
        :return: None
        '''
        root.quit()
    root.wm_title("CSV2VCF")
    label_1=Label(root,text="CSV2VCF",font=("arial", 30, "bold")).pack()
    label_2=Label(root,text="By Moduland",font=("arial", 22, "bold")).pack()
    b = Button(root, text="Open File", bg="gray40", fg="blue", font=("arial", 22, "bold"),width=10,height=3, command=openfile).pack(
        padx="12", pady="12")
    i = Button(root, text="Exit", bg="gray40", fg="blue", font=("arial", 22, "bold"), width=10, height=3,
               command=tkinter_exit).pack(
        padx="12", pady="12")
    root.mainloop()
