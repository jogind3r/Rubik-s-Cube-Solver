import random
from visual import *
from visual.controls import *
wid = 200
print """ press both buttons of mouse and move to zoom in and out
            press right mouse button and move to rotate the cube"""
display(x=wid, y=0, width=900, height=700, range=1.5, forward=-vector(0,1,1), newzoom=1)

c = controls(x=0, y=0, width=wid, height=700, range=60)

bl = button(pos=(-10,30), height=15, width=20, text='jumble', action=lambda: jumble())
br = button(pos=(10,30), height=15, width=20, text='solve', action=lambda: solve())
bU = button(pos=(0,-0), height=10, width=10, text='U', action=lambda: MU())
bD = button(pos=(0,-10), height=10, width=10, text='D', action=lambda: MD())
bR = button(pos=(0,-20), height=10, width=10, text='R', action=lambda: MR())
bL = button(pos=(0,-30), height=10, width=10, text='L', action=lambda: ML())
bF = button(pos=(0,-40), height=10, width=10, text='F', action=lambda: MF())
bB = button(pos=(0,-50), height=10, width=10, text='B', action=lambda: MB())
bUc = button(pos=(10,-0), height=10, width=10, text='cU', action=lambda: Mu())
bDc = button(pos=(10,-10), height=10, width=10, text='cD', action=lambda: Md())
bRc = button(pos=(10,-20), height=10, width=10, text='cR', action=lambda: Mr())
bLc = button(pos=(10,-30), height=10, width=10, text='cL', action=lambda: Ml())
bFc = button(pos=(10,-40), height=10, width=10, text='cF', action=lambda: Mf())
bBc = button(pos=(10,-50), height=10, width=10, text='cB', action=lambda: Mb())

s1 = slider(pos=(-15,-50), width=7, length=50, axis=(0,1,0), action=lambda: setrate())
s1.min=200
s1.max=2000
def setrate():
    global speed
    speed=s1.getvalue()

cF=color.red
cB=color.orange
cU=color.blue
cD=color.yellow
cL=color.gray(2)
cR=color.green
f="f"
b="b"
l="l"
r="r"
u="u"
d="d"
B="blue"
R="red"
Y="yellow"
W="white"
O="orange"
G="green"
speed=200

debug=1
hide=0

class dice():
    val=[0,0,0]
    d=0
    s=[]
    def __init__(self,x,y,z):
        self.s=[box(),box(),box(),box(),box(),box()]
        self.s[0].height=.04
        self.s[1].height=.04
        self.s[2].width=.04
        self.s[3].width=.04
        self.s[4].length=.04
        self.s[5].length=.04
        self.s[0].y+=.5
        self.s[1].y-=.5
        self.s[2].z-=.5
        self.s[3].z+=.5
        self.s[4].x-=.5
        self.s[5].x+=.5
        self.pos(x,y,z)
        
        
    def pos(self,x,y,z):
        self.s[0].y=.5+y
        self.s[0].x=x
        self.s[0].z=z
        self.s[1].y=y-.5
        self.s[1].z=z
        self.s[1].x=x
        self.s[2].z=z-.5
        self.s[2].x=x
        self.s[2].y=y
        self.s[3].z=z+.5
        self.s[3].x=x
        self.s[3].y=y
        self.s[4].x=x-.5
        self.s[4].y=y
        self.s[4].z=z
        self.s[5].x=x+.5
        self.s[5].y=y
        self.s[5].z=z
        

        
class cen():
    val=[0,0,0]
    s=[]
    d=0
    def __init__(self,x,y,z,pb):
        self.s=[box(),box(),box(),box(),box(),box()]
        self.s[0].height=.04
        self.s[1].height=.04
        self.s[2].width=.04
        self.s[3].width=.04
        self.s[4].length=.04
        self.s[5].length=.04
        self.s[0].y+=.5
        self.s[1].y-=.5
        self.s[2].z-=.5
        self.s[3].z+=.5
        self.s[4].x-=.5
        self.s[5].x+=.5
        self.pos(x,y,z)
        self.d=pb
        
    def axis(self,p):
        for a in self.s:
            a.axis+=a.pos * -0.3
        
        
    def pos(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
        self.s[0].y=.5+y
        self.s[0].x=x
        self.s[0].z=z
        self.s[1].y=y-.5
        self.s[1].z=z
        self.s[1].x=x
        self.s[2].z=z-.5
        self.s[2].x=x
        self.s[2].y=y
        self.s[3].z=z+.5
        self.s[3].x=x
        self.s[3].y=y
        self.s[4].x=x-.5
        self.s[4].y=y
        self.s[4].z=z
        self.s[5].x=x+.5
        self.s[5].y=y
        self.s[5].z=z

    active=0
    def act(self,a):
        self.s[self.active].color=color.gray(0.7)
        self.active=a
        self.s[self.active].color=self.color

    color=color.gray(.7)
    def col(self,color):
        self.color=color
        self.s[self.active].color=self.color

class cor():
    val=[0,0,0]
    s=[]
    d=0
    def __init__(self,x,y,z,pb):
        self.s=[box(),box(),box(),box(),box(),box()]
        self.s[0].height=.04
        self.s[1].height=.04
        self.s[2].width=.04
        self.s[3].width=.04
        self.s[4].length=.04
        self.s[5].length=.04
        self.s[0].y+=.5
        self.s[1].y-=.5
        self.s[2].z-=.5
        self.s[3].z+=.5
        self.s[4].x-=.5
        self.s[5].x+=.5
        self.pos(x,y,z)
        self.d=pb
        
    def axis(self,p):
        for a in self.s:
            a.axis+=a.pos * -0.3
        
        
    def pos(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
        self.s[0].y=.5+y
        self.s[0].x=x
        self.s[0].z=z
        self.s[1].y=y-.5
        self.s[1].z=z
        self.s[1].x=x
        self.s[2].z=z-.5
        self.s[2].x=x
        self.s[2].y=y
        self.s[3].z=z+.5
        self.s[3].x=x
        self.s[3].y=y
        self.s[4].x=x-.5
        self.s[4].y=y
        self.s[4].z=z
        self.s[5].x=x+.5
        self.s[5].y=y
        self.s[5].z=z
    color=[color.green,color.blue,color.red]
    active=0
    def act(self,a):
        for n in range(6):
            self.s[n].color=color.gray(.7)
            pass
        self.active=a
        if(self.active==1):
            self.s[0].color=self.color[0]
            self.s[3].color=self.color[1]
            self.s[4].color=self.color[2]
        elif(self.active==2):
            self.s[0].color=self.color[0]
            self.s[4].color=self.color[1]
            self.s[2].color=self.color[2]
        elif(self.active==3):
            self.s[0].color=self.color[0]
            self.s[2].color=self.color[1]
            self.s[5].color=self.color[2]
        elif(self.active==4):
            self.s[0].color=self.color[0]
            self.s[5].color=self.color[1]
            self.s[3].color=self.color[2]
        elif(self.active==5):
            self.s[1].color=self.color[0]
            self.s[3].color=self.color[1]
            self.s[4].color=self.color[2]
        elif(self.active==6):
            self.s[1].color=self.color[0]
            self.s[4].color=self.color[1]
            self.s[2].color=self.color[2]
        elif(self.active==7):
            self.s[1].color=self.color[0]
            self.s[2].color=self.color[1]
            self.s[5].color=self.color[2]
        elif(self.active==8):
            self.s[1].color=self.color[0]
            self.s[5].color=self.color[1]
            self.s[3].color=self.color[2]
                    
            

class mid(dice):
    val=[0,0,0]
    s=[]
    d=0
    def __init__(self,x,y,z,pb):
        self.x=x
        self.y=y
        self.z=z
        self.d=pb
        self.s=[box(),box(),box(),box(),box(),box()]
        self.s[0].height=.04
        self.s[1].height=.04
        self.s[2].width=.04
        self.s[3].width=.04
        self.s[4].length=.04
        self.s[5].length=.04
        self.s[0].y+=.5
        self.s[1].y-=.5
        self.s[2].z-=.5
        self.s[3].z+=.5
        self.s[4].x-=.5
        self.s[5].x+=.5
        self.pos(x,y,z)
        
    def axis(self,p):
        for a in self.s:
            a.axis+=a.pos * -0.3
    def pos(self,x,y,z):
        self.s[0].y=.5+y
        self.s[0].x=x
        self.s[0].z=z
        self.s[1].y=y-.5
        self.s[1].z=z
        self.s[1].x=x
        self.s[2].z=z-.5
        self.s[2].x=x
        self.s[2].y=y
        self.s[3].z=z+.5
        self.s[3].x=x
        self.s[3].y=y
        self.s[4].x=x-.5
        self.s[4].y=y
        self.s[4].z=z
        self.s[5].x=x+.5
        self.s[5].y=y
        self.s[5].z=z        
    color=[color.gray(.7),color.gray(.7),color.gray(.7)]
    active=0
    def act(self,a):
        for n in range(6):
            self.s[n].color=color.gray(.7)
            pass
        self.active=a
        if(self.active==1):
            self.s[0].color=self.color[0]
            self.s[3].color=self.color[1]
        elif(self.active==2):
            self.s[0].color=self.color[0]
            self.s[4].color=self.color[1]
        elif(self.active==3):
            self.s[0].color=self.color[0]
            self.s[2].color=self.color[1]
        elif(self.active==4):
            self.s[0].color=self.color[0]
            self.s[5].color=self.color[1]
        elif(self.active==5):
            self.s[4].color=self.color[0]
            self.s[2].color=self.color[1]
        elif(self.active==6):
            self.s[2].color=self.color[0]
            self.s[5].color=self.color[1]
        elif(self.active==7):
            self.s[5].color=self.color[0]
            self.s[3].color=self.color[1]
        elif(self.active==8):
            self.s[3].color=self.color[0]
            self.s[4].color=self.color[1]
        elif(self.active==9):
            self.s[1].color=self.color[0]
            self.s[3].color=self.color[1]
        elif(self.active==10):
            self.s[1].color=self.color[0]
            self.s[4].color=self.color[1]
        elif(self.active==11):
            self.s[1].color=self.color[0]
            self.s[2].color=self.color[1]
        elif(self.active==12):
            self.s[1].color=self.color[0]
            self.s[5].color=self.color[1]



x=1.1

cube=[[[cor(-x,x,x,1),mid(0,x,x,2),cor(x,x,x,3)],
       [mid(-x,0,x,4),cen(0,0,x,5),mid(x,0,x,6)],
       [cor(-x,-x,x,7),mid(0,-x,x,8),cor(x,-x,x,9)]],

      [[mid(-x,x,0,10),cen(0,x,0,11),mid(x,x,0,12)],
       [cen(-x,0,0,13),cen(0,0,0,14),cen(x,0,0,15)],
       [mid(-x,-x,0,16),cen(0,-x,0,17),mid(x,-x,0,18)]],

      [[cor(-x,x,-x,19),mid(0,x,-x,20),cor(x,x,-x,21)],
       [mid(-x,0,-x,22),cen(0,0,-x,23),mid(x,0,-x,24)],
       [cor(-x,-x,-x,25),mid(0,-x,-x,26),cor(x,-x,-x,27)]]]


cell=[cube[0][0][0],cube[0][0][1],cube[0][0][2],
      cube[0][1][0],cube[0][1][1],cube[0][1][2],
      cube[0][2][0],cube[0][2][1],cube[0][2][2],
      cube[1][0][0],cube[1][0][1],cube[1][0][2],
      cube[1][1][0],cube[1][1][1],cube[1][1][2],
      cube[1][2][0],cube[1][2][1],cube[1][2][2],
      cube[2][0][0],cube[2][0][1],cube[2][0][2],
      cube[2][1][0],cube[2][1][1],cube[2][1][2],
      cube[2][2][0],cube[2][2][1],cube[2][2][2]]

cell[1-1].color=(color.blue,color.red,color.gray(2))
cell[1-1].act(1)
cell[1-1].o={B:u,R:f,W:l}

cell[2-1].color=[color.blue,color.red]
cell[2-1].act(1)
cell[2-1].o={B:u,R:f}

cell[3-1].color=(color.blue,color.green,color.red)
cell[3-1].act(4)
cell[3-1].o={B:u,R:f,G:r}

cell[4-1].color=[color.red,color.gray(2)]
cell[4-1].act(8)
cell[4-1].o={W:l,R:f}

cell[5-1].color=color.red
cell[5-1].act(3)
cell[5-1].o={R:f}

cell[6-1].color=[color.green,color.red]
cell[6-1].act(7)
cell[6-1].o={R:f,G:r}

cell[7-1].color=[color.yellow,color.red,color.gray(2)]
cell[7-1].act(5)
cell[7-1].o={W:l,R:f,Y:d}

cell[8-1].color=[color.yellow,color.red]
cell[8-1].act(9)
cell[8-1].o={R:f,Y:d}

cell[9-1].color=[color.yellow,color.green,color.red]
cell[9-1].act(8)
cell[9-1].o={Y:d,R:f,G:r}

cell[10-1].color=[color.blue,color.gray(2)]
cell[10-1].act(2)
cell[10-1].o={B:u,W:l}

cell[11-1].color=color.blue
cell[11-1].act(0)
cell[11-1].o={B:u}

cell[12-1].color=[color.blue,color.green]
cell[12-1].act(4)
cell[12-1].o={B:u,G:r}

cell[13-1].color=color.gray(2)
cell[13-1].act(4)
cell[13-1].o={W:l}

cell[15-1].color=color.green
cell[15-1].act(5)
cell[15-1].o={G:r}

cell[16-1].color=[color.yellow,color.gray(2)]
cell[16-1].act(10)
cell[16-1].o={W:l,Y:d}

cell[17-1].color=color.yellow
cell[17-1].act(1)
cell[17-1].o={Y:d}

cell[18-1].color=[color.yellow,color.green]
cell[18-1].act(12)
cell[18-1].o={Y:d,G:r}

cell[19-1].color=[color.blue,color.gray(2),color.orange]
cell[19-1].act(2)
cell[19-1].o={B:u,W:l,O:b}

cell[20-1].color=[color.blue,color.orange]
cell[20-1].act(3)
cell[20-1].o={B:u,O:b}

cell[21-1].color=[color.blue,color.orange,color.green]
cell[21-1].act(3)
cell[21-1].o={B:u,O:b,G:r}

cell[22-1].color=[color.gray(2),color.orange]
cell[22-1].act(5)
cell[22-1].o={W:l,O:b}

cell[23-1].color=color.orange
cell[23-1].act(2)
cell[23-1].o={O:b}

cell[24-1].color=[color.orange,color.green]
cell[24-1].act(6)
cell[24-1].o={G:r,O:b}

cell[25-1].color=[color.yellow,color.gray(2),color.orange]
cell[25-1].act(6)
cell[25-1].o={W:l,O:b,Y:d}

cell[26-1].color=[color.yellow,color.orange]
cell[26-1].act(11)
cell[26-1].o={O:b,Y:d}

cell[27-1].color=[color.yellow,color.orange,color.green]
cell[27-1].act(7)
cell[27-1].o={Y:d,O:b,G:r}

dyn=cell[:]

left=text(text="L")
front = text(text="F")
front.height=0.4
front.pos=(-0.13,-0.15,1.6)
back=text(text="B")
back.rotate(angle=pi,axis=(0,1,0),origin=back.pos)
back.height=0.4
back.pos=(0.13,-0.15,-1.6)
right=text(text="R")
upper=text(text="U")
down=text(text="D")
right.pos=left.pos=upper.pos=down.pos=front.pos
right.height=left.height=upper.height=down.height=front.height
left.rotate(angle=-pi/2,axis=(0,1,0),origin=(0,0,0))
right.rotate(angle=pi/2,axis=(0,1,0),origin=(0,0,0))
down.rotate(angle=pi/2,axis=(1,0,0),origin=(0,0,0))
upper.rotate(angle=-pi/2,axis=(1,0,0),origin=(0,0,0))

def MF():
    for a in range(50):
        rate(speed)
        for n in range(9):
            for m in range(6):
                if(not hide):
                    dyn[n].s[m].rotate(angle=-pi/100,axis=(0,0,1),origin=(0,0,1))
    
    dyn[:9]=(dyn[6],dyn[3],dyn[0],dyn[7],dyn[4],dyn[1],dyn[8],dyn[5],dyn[2])
    for n in range(9):
        for ZX in dyn[n].o.keys():
            if dyn[n].o[ZX]=="u":
                dyn[n].o[ZX]="r"
            elif dyn[n].o[ZX]=="r":
                dyn[n].o[ZX]="d"
            elif dyn[n].o[ZX]=="d":
                dyn[n].o[ZX]="l"
            elif dyn[n].o[ZX]=="l":
                dyn[n].o[ZX]="u"

def Mf():
    for a in range(50):
        rate(speed)
        for n in range(9):
            for m in range(6):
                if(not hide):
                    dyn[n].s[m].rotate(angle=pi/100,axis=(0,0,1),origin=(0,0,1))
    dyn[:9]=(dyn[2],dyn[5],dyn[8],dyn[1],dyn[4],dyn[7],dyn[0],dyn[3],dyn[6])
    for n in range(9):
        for ZX in dyn[n].o.keys():
            if dyn[n].o[ZX]=="u":
                dyn[n].o[ZX]="l"
            elif dyn[n].o[ZX]=="l":
                dyn[n].o[ZX]="d"
            elif dyn[n].o[ZX]=="d":
                dyn[n].o[ZX]="r"
            elif dyn[n].o[ZX]=="r":
                dyn[n].o[ZX]="u"

def MB():
    for a in range(50):
        rate(speed)
        for n in range(18,27):
            for m in range(6):
                if(not hide):
                    dyn[n].s[m].rotate(angle=pi/100,axis=(0,0,1),origin=(0,0,1))
    dyn[18:27]=(dyn[20],dyn[23],dyn[26],dyn[19],dyn[22],dyn[25],dyn[18],dyn[21],dyn[24])
    for n in range(18,27):
        for ZX in dyn[n].o.keys():
            if dyn[n].o[ZX]=="u":
                dyn[n].o[ZX]="l"
            elif dyn[n].o[ZX]=="l":
                dyn[n].o[ZX]="d"
            elif dyn[n].o[ZX]=="d":
                dyn[n].o[ZX]="r"
            elif dyn[n].o[ZX]=="r":
                dyn[n].o[ZX]="u"
        

def Mb():
    for a in range(50):
        rate(speed)
        for n in range(18,27):
            for m in range(6):
                if(not hide):
                    dyn[n].s[m].rotate(angle=-pi/100,axis=(0,0,1),origin=(0,0,1))
    dyn[18:27]=(dyn[24],dyn[21],dyn[18],dyn[25],dyn[22],dyn[19],dyn[26],dyn[23],dyn[20])
    for n in range(18,27):
        for ZX in dyn[n].o.keys():
            if dyn[n].o[ZX]=="u":
                dyn[n].o[ZX]="r"
            elif dyn[n].o[ZX]=="r":
                dyn[n].o[ZX]="d"
            elif dyn[n].o[ZX]=="d":
                dyn[n].o[ZX]="l"
            elif dyn[n].o[ZX]=="l":
                dyn[n].o[ZX]="u"

ul=[0,1,2,9,10,11,18,19,20]


def MU():
    for a in range(50):
        rate(speed)
        for n in ul:
            for m in range(6):
                if(not hide):
                    dyn[n].s[m].rotate(angle=-pi/100,axis=(0,1,0),origin=(0,1,0))
    (dyn[0],dyn[1],dyn[2],dyn[9],dyn[10],dyn[11],dyn[18],dyn[19],dyn[20])=(dyn[2],dyn[11],dyn[20],dyn[1],dyn[10],dyn[19],dyn[0],dyn[9],dyn[18])
    for n in ul:
        for ZX in dyn[n].o.keys():
            if dyn[n].o[ZX]=="f":
                dyn[n].o[ZX]="l"
            elif dyn[n].o[ZX]=="l":
                dyn[n].o[ZX]="b"
            elif dyn[n].o[ZX]=="b":
                dyn[n].o[ZX]="r"
            elif dyn[n].o[ZX]=="r":
                dyn[n].o[ZX]="f"        

def Mu():
    for a in range(50):
        rate(speed)
        for n in ul:
            for m in range(6):
                if(not hide):
                    dyn[n].s[m].rotate(angle=pi/100,axis=(0,1,0),origin=(0,1,0))
    (dyn[0],dyn[1],dyn[2],dyn[9],dyn[10],dyn[11],dyn[18],dyn[19],dyn[20])=(dyn[18],dyn[9],dyn[0],dyn[19],dyn[10],dyn[1],dyn[20],dyn[11],dyn[2])
    for n in ul:
        for ZX in dyn[n].o.keys():
            if dyn[n].o[ZX]=="f":
                dyn[n].o[ZX]="r"
            elif dyn[n].o[ZX]=="r":
                dyn[n].o[ZX]="b"
            elif dyn[n].o[ZX]=="b":
                dyn[n].o[ZX]="l"
            elif dyn[n].o[ZX]=="l":
                dyn[n].o[ZX]="f"

                
ll=[18,9,0,21,12,3,24,15,6]

def ML():
    for a in range(50):
        rate(speed)
        for n in ll:
            for m in range(6):
                if(not hide):
                    dyn[n].s[m].rotate(angle=pi/100,axis=(1,0,0),origin=(1,0,0))
    (dyn[18],dyn[9],dyn[0],dyn[21],dyn[12],dyn[3],dyn[24],dyn[15],dyn[6])=(dyn[24],dyn[21],dyn[18],dyn[15],dyn[12],dyn[9],dyn[6],dyn[3],dyn[0])
    for n in ll:
        for ZX in dyn[n].o.keys():
            if dyn[n].o[ZX]=="u":
                dyn[n].o[ZX]="f"
            elif dyn[n].o[ZX]=="f":
                dyn[n].o[ZX]="d"
            elif dyn[n].o[ZX]=="d":
                dyn[n].o[ZX]="b"
            elif dyn[n].o[ZX]=="b":
                dyn[n].o[ZX]="u"
    

def Ml():
    for a in range(50):
        rate(speed)
        for n in ll:
            for m in range(6):
                if(not hide):
                    dyn[n].s[m].rotate(angle=-pi/100,axis=(1,0,0),origin=(1,0,0))
    (dyn[18],dyn[9],dyn[0],dyn[21],dyn[12],dyn[3],dyn[24],dyn[15],dyn[6])=(dyn[0],dyn[3],dyn[6],dyn[9],dyn[12],dyn[15],dyn[18],dyn[21],dyn[24])
    for n in ll:
        for ZX in dyn[n].o.keys():
            if dyn[n].o[ZX]=="u":
                dyn[n].o[ZX]="b"
            elif dyn[n].o[ZX]=="b":
                dyn[n].o[ZX]="d"
            elif dyn[n].o[ZX]=="d":
                dyn[n].o[ZX]="f"
            elif dyn[n].o[ZX]=="f":
                dyn[n].o[ZX]="u"

rl=[2,11,20,5,14,23,8,17,26]
def MR():
    for a in range(50):
        rate(speed)
        for n in rl:
            for m in range(6):
                if(not hide):
                    dyn[n].s[m].rotate(angle=-pi/100,axis=(1,0,0),origin=(1,0,0))
    (dyn[2],dyn[11],dyn[20],dyn[5],dyn[14],dyn[23],dyn[8],dyn[17],dyn[26])=(dyn[8],dyn[5],dyn[2],dyn[17],dyn[14],dyn[11],dyn[26],dyn[23],dyn[20])
    for n in rl:
        for ZX in dyn[n].o.keys():
            if dyn[n].o[ZX]=="u":
                dyn[n].o[ZX]="b"
            elif dyn[n].o[ZX]=="b":
                dyn[n].o[ZX]="d"
            elif dyn[n].o[ZX]=="d":
                dyn[n].o[ZX]="f"
            elif dyn[n].o[ZX]=="f":
                dyn[n].o[ZX]="u"


def Mr():
    for a in range(50):
        rate(speed)
        for n in rl:
            for m in range(6):
                if(not hide):
                    dyn[n].s[m].rotate(angle=pi/100,axis=(1,0,0),origin=(1,0,0))
    (dyn[2],dyn[11],dyn[20],dyn[5],dyn[14],dyn[23],dyn[8],dyn[17],dyn[26])=(dyn[20],dyn[23],dyn[26],dyn[11],dyn[14],dyn[17],dyn[2],dyn[5],dyn[8])
    for n in rl:
        for ZX in dyn[n].o.keys():
            if dyn[n].o[ZX]=="u":
                dyn[n].o[ZX]="f"
            elif dyn[n].o[ZX]=="f":
                dyn[n].o[ZX]="d"
            elif dyn[n].o[ZX]=="d":
                dyn[n].o[ZX]="b"
            elif dyn[n].o[ZX]=="b":
                dyn[n].o[ZX]="u"
        
dl=[6,7,8,15,16,17,24,25,26]

def MD():
    for a in range(50):
        rate(speed)
        for n in dl:
            for m in range(6):
                if(not hide):
                    dyn[n].s[m].rotate(angle=pi/100,axis=(0,1,0),origin=(0,1,0))
    (dyn[6],dyn[7],dyn[8],dyn[15],dyn[16],dyn[17],dyn[24],dyn[25],dyn[26])=(dyn[24],dyn[15],dyn[6],dyn[25],dyn[16],dyn[7],dyn[26],dyn[17],dyn[8])
    for n in dl:
        for ZX in dyn[n].o.keys():
            if dyn[n].o[ZX]=="f":
                dyn[n].o[ZX]="r"
            elif dyn[n].o[ZX]=="r":
                dyn[n].o[ZX]="b"
            elif dyn[n].o[ZX]=="b":
                dyn[n].o[ZX]="l"
            elif dyn[n].o[ZX]=="l":
                dyn[n].o[ZX]="f"

def Md():
    for a in range(50):
        rate(speed)
        for n in dl:
            for m in range(6):
                if(not hide):
                    dyn[n].s[m].rotate(angle=-pi/100,axis=(0,1,0),origin=(0,1,0))
    (dyn[6],dyn[7],dyn[8],dyn[15],dyn[16],dyn[17],dyn[24],dyn[25],dyn[26])=(dyn[8],dyn[17],dyn[26],dyn[7],dyn[16],dyn[25],dyn[6],dyn[15],dyn[24])
    for n in dl:
        for ZX in dyn[n].o.keys():
            if dyn[n].o[ZX]=="f":
                dyn[n].o[ZX]="l"
            elif dyn[n].o[ZX]=="l":
                dyn[n].o[ZX]="b"
            elif dyn[n].o[ZX]=="b":
                dyn[n].o[ZX]="r"
            elif dyn[n].o[ZX]=="r":
                dyn[n].o[ZX]="f"        

moves=["MU()","Mu()","MD()","Md()","MR()","Mr()","ML()","Ml()","MF()","Mf()","MB()","Mb()"]
def jumble():
    speed=500
    for zsd in range(20):
        random.random()
        exec(moves[int(random.random()*100%12)])
    speed=200


def flmiddle():
    if(debug):
        print "c1--",dyn.index(cell[1])
    lok=dyn.index(cell[1])
    if(lok==1):
        if(dyn[lok].o[B]==u):
            pass
        else:
            Mf()
            MU()
            Ml()
            Mu()
    elif(lok==3):
        if(dyn[lok].o[B]==l):
            MF()
        else:
            MU()
            Ml()
            Mu()
    elif(lok==5):
        if(dyn[lok].o[B]==r):
            Mf()
        else:
            Mu()
            MR()
            MU()

    elif(lok==7):
        if(dyn[lok].o[B]==d):
            MF();MF()
        else:
            MD()
            MR()
            Mf()
            Mr()

    elif(lok==9):
        if(dyn[lok].o[B]==u):
            Mu()
        else:
            ML()
            MF()

    elif(lok==11):
        if(dyn[lok].o[B]==u):
            MU()
        else:
            Mr()
            Mf()

    elif(lok==15):
        if(dyn[lok].o[B]==d):
            MD()
            MF();MF()
        else:
            Ml()
            MF()
            ML()
            
    elif(lok==17):
        if(dyn[lok].o[B]==d):
            Md()
            MF();MF()
        else:
            MR()
            Mf()
            Mr()

    elif(lok==19):#error corrected
        if(dyn[lok].o[B]==u):
            MU();MU()
        else:
            MB()
            ML()
            Mu()

    elif(lok==21):
        if(dyn[lok].o[B]==l):
            MU();MU()
            Mb()
            Mu();Mu()
        else:
            MU()
            ML()
            Mu()

    elif(lok==23):
        if(dyn[lok].o[B]==b):
            Mr()
            MU()
        else:
            Mr();Mr()
            Mf()

    elif(lok==25):
        if(dyn[lok].o[B]==b):
            Md()
            MR()
            Mf()
            Mr()

        else:
            MD();MD()
            MF();MF()
    if(debug):
        if(dyn[1]!=cell[1]):
            print "check--one"

    if(debug):
        print "c1--",dyn.index(cell[9])   
    lok=dyn.index(cell[9])    
##    if(lok==1):
##        if(dyn[lok].o[B]==u):
##            pass
##        else:
##            Mf()
##            MU()
##            Ml()
##            Mu()
    if(lok==3):
        if(dyn[lok].o[B]==f):
            Ml()
        else:
            Mu()
            MF()
            MU()
    elif(lok==5):
        if(dyn[lok].o[B]==f):
            MU();MU()
            MR()
            Mu();Mu();
        else:
            Mu()
            Mf()
            MU()

    elif(lok==7):
        if(dyn[lok].o[B]==d):
            Mu()
            MF();MF()
            MU()
        else:
            Mu()
            MF()
            MU()
            Ml()

    elif(lok==9):
        if(dyn[lok].o[B]==u):
            pass
        else:
            ML()
            Mu()
            MF()
            MU()

    elif(lok==11):
        if(dyn[lok].o[B]==u):
            MF()
            MU();MU()
            Mf()
        else:
            MR()
            MB()
            MF()
            Mu()
            Mf()

    elif(lok==15):
        if(dyn[lok].o[B]==d):
            Ml();Ml()
        else:
            Ml()
            Mu()
            MF()
            MU()
            
    elif(lok==17):
        if(dyn[lok].o[B]==d):
            Md();Md()
            Ml();Ml()
        else:
            MD();MD()
            Ml()
            Mu()
            MF()
            MU()

    elif(lok==19):
        if(dyn[lok].o[B]==u):
            MF();Mu()
            Mf()
            
        else:
            MB()
            ML()

    elif(lok==21):
        if(dyn[lok].o[B]==l):
            MU()
            Mb()
            Mu()
        else:
            ML()

    elif(lok==23):
        if(dyn[lok].o[B]==b):
            MB();MB()
            ML()
        else:
            MU();MB()
            Mu()

    elif(lok==25):
        if(dyn[lok].o[B]==b):
            MD()
            Ml()
            Mu()
            MF()
            MU()
        else:
            MD()
            ML();ML()
    if(debug):
        if(dyn[9]!=cell[9]):
            print "check--one"



    if(debug):
        print "c1--",dyn.index(cell[19])
    
    lok=dyn.index(cell[19])    
##    if(lok==1):
##        if(dyn[lok].o[B]==u):
##            pass
##        else:
##            Mf()
##            MU()
##            Ml()
##            Mu()
    if(lok==3):
        if(dyn[lok].o[B]==f):
            Mu()
            Ml()
            MU()
        else:
            MU();MU()
            MF()
            MU();MU()
    elif(lok==5):
        if(dyn[lok].o[B]==f):
            MU()
            MR()
            Mu()
        else:
            Mu();Mu()
            Mf()
            MU();MU()

    elif(lok==7):
        if(dyn[lok].o[B]==d):
            Mu();Mu()
            MF();MF()
            MU();MU()
        else:
            Mu();Mu()
            MF()
            MU()
            Ml()
            MU()
            
##    elif(lok==9):
##        if(dyn[lok].o[B]==u):
##            pass
##        else:
##            ML()
##            Mu()
##            MF()
##            MU()
##
    elif(lok==11):
        if(dyn[lok].o[B]==u):
            MF()
            ML();Mu()
            Ml()
            Mf()
        else:
            MR()
            MB()

    elif(lok==15):
        if(dyn[lok].o[B]==d):
            Mu()
            Ml();Ml()
            MU()
        else:
            Mu()
            ML()
            MU()
            Mb()            
    elif(lok==17):#error corrected
        if(dyn[lok].o[B]==d):
            MD()
            MB()
            MB()
        else:
            Mr()
            MB()
            
    elif(lok==19):
        if(dyn[lok].o[B]==u):
            pass            
        else:
            MB()
            Mu()
            ML()
            MU()

    elif(lok==21):
        if(dyn[lok].o[B]==l):
            Mb()
        else:
            Mu()
            ML()
            MU()
    elif(lok==23):
        if(dyn[lok].o[B]==b):
            MU();Mr()
            Mu()
        else:
            MB()

    elif(lok==25):
        if(dyn[lok].o[B]==b):
            MB()
            MU()
            Mr()
            Mu()
        else:
            MB();MB()
    if(debug):
        if(dyn[19]!=cell[19]):
            print "check--one"




    if(debug):
        print "c1--",dyn.index(cell[11])
    
    lok=dyn.index(cell[11])    
##    if(lok==1):
##        if(dyn[lok].o[B]==u):
##            pass
##        else:
##            Mf()
##            MU()
##            Ml()
##            Mu()
    if(lok==3):
        if(dyn[lok].o[B]==f):
            Mu();Mu()
            Ml()
            MU();MU()
        else:
            MU()
            MF()
            Mu()
    elif(lok==5):
        if(dyn[lok].o[B]==f):
            MR()
        else:
            MU()
            Mf()
            Mu()

    elif(lok==7):
        if(dyn[lok].o[B]==d):
            MD()
            MR();MR()
        else:
            MD()
            MR()
            MU()
            Mf()
            Mu()
            
##    elif(lok==9):
##        if(dyn[lok].o[B]==u):
##            pass
##        else:
##            ML()
##            Mu()
##            MF()
##            MU()
##
    elif(lok==11):
        if(dyn[lok].o[B]==u):
            pass
        else:
            Mr()
            MU()
            Mf()
            Mu()

    elif(lok==15):
        if(dyn[lok].o[B]==d):
            Md();Md()
            Mr();Mr()
        else:
            Md();Md()
            Mr()
            Mu()
            MB()
            MU()
            
    elif(lok==17):
        if(dyn[lok].o[B]==d):
            MR();MR()
        else:
            MR()
            MU()
            Mf()
            Mu()
            
##    elif(lok==19):
##        if(dyn[lok].o[B]==u):
##            pass            
##        else:
##            MB()
##            Mu()
##            ML()
##            MU()

    elif(lok==21):
        if(dyn[lok].o[B]==l):
            Mu()
            Mb()
            MU()
        else:
            Mu();Mu()
            ML()
            MU();MU()
    elif(lok==23):#error corrected
        if(dyn[lok].o[B]==b):
            Mr()
        else:
            Mu()
            MB()
            MU()

    elif(lok==25):
        if(dyn[lok].o[B]==b):
            Mu()
            Mb()
            Mu()
            ML()
            MU();MU()
        else:
            Mu()
            MB();MB()
            MU()

    if(debug):
        if(dyn[11]!=cell[11]):
            print "check--one"



#  corner pieces

def flcorner():
    if(debug):
        print "c1--",dyn.index(cell[0])
    lok=dyn.index(cell[0])
    if(lok==0):
        if(dyn[lok].o[B]==u):
            pass
        elif(dyn[lok].o[B]==f):
            Mf()
            Md()
            MF()
            MD()
            Ml()
            MF()
            ML()
            Mf()
        else:
            ML()
            MD()
            Ml()
            Md()
            MF()
            Ml()
            Mf()
            ML()
    elif(lok==2):
        if(dyn[lok].o[B]==u):
            Mr()
            Md()
            MR()
            MF()
            Ml()
            Mf()
            ML()
        elif(dyn[lok].o[B]==f):
            MF()
            MD()
            Mf()
            MD()
            MD()
            MF()
            Ml()
            Mf()
            ML()
        else:
            Mr()
            Md()
            MR()
            Ml()
            MF()
            ML()
            Mf()
    elif(lok==6):
        lok=75
    elif(lok==8):
        Md()
        lok=75
    elif(lok==18):
        Ml()
        Md()
        ML()
        MD()
        MD()
        lok=75
        
    elif(lok==20):
        MR()
        MD()
        Mr()
        MD()
        lok=75
    elif(lok==24):
        MD()
        lok=75
    elif(lok==26):
        Md()
        Md()
        lok=75
    if(lok==75):
        if(dyn[6].o[B]==l):
            MF()
            Ml()
            Mf()
            ML()
        elif(dyn[6].o[B]==f):
            Ml()
            MF()
            ML()
            Mf()
        else:
            Mf()
            Md()
            Md()
            MF()
            MD()
            Ml()
            MF()
            ML()
            Mf()
            
    if(debug):
        if(dyn[0]!=cell[0]):
            print "check--one first layer 0 th corner"
    
##corner 2nd
        if(debug):
            print "c1--",dyn.index(cell[2])
    lok=dyn.index(cell[2])
##    if(lok==0):
##        if(dyn[lok].o[B]==u):
##            pass
##        elif(dyn[lok].o[B]==f):
##            Mf()
##            Md()
##            MF()
##            MD()
##            Ml()
##            MF()
##            ML()
##            Mf()
##        else:
##            ML()
##            MD()
##            Ml()
##            Md()
##            MF()
##            Ml()
##            Mf()
##            ML()
    if(lok==2):
        if(dyn[lok].o[B]==u):
            pass
        elif(dyn[lok].o[B]==f):
            MF()
            MD()
            Mf()
            Md()
            MR()
            Mf()
            Mr()
            MF()
        else:
            Mr()
            Md()
            MR()
            MD()
            Mf()
            MR()
            MF()
            Mr()
    elif(lok==6):
        MD()
        lok=75
    elif(lok==8):
        lok=75
    elif(lok==18):
        MB()
        Md()
        Md()
        Mb()
        lok=75
        
    elif(lok==20):
        MR()
        MD()
        Mr()
        Md()
        Md()
        
        lok=75
    elif(lok==24):
        Md()
        Md()
        lok=75
    elif(lok==26):
        Md()
        lok=75
    if(lok==75):
        if(dyn[8].o[B]==r):
            Mf()
            MR()
            MF()
            Mr()
        elif(dyn[8].o[B]==f):
            MR()
            Mf()
            Mr()
            MF()
        else:
            MF()
            MD()
            MD()
            Mf()
            Md()
            MR()
            Mf()
            Mr()
            MF()
            
    if(debug):
        if(dyn[2]!=cell[2]):
            print "check--one first layer 2 nd corner"
    


## third corner piece----
    if(debug):
        print "c1--",dyn.index(cell[18])
    lok=dyn.index(cell[18])
##    if(lok==0):
##        if(dyn[lok].o[B]==u):
##            pass
##        elif(dyn[lok].o[B]==f):
##            Mf()
##            Md()
##            MF()
##            MD()
##            Ml()
##            MF()
##            ML()
##            Mf()
##        else:
##            ML()
##            MD()
##            Ml()
##            Md()
##            MF()
##            Ml()
##            Mf()
##            ML()
##    elif(lok==2):
##        if(dyn[lok].o[B]==u):
##            Mr()
##            Md()
##            MR()
##            MF()
##            Ml()
##            Mf()
##            ML()
##        elif(dyn[lok].o[B]==f):
##            MF()
##            MD()
##            Mf()
##            MD()
##            MD()
##            MF()
##            Ml()
##            Mf()
##            ML()
##        else:
##            Mr()
##            Md()
##            MR()
##            Ml()
##            MF()
##            ML()
##            Mf()
    if(lok==6):
        Md()
        lok=75
    elif(lok==8):
        Md()
        Md()
        lok=75
    elif(lok==18):
        if(dyn[lok].o[B]==u):
            pass
        elif(dyn[lok].o[B]==b):
            MB()
            MD()
            Mb()
            Md()
            ML()
            Mb()
            Ml()
            MB()
        else:
            Ml()
            Md()
            ML()
            MD()
            Mb()
            ML()
            MB()
            Ml()
        
    elif(lok==20):
        MR()
        MD()
        Mr()
        lok=75
    elif(lok==24):
        lok=75
    elif(lok==26):
        MD()
        lok=75
    if(lok==75):
        if(dyn[24].o[B]==l):
            Mb()
            ML()
            MB()
            Ml()
        elif(dyn[24].o[B]==b):
            ML()
            Mb()
            Ml()
            MB()
        else:
            MB()
            Md()
            Md()
            Mb()
            Md()
            ML()
            Mb()
            Ml()
            MB()
            
    if(debug):
        if(dyn[18]!=cell[18]):
            print "check--one first layer 3 rd corner"
    

##corner 4th
        if(debug):
            print "c1--",dyn.index(cell[20])
    lok=dyn.index(cell[20])
##    if(lok==0):
##        if(dyn[lok].o[B]==u):
##            pass
##        elif(dyn[lok].o[B]==f):
##            Mf()
##            Md()
##            MF()
##            MD()
##            Ml()
##            MF()
##            ML()
##            Mf()
##        else:
##            ML()
##            MD()
##            Ml()
##            Md()
##            MF()
##            Ml()
##            Mf()
##            ML()
##    if(lok==2):
##        if(dyn[lok].o[B]==u):
##            pass
##        elif(dyn[lok].o[B]==f):
##            MF()
##            MD()
##            Mf()
##            Md()
##            MR()
##            Mf()
##            Mr()
##            MF()
##        else:
##            Mr()
##            Md()
##            MR()
##            MD()
##            Mf()
##            MR()
##            MF()
##            Mr()
    if(lok==6):
        MD()
        MD()
        lok=75
    elif(lok==8):
        MD()
        lok=75
##    elif(lok==18):
##        MB()
##        Md()
##        Md()
##        Mb()
##        lok=75
##        
    elif(lok==20):
        if(dyn[lok].o[B]==u):
            pass
        else:
            Mb()
            Md()
            MB()
            MD()
            lok=75
    elif(lok==24):
        Md()
        lok=75
    elif(lok==26):
        lok=75
    if(lok==75):
        if(dyn[26].o[B]==r):
            MB()
            Mr()
            Mb()
            MR()
        elif(dyn[26].o[B]==b):
            Mr()
            MB()
            MR()
            Mb()
        else:
            Mb()
            MD()
            MD()
            MB()
            MD()
            Mr()
            MB()
            MR()
            Mb()
            
    if(debug):
        if(dyn[20]!=cell[20]):
            print "check--one first layer 4th th corner"
    


def uprlyr():
    flmiddle()
    flcorner()

##upper layer finished...........................................

def algo11(faceblock):
    f_l=["MU()","Mu()","MD()","Md()","ML()","Ml()","MR()","Mr()","MF()","Mf()","MB()","Mb()"]

    if(faceblock=="f"):
        dr=f_l[2]
        ld=f_l[4]
        dl=f_l[3]
        lu=f_l[5]
        rfa=f_l[-3]
        rfc=f_l[-4]
    elif(faceblock=="r"):
        dr=f_l[2]
        ld=f_l[-4]
        dl=f_l[3]
        lu=f_l[-3]
        rfa=f_l[7]
        rfc=f_l[6]
    elif(faceblock=="b"):
        dr=f_l[2]
        ld=f_l[6]
        dl=f_l[3]
        lu=f_l[7]
        rfa=f_l[-1]
        rfc=f_l[-2]
    elif(faceblock=="l"):
        dr=f_l[2]
        ld=f_l[-2]
        dl=f_l[3]
        lu=f_l[-1]
        rfa=f_l[5]
        rfc=f_l[4]
    exec(dr);
    exec(ld);
    exec(dl);
    exec(lu);
    exec(dl);
    exec(rfa);
    exec(dr);
    exec(rfc);

    
def algo12(faceblock):
    f_l=["MU()","Mu()","MD()","Md()","ML()","Ml()","MR()","Mr()","MF()","Mf()","MB()","Mb()"]

    if(faceblock=="f"):
        dr=f_l[3]
        ld=f_l[7]
        dl=f_l[2]
        lu=f_l[6]
        rfa=f_l[-4]
        rfc=f_l[-3]
    elif(faceblock=="r"):
        dr=f_l[3]
        ld=f_l[-1]
        dl=f_l[2]
        lu=f_l[-2]
        rfa=f_l[6]
        rfc=f_l[7]
    elif(faceblock=="b"):
        dr=f_l[3]
        ld=f_l[5]
        dl=f_l[2]
        lu=f_l[4]
        rfa=f_l[-2]
        rfc=f_l[-1]
    elif(faceblock=="l"):
        dr=f_l[3]
        ld=f_l[-3]
        dl=f_l[2]
        lu=f_l[-4]
        rfa=f_l[4]
        rfc=f_l[5]

    exec(dr);
    exec(ld);
    exec(dl);
    exec(lu);
    exec(dl);
    exec(rfa);
    exec(dr);
    exec(rfc);


def mdlayer():
## first corner(middle piece)
    if(debug):
        print "m1--",dyn.index(cell[3])
    lok=dyn.index(cell[3])
    if(lok==3):
        if(dyn[lok].o[R]==f):
            pass
        else:
            algo11("f")
            MD()
            MD()
            algo11("f")
    if(lok==5):
        if(dyn[lok].o[R]==f):
            algo12("f")
            MD()
            algo12("l")
        else:
            algo12("f")
            MD()
            MD()
            algo11("f")
    if(lok==7):
        if(dyn[lok].o[R]==f):
            algo11("f")
        else:
            Md()
            algo12("l")
    elif(lok==15):
        if(dyn[lok].o[R]==l):
            MD()
            algo11("f")
        else:
            algo12("l")
    elif(lok==17):
        if(dyn[lok].o[R]==r):
            Md()
            algo11("f")
        else:
            Md()
            Md()
            algo12("l")
    elif(lok==21):
        if(dyn[lok].o[R]==b):
            algo12("b")
            Md()
            algo12("l")
        else:
            algo12("b")
            algo11("f")
    elif(lok==23):
        if(dyn[lok].o[R]==b):
            algo11("b")
            Md()
            algo12("l")
        else:
            algo11("b")
            algo11("f")
    elif(lok==25):
        if(dyn[lok].o[R]==b):
            Md()
            Md()
            algo11("f")
        else:
            MD()
            algo12("l")
            
    if(debug):
        if(dyn[3]!=cell[3]):
            print "check--one middle layer 1st corner"

## second corner(middle piece)
    if(debug):
        print "m1--",dyn.index(cell[5])
    lok=dyn.index(cell[5])
##    if(lok==3):
##        if(dyn[lok].o[R]==f):
##            pass
##        else:
##            algo11("f")
##            MD()
##            MD()
##            algo11("f")
    if(lok==5):
        if(dyn[lok].o[R]==f):
            pass
        else:
            algo12("f")
            MD()
            MD()
            algo12("f")
    if(lok==7):
        if(dyn[lok].o[R]==f):
            algo12("f")
        else:
            MD()
            algo11("r")
    elif(lok==15):
        if(dyn[lok].o[R]==l):
            MD()
            algo12("f")
        else:
            Md()
            Md()
            algo11("r")
    elif(lok==17):
        if(dyn[lok].o[R]==r):
            Md()
            algo12("f")
        else:
            algo11("r")
    elif(lok==21):
        if(dyn[lok].o[R]==b):
            algo12("b")
            MD()
            algo11("r")
        else:
            algo12("b")
            algo12("f")
    elif(lok==23):
        if(dyn[lok].o[R]==b):
            algo11("b")
            MD()
            algo11("r")
        else:
            algo11("b")
            algo12("f")
    elif(lok==25):
        if(dyn[lok].o[R]==b):
            Md()
            Md()
            algo12("f")
        else:
            Md()
            algo11("r")
            
    if(debug):
        if(dyn[5]!=cell[5]):
            print "check--one middle layer  2nd corner"
## third corner(middle piece)
    if(debug):
        print "m1--",dyn.index(cell[21])
    lok=dyn.index(cell[21])
##    if(lok==3):
##        if(dyn[lok].o[R]==f):
##            pass
##        else:
##            algo11("f")
##            MD()
##            MD()
##            algo11("f")
##    if(lok==5):
##        if(dyn[lok].o[R]==f):
##            pass
##        else:
##            algo12("f")
##            MD()
##            MD()
##            algo12("f")
    if(lok==7):
        if(dyn[lok].o[O]==f):
            MD()
            MD()
            algo12("b")
        else:
            Md()
            algo11("l")
    elif(lok==15):
        if(dyn[lok].o[O]==l):
            Md()
            algo12("b")
        else:
            algo11("l")
    elif(lok==17):
        if(dyn[lok].o[O]==r):
            MD()
            algo12("b")
        else:
            Md()
            Md()
            algo11("l")
    elif(lok==21):
        if(dyn[lok].o[O]==b):
            pass
        else:
            algo12("b")
            Md()
            Md()
            algo12("b")
    elif(lok==23):
        if(dyn[lok].o[O]==b):
            algo11("b")
            Md()
            algo11("l")
        else:
            algo11("b")
            MD()
            MD()
            algo12("b")
    elif(lok==25):
        if(dyn[lok].o[O]==b):
            algo12("b")
        else:
            MD()
            algo11("l")
            
    if(debug):
        if(dyn[21]!=cell[21]):
            print "check--one middle layer  3rd corner"

## third corner(middle piece)
    if(debug):
        print "m1--",dyn.index(cell[23])
    lok=dyn.index(cell[23])
##    if(lok==3):
##        if(dyn[lok].o[R]==f):
##            pass
##        else:
##            algo11("f")
##            MD()
##            MD()
##            algo11("f")
##    if(lok==5):
##        if(dyn[lok].o[R]==f):
##            pass
##        else:
##            algo12("f")
##            MD()
##            MD()
##            algo12("f")
    if(lok==7):
        if(dyn[lok].o[O]==f):
            MD()
            MD()
            algo11("b")
        else:
            MD()
            algo12("r")
    elif(lok==15):
        if(dyn[lok].o[O]==l):
            Md()
            algo11("b")
        else:
            MD()
            MD()
            algo12("r")
    elif(lok==17):
        if(dyn[lok].o[O]==r):
            MD()
            algo11("b")
        else:
            algo12("r")
##    elif(lok==21):
##        if(dyn[lok].o[O]==b):
##            pass
##        else:
##            algo12("b")
##            Md()
##            Md()
##            algo12("b")
    elif(lok==23):
        if(dyn[lok].o[O]==b):
            pass
        else:
            algo11("b")
            MD()
            MD()
            algo11("b")
    elif(lok==25):
        if(dyn[lok].o[O]==b):
            algo11("b")
        else:
            Md()
            algo12("r")
            
    if(debug):
        if(dyn[23]!=cell[23]):
            print "check--one middle layer  4th corner"

def change(vx,vy):
    if(vx==8 and vy == 26):
        Mb()
        Md()
        MB()
        MR()
        MD()
        Mr()
        Mb()
        MD()
        MB()
        MD()
        MD()
    elif(vx==24 and vy == 26):
        Ml()
        Md()
        ML()
        MB()
        MD()
        Mb()
        Ml()
        MD()
        ML()
        MD()
        MD()
    
    
    
def llcpos():
    if(debug):
        print "m1--",dyn.index(cell[6])
    lok=dyn.index(cell[6])
    if(lok==6):
        pass
    elif(lok==8):
        Md()
    elif(lok==24):
        MD()
    elif(lok==26):
        MD()
        MD()

    if(dyn.index(cell[8])==8):
        if(dyn.index(cell[26])==24):
            if(dyn.index(cell[24])==26):
                change(24,26)
    elif(dyn.index(cell[8])==26):
        if(dyn.index(cell[26])==8):
            if(dyn.index(cell[24])==24):
                change(8,26)
        elif(dyn.index(cell[26])==24):
            if(dyn.index(cell[24])==8):
                change(8,26)
                change(24,26)
    elif(dyn.index(cell[8])==24):
        if(dyn.index(cell[26])==26):
            if(dyn.index(cell[24])==8):
                change(24,26)
                change(8,26)
                change(24,26)
        elif(dyn.index(cell[26])==8):
            if(dyn.index(cell[24])==26):
                change(24,26)
                change(8,26)
            
            
    if(debug):
        if(dyn[6]!=cell[6] or dyn[8]!=cell[8] or dyn[24]!=cell[24] or dyn[26]!=cell[26]):
            print "check--one last layer......."
   
def solve():
    uprlyr()
    mdlayer()
    llcpos()
    orient()
    llmpcs()
    llmpso()

def stay(stack):
    for st in stack:
        st="M"+st+"()"
        exec(st)
ornt=[]

def orient():
    ornt=(dyn[6].o[Y],dyn[8].o[Y],dyn[26].o[Y],dyn[24].o[Y])
    if(dyn[6].o[Y]==f and dyn[8].o[Y]==d and dyn[26].o[Y]==b and dyn[24].o[Y]==l):
        stay("LDlDLDDlDD")
    elif(dyn[6].o[Y]==f and dyn[8].o[Y]==r and dyn[26].o[Y]==d and dyn[24].o[Y]==l):
        stay("FDfDFDDfDD")
    elif(dyn[6].o[Y]==f and dyn[8].o[Y]==r and dyn[26].o[Y]==b and dyn[24].o[Y]==d):
        stay("RDrDRDDrDD")
    elif(dyn[6].o[Y]==d and dyn[8].o[Y]==r and dyn[26].o[Y]==b and dyn[24].o[Y]==l):
        stay("BDbDBDDbDD")

    elif(dyn[6].o[Y]==d and dyn[8].o[Y]==f and dyn[26].o[Y]==r and dyn[24].o[Y]==b):
        stay("rdRdrddRdd")
    elif(dyn[6].o[Y]==l and dyn[8].o[Y]==f and dyn[26].o[Y]==r and dyn[24].o[Y]==d):
        stay("fdFdfddFdd")
    elif(dyn[6].o[Y]==l and dyn[8].o[Y]==f and dyn[26].o[Y]==d and dyn[24].o[Y]==b):
        stay("ldLdlddLdd")
    elif(dyn[6].o[Y]==l and dyn[8].o[Y]==d and dyn[26].o[Y]==r and dyn[24].o[Y]==b):
        stay("bdBdbddBdd")

    elif(dyn[6].o[Y]==l and dyn[8].o[Y]==f and dyn[26].o[Y]==b and dyn[24].o[Y]==l):
        stay("rdRdrddRdd")
        stay("bdBdbddBdd")
    elif(dyn[6].o[Y]==l and dyn[8].o[Y]==r and dyn[26].o[Y]==b and dyn[24].o[Y]==b):
        stay("fdFdfddFdd")
        stay("rdRdrddRdd")
    elif(dyn[6].o[Y]==f and dyn[8].o[Y]==r and dyn[26].o[Y]==r and dyn[24].o[Y]==b):
        stay("fdFdfddFdd")
        stay("ldLdlddLdd")        
    elif(dyn[6].o[Y]==f and dyn[8].o[Y]==f and dyn[26].o[Y]==r and dyn[24].o[Y]==l):
        stay("ldLdlddLdd")
        stay("bdBdbddBdd")
        

    elif(dyn[6].o[Y]==d and dyn[8].o[Y]==d and dyn[26].o[Y]==r and dyn[24].o[Y]==l):
        stay("FDfDFDDfDD")
        stay("fdFdfddFdd")
    elif(dyn[6].o[Y]==d and dyn[8].o[Y]==f and dyn[26].o[Y]==b and dyn[24].o[Y]==d):
        stay("LDlDLDDlDD")
        stay("ldLdlddLdd")
    elif(dyn[6].o[Y]==l and dyn[8].o[Y]==r and dyn[26].o[Y]==d and dyn[24].o[Y]==d):
        stay("BDbDBDDbDD")
        stay("bdBdbddBdd")
    elif(dyn[6].o[Y]==f and dyn[8].o[Y]==d and dyn[26].o[Y]==d and dyn[24].o[Y]==b):
        stay("RDrDRDDrDD")
        stay("rdRdrddRdd")

    elif(dyn[6].o[Y]==d and dyn[8].o[Y]==d and dyn[26].o[Y]==b and dyn[24].o[Y]==b):
        stay("ldLdlddLdd")
        stay("RDrDRDDrDD")
    elif(dyn[6].o[Y]==d and dyn[8].o[Y]==r and dyn[26].o[Y]==r and dyn[24].o[Y]==d):
        stay("bdBdbddBdd")
        stay("FDfDFDDfDD")
    elif(dyn[6].o[Y]==f and dyn[8].o[Y]==f and dyn[26].o[Y]==d and dyn[24].o[Y]==d):
        stay("LDlDLDDlDD")
        stay("rdRdrddRdd")
    elif(dyn[6].o[Y]==l and dyn[8].o[Y]==d and dyn[26].o[Y]==d and dyn[24].o[Y]==l):
        stay("BDbDBDDbDD")
        stay("fdFdfddFdd")

    elif(dyn[6].o[Y]==f and dyn[8].o[Y]==d and dyn[26].o[Y]==r and dyn[24].o[Y]==d):
        stay("FDfDFDDfDD")
        stay("rdRdrddRdd")
    elif(dyn[6].o[Y]==d and dyn[8].o[Y]==f and dyn[26].o[Y]==d and dyn[24].o[Y]==l):
        stay("LDlDLDDlDD")
        stay("fdFdfddFdd")
    elif(dyn[6].o[Y]==l and dyn[8].o[Y]==d and dyn[26].o[Y]==b and dyn[24].o[Y]==d):
        stay("BDbDBDDbDD")
        stay("ldLdlddLdd")
    elif(dyn[6].o[Y]==d and dyn[8].o[Y]==r and dyn[26].o[Y]==d and dyn[24].o[Y]==b):
        stay("RDrDRDDrDD")
        stay("bdBdbddBdd")

    elif(dyn[6].o[Y]==l and dyn[8].o[Y]==r and dyn[26].o[Y]==r and dyn[24].o[Y]==l):
        stay("LDlDLDDlDD")
        stay("RDrDRDDrDD")
    elif(dyn[6].o[Y]==f and dyn[8].o[Y]==f and dyn[26].o[Y]==b and dyn[24].o[Y]==b):
        stay("BDbDBDDbDD")
        stay("FDfDFDDfDD")
    elif(dyn[6].o[Y]==l and dyn[8].o[Y]==r and dyn[26].o[Y]==r and dyn[24].o[Y]==l):
        stay("LDlDLDDlDD")
        stay("RDrDRDDrDD")
    elif(dyn[6].o[Y]==f and dyn[8].o[Y]==f and dyn[26].o[Y]==b and dyn[24].o[Y]==b):
        stay("BDbDBDDbDD")
        stay("FDfDFDDfDD")

    if(dyn[6].o[Y]==d and dyn[8].o[Y]==d and dyn[26].o[Y]==d and dyn[24].o[Y]==d):
        pass
    else:
        print "check orientation.............",ornt

def swappcsl(k):
    if(k=="f"):
        stay("lRfLrddlRfLr")
    if(k=="r"):
        stay("fBrFbddfBrFb")
    if(k=="b"):
        stay("rLbRlddrLbRl")
    if(k=="l"):
        stay("bFlBfddbFlBf")
        
def swappcsr(k):
    if(k=="f"):
        stay("lRFLrddlRFLr")
    if(k=="r"):
        stay("fBRFbddfBRFb")
    if(k=="b"):
        stay("rLBRlddrLBRl")
    if(k=="l"):
        stay("bFLBfddbFLBf")
    

# last layer middle pieces  position only...........
def llmpcs():
    if((dyn.index(cell[7])!=7) and (dyn.index(cell[17])!=17) and (dyn.index(cell[25])!=25) and (dyn.index(cell[15])!=15)):
        tmp_v=dyn.index(cell[7])
        if(tmp_v==15):
            swappcsr("r")
        elif(tmp_v==17):
            swappcsl("l")
        elif(tmp_v==25):
            swappcsl("r")

    if(dyn.index(cell[7])==7):
        if(dyn.index(cell[25])==17):
            swappcsr("f")
        elif(dyn.index(cell[25])==15):
            swappcsl("f")
    elif(dyn.index(cell[17])==17):
        if(dyn.index(cell[15])==25):
            swappcsr("r")
        elif(dyn.index(cell[15])==7):
            swappcsl("r")

    elif(dyn.index(cell[25])==25):
        if(dyn.index(cell[7])==15):
            swappcsr("b")
        elif(dyn.index(cell[7])==17):
            swappcsl("b")

    elif(dyn.index(cell[15])==15):
        if(dyn.index(cell[17])==7):
            swappcsr("l")
        elif(dyn.index(cell[17])==25):
            swappcsl("l")

def llmpso():
    if(dyn[7].o[Y]!=d):
        if(dyn[25].o[Y]!=d):
            stay("lRFlRUlRBBLrULrFLrdd")
        elif(dyn[15].o[Y]!=d):
            stay("LBlRFlRUlRBBLrULrFLrddbl")
        elif(dyn[17].o[Y]!=d):
            stay("rblRFlRUlRBBLrULrFLrddBR")

    if(dyn[25].o[Y]!=d):
        if(dyn[15].o[Y]!=d):
            stay("lflRFlRUlRBBLrULrFLrddFL")
        elif(dyn[17].o[Y]!=d):
            stay("RFlRFlRUlRBBLrULrFLrddfr")

    if(dyn[15].o[Y]!=d and dyn[17].o[Y]!=d):
        stay("fBRfBUfBLLFbUFbRFbdd")
    


def test():
    you=0
    while(1):
        jumble()
        solve()
        if((dyn.index(cell[26])!=cell.index(cell[26])) or (dyn.index(cell[24])!=cell.index(cell[24])) or (dyn.index(cell[8])!=cell.index(cell[8])) or (dyn.index(cell[6])!=cell.index(cell[6])) or (dyn.index(cell[2])!=cell.index(cell[2])) or (dyn.index(cell[18])!=cell.index(cell[18])) or (dyn.index(cell[20])!=cell.index(cell[20])) or (dyn.index(cell[1])!=cell.index(cell[1])) or (dyn.index(cell[9])!=cell.index(cell[9])) or (dyn.index(cell[19])!=cell.index(cell[19])) or (dyn.index(cell[11])!=cell.index(cell[11])) or (dyn.index(cell[0])!=cell.index(cell[0]))):
            print "check----------"
            break
        you+=1
        print "done ",you," times"
