# -*- coding: utf-8 -*-
import time
from VCF import *
from tkinter.filedialog import askopenfilename
from tkinter import *

filename=""
global filename




if __name__=="__main__":
    root = Tk()
    root.overrideredirect(1)
    w = 400  # width for the Tk root
    h = 100  # height for the Tk root
    ws = root.winfo_screenwidth()  # width of the screen
    hs = root.winfo_screenheight()  # height of the screen
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    def openfile():
        global filename
        filename = askopenfilename(filetypes=(("CSV File", "*.csv")
                                              , ("Text File", "*.txt")
                                              ))
        time_1 = time.perf_counter()
        counter = csv_reader(filename)
        time_2 = time.perf_counter()
        delta_time = time_2 - time_1
        if counter!=None:
            print(str(counter) + " VCF File Generated In " + time_convert(delta_time))
            messagebox.showinfo("CSV2VCF",str(counter) + " VCF File Generated In " + time_convert(delta_time))
        return filename
    root.wm_title("CSV2VCF")
    b = Button(root, text="Open File", bg="gray40", fg="blue", font=("arial", 22, "bold"),width=10,height=5, command=openfile).pack(
        padx="10", pady="10")
    i = Button(root, text="Exit", bg="gray40", fg="blue", font=("arial", 22, "bold"), width=10, height=5,
               command=openfile).pack(
        padx="10", pady="10")
    root.mainloop()
