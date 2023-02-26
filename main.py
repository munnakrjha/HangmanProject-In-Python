import random
from tkinter import *

print("-----------Welcome to ProjectGurukul------------")

root=Tk()
root.title('ProjectGurukul Hangman Game')

words = ['Project', 'Gurukul', 'Python', 'Hangman', 'Coding', 'Computer', 'Laptop', 'String', 'Guess', 'Tkinter' ]
greet = Label(root, font = ('arial', 30, 'bold'), text = "Welcome!").grid(row = 0,columnspan = 3)

won=0
entered=''

curr = random.choice(words)
print(curr)

guessed=''
moves=len(curr)+1
str=''

#This function contains the complete logic of hangman game
def play():
    global guessed
    global curr
    global won
    global entered
    global moves
    global str

    entered=f"{en.get()}"

    if(entered in guessed):
        btn=Entry(root,textvariable=en,width=5,font =('arial', 20, 'bold'))
        btn.grid(row=2,column=2)
        submitbtn=Button(root,text="Submit",command=play,bg="DodgerBlue2",fg="white",font = ('arial', 20, 'bold')).grid(row=4,columnspan=3)
        return

    guessed+=entered
    entered=entered[0]
    print(entered)

    won=1
    str=''
    for ch in curr:
        if ch in guessed:
            str+=ch
            print(ch,end = '')
        else:
            won=0
            str+='_'
            print("_",end = '')

    print('')    
    entered_string =Label(root, font = ('arial', 20, 'bold'),text=str).grid(row=6,columnspan=3)
    
    moves-=1
    print(moves)

    if(won==1):
        Win = Label(root, font = ('arial', 20, 'bold'), text = "You Won!!!")
        Win.grid(row = 8, columnspan = 3)

    elif won==0 and moves<=0:
        Lost = Label(root, font = ('arial', 20, 'bold'), text = "You Lost!!!")
        Lost.grid(row = 8, columnspan = 3)

    else:
        btn=Entry(root,textvariable=en,width=5,font =('arial', 20, 'bold'))
        btn.grid(row=2,column=2)
        submitbtn=Button(root,text="Submit",command=play,bg="DodgerBlue2",fg="white",font = ('arial', 20, 'bold'))
        submitbtn.grid(row=4,columnspan=3)


msg = Label(root, font = ('arial', 20, 'bold'), text = "Enter a character")
msg.grid(row = 2,column = 1)

# while won==0 and moves>0:
en=StringVar() 
btn=Entry(root,textvariable=en,width=5,font =('arial', 20, 'bold'))
btn.grid(row=2,column=2)

submitbtn=Button(root,text="Submit",command=play,bg="DodgerBlue2",fg="white",font = ('arial', 20, 'bold'))
submitbtn.grid(row=4,columnspan=3)

mainloop()