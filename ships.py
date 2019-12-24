from math import *
class islands:
    def __init__(self,ind,a1,b1,a2,b2):
        self.index=ind
        self.x1=int(a1)
        self.y1=int(b1)
        self.x2=int(a2)
        self.y2=int(b2)
        self.dis=0
    def min_dist_ship(self,s):
        pos_dis=abs((self.x1-s[0]))+abs((self.y1-s[1]))
        pos_dis1=abs((self.x2-s[0]))+abs((self.y2-s[1]))
        pos_dis2=abs((self.x1-s[0]))+abs((self.y2-s[1]))
        pos_dis3=abs((self.x2-s[0]))+abs((self.y1-s[1]))
        self.dis=min(pos_dis,pos_dis1,pos_dis2,pos_dis3)

def partition(arr,low,high):
    i = ( low-1 )
    pivot = arr[high].dis
    for j in range(low , high):
        if   arr[j].dis <= pivot:
            i = i+1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[high] = arr[high],arr[i+1]
    return ( i+1 )

def quicksort(arr,low,high):
    if low < high:
        pi = partition(arr,low,high)
        quicksort(arr, low, pi-1)
        quicksort(arr, pi+1, high)

N=int(input(""))
ship=[]
island=[]
for i in range(N):
    ls=input("").split(" ")
    island.append(islands(i+1,ls[0],ls[1],ls[2],ls[3]))

t=input("").split(" ")
ship=[int(i) for i in t]
for i in island:
    i.min_dist_ship(ship)

quicksort(island,0,N-1)

for i in range(N-1):
    print((island[i].index),end=" ")
print((island[i+1].index),end='')
