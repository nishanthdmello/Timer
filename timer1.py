from tkinter import *
# from pygame import *
# mixer.init()



# global it;it=0 

def insert(*time):        
    for i in range(3):
            e[i].insert(0,time[i])       

def get():
    
    #adds 00 where no input is given
    try:
        h=int(e1.get())                 
    except:
        e1.insert(0,0)
        h=0
    try:
        m=int(e2.get())
    except:
        e2.insert(0,0)
        m=0
    try:
        s=int(e3.get())
    except:
        e3.insert(0,0)
        s=0
        
    for i in range(3):
            e[i].delete(0,END)

    if h<0 or m<0 or s<0:#makes -ve inputs zero
        insert('00','00','00')
        global a,it;a=0;it=0  
    else:
        h,m,s,cs=check(h,m,s,0)
        insert(h,m,s)
        # for i in range(3):
        #     e[i].delete(0,END)                
    return(int(h),int(m),int(s))       

def check(h,m,s,cs):#makes single digit double by concatenating 0
    
    if h<10:
        h="0"+str(h)
    if m<10:
        m="0"+str(m)
    if s<10:
        s="0"+str(s)
    if cs<10:
        cs="0"+str(cs)
    return(h,m,s,cs)

def update():
    
    global it,a        
    if it and a:

        t=it
        h=t//360000;  t%=360000
        m=t//6000;    t%=6000
        s=t//100;     cs=t%100            
        h,m,s,cs=check(h,m,s,cs) 
        l.config(text=f"{h}:{m}:{s}.{cs}")          
        it-=1;     
        l.after(10,update)

    elif it==0 and a:
        
        b1['state']=DISABLED
        l.config(text="Timer Done")            
        # mixer.music.load("sound.mp3")
        # mixer.music.play(loops=100)            

def start():

    # global it,a;a=1    
    global a;a=1    
    # h,m,s=get()
        
    # if h>=0 and m>=0 and s>=0:
    b1.config(command=stop,image=img[1])            
    # for i in range(3):
    #     e[i]['state']=DISABLED          
    # for i in but:
    #     i['state']=DISABLED
    update()  

def initstart():

    global it,a;a=1    
    h,m,s=get()
    it=(h*3600+m*60+s)*100 
    # if h+m+s==0:
    #     h,m,s,cs=check(0,0,0,0)
    #     for i in range(3):
    #         e[i].delete(0,END) 
    #     insert(h,m,s)
        
    if h>0 and m>0 and s>0:
        b1.config(command=stop,image=img[1])            
        for i in range(3):
            e[i]['state']=DISABLED          
        update()       
    
def stop():        
    global a;a=0
    b1.config(command=start,image=img[0])

def reset():
    
    global a,it;a=0;it=0
    for i in range(3):
        e[i]['state']=NORMAL      
    b1.config(command=initstart,state=NORMAL,image=img[0])        
    # mixer.music.stop()        
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
insert('00','00','00')

b1=Button(but_frame,padx=10,relief=FLAT,command=initstart,image=img[0],bg="black")
b2=Button(but_frame,padx=10,relief=FLAT,command=reset,image=img[2],bg="black")
b1.grid(row=0,pady=5,padx=10)
b2.grid(row=0,column=1,padx=10)

l=Label(root,text="00:00:00.00",font=("Helvetica",50),bg="black",fg="white")
l.grid(row=4,column=0,columnspan=3,pady=10)

mainloop()

