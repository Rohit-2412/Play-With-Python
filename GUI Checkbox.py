from tkinter import *


class login:
    def __init__(self, root) -> None:
        self.f = Frame(root, height=500, width=500)
        self.f.propagate(0)
        self.f.pack()

        self.v1 = IntVar()
        self.v2 = IntVar()
        self.v3 = IntVar()
        self.v4 = IntVar()

        self.cb1 = Checkbutton(self.f, text="C", variable=self.v1)
        self.cb1.pack()
        self.cb2 = Checkbutton(self.f, text="C++", variable=self.v2)
        self.cb2.pack()
        self.cb3 = Checkbutton(self.f, text="Java", variable=self.v3)
        self.cb3.pack()
        self.cb4 = Checkbutton(self.f, text="Python", variable=self.v4)
        self.cb4.pack()

        self.b = Button(self.f, text="Submit", command=self.submit)
        self.b.pack()

    def submit(self):
        s = "You have selected: "
        choice1 = self.v1.get()
        choice2 = self.v2.get()
        choice3 = self.v3.get()
        choice4 = self.v4.get()
        if choice1 == 1:
            s += "C "
        if choice2 == 1:
            s += "C++ "
        if choice3 == 1:
            s += "Java "
        if choice4 == 1:
            s += "Python "
        choices_label = Label(self.f, text=s)
        choices_label.pack()


root = Tk()
root.title("Checkbox")
user1 = login(root)
root.mainloop()