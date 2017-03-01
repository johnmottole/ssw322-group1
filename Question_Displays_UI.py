from tkinter import *
from Questionnaire import *
from question import *
from answer import *
from answerSheet import *
class PreviewWindow():
    def __init__(self, parent,questionnarire_object, index):
        self.var = IntVar()
        self.parent = parent
        self.frame = Frame(parent)
        self.frame.pack()
        self.frame.place(height = 600, width= 800)
        self.questionnarire = questionnarire_object
        self.index = index
        prompt = self.questionnarire.question_list[index].prompt
        label = Label(self.frame, text=prompt)
        label.pack()
        label.place(x=200, y=75, height=30, width=400)
class trueFalsePreviewWindow(PreviewWindow):
    def __init__(self, parent, questionnarie_object, index):
        super().__init__(parent,questionnarie_object, index)
    def displayWindow(self):
        radio1 = Radiobutton(self.frame, indicatoron=False, text="True")
        radio1.pack()
        radio1.place(x=400, y=100, height=30, width=300)
        radio2 = Radiobutton(self.frame, indicatoron=False, text="False")
        radio2.pack()
        radio2.place(x=400, y=150, height=30, width=300)
        button1 = Button(self.frame, text="Next")
        button1.pack()
        button1.place(x=400, y=200, height=30, width=300)
    def next(self):
        self.index = self.index + 1
        if self.index >= len(self.questionnarire.question_list):
            print("Done")