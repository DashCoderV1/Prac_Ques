class Bottle:
    def __init__(self,r):
        self.radius=int(r)
        self.hid=False
        self.inside=False
    def hide(self):
        self.hid=True
    def into(self):
        self.inside=True

Bottles=[]
n=int(input(""))
Bottle_string=input()
ls=Bottle_string.split(" ")
Bottles=[Bottle(i) for i in ls]

for i in Bottles:
    for j in range(n):
        if ((i.radius<Bottles[j].radius) and (not(i.hid)) and (not(Bottles[j].inside)) ):
            i.hide()
            Bottles[j].into()
            break
size=0
for i in Bottles:
    if (not(i.hid)):
        size+=1
print("size=",size)
