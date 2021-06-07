# the json module to work with json files 
import json
import tkinter
from tkinter import *
import random


# questions = [
#     "How many Keywords are there in C Programming language ?",
#     "Which of the following functions takes A console Input in Python ?",
#     "In which language is Python written?",
#     "Which of The Following is must to Execute a Python Code ?",
#     "Which character is used in Python to make a single line comment?",
#     "The append Method adds value to the list at the  ?",
#     "What do we use to define a block of code in Python language",
#     "Which of The following is executed in browser(client side) ?",
#     "Which of the following keyword is used to create a function in Python ?",
#     "To Declare a Global variable in python we use the keyword ?",
# ]

# answers_choice = [
#     ["23","32","33","43",],
#     ["get()","input()","gets()","scan()",],
#     ["English","PHP","C","All of the above",],
#     ["TURBO C","Py Interpreter","Notepad","IDE",],
#     ["//","/","#","!",],
#     ["custom location","end","center","beginning",],
#     ["Indentation","Key","Brackets","Non of these",],
#     ["perl","css","python","java",],
#     ["function","void","fun","def",],
#     ["all","var","let","global",],
# ] 

# load questions and answer choices from json file instead of the file
with open('./data.json', encoding="utf8") as f:
    data = json.load(f)


questions = [v for v in data[0].values()]
answers_choice = [v for v in data[1].values()]

answers = [1,1,2,1,2,1,0,1,3,3] 

user_answer = []

indexes = []
def gen():
    global indexes
    while(len(indexes) < 5):
        x = random.randint(0,9)
        if x in indexes:
            continue
        else:
            indexes.append(x)


def showresult(score):
    lblQuestion.destroy()
    r1.destroy()
    r2.destroy()
    r3.destroy()
    r4.destroy()
    #labelimage = Label(
      #  root,
      #  background = "#000000",
      #  border = 0,
    #)
    #labelimage.pack(pady=(50,30))
    labelresulttext = Label(
        root,
        font = ("Calibri",20),
        background = "#86CED2",
        foreground = "#18252A",
    )
    labelresulttext.pack(pady=(170,50))
    if score == 25:
       # img = PhotoImage(file="great.png")
       # labelimage.configure(image=img)
       # labelimage.image = img
        labelresulttext.configure(text="Well done!!\n\nyou've got 25 marks out of 25.")
    elif (score == 20):
       # img = PhotoImage(file="ok.png")
       # labelimage.configure(image=img)
       # labelimage.image = img
        labelresulttext.configure(text="Excellent!!\n\n you've got 20 out of 25.")
    elif (score == 15):
        #img = PhotoImage(file="ok.png")
       # labelimage.configure(image=img)
       # labelimage.image = img
        labelresulttext.configure(text="Keep it up!!\n\nyou've got 15 marks out of 25.")
    elif (score == 10):
        
       # img = PhotoImage(file="bad.png")
       # labelimage.configure(image=img)
       # labelimage.image = img
         labelresulttext.configure(text="Not satifactory!!\n\nYou've got 10 marks out of 25.")
    else:
       # img = PhotoImage(file="bad.png")
       # labelimage.configure(image=img)
       # labelimage.image = img
         labelresulttext.configure(text="You are failed this quiz!!\n\nYou've got 5 marks out of 25.")


def calc():
    global indexes,user_answer,answers
    x = 0
    score = 0
    for i in indexes:
        if user_answer[x] == answers[i]:
            score = score + 5
        x += 1
    print(score)
    showresult(score)


ques = 1
def selected():
    global radiovar,user_answer
    global lblQuestion,r1,r2,r3,r4
    global ques
    x = radiovar.get()
    user_answer.append(x)
    radiovar.set(-1)
    if ques < 5:
        lblQuestion.config(text= questions[indexes[ques]])
        r1['text'] = answers_choice[indexes[ques]][0]
        r2['text'] = answers_choice[indexes[ques]][1]
        r3['text'] = answers_choice[indexes[ques]][2]
        r4['text'] = answers_choice[indexes[ques]][3]
        ques += 1
    else:
        calc()
    




def startquiz():
    global lblQuestion,r1,r2,r3,r4
    lblQuestion = Label(
        root,
        text = questions[indexes[0]],
        font = ("Times New Roman", 18),
         background = "#86CED2",
        foreground = "#18252A",
        width = 500,
        justify = "center",
        wraplength = 400,
        #background = "#ffffff",
    )
    lblQuestion.pack(pady=(100,30))

    global radiovar
    radiovar = IntVar()
    radiovar.set(-1)

    r1 = Radiobutton(
        root,
        text = answers_choice[indexes[0]][0],
        font = ("Calibri", 18),
        background = "#FFEC00",
        foreground = "#18252A",
        value = 0,
        variable = radiovar,
        justify = "left",
        command = selected,
       
    )
    r1.pack(pady=5)

    r2 = Radiobutton(
        root,
        text = answers_choice[indexes[0]][1],
        font = ("Calibri", 18),
         background = "#FFEC00",
        foreground = "#18252A",
        value = 1,
        variable = radiovar,
         justify = "left",
        command = selected,
        
    )
    r2.pack(pady=5)

    r3 = Radiobutton(
        root,
        text = answers_choice[indexes[0]][2],
        font = ("Calibri", 18),
         background = "#FFEC00",
        foreground = "#18252A",
        value = 2,
        variable = radiovar,
         justify = "left",
        command = selected,
    
    )
    r3.pack(pady=5)

    r4 = Radiobutton(
        root,
        text = answers_choice[indexes[0]][3],
        font = ("Calibrir", 18),
         background = "#FFEC00",
        foreground = "#18252A",
        value = 3,
        variable = radiovar,
        justify = "left",
        command = selected,
    )
    r4.pack(pady=5)


def startIspressed():
    labeltext.destroy()
    lblinstruction.destroy()
    btnstart.destroy()
    gen()
    startquiz()



root = tkinter.Tk()
root.title("Quizstar")
root.geometry("700x600")
img0 = PhotoImage(file="wawa1.Png")
root.resizable(0,0)
#root.config(background="#ffffff")

bgimglabel = Label(
    root,
    image = img0,
)
bgimglabel.place(x=0, y=0, relwidth=1, relheight=1)

labeltext = Label(
    root,
    text = "Quiz Star",
    font = ("Showcard Gothic",24,"bold"),
    background = "#FFEC00",
    foreground = "#18252A",
     justify = "center",
    
)
labeltext.pack(pady=(100,60))


img2 = PhotoImage(file="Untitled-9.Png")

btnstart = Button(
    root,
    image = img2,
   #background1 = "#ffffff", 
   background =  "#FFEC00",
   #foreground = "#000000",
    relief = FLAT,
    border = 0,
    command = startIspressed,
     justify = "center",
    
)
btnstart.pack(pady = (30))

lblinstruction = Label(
    root,
    text = "Click start once you are ready",
    background = "#FFEC00",
    foreground = "#18252A",
    font = ("Calibri",16),
    justify = "center",
)
lblinstruction.pack(pady = (60,30))

lbrules = Label(
    root,
    text = "Good luck.",
    width = 100,
    font = ("Calibri",14),
   background = "#FFEC00",
    foreground = "#18252A",
)
lbrules.pack(pady=(40,0))

root.mainloop()