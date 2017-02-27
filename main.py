from tkinter import *
from Application_UI import MainMenu

def main():
    root = Tk()
    root.title('Welcome to the most awesomest survey/quiz system thats way better than Google forms')
    root.geometry('800x600')

    mainMenu = MainMenu(root)
    mainMenu.displayMainMenu()
    root.mainloop()


if __name__ == '__main__':
    main()