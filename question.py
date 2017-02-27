'''
Header here
'''

#Imports
from random import randint

#SUPER CLASS: QUESTION
class question(object):
    '''
    question is the super class.  It holds the:
    question string
    question ID
    '''
    
    #Initialize
    def __init__(self):
        self.__prompt = ""
        self.__questionID = "201" + randint(1000, 9999).str()
        
    #Properties
    @property
    def prompt(self):
        return self.__prompt
    
    @property
    def questionID(self):
        return self.__questionID

    #Setters
    @prompt.setter
    def sePrompt(self, newPrompt):
        self.__prompt = newPrompt
    
#CHILD CLASS: TRUE FALSE
class trueFalse(question):
    '''
    true false is a child class.  It holds the:
    true prompt
    false prompt
    tag
    '''
    def __init__(self):
        super().__init__()
        self.__tag = "TF"
        
    #Properties
    @property
    def tag(self):
        return self.__tag
        
#CHILD CLASS: MULTIPLE CHOICE
class multipleChoice(question):
    '''
    multiple choice is a child class.  It holds the:
    dictionary of options
    tag
    '''
    def __init__(self):
        super().__init__()
        self.__options = {}
        self.__tag = "MC"
        
    #Properties
    @property
    def options(self):
        return self.__options
    
    @property
    def tag(self):
        return self.__tag
    
    #Setters
    @options.setter
    def setOptions(self, newOptions):
        self.__options = newOptions
        
    def addOption(self, newOption, key):
        self.__options[key] = newOption


#CHILD CLASS: SHORT ANSWER
class shortAnswer(question):
    '''
    short answer is a child class.  It hold the:
    character limit
    tag
    '''
    def __init__(self):
        super().__init__()
        self.__charLimit = 0
        self.__tag = "SA"
        
    #Properties
    @property
    def charLimit(self):
        return self.__charLimit
    
    @property
    def tag(self):
        return self.__tag
    
    #Setters
    @charLimit.setter
    def setOptions(self, newLimit):
        self.__charLimit = newLimit
        
#CHILD CLASS: SHORT ANSWER
class essay(question):
    '''
    essay is a child class.  It hold the:
    minimum characters
    tag
    '''
    def __init__(self):
        super().__init__()
        self.__minChars = 0
        self.__tag = "ES"
        
    #Properties
    @property
    def minChars(self):
        return self.__minChars
    
    @property
    def tag(self):
        return self.__tag
    
    #Setters
    @minChars.setter
    def setOptions(self, newMinChars):
        self.__minChars = newMinChars
        
#CHILD CLASS: SHORT ANSWER
class matching(question):
    '''
    matching is a child class.  It hold the:
    number of options
    left options
    right options
    option count
    tag
    '''
    def __init__(self):
        super().__init__()
        self.__numOptions = 0
        self.__leftOptions = []
        self.__rightOptions = []
        self.__optionCount = 0
        self.__tag = "MA"
                
    #Properties
    @property
    def numOptions(self):
        return self.__numOptions
    
    @property
    def leftOptions(self):
        return self.__leftOptions
    
    @property
    def rightOptions(self):
        return self.__rightOptions
    
    @property
    def optionCount(self):
        return self.__optionCount
    
    @property
    def tag(self):
        return self.__tag
    
    #Setters
    @numOptions.setter
    def setNumOptions(self, newNumOptions):
        self.__numOptions = newNumOptions
        
    @leftOptions.setter
    def setLeftOptions(self, newLeftOptions):
        self.__leftOptions = newLeftOptions
    
    @rightOptions.setter
    def setRightOptions(self, newRightOptions):
        self.__rightOptions = newRightOptions
        
    def addOption(self):
        if self.__optionCount < self.__numOptions:
            leftOption = input("Enter an option to appear on the left: ")
            self.__leftOptions.append(leftOption)
            rightOption = input("Enter an option to appear on the right: ")
            self.__rightOptions.append(rightOption)
            self.__optionCount += 1
        else:
            print("Error: Number of options has already reached max.")            
        
#CHILD CLASS: MULTIPLE CHOICE
class ranking(question):
    '''
    ranking question is a child class.  It holds the:
    dictionary of options (number being key)
    tag
    '''
    def __init__(self):
        super().__init__()
        self.__options = {}
        self.__tag = "RA"
        
    #Properties
    @property
    def options(self):
        return self.__options
    
    @property
    def tag(self):
        return self.__tag
    
    #Setters
    @options.setter
    def setOptions(self, newOptions):
        self.__options = newOptions
        
    def addOption(self, newOption, key):
        self.__options[key] = newOption