from src.assignments.assignment12.converter import Converter
import tkinter

class Win():
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.top = tkinter.Frame(self.main_window)
        self.bottom = tkinter.Frame(self.main_window)
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
        
        self.top.pack()
        self.bottom.pack()
        tkinter.mainloop()

