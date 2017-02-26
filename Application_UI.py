from tkinter import *
class MainMenu():
    def __init__(self, parent):
        self.var = IntVar()
        self.parent = parent
        self.frame = Frame(parent)
        self.frame.pack()
        self.frame.place(height = 600, width= 800)
    def create(self):
        self.frame.destroy()
        newWindow = createChooseQuizOrSurveyWindow(self.parent)
        newWindow.displayOptions()
    def quit(self):
        self.parent.quit()
    def displayMainMenu(self):
        button = Button(self.frame, text="Create", command=self.create)
        button.pack()
        button.place(x = 350, y = 250, height = 30, width = 100)
        button1 = Button(self.frame, text="Exit", command=self.quit)
        button1.pack()
        button1.place(x = 350, y = 280, height = 30, width = 100)

class createChooseQuizOrSurveyWindow():
    def __init__(self, parent):
        self.var = IntVar()
        self.parent = parent
        self.frame = Frame(parent)
        self.frame.pack()
        self.frame.place(height = 600, width= 800)
    def displayOptions(self):
        label = Label(self.frame,text="Are you making a quiz or survey?")
        button = Button(self.frame, text="Quiz")
        button1 = Button(self.frame, text="Survey")
        button2 = Button(self.frame, text="Go Back", command = self.toMainMenu)
        label.pack()
        button.pack()
        button1.pack()
        button2.pack()
        label.place(x = 250, y = 100, height = 30, width = 300)
        button.place(x = 300, y = 250, height = 30, width = 100)
        button1.place(x = 400, y = 250, height = 30, width = 100)
        button2.place(x=350, y=280, height=30, width=100)
    def toMainMenu(self):
        self.frame.destroy()
        newWindow = MainMenu(self.parent)
        newWindow.displayMainMenu()

