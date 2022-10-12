from tkinter import *


class threeButton:
    def __init__(self, root):
        self.f = Frame(root, width=300, height=600, bg="yellow")
        self.f.propagate(0)
        self.f.pack()

        self.b1 = Button(self.f, text="Red", height=10,
                         width=50, fg="red", command=self.buttonClickRed())
        self.b1.pack()
        self.b2 = Button(self.f, text="Blue", height=10, width=50,
                         fg="blue", command=self.buttonClickBlue())
        self.b2.pack()
        self.b3 = Button(self.f, text="Green", height=10,
                         width=50, fg="green", command=self.buttonClickGreen())
        self.b3.pack()

    def buttonClickRed(self):
        self.f.config(bg="red")

    def buttonClickBlue(self):
        self.f.config(bg="blue")

    def buttonClickGreen(self):
        self.f.config(bg="green")


root = Tk()
root.title("Tkinter")
# f1 = Frame(root, height=200, width=300,
#            bg="#98b4d4", cursor="cross", highlightthickness="10")
# f2 = Frame(root, height=200, width=300,
#            bg="#d65076", cursor="cross", highlightthickness="10")
# f3 = Frame(root, height=200, width=300,
#            bg="#009b77", cursor="cross", highlightthickness="10")
# f1.pack()
# f2.pack()
# f3.pack()

# b1 = Button(f1, text="Red")
# b2 = Button(f2, text="Blue")
# b3 = Button(f3, text="Green")

# b1.place(x=95, y=70, height=40, width=60)
# b2.place(x=95, y=70, height=40, width=60)
# b3.place(x=95, y=70, height=40, width=60)
btn = threeButton(root)
root.mainloop()