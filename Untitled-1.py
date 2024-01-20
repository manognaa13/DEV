from tkinter import *
from PIL import Image, ImageTk
from string import ascii_uppercase
import random
from tkinter import messagebox
import tkinter as tk
import pygame

run = True
global count
global img
global chances
global la
chances = 7
count = 0
global temp
global length
global word
temp = 0
global l1
l1 = []

root1=Tk()
root1.geometry("1050x550")
root1.title("Hangman")
root1.configure(bg = '#000000')
bg = PhotoImage(file = "bcg.png")
canvas = Canvas(root1, width = 1050, height=550)
bglabel = Label(root1,image = bg)
bglabel.place(x=0,y=0)
root1.attributes('-fullscreen',True)

def instructions():
            messagebox.showinfo("INSTRUCTIONS"," \n                                     Want to win???\n\n                          ----Follow the instructions----\n\n1.  The computer randomly generates a word from the list. \n\n 2.  It draws a number of dashes equivalent to the number of letters in the word. \n\n 3.  If a guessed letter appears in the word, all instances of it are revealed. \n\n 4.  If not, guesser loses a chance.\n\n 5.  For every chance lost, body parts of hangman are displayed one after the other. \n\n 6.  The guesser loses, when the entire figure has been drawn\n\n 7.  The guesser wins, when all the letters in the word are correctly guessed!!\n\n                                 ALL THE BEST\n")

def close1():
            global run
            res1 = messagebox.askyesno("Hangman","Do you want to exit the game?")
            if res1:
                run = False
                root1.destroy()
            else:
                run = True

def game_tab():
    global la
    i=0  
    root=Toplevel(root1)
    root.geometry("1050x550")
    root.attributes('-fullscreen',True)
    root.title("Hangman")
    bg1 = PhotoImage(file = "gamebg.png")
    canvas = Canvas(root, width = 1050, height=550)
    bglabel1 = Label(root,image = bg1)
    bglabel1.place(x=0,y=0)

    while run:
        
            la=Label(root)
            la.place(x=0,y=90)
            l=['apple','banana','orange','watermelon','cherry','strawberry','hangman','invert','python','tkinter','java','technology','server','interface','error','hardware','rapid','repeat','rabbit','program','technical','vision','mission','practice','skills','movie','film','cartoon','teacher','knowledge','compete','competition','freedom','unique','simple','standard']
            himg=['stage00.png','stage11.png','stage22.png','stage33.png','stage44.png','stage55.png','stage66.png']
            l1=[]
                
            def close():
                    global run
                    chances = 7
                    i = 0
                    root.destroy()
        
        #lives printing
            l2=Label(root,text=" ",bg="#000000",fg='#FFFFFF',font=("arial",25))
            l2.config(text="Remaining chances :" + str(chances))
            l2.place(x=2,y=500)

        #lost case
            l4=Label(root,text=" ",bg="#000000",fg='#FFFFFF',font=("arial",30))
        #won case
            l5=Label(root,text=" ",bg="#000000",fg='#FFFFFF',font=("arial",30))
        #actual word display
            l3=Label(root,text=" ",bg="#000000",fg='#FFFFFF',font=("arial",25))

        #exit image printing
            exited=ImageTk.PhotoImage(Image.open('exit.png'))
            exitbtn=Button(root,image=exited,command=close)
            exitbtn.place(x=1200,y=0)
    
            def checkwin(s):
                global run
                global count
                global la
                if s == len(act_word):
                        wonimg = ImageTk.PhotoImage(Image.open('WIN.png'))
                        la.configure(image = wonimg)
                        la.image = wonimg
                        la.place(x=1068,y=230)
                        l5.configure(text = "Congrats !!! You won the game")
                        l5.place(x=0,y=200)

            def Hangman():
                global img
                global la
                global length
                global temp
                if temp != len(act_word) and temp < len(act_word):
                        img = ImageTk.PhotoImage(Image.open(himg[6-chances]))
                        la = Label(root,image=img)
                        la.place(x=1070,y=200)


            def play(letter):
                global chances
                global run
                global count
                global temp
                global word

                if chances > 0:
                    if letter in word:
                            l2.config(text="Lives left : " + str(chances))
                            for i in range(0,len(word)):
                                if word[i]==letter:
                                    temp += 1
                                    l1[i].config(text=letter)
                                    count += 1
                                    checkwin(count) 

                    elif letter not in word:
                            if temp != len(act_word) and temp < len(act_word):                                  
                                    chances = chances - 1
                                    l2.config(text="Lives left : " + str(chances))
                                    if chances==0:
                                        l2.config(text="Lives left : " + str(0))
                                        l3.config(text="Actual word : " + act_word.upper())
                                        l3.place(x=2,y=400)
                                        l4.configure(text = "You lost the game")
                                        l4.place(x=2,y=200)
                                        loseimg = ImageTk.PhotoImage(Image.open('lose.png'))
                                        la.configure(image = loseimg)
                                        la.image = loseimg
                                        la.place(x = 2 ,y = 0)  
                                        chances = 7                                      
                            Hangman()

            def game():
                global word
                global act_word
                global chances
                global run
                global count
                global length
                global temp
                temp = 0
                word = random.choice(l)
                act_word = word
                length = len(act_word)
                chances = 7
                count = 0
                x = 80
                l2.config(text="Lives left : " + str(chances))
                for i in range(0,len(word)):
                    x += 60
                    l1.append(Label(root,text=" _ ",bg='#E7FFFF',fg='#000000',font=("arial",30)))
                    l1[i].place(x = x,y='300')
                
            if(chances!=0):
                    img1=ImageTk.PhotoImage(Image.open('a.png'))
                    btn1=Button(root,image=img1,bd=0,command=lambda:play('a'))
                    btn1.place(x=210,y=580)
                    img2=ImageTk.PhotoImage(Image.open('b.png'))
                    btn2=Button(root,image=img2,bd=0,command=lambda:play('b'))
                    btn2.place(x=280,y=580)
                    img3=ImageTk.PhotoImage(Image.open('c.png'))
                    btn3=Button(root,image=img3,bd=0,command=lambda:play('c'))
                    btn3.place(x=350,y=580)
                    img4=ImageTk.PhotoImage(Image.open('d.png'))
                    btn4=Button(root,image=img4,bd=0,command=lambda:play('d'))
                    btn4.place(x=420,y=580)
                    img5=ImageTk.PhotoImage(Image.open('e.png'))
                    btn5=Button(root,image=img5,bd=0,command=lambda:play('e'))
                    btn5.place(x=490,y=580)
                    img6=ImageTk.PhotoImage(Image.open('f.png'))
                    btn6=Button(root,image=img6,bd=0,command=lambda:play('f'))
                    btn6.place(x=560,y=580)
                    img7=ImageTk.PhotoImage(Image.open('g.png'))
                    btn7=Button(root,image=img7,bd=0,command=lambda:play('g'))
                    btn7.place(x=630,y=580)
                    img8=ImageTk.PhotoImage(Image.open('h.png'))
                    btn8=Button(root,image=img8,bd=0,command=lambda:play('h'))
                    btn8.place(x=700,y=580)
                    img9=ImageTk.PhotoImage(Image.open('i.png'))
                    btn9=Button(root,image=img9,bd=0,command=lambda:play('i'))
                    btn9.place(x=770,y=580)
                    img10=ImageTk.PhotoImage(Image.open('j.png'))
                    btn10=Button(root,image=img10,bd=0,command=lambda:play('j'))
                    btn10.place(x=840,y=580)
                    img11=ImageTk.PhotoImage(Image.open('k.png'))
                    btn11=Button(root,image=img11,bd=0,command=lambda:play('k'))
                    btn11.place(x=910,y=580)
                    img12=ImageTk.PhotoImage(Image.open('l.png'))
                    btn12=Button(root,image=img12,bd=0,command=lambda:play('l'))
                    btn12.place(x=980,y=580)
                    img13=ImageTk.PhotoImage(Image.open('m.png'))
                    btn13=Button(root,image=img13,bd=0,command=lambda:play('m'))
                    btn13.place(x=1050,y=580)
                    img14=ImageTk.PhotoImage(Image.open('n.png'))
                    btn14=Button(root,image=img14,bd=0,command=lambda:play('n'))
                    btn14.place(x=210,y=640)
                    img15=ImageTk.PhotoImage(Image.open('o.png'))
                    btn15=Button(root,image=img15,bd=0,command=lambda:play('o'))
                    btn15.place(x=280,y=640)
                    img16=ImageTk.PhotoImage(Image.open('p.png'))
                    btn16=Button(root,image=img16,bd=0,command=lambda:play('p'))
                    btn16.place(x=350,y=640)
                    img17=ImageTk.PhotoImage(Image.open('q.png'))
                    btn17=Button(root,image=img17,bd=0,command=lambda:play('q'))
                    btn17.place(x=420,y=640)
                    img18=ImageTk.PhotoImage(Image.open('r.png'))
                    btn18=Button(root,image=img18,bd=0,command=lambda:play('r'))
                    btn18.place(x=490,y=640)
                    img19=ImageTk.PhotoImage(Image.open('s.png'))
                    btn19=Button(root,image=img19,bd=0,command=lambda:play('s'))
                    btn19.place(x=560,y=640)
                    img20=ImageTk.PhotoImage(Image.open('t.png'))
                    btn20=Button(root,image=img20,bd=0,command=lambda:play('t'))
                    btn20.place(x=630,y=640)
                    img21=ImageTk.PhotoImage(Image.open('u.png'))
                    btn21=Button(root,image=img21,bd=0,command=lambda:play('u'))
                    btn21.place(x=700,y=640)
                    img22=ImageTk.PhotoImage(Image.open('v.png'))
                    btn22=Button(root,image=img22,bd=0,command=lambda:play('v'))
                    btn22.place(x=770,y=640)
                    img23=ImageTk.PhotoImage(Image.open('w.png'))
                    btn23=Button(root,image=img23,bd=0,command=lambda:play('w'))
                    btn23.place(x=840,y=640)
                    img24=ImageTk.PhotoImage(Image.open('x.png'))
                    btn24=Button(root,image=img24,bd=0,command=lambda:play('x'))
                    btn24.place(x=910,y=640)
                    img25=ImageTk.PhotoImage(Image.open('y.png'))
                    btn25=Button(root,image=img25,bd=0,command=lambda:play('y'))
                    btn25.place(x=980,y=640)
                    img26=ImageTk.PhotoImage(Image.open('z.png'))
                    btn26=Button(root,image=img26,bd=0,command=lambda:play('z'))
                    btn26.place(x=1050,y=640)
                    
            game()
            root.mainloop()

def play():
        pygame.mixer.music.load('audio.mp3')
        pygame.mixer.music.play()
    
def stop():
        pygame.mixer.music.stop()


start=ImageTk.PhotoImage(Image.open('start.png'))
btnstart=Button(root1,image=start,command=game_tab)
btnstart.place(x=650,y=250)

exit1=ImageTk.PhotoImage(Image.open('exit.png'))
exitbtn1=Button(root1,image=exit1,command=close1)
exitbtn1.place(x=1200,y=0)

instr = ImageTk.PhotoImage(Image.open('instr.png'))
btninst = Button(root1,image=instr,command = instructions)
btninst.place(x=620,y=330)

play_m=ImageTk.PhotoImage(Image.open('startm.png'))
play_button=Button(root1,image=play_m,command=play)
play_button.pack()
play_button.place(x=622,y=410)

stop_m=ImageTk.PhotoImage(Image.open('stopm.png'))
stop_button=Button(root1,image=stop_m,command=stop,bg='#55CFFE')
stop_button.pack()
stop_button.place(x=622,y=490)

pygame.mixer.init()
root1.mainloop()