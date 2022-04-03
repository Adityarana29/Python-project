## import libraries
from tkinter import *
from gtts import gTTS
from playsound import playsound

#created a window
root = Tk()
root.geometry('300x250')
root.resizable(0,0)
root.config(bg = 'ghost white')
root.title('Aditya Rana- TEXT_TO_SPEECH')


#Heading
Label(root, text = 'TEXT_TO_SPEECH' , font='arial 20 bold' , bg ='white smoke').pack()

#Label
Label(root, text ='Enter Text', font ='Roman 15 bold', bg ='white smoke').place(x=20,y=60)

#text variable
Msg = StringVar()

#Entry
entry_field = Entry(root,textvariable =Msg, width ='50')
entry_field.place(x=20 , y=100)

#defined a function of text to speech 
def Text_to_speech():
    Message = entry_field.get()
    speech = gTTS(text = Message)
    speech.save('text-to-speech.mp3')
    playsound('text-to-speech.mp3')

def Exit():
    root.destroy()

def Reset():
    Msg.set("")

#created Button
Button(root, text = "PLAY" , font = 'arial 15 bold', command = Text_to_speech, bg = 'green',width =4).place(x=25, y=140)
Button(root,text = 'EXIT',font = 'arial 15 bold' , command = Exit, bg = 'red').place(x=100,y=140)
Button(root, text = 'RESET', font='arial 15 bold', command = Reset, bg = 'blue').place(x=175 , y =140)

#infinite loop to run program
root.mainloop()

#Aditya Rana
