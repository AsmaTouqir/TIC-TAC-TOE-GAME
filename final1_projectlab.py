
from tkinter import *
from tkinter import messagebox
import random as r

#add all main widgets for taking player information
def button(frame):#Function to define a button
    Label(frame,text='Player 1 name:',font=('times 20 bold italic'),bg="#765751").grid(row=5,column=0)                  #label for planyer name 1
    player1name=StringVar()                                                 #Special Variable for storing player name 1
    enterplayer1name=Entry(frame,textvariable=player1name,width=40)           #creating text-box
    enterplayer1name.grid(row=5,column=1)                                 
    Label(frame,text='Player 2 name:',font=('times 20 bold italic'),bg="#765751").grid(row=6,column=0)   #label for player name 2
    player2name=StringVar()                                                     #special variable for storing player name 2
    enterplayer2name=Entry(frame,textvariable=player2name,width=40)              #text box for player number two
    enterplayer2name.grid(row=6,column=1) #placing the above widget
    b=Button(frame,padx=1,bg="#84EA11",width=3,text="   ",font=('arial',50,'bold'),relief=GROOVE,bd=5)
    #save information button
    def save():
        text="TIC TAC TOE PLAYERS:"+"\n"+"p1: "+enterplayer1name.get()+"\n"+"p2: "+enterplayer2name.get()+"\n"+"'"+a+"' has won"
        with open("data.txt",'w') as f:
            f.writelines(text)
    button_ok=Button(frame,text='save',font=('Ariel 15 bold italic'),bg='#84EA11',relief=GROOVE,command=save)
    button_ok.grid(row=7,column=1)
    button_quit=Button(frame,text='exit',font=('Ariel 15 bold italic'),bg='#84EA11',relief=GROOVE,command=root.destroy)
    button_quit.grid(row=8,column=1)
    def enterplayername_delete():
        enterplayer1name.delete(first=0,last=22)
        enterplayer2name.delete(first=0,last=22)
    B=Button(frame, text="clear",font=('Ariel 15 bold italic'),bg='#84EA11',relief=GROOVE,command=enterplayername_delete)
    B.grid(row=8,column=2)    
    return b
def change_a():             #Function to change the operand for the next player
    global a
    for i in ['O','X']:
        if not(i==a):
            a=i
            break
def reset():                #Resets the game
    global a
    for i in range(3):
        for j in range(3):
                b[i][j]["text"]=" "
                b[i][j]["state"]=NORMAL
    a=r.choice(['O','X'])
def check():                #Checks for victory or Draw
    for i in range(3):
            if(b[i][0]["text"]==b[i][1]["text"]==b[i][2]["text"]==a or b[0][i]["text"]==b[1][i]["text"]==b[2][i]["text"]==a):
                    messagebox.showinfo("Congrats!!","'"+a+"' has won")
                    reset()
    if(b[0][0]["text"]==b[1][1]["text"]==b[2][2]["text"]==a or b[0][2]["text"]==b[1][1]["text"]==b[2][0]["text"]==a):
        messagebox.showinfo("Congrats!!","'"+a+"' has won")
        reset()   
    elif(b[0][0]["state"]==b[0][1]["state"]==b[0][2]["state"]==b[1][0]["state"]==b[1][1]["state"]==b[1][2]["state"]==b[2][0]["state"]==b[2][1]["state"]==b[2][2]["state"]==DISABLED):
        messagebox.showinfo("Tied!!","The match ended in a draw")
        reset()

def click(row,col):
        b[row][col].config(text=a,state=DISABLED,disabledforeground=colour[a])
        check()
        change_a()
        label.config(text=a+"'s Chance",bg="#765751")

###############   Main Program #################
root=Tk()                   #Window defined
root.title("Tic-Tac-Toe")#Title given
root.configure(bg="#765751")
a=r.choice(['O','X'])       #Two operators defined
colour={'O':"#1142EA",'X':"#FF2E24"}
b=[[],[],[]]
for i in range(3):
        for j in range(3):
                b[i].append(button(root))
                b[i][j].config(command= lambda row=i,col=j:click(row,col))
                b[i][j].grid(row=i,column=j)
label=Label(text=a+"'s Chance",font=('arial',20,'bold'),bg="#765751")
label.grid(row=3,column=0,columnspan=3)
root.mainloop()
