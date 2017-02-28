'''
Header here
'''

#Imports
from random import randint

#SUPER CLASS: answerSheet
class answerSheet(object):
    '''
    answer sheet is a parent class.  It holds:
    answers
    name
    tag
    '''
    
    #Initialize
    def __init__(self):
        self.__answers = []
        self.__name = ""
        self.__tag = ""
        
    @property
    def answers(self):
        return self.__answers
    
    @property
    def name(self):
        return self.__name
    
    @property
    def tag(self):
        return self.__tag

    def addAnswer(self, newAnswers):
        self.__answers.append(newAnswers)
        
    @name.setter
    def name(self, newName):
        self.__name = newName
    
    @tag.setter
    def tag(self, newTag):
        self.__tag = newTag
        

class grader(answerSheet):
    '''
    grader is a child class of answerSheet.  It holds:
    function to grade
    grade
    '''
    
    def __init__(self):
        super().__init__()
        self.__grade = 0
        
    @property
    def grade(self):
        return grader
    
    #Insert grader function here
    
class tabulator(answerSheet):
    '''tabulator is a child class of answerSheet.  It holds:
    
    '''
    
    def __init__(self):
        super().__init__()
        
    