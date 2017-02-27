'''
Header here
'''

#Imports
from random import randint
from ctypes.wintypes import BOOLEAN

#SUPER CLASS: ANSWER
class answer(object):
    '''
    answer is the super class.  It holds the:
    answer ID
    '''
    
    #Initialize
    def __init__(self):
        self.__answerID = 0
        
    #Properties
    @property
    def answerID(self):
        return self.__answerID

    #Setters
    @answerID.setter
    def setAnswerID(self, newID):
        self.__answerID = newID
    
#CHILD CLASS: TRUE FALSE ANSWER
class trueFalseAnswer(answer):
    '''
    true false answer is a child class.  It holds the:
    answer
    '''
    def __init__(self):
        super().__init__()
        self.__answer = bool
        
    #Properties
    @property
    def answer(self):
        return self.__answer
    
    #Setters
    @answer.setter
    def setAnswer(self, newAnswer):
        self.__answer = newAnswer
        
#CHILD CLASS: MULTIPLE CHOICE ANSWER
class multipleChoiceAnswer(answer):
    '''
    multiple choice answer is a child class.  It holds the:
    answer
    '''
    def __init__(self):
        super().__init__()
        self.__answer = 0
        
    #Properties
    @property
    def answer(self):
        return self.__answer
    
    #Setters
    @answer.setter
    def setAnswer(self, newAnswer):
        self.__answer = newAnswer

#CHILD CLASS: SHORT ANSWER ANSWER
class shortAnswerAnswer(answer):
    '''
    short answer answer is a child class.  It hold the:
    answer
    '''
    def __init__(self):
        super().__init__()
        self.__answer = ""
        
    #Properties
    @property
    def answer(self):
        return self.__answer
    
    #Setters
    @answer.setter
    def setAnswer(self, newAnswer):
        self.__answer = newAnswer
        
#CHILD CLASS: ESSAY ANSWER
class essayAnswer(answer):
    '''
    essay answer is a child class.  It hold the:
    answer
    '''
    def __init__(self):
        super().__init__()
        self.__answer = ""
        
    #Properties
    @property
    def answer(self):
        return self.__answer
    
    #Setters
    @answer.setter
    def setAnswer(self, newAnswer):
        self.__answer = newAnswer
        
#CHILD CLASS: MATCHING ANSWER
class matchingAnswer(answer):
    '''
    matching answer is a child class.  It hold the:
    answer
    '''
    def __init__(self):
        super().__init__()
        self.__answer = []
                
    #Properties
    @property
    def answer(self):
        return self.__answer

    #Setters
    @answer.setter
    def setAnswer(self, newAnswer):
        self.__answer = newAnswer          
        
#CHILD CLASS: RANKING ANSWER
class rankingAnswer(answer):
    '''
    ranking answer is a child class.  It holds the:
    answer
    '''
    def __init__(self):
        super().__init__()
        self.__answer = []
        
    #Properties
    @property
    def answer(self):
        return self.__answer
    
    #Setters
    @options.setter
    def setAnswer(self, newAnswer):
        self.__answer = newAnswer