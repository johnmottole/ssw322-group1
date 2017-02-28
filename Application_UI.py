from tkinter import *
from Questionnaire import *
from question import *
from answer import *
from answerSheet import *
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
        if self.questionnarire.question_list:
            print("sup")
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
        button = Button(self.frame, text="Next", command=self.continueToNextStep)
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
    def continueToNextStep(self):
        if (self.questionTypeChoice.get() == 'TF'):
            question = trueFalse()
            question.prompt = self.entry.get()
            if self.questionnarire.tag == "survey":
                self.frame.destroy()
                newWindow = editQuizWindow(self.parent, self.questionnarire)
                newWindow.displayWindow()
            else:
                self.frame.destroy()
                newWindow = getFinalInfoTFWindow(self.parent, self.questionnarire, question)
                newWindow.displayWindow()
        if self.questionTypeChoice.get() == 'MC':
            mc_question = multipleChoice()
            mc_question.prompt = self.entry.get()
            self.frame.destroy()
            newWindow = getFinalInfoMCWindow(self.parent, self.questionnarire, mc_question)
            newWindow.displayWindow()
class getFinalInfoOnQuestionWindow:
    def __init__(self, parent,questionnarire_object, question):
        self.var = IntVar()
        self.parent = parent
        self.frame = Frame(parent)
        self.frame.pack()
        self.frame.place(height = 600, width= 800)
        self.questionnarire = questionnarire_object
        self.question = question

    def finishAddQuestion(self, correct_answer):
        if not self.questionnarire.answer_sheets:
            answer_sheet = answerSheet()
            answer_sheet.addAnswer(correct_answer)
            answer_sheet.tag = "Correct-Answers"
            self.questionnarire.add_answerSheet(answer_sheet)
        else:
            answer_sheet = self.questionnarire.answer_sheets[0]
            answer_sheet.addAnswer(correct_answer)
        self.questionnarire.add_question(self.question)
        self.frame.destroy()
        newWindow = editQuizWindow(self.parent, self.questionnarire)
        newWindow.displayWindow()
    def finishAddQuestionSurvey(self):
        self.questionnarire.add_question(self.question)
        self.frame.destroy()
        newWindow = editQuizWindow(self.parent, self.questionnarire)
        newWindow.displayWindow()
class getFinalInfoTFWindow(getFinalInfoOnQuestionWindow):
    def __init__(self, parent, questionare, question):
        super().__init__(parent,questionare, question)
    def displayWindow(self):
        label = Label(self.frame, text="Is the correct answer true or false?")
        button = Button(self.frame, text="True", command=self.answerTrue)
        button1 = Button(self.frame, text="False", command=self.answerFalse)
        label.pack()
        label.place(x = 250, y = 100, height = 30, width = 300)
        button.pack()
        button.place(x=225, y=200, height=30, width=100)
        button1.pack()
        button1.place(x=475, y=200, height=30, width=100)
    def answerTrue(self):
        correct_answer = trueFalseAnswer()
        correct_answer.answer = "t"
        self.finishAddQuestion(correct_answer)
    def answerFalse(self):
        correct_answer = trueFalseAnswer()
        correct_answer.answer = "f"
        self.finishAddQuestion(correct_answer)
class getFinalInfoMCWindow(getFinalInfoOnQuestionWindow):
    def __init__(self, parent, questionare, question):
        super().__init__(parent,questionare, question)
        self.choice = IntVar()
        self.entries = []
        self.choices = []
    def displayWindow(self):
        message = "Enter your options"
        if self.questionnarire.tag == "quiz":
            message = message + " and select the correct answer"
        label = Label(self.frame, text=message)
        label.pack()
        label.place(x = 200, y = 75, height = 30, width = 400)
        options = [0, 1, 2, 3, 4]
        i = 0
        self.choice.set(0)
        for letter in options:
            entry1 = Entry(self.frame)
            entry1.pack()
            entry1.place(x=250, y = 150+i, height = 30, width = 300)
            self.entries.append(entry1)
            if self.questionnarire.tag == "quiz":
                radio1 = Radiobutton(self.frame, value=letter, indicatoron = TRUE, variable=self.choice)
                radio1.pack()
                radio1.place(x=550, y = 150+i, height = 30, width = 300)
            i = i + 50
        button = Button(self.frame, text="Submit", command=self.submit)
        button.pack()
        button.place(x = 375, y = 400,height=30, width=100 )
    def submit(self):
        for entry in self.entries:
            self.choices.append(entry.get())
        self.question.options = self.choices
        if self.questionnarire.tag == "quiz":
            correct_answer = multipleChoiceAnswer()
            correct_answer = self.choice.get()
            self.finishAddQuestion(correct_answer)
        else:
            self.finishAddQuestionSurvey()