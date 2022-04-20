
#%% q1
from cmath import sqrt
import math



a1 = float(input("enter a1: "))
b1 = float(input("enter b1: "))
t = float(input("enter t: "))
#teta1 = float(input("enter teta1"))

teta1 = - math.atan2(b1,a1)
A1 = math.sqrt( a1 ** 2 + b1 ** 2)

g1 = A1 * math.cos(math.pi/4 * t + teta1)

print("g1 is: ", g1)


#%% q2
import math
x1 = float(input("enter x1: "))
x2 = float(input("enter x2: "))
w1 = float(input("enter w1: "))
w2 = float(input("enter w2: "))
b = float(input("enter b: "))

z = x1*w1 + x2*w2 + b
fz = 1 / (1 + math.e ** z )

print("y is= ",fz)


#%% q3

import math


x0 = float(input("enter x0: "))
y0 = float(input("enter y0: "))
teta0 = float(input("enter teta0: "))
r = float(input("enter r: "))
omega = float(input("enter omega: "))
t = float(input("enter t: "))

x = x0 - r * math.sin(teta0) + r * math.sin(teta0 + omega * t)
y = y0 + r * math.cos(teta0) - r * math.cos(teta0 + omega * t)
teta = teta0 + omega * t

print("x is: ", x , "y is: " , y , "teta is: ", teta)


#%% q4
import math

L1 = float(input("enter L1: "))
L2 = float(input("enter L2: "))
A = float(input("enter A: "))
Z = float(input("enter Z: "))

teta1 = math.acos((L1**2 + A**2 + Z**2 - L2**2) / (2*L1*math.sqrt(A**2 + Z**2))) + math.atan2(Z,A)
teta2 = math.acos( (L1**2 - A**2 - Z**2 + L2**2) / (2*L1*L2) )

print("teta1 is: ", teta1 , "\n", "teta2 is: ",teta2)

# %% q5
import math

x1,y1,x2,y2,x3,y3,xq,yq=1,1,2,2,6,6,6,6

def euc_dist_2d(x,y,xq,yq):
    return math.sqrt((x-xq)**2 + (y-yq)**2 )

dist1 = euc_dist_2d(x1,y1,xq,yq)
dist2 = euc_dist_2d(x2,y2,xq,yq)
dist3 = euc_dist_2d(x3,y3,xq,yq)

if(dist1 < dist2):
    if(dist1 < dist3):
        print("query is closer to class1")
    else:
        print("query is closer to class3")
elif(dist2 < dist3):
     print("query is closer to class2")
else:
    print("query is closer to class3")


#%% q6

import math

p1x,p1y,p1z,p2x,p2y,p2z,rOuter,rInner = 1,1,1,4,5,13,15,13.0001

def euc_dist_3d(x1,y1,z1,x2,y2,z2):
    return math.sqrt((p1x-p2x)**2 + (p1y-p2y)**2 + (p1z-p2z)**2 )


distP1P2 = euc_dist_3d(p1x,p1y,p1z,p2x,p2y,p2z)

if(distP1P2 < rOuter):
    if(distP1P2 < rInner):
        print("Inner region")
    else:
        print("Outer region")   
else:
    print("not in region")
#%% q7
import math

sOpen = 1.8
sClose = 8.6
sSemiOpen = 2.4

def prob_calculate(n1,d1,d2,d3):
    return math.e ** n1 / ( math.e ** d1 + math.e ** d2 + math.e ** d3 )

pOpen = prob_calculate(sOpen,sOpen,sClose,sSemiOpen)
pClose = prob_calculate(sClose,sOpen,sClose,sSemiOpen)
pSemiOpen = prob_calculate(sSemiOpen,sOpen,sClose,sSemiOpen)

if(pOpen > pClose):
    if(pOpen > pSemiOpen):
        print("open door")
    else:
        print("semi open door")
elif(pClose>pSemiOpen):
    print("close door")
else: 
    print("semi open door")





#%% q8
goal,dist=1,16.5

if(goal == 1):
    if(dist >= 16.5):
        print("He scores, absolutely brilliant! ")
    elif(dist >= 5.5):
        print("A fantastic move and a good finish! ")
    else:
        print("He finds the net with ease!")
else:
    print("He should have scored! ")

# %%
