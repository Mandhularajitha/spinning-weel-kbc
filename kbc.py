
from tkinter import*
#pygame.init()
root=Tk()  #root = tk.Tk() The next line of code contains the Label widget.
root.title('who wants to be a millionaire')
root.geometry('1352x652+0+0')
root.configure(background='black')


#========================================Frames============================================================
ABC=Frame(root,bg='black')
ABC.grid()

ABC1=Frame(root,bg='black',bd=20,width=900,height=600)
ABC1.grid(row=0,column=0)
ABC2=Frame(root,bg='black',bd=20,width=452,height=600)
ABC2.grid(row=0,column=1)


ABC1a=Frame(ABC1,bg='black',bd=20,width=900,padx=110,height=200)
ABC1a.grid(row=0,column=0)
ABC1b=Frame(ABC1,bg='black',bd=20,width=900,height=200)
ABC1b.grid(row=1,column=0)
ABC1c=Frame(ABC1,bg='black',bd=20,width=900,height=200)
ABC1c.grid(row=2,column=0)

#========
# =================================images=======================================================
def change50_50():
    canvas=Canvas(ABC1a,bg='black',width=180,height=80)
    canvas.grid(column=0,row=0)
    canvas.delete('all')
    image1=PhotoImage(file='50-50-X.png')
    canvas.create_image(90,40,image=image1)
    canvas.image=image1

def peoplechange():
    canvas=Canvas(ABC1a,bg='black',width=180,height=80)
    canvas.grid(column=1,row=0)
    canvas.delete('all')
    image1=PhotoImage(file='audiencePoleX.png')
    canvas.create_image(90,40,image=image1)
    canvas.image=image1


def changephone():
    canvas=Canvas(ABC1a,bg='black',width=180,height=80)
    canvas.grid(column=2,row=0)
    canvas.delete('all')
    image1=PhotoImage(file='phoneAFriendx.png')
    canvas.create_image(90,40,image=image1)
    canvas.image=image1


def millionpicture1():
    canvas=Canvas(ABC2,bg='black',width=430,height=600)
    canvas.grid(column=0,row=0)
    canvas.delete('all')
    image1=PhotoImage(file='picture3.png')
    canvas.create_image(215,300,image=image1)
    canvas.image=image1


def millionpicture2():
    canvas=Canvas(ABC2,bg='black',width=430,height=600)
    canvas.grid(column=0,row=0)
    canvas.delete('all')
    image1=PhotoImage(file='picture1.png')
    canvas.create_image(215,300,image=image1)
    canvas.image=image1



def millionpicture3():
    canvas=Canvas(ABC2,bg='black',width=430,height=600)
    canvas.grid(column=0,row=0)
    canvas.delete('all')
    image1=PhotoImage(file='picture2(1).png')
    canvas.create_image(215,300,image=image1)
    canvas.image=image1



    
#==============================================Images=======================================================

centreimage=PhotoImage(file='center.png')
logocentre=Button(ABC1b,image=centreimage,bg='black',width=300,height=200)
logocentre.grid()

image50_50=PhotoImage(file='50-50.png')
live50_50=Button(ABC1a,image=image50_50,bg='black',width=180,height=80,command=change50_50)
live50_50.grid(row=0,column=0)

imagepeople=PhotoImage(file='audiencePole.png')
livepeople=Button(ABC1a,image=imagepeople,bg='black',width=180,height=80,command=peoplechange)
livepeople.grid(row=0,column=1)

imagephone=PhotoImage(file='phoneAFriend.png')
livephone=Button(ABC1a,image=imagephone,bg='black',width=180,height=80,command=changephone)
livephone.grid(row=0,column=2)

millionimage=PhotoImage(file='Picture0.png')
millionImg=Button(ABC2,image=millionimage,bg='black',width=430,height=600)
millionImg.grid(row=0,column=0)






#=====================================Questions=======================================================
Question1=StringVar()
Question2=StringVar()
Question3=StringVar()
Question4=StringVar()

Answer1=StringVar()
Answer2=StringVar()
Answer3=StringVar()
Answer4=StringVar()

Question1.set('Q1:What is 2+32')
Answer1.set('22')
Answer2.set('32')
Answer3.set('31')
Answer4.set('34')

def Question2():
    Question1.set('Q1:What is 7*7')
    Answer1.set('21')
    Answer2.set('14')
    Answer3.set('49')
    Answer4.set('7')
    millionpicture1()


def Question3():
    Question1.set('Q1:What is 5+5')
    Answer1.set('10')
    Answer2.set('55')
    Answer3.set('35')
    Answer4.set('15')
    millionpicture2()


#==================================Text,LABELS,Button==================================================



textquestion=Entry(ABC1c,font=('arial',18,'bold'),bg='blue',fg='white',bd=5,width=44,justify=CENTER,textvariable=Question1)
textquestion.grid(row=0,column=0,columnspan=4,pady=4,)


lblquestionA=Label(ABC1c,font=('arial',14,'bold'),text='A:',bg='black',fg='white',bd=5,justify=CENTER)
lblquestionA.grid(row=1,column=0,pady=4,sticky=W)
textquestion1=Button(ABC1c,font=('arial',14,'bold'),bg='blue',fg='white',bd=1,width=17,height=2,justify=CENTER,textvariable=Answer1,command=Question2)
textquestion1.grid(row=1,column=1,pady=4)

lblquestB=Label(ABC1c,font=('arial',14,'bold'),text='B:',bg='black',fg='white',bd=5,justify=LEFT)
lblquestB.grid(row=1,column=2,sticky=W)
textquestion2=Button(ABC1c,font=('arial',14,'bold'),bg='blue',fg='white',bd=1,width=17,height=2,justify=CENTER,textvariable=Answer2,command=Question3)
textquestion2.grid(row=1,column=3,pady=4)

lblquestC=Label(ABC1c,font=('arial',14,'bold'),text='C:',bg='black',fg='white',bd=5,justify=LEFT)
lblquestC.grid(row=2,column=0,sticky=W)
textquestion3=Button(ABC1c,font=('arial',14,'bold'),bg='blue',fg='white',bd=1,width=17,height=2,justify=CENTER,textvariable=Answer3)
textquestion3.grid(row=2,column=1,pady=4)


lblquestionD=Label(ABC1c,font=('arial',14,'bold'),text='D:',bg='black',fg='white',bd=5,justify=LEFT)
lblquestionD.grid(row=2,column=2,sticky=W)
textquestion4=Button(ABC1c,font=('arial',14,'bold'),bg='blue',fg='white',bd=1,width=17,height=2,justify=CENTER,textvariable=Answer4,command=millionpicture1)
textquestion4.grid(row=2,column=3,pady=4)




root.mainloop()


