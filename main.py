from tkinter import *
import sys
root=Tk()
root.title('Pongunlimited')
import cv2
import numpy as np
import mouse

def click(n):

    if n==1:

        vid=cv2.VideoCapture(0)

        ret=vid.set(3,1280)
        ret=vid.set(4,720)

        import pygame
        import random
        import time
        import mysql.connector
        import datetime

        dbcon=mysql.connector.connect(
            host='localhost',
            user='shreetesh',                   # username
            password='root'                     # password
        )

        cur=dbcon.cursor()
        try:
            cur.execute('create database pongundb;')
            cur.execute('use pongundb;')
            cur.execute('create table scores (Name varchar(25), Score int, Type varchar(10), Date varchar(15));')
        except mysql.connector.errors.DatabaseError:
            cur.execute('use pongundb;')

        pygame.init()
        screen=pygame.display.set_mode((500,500))
        done=False
        start=0
        sta=time.time()
        clock=pygame.time.Clock()
        x=40;tx=5;ty=5;yc=145;s=0;j=0
        xc=random.randrange(15,485)
        X=xc
        l=[]
        namev=name.get()
        if namev=='':
            namev='Anonymous'
        sound1=pygame.mixer.Sound('eat.wav')
        sound2=pygame.mixer.Sound('game_over_normal2.wav')
        font1=pygame.font.SysFont('comicsancms',50)
        font2=pygame.font.SysFont('comicsancms',80)
        text2=font2.render('GAME OVER',True,(250,250,250))
        while not done:

            ret,frame=vid.read()

            frame=cv2.flip(frame,1)

            hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

            l_green=np.array([31,107,135])
            u_green=np.array([59,208,255])

            mask=cv2.inRange(hsv,l_green,u_green)

            contours,_=cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

            for c in contours:
                if cv2.contourArea(c)>25:
                    posx,posy,_,_=cv2.boundingRect(c)
                    mouse.move(posx,posy,duration=0)

            for i in pygame.event.get():
                if i.type==pygame.QUIT:
                    done=True
            stop=time.time()
            screen.fill((0,0,0))
            clock.tick()
            text3=font2.render('%d'%(4-(stop-sta)),True,(250,250,250))
            press=pygame.key.get_pressed()
            if (stop-sta)>4:
                start=1
            else:
                screen.blit(text3,(250-text3.get_width()//2,250-text3.get_height()//2))
            (m,n)=pygame.mouse.get_pos()
            if start==1:
                pygame.draw.rect(screen,(100,100,100),pygame.Rect(0,60,500,10))
                pygame.draw.rect(screen,(100,100,100),pygame.Rect(490,60,10,440))
                pygame.draw.rect(screen,(100,100,100),pygame.Rect(0,490,500,10))
                pygame.draw.rect(screen,(100,100,100),pygame.Rect(0,60,10,440))
                pygame.draw.rect(screen,(200,200,200),pygame.Rect(x,420,60,10))
                pygame.draw.rect(screen,(200,200,200),pygame.Rect(X,130,60,10))
                x=m
                X=xc-30
                if X>=430: X=430
                elif X<=10: X=10
                if x>=430: x=430
                elif x<=10: x=10
                pygame.draw.circle(screen,(10,200,10),(xc,yc),5)
                xc+=tx
                yc+=ty
                if yc>=415 and yc<=418:
                    if xc>=x and xc<=x+60:
                        sound1.play(0)
                        ty*=-1
                        s+=1
                        if tx>0:
                            if l[1]>l[0]:
                                tx+=1
                            else:
                                tx-=1
                        if tx<0:
                            if l[1]<l[0]:
                                tx-=1
                            else:
                                tx+=1
                if yc<=125 and yc>=128:
                    if tx==0:
                        tx+=2
                if xc>=485:
                    tx=-5
                elif xc<=15:
                    tx=5
                if yc<=145:
                    ty=5
                    sound1.play(0)
                if yc>515:
                    tx=0
                    ty=0
                    screen.blit(text2,(250-text2.get_width()//2,250-text2.get_height()//2))
                    sound2.play(0)
                    if press[pygame.K_SPACE]: done=True
                    j+=1
                    if j==1:
                        sta1=time.time()
                    sto=time.time()
                    if (sto-sta1)>=2:
                        done=True
                l.append(m)
                if len(l)>2:
                    l.remove(l[0])
                text1=font1.render('SCORE= %d'%s,True,(150,150,150))
                screen.blit(text1,(295,15))
            pygame.display.flip()

        vid.release()
        cv2.destroyAllWindows()
        
        dt=datetime.date.today()
        dtv=dt.strftime('%d/%m/%Y')

        query='insert into scores values ("'+namev+'",'+'%d'%s+',"Normal","'+dtv+'");'

        cur.execute(query)
        dbcon.commit()

        print('Normal: Score= %d'%s)
        pygame.quit()

    elif n==2:

        vid=cv2.VideoCapture(0)

        ret=vid.set(3,1280)
        ret=vid.set(4,720)

        import pygame
        import random
        import time
        import mysql.connector
        import datetime

        dbcon=mysql.connector.connect(
            host='localhost',
            user='shreetesh',                   # username
            password='root'                     # password
        )

        cur=dbcon.cursor()
        try:
            cur.execute('create database pongundb;')
            cur.execute('use pongundb;')
            cur.execute('create table scores (Name varchar(25), Score int, Type varchar(10), Date varchar(15));')
        except mysql.connector.errors.DatabaseError:
            cur.execute('use pongundb;')

        pygame.init()
        screen=pygame.display.set_mode((500,500))
        done=False
        start=0
        sta=time.time()
        clock=pygame.time.Clock()
        x=40;tx=5;ty=5;yc=145;s=0;j=0
        xc=random.randrange(15,485)
        X=xc
        l=[]
        namev=name.get()
        if namev=='':
            namev='Anonymous'
        sound1=pygame.mixer.Sound('eat.wav')
        sound2=pygame.mixer.Sound('game_over_neon.wav')
        font1=pygame.font.SysFont('comicsancms',50)
        font2=pygame.font.SysFont('comicsancms',80)
        text2=font2.render('GAME OVER',True,(200,10,25))
        while not done:

            ret,frame=vid.read()

            frame=cv2.flip(frame,1)

            hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

            l_green=np.array([31,107,135])
            u_green=np.array([59,208,255])

            mask=cv2.inRange(hsv,l_green,u_green)

            contours,_=cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

            for c in contours:
                if cv2.contourArea(c)>25:
                    posx,posy,_,_=cv2.boundingRect(c)
                    mouse.move(posx,posy,duration=0)

            for i in pygame.event.get():
                if i.type==pygame.QUIT:
                    done=True
            stop=time.time()
            screen.fill((0,0,0))
            clock.tick(60)
            press=pygame.key.get_pressed()
            text3=font2.render('%d'%(4-(stop-sta)),True,(25,250,25))
            if (stop-sta)>4:
                start=1
            else:
                screen.blit(text3,(250-text3.get_width()//2,250-text3.get_height()//2))
            (m,n)=pygame.mouse.get_pos()
            if start==1:
                pygame.draw.rect(screen,(200,200,200),pygame.Rect(0,60,500,10))
                pygame.draw.rect(screen,(200,200,200),pygame.Rect(490,60,10,440))
                pygame.draw.rect(screen,(200,200,200),pygame.Rect(0,490,500,10))
                pygame.draw.rect(screen,(200,200,200),pygame.Rect(0,60,10,440))
                pygame.draw.rect(screen,(250,100,25),pygame.Rect(x,420,60,10),2)
                pygame.draw.rect(screen,(250,100,25),pygame.Rect(X,130,60,10),2)
                x=m
                X=xc-30
                if X>=430: X=430
                elif X<=10: X=10
                if x>=430: x=430
                elif x<=10: x=10
                pygame.draw.circle(screen,(10,200,10),(xc,yc),5)
                xc+=tx
                yc+=ty
                if yc>=415 and yc<=418:
                    if xc>=x and xc<=x+60:
                        sound1.play(0)
                        ty*=-1
                        s+=1
                        if tx>0:
                            if l[1]>l[0]:
                                tx+=1
                            else:
                                tx-=1
                        if tx<0:
                            if l[1]<l[0]:
                                tx-=1
                            else:
                                tx+=1
                if yc<=125 and yc>=128:
                    if tx==0:
                        tx+=2
                if xc>=485:
                    tx=-5
                elif xc<=15:
                    tx=5
                if yc<=145:
                    ty=5
                    sound1.play(0)
                if yc>515:
                    tx=0
                    ty=0
                    screen.blit(text2,(250-text2.get_width()//2,250-text2.get_height()//2))
                    sound2.play(0)
                    if press[pygame.K_SPACE]: done=True
                    j+=1
                    if j==1:
                        sta1=time.time()
                    sto=time.time()
                    if (sto-sta1)>=2:
                        done=True
                l.append(m)
                if len(l)>2:
                    l.remove(l[0])
                text1=font1.render('SCORE= %d'%s,True,(0,15,150))
                screen.blit(text1,(295,15))
            pygame.display.flip()

        vid.release()
        cv2.destroyAllWindows()

        dt=datetime.date.today()
        dtv=dt.strftime('%d/%m/%Y')

        query='insert into scores values ("'+namev+'",'+'%d'%s+',"Neon","'+dtv+'");'

        cur.execute(query)
        dbcon.commit()

        print('Neon: Score= %d'%s)
        pygame.quit()

    elif n==3:
        sys.exit(0)
    
    elif n==4:

        import mysql.connector

        dbcon=mysql.connector.connect(
            host='localhost',
            user='shreetesh',                       # username
            password='root'                         # password
        )

        cur=dbcon.cursor()

        try:
            cur.execute('create database pongundb;')
            cur.execute('use pongundb;')
            cur.execute('create table scores (Name varchar(25), Score int, Type varchar(10), Date varchar(15));')
        except mysql.connector.errors.DatabaseError:
            cur.execute('use pongundb;')

        cur.execute('select * from scores;')
        val=cur.fetchall()

        scores=''

        if len(val)==0:
            scores='\nNo games played yet.\nScoreboard is empty'
        else:
            for i in range(len(val)-1,-1,-1):
                scores+='\n%d.\t'%(len(val)-i)
                scores+='Name: '+val[i][0]+'\n\t'+'Score: %d'%val[i][1]+'\n\t'+'Type: '+val[i][2]+'\n\t'+'Date Played: '+val[i][3]+'\n'

        newroot=Tk()
        newroot.title('Scores')
        newf=Frame(newroot,height=500,width=500,bg='black')
        newlbl1=Label(newf,text='SCORECARD',font=('Lucida console',30,'bold'),bg='black',fg='white')
        newlbl1.pack()

        table=Text(newroot,height=24,width=52,font=('calibre',12))
        scroll=Scrollbar(newroot,command=table.yview)
        table.configure(yscrollcommand=scroll.set)
        table.insert(END,scores,'grey')
        table.config(state=DISABLED)
        table.place(x=15,y=50)
        newf.propagate(0)
        newf.pack()
        newroot.mainloop()

namev=''
f=Frame(root,height=500,width=500,bg='black')
txt=Text(root,height=14,width=28)
lbl1=Label(f,text='WELCOME TO',font=('Lucida console',30,'bold'),bg='black',fg='white')
lbl2=Label(f,text='PONG UNLIMITED',font=('Lucida console',30,'bold'),bg='black',fg='white')
lbl4=Label(f,text='Your Name:',font=('Lucida console',15),bg='black',fg='white')
img=PhotoImage(file='pongimage.png')
txt.image_create(END,image=img)
txt.place(x=15,y=190)
lbl1.pack(pady=0)
lbl2.pack()
lbl4.place(x=15,y=120)
name=Entry(root,textvariable=namev,font=('clibre',15))
name.place(x=150,y=120)
b1=Button(f,text='PLAY: Normal',height=2,width=20,font=('bold',10),command=lambda:click(1),activebackground='gray')
b2=Button(f,text='PLAY: Neon',height=2,width=20,font=('bold',10),command=lambda:click(2),fg='dark orange',activebackground='gray')
b3=Button(f,text='EXIT',height=2,width=20,font=('bold',10),command=lambda:click(3),activebackground='red')
b4=Button(f,text='DISPLAY SCORES',height=2,width=20,font=('bold',10),command=lambda:click(4),activebackground='gray')
b1.place(x=285,y=190)
b2.place(x=285,y=250)
b4.place(x=285,y=310)
b3.place(x=285,y=370)
lbl3=Label(f,text='Version: v2020',font=('Times',10),bg='black',fg='gray')
lbl3.pack(side=BOTTOM,pady=5)
f.propagate(0)
f.pack()
root.mainloop()