from tkinter import Tk, IntVar, Checkbutton, Button, Label, StringVar
from src.assignments.assignment13.evaluator import Evaluator

class Win(Tk):

    def __init__(self):

        Tk.__init__(self, None, None)
        self.wm_title('My first window')
        self.evaluator = Evaluator()
        self.label_var = StringVar()
        Label(self, text="Result: ").pack()

        #ASSIGNMENT13: add the textvariable property and set its value to self.label_var
        Label(self, textvariable=self.label_var).pack()

        #ASSIGNMENT13: add the command property for the button and set its value to self.button_evaluate_handler
        Button(self, text='Evaluate', command=self.button_evaluate_handler).pack()
        self.__init__radio_buttons()

        self.mainloop()

    def __init__radio_buttons(self):

        self.check_var_nev = IntVar()
        self.check_var_rar = IntVar()
        self.check_var_som = IntVar()
        self.check_var_oft = IntVar()
        self.check_var_v_oft = IntVar()
        self.check_var_always = IntVar()

        self.check_var_nev.set(0)
        self.check_var_rar.set(0)
        self.check_var_som.set(0)
        self.check_var_oft.set(0)
        self.check_var_v_oft.set(0)
        self.check_var_always.set(0)

        #ASSIGNMENT 13:
        #for each write code IntVar above create a checkbox with attribute text
        #Never, Rarely, Sometimes, Often, Very Often, Always
        #and link the IntVar to the Checkbox variable attribute
        self.check_nev =Checkbutton(self, text="Never",variable=self.check_var_nev)
        self.check_rar =Checkbutton(self, text="Rarely",variable=self.check_var_rar)
        self.check_som =Checkbutton(self, text="Sometimes",variable=self.check_var_som)
        self.check_oft =Checkbutton(self, text="Often",variable=self.check_var_oft)
        self.check_v_oft =Checkbutton(self, text="Very Often",variable=self.check_var_v_oft)
        self.check_always =Checkbutton(self, text="Always",variable=self.check_var_always)

        self.check_nev.pack()
        self.check_rar.pack()
        self.check_som.pack()
        self.check_oft.pack()
        self.check_v_oft.pack()
        self.check_always.pack()

    def button_evaluate_handler (self):

        self.label_var.set(self.evaluator.faculty_evaluation_result(
            0 if self.check_var_nev.get()== 0 else 1 ,
            0 if self.check_var_rar.get()== 0 else 2,
            0 if self.check_var_som.get()== 0 else 3,
            0 if self.check_var_oft.get()== 0 else 25,
            0 if self.check_var_v_oft.get()== 0 else 50,
            0 if self.check_var_always.get()== 0 else 150))

