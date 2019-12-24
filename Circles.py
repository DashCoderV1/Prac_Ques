from math import *

R1,R2,D,X1,X2=list(map(int,input().split()))
Dtr1=D-(((pi*R1)/2)*X1)
Dtr2=Dtr1+(((pi*R2)/2)*X2)
ang=0
pos1,pos2=(X1%4),(X2%2)
try:
    if (pos1==0 and (not pos2)):
        ang=degrees(atan((2*R2)/Dtr2))
    elif (pos1==0 and pos2):
        ang=degrees(atan( R2/(Dtr2-R2)))-degrees(atan( R2/(Dtr2+R2) ))
    elif (pos1==1 and (not pos2)):
        ang=degrees(atan( ((2*R2)-(R1)) / (Dtr2+R1) ))+degrees(atan( R1/ (Dtr2+R1) ))
    elif (pos1==1 and pos2):
        ang=degrees(atan( (R2-R1) /(Dtr2-R2+R1) ))-degrees(atan( (R2-R1)/(Dtr2+R1+R2) ))

    elif (pos1==2 and (not pos2)):
        ang=degrees(atan( (2*(R2-R1)) / Dtr2 ))+degrees(atan( (2*R1)/Dtr2 ))
    elif (pos1==2 and pos2):
        ang=degrees(atan(  (R2-R1)/(Dtr2-R2) ))-degrees(atan( (R2-R1)/(Dtr2+R2) ))

    elif (pos1==3 and (not pos2)):
        ang=degrees(atan( ((2*R2)-R1) / (Dtr2-R1) ))+degrees(atan( R1/(Dtr2-R1) ))
    elif (pos1==3 and pos2):
        ang=degrees(atan( (R2-R1) / (Dtr2-R2-R1) ))-degrees(atan( (R2-R1)/(Dtr2-R1+R2) ))

    print(round(ang,6))
except e:
    print(None)
