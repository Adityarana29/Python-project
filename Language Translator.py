#importing modules
from tkinter import *
from translate import Translator

# initializing window
Screen = Tk()
Screen.geometry('500x250')
Screen.resizable(0,0)
Screen.config(bg = 'ghost white')
Screen.title("Language Translator by- Aditya Rana")

InputLanguageChoice = StringVar()
TranslateLanguageChoice = StringVar()

#tuple for choosing languages
LanguageChoices = {'Hindi','English','French','German','Spanish'}
InputLanguageChoice.set('English')
TranslateLanguageChoice.set('Hindi')

def Translate():
    translator = Translator(from_lang= InputLanguageChoice.get(),to_lang=TranslateLanguageChoice.get())
    Translation = translator.translate(TextVar.get())
    OutputVar.set(Translation)


#choice for input language
InputLanguageChoiceMenu = OptionMenu(Screen,InputLanguageChoice,*LanguageChoices)
Label(Screen,text="Choose a Language",font ='arail 10 bold').grid(row=0,column=1)
InputLanguageChoiceMenu.grid(row=1,column=1)


#choice in which the language is to be translated
NewLanguageChoiceMenu = OptionMenu(Screen,TranslateLanguageChoice,*LanguageChoices)
Label(Screen,text="Translated Language",font ='arail 10 bold').grid(row=0,column=11)
NewLanguageChoiceMenu.grid(row=1,column=2)

Label(Screen,text="Enter Text", bg = 'green').grid(row=2,column =0)
TextVar = StringVar()
TextBox = Entry(Screen,textvariable=TextVar).grid(row=2,column = 1)

Label(Screen,text="Output Text", bg = 'blue').grid(row=2,column =4)
OutputVar = StringVar()
TextBox = Entry(Screen,textvariable=OutputVar).grid(row=2,column = 11)


#Button for calling function
B = Button(Screen,text="Translate",command=Translate, relief = GROOVE).grid(row=3,column=1,columnspan = 3)

mainloop()
