from tkinter import *


class login:
    def __init__(self, root) -> None:
        self.f = Frame(root, height=500, width=500)
        self.f.propagate(0)
        self.f.pack()

        self.l1 = Label(self.f, text="Username")
        self.l1.place(x=100, y=100)

        self.l2 = Label(self.f, text="Password")
        self.l2.place(x=100, y=150)

        self.e1 = Entry(self.f)
        self.e1.place(x=200, y=100)

        self.e2 = Entry(self.f, show="*")
        self.e2.place(x=200, y=150)
        self.e2.bind("<Return>", self.login)  # attaching button to enter key

        self.b1 = Button(self.f, text="Login", command=self.login)
        self.b1.place(x=225, y=200)

    def login(self):
        s1 = self.e1.get()
        s2 = self.e2.get()

        # clear the previous frame
        # label1 = Label(self.f, text="Username: " + s1)
        # label1.place(x=100, y=275)
        #
        # label2 = Label(self.f, text="Password: " + s2)
        # label2.place(x=100, y=300)

        if len(s2) < 6:
            error_label = Label(
                self.f, text="Password should be greater than 6 characters")
            error_label.place(x=100, y=275)
        else:
            label1 = Label(self.f, text="Username: " + s1)
            label1.place(x=100, y=275)
        #
        #     label2 = Label(self.f, text="Password: " + s2)
        #     label2.place(x=100, y=300)


root = Tk()
root.title("User Login")
user1 = login(root)
root.mainloop()