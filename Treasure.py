def rotation(arr,rotate):
    ln=(len(rotate)*2)+1
    '''        rx=rotate[i]
            if (rx<0):
                rx=-rx
                if (rx>(ln-1-l)):
                    i=(ln-1)
                    j=(rx-i)
                else:
                    i=rx
                    j=0
            else:
                if (rx>(ln-1-l)):
                    j=(ln-1)
                    i=(rx-j)
                else:
                    j=rx
                    i=0
'''
    for i in range(ln):
        for j in range(ln):
            
num=7
mz=[['L','E','A','R','K','X','G'],['N','Z','N','Z','Q','B','S'],['O','P','E','B','M','S','I'],['A','Z','R','T','X','M','U'],['A','W','S','S','O','K','U'],['A','X','B','A','G','M','O'],['D','F','Q','A','C','U','U']]
'''
for i in range(num):
    mz.append(input().split())
'''
rot=[]
for k in range(num//2):
    i,j=k,k
    ln=(num-1-k)
    count=None
    #AntiClockWise
    while (i<ln):
        if (mz[i][j]=='X'):
            count=(i-(2*k))
            break
        i+=1
    i,j=ln,0
    while (j<(ln+1)):
        if (mz[i][j]=='X'):
            count=(i+j-(2*k))
            break
        j+=1
    if (count!=None):
        print(-count,end=" ")
        rot.append((-count))
    else:
        #ClockWise
        i,j=0,1
        while (j<ln):
            if (mz[i][j]=='X'):
                count=(j-(2*k))
                break
            j+=1
        i,j=0,ln
        while (i<ln):
            if (mz[i][j]=='X'):
                count=(i+j-(2*k))
                break
            i+=1
        print(count,end=" ")
        rot.append(count)

array=rotation(mz,rot)
