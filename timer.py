from tkinter import *
from pygame import *
mixer.init()

def insert(t):        
    for i in range(3):
            e[i].insert(0,t[i])  

def get():

    t=[0,0,0,0]
    for i in range(3):
        try:
            t[i]=int(e[i].get())
            e[i].delete(0,END)
            if t[i]<0:
                t[i]=0
        except:
            t[i]=0
    
    t[2]=t[0]*36000+t[1]*60+t[2]
    t[0]=t[2]//36000; t[2]%=36000
    t[1]=t[2]//60;    t[2]%=60
        
    t=check(t)
    insert(t)
    return(int(t[0]),int(t[1]),int(t[2]))       

def check(t): 
    for i in range(4):
        if t[i]<10:
            t[i]="0"+str(t[i])
    return(t)

def update():
    
    global a,it        
    if it and a:

        t=it
        h=t//360000;  t%=360000
        m=t//6000;    t%=6000
        s=t//100;     cs=t%100 
        t=[h,m,s,cs]           
        h,m,s,cs=check(t) 
        l.config(text=f"{h}:{m}:{s}.{cs}")          
        it-=1;     
        l.after(10,update)

    elif it==0 and a:
        
        b1['state']=DISABLED
        l.config(text="Timer Done")            
        mixer.music.load("sound.mp3")
        mixer.music.play(loops=100)            

def start():

    global a;a=1    
    b1.config(command=stop,image=img[1])            
    update()  

def initstart():

    global it,a;a=1
    h,m,s=get()
    if h>0 or m>0 or s>0:
        it=(h*3600+m*60+s)*100
        b1.config(command=stop,image=img[1])
        b2['state']=NORMAL       

        for i in range(3):
            e[i]['state']=DISABLED          
        update()       
    
def stop():        
    global a;a=0
    b1.config(command=start,image=img[0])

def reset():
    
    global a;a=0
    for i in range(3):
        e[i]['state']=NORMAL      
    b1.config(command=initstart,state=NORMAL,image=img[0])
    b2['state']=DISABLED

    mixer.music.stop()        
    l.config(text="00:00:00.00")  

#All declarations are here

root=Tk()
root.title("Timer")
root.geometry('490x280')
root.configure(bg="black") 

strimg=PhotoImage(file="play.png")
stpimg=PhotoImage(file="pause.png")
rstimg=PhotoImage(file="reset.png")
img=[strimg,stpimg,rstimg] 

l=Label(root,text="Please keep the maximum time under 100 hours for good interface",font=10,bg="black",fg="red")
l.place(x=10,y=0)

ipt_frame=LabelFrame(root,padx=5,pady=10,bg="black")
but_frame=LabelFrame(root,padx=0,pady=10,bg="black")    
ipt_frame.grid(row=0,pady=40,column=0,rowspan=2,padx=40)
but_frame.grid(row=1,column=2,padx=40,pady=40)    

l1=Label(ipt_frame,text="HR",bg="black",fg="white")
l2=Label(ipt_frame,text="MIN",bg="black",fg="white")
l3=Label(ipt_frame,text="SEC",bg="black",fg="white")
l1.grid(row=0,column=0)
l2.grid(row=0,column=1)
l3.grid(row=0,column=2)

e1=Entry(ipt_frame,width=2,font=("Helvetica",20))
e2=Entry(ipt_frame,width=2,font=("Helvetica",20))
e3=Entry(ipt_frame,width=2,font=("Helvetica",20))
e=[e1,e2,e3]
for i in range(3):
    e[i].grid(row=1,column=i,padx=10)
insert(['00','00','00'])

b1=Button(but_frame,padx=10,relief=FLAT,command=initstart,image=img[0],bg="black")
b2=Button(but_frame,padx=10,relief=FLAT,command=reset,image=img[2],bg="black",state=DISABLED)
b1.grid(row=0,pady=5,padx=10)
b2.grid(row=0,column=1,padx=10)

l=Label(root,text="00:00:00.00",font=("Helvetica",50),bg="black",fg="white")
l.grid(row=4,column=0,columnspan=3,pady=10)

mainloop()

