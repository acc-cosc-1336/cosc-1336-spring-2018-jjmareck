from src.homework.homework12.converter import Converter
import tkinter

class Win():
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.outframe = tkinter.Frame(self.main_window)
        self.inframe = tkinter.Frame(self.main_window)
        self.top = tkinter.Frame(self.outframe)
        self.bottom = tkinter.Frame(self.outframe)
        km=100
        con = Converter()
        miles = format(con.get_miles_from_km(km),'.2f')

        self.label_km = tkinter.Label(self.top, text='Km:')
        self.label_km_num = tkinter.Label(self.top, text=km)
        self.label_km.pack(side='left')
        self.label_km_num.pack(side='left')

        self.label_mi = tkinter.Label(self.bottom, text='Miles:')
        self.label_mi_num = tkinter.Label(self.bottom, text=miles)
        self.label_mi.pack(side='left')
        self.label_mi_num.pack(side='left')

        self.display_button = tkinter.Button(self.inframe,text="Display Conversion", command=self.display)
        self.quit_button = tkinter.Button(self.inframe,text="Quit", command=self.main_window.destroy)
        self.display_button.pack()
        self.quit_button.pack()
        
        self.top.pack()
        self.bottom.pack()
        
        self.inframe.pack(side='bottom')
        tkinter.mainloop()

    def display(self):
        self.outframe.pack(side='top')

