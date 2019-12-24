
num=int(input())
array1=input().split()
array2=input().split()
dic={}
for i in range(num):
    if (array1[i] in dic):
        dic[array1[i]]+=1
    else:
        dic[array1[i]]=0
    if (array2[i] in dic):
        dic[array2[i]]+=1
    else:
        dic[array2[i]]=0
ln=len(dic)
Q=int(input())
ls=[]
for i in range(Q):
    l1,h1,l2,h2=input().split()
    ls.append([int(l1),int(h1),int(l2),int(h2)])
for i in ls:
    count=0
    l1,h1,l2,h2=i
    for i in dic:
        if ((i in array1[(l1-1):h1]) or (i in array2[(l2-1):h2])):
            count+=1
    print(ln-count)
