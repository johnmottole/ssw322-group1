from tkinter import *
from Questionnaire import Questionnaire
from question import question
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
        button = Button(self.frame, text="Quiz", command = self.chosenQuiz)
        button1 = Button(self.frame, text="Survey", command = self.chosenSurvey)
        button2 = Button(self.frame, text="Go Back", command = self.toMainMenu)
        label.pack()
        button.pack()
        button1.pack()
        button2.pack()
        label.place(x = 250, y = 100, height = 30, width = 300)
        button.place(x = 300, y = 250, height = 30, width = 100)
        button1.place(x = 400, y = 250, height = 30, width = 100)
        button2.place(x=350, y=280, height=30, width=100)
    def chosenQuiz(self):
        self.toQuestioniareNameing("quiz")
    def chosenSurvey(self):
        self.toQuestioniareNameing("survey")
    def toQuestioniareNameing(self, tag):
        self.frame.destroy()
        newWindow = getNameForQuizWindow(self.parent, tag)
        newWindow.displayWindow()
    def toMainMenu(self):
        self.frame.destroy()
        newWindow = MainMenu(self.parent)
        newWindow.displayMainMenu()
class getNameForQuizWindow():
    def __init__(self, parent,tag):
        self.var = IntVar()
        self.parent = parent
        self.frame = Frame(parent)
        self.frame.pack()
        self.frame.place(height = 600, width= 800)
        self.tag = tag
        self.entry = Entry(self.frame)
    def displayWindow(self):
        label = Label(self.frame,text="What is the name of your " + self.tag + "?")
        button = Button(self.frame, text="Next", command = self.submit)
        label.pack()
        button.pack()
        self.entry.pack()
        label.place(x = 250, y = 100, height = 30, width = 300)
        button.place(x = 350, y = 200, height = 30, width = 100)
        self.entry.place(x=250, y = 150, height = 30, width = 300)
    def submit(self):
        name = self.entry.get()
        theQuestionnaire = Questionnaire(name, self.tag)
        self.frame.destroy()
        newWindow = editQuizWindow(self.parent, theQuestionnaire)
        newWindow.displayWindow()
class editQuizWindow():
    def __init__(self, parent,questionnarireObject):
        self.var = IntVar()
        self.parent = parent
        self.frame = Frame(parent)
        self.frame.pack()
        self.frame.place(height = 600, width= 800)
        self.questionnarire = questionnarireObject
    def displayWindow(self):
        label = Label(self.frame, text=self.questionnarire.name_id)
        button = Button(self.frame, text="Add A Question", command=self.addQuestion)
        label.pack()
        label.place(x = 250, y = 100, height = 30, width = 300)
        button.pack()
        button.place(x=325, y=150, height=30, width=150)
    def addQuestion(self):
        self.frame.destroy()
        newWindow = addQuestionWindow(self.parent, self.questionnarire)
        newWindow.displayWindow()
class addQuestionWindow():
    def __init__(self, parent,questionnarire_object):
        self.var = IntVar()
        self.parent = parent
        self.frame = Frame(parent)
        self.frame.pack()
        self.frame.place(height = 600, width= 800)
        self.questionnarire = questionnarire_object
        self.entry = Entry(self.frame)
        self.questionTypeChoice = StringVar()
    def displayWindow(self):
        label = Label(self.frame, text="Enter the question")
        button = Button(self.frame, text="Next")
        label2 = Label(self.frame, text="What type of question is it?")
        label.pack()
        button.pack()
        label2.pack()
        self.entry.pack()
        label.place(x=200, y=50, height=30, width=300)
        button.place(x=600, y=500, height=30, width=100)
        self.entry.place(x=200, y=100, height=30, width=300)
        label2.place(x=250, y=200, height=30, width=200)
        typesQ = [("Multiple Choice","MC"), ("True or False", "TF"), ("Short Answer", "SA"), ("Essay", "ES"), ("Matching", "MG"), ("Ranking", "RK")]
        x = 0
        self.questionTypeChoice.set("MC")
        for text, choice in typesQ:
            b = Radiobutton(self.frame, text=text,
                            variable=self.questionTypeChoice, value=choice, indicatoron = TRUE)
            b.pack()
            b.place(x = 260, y = 250 + x)
            x = x + 30