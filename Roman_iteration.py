def Roman(num):
    val=[1000, 900, 500, 400,100, 90, 50, 40,10, 9, 5, 4,1]
    symbol=["M", "CM", "D", "CD","C", "XC", "L", "XL","X", "IX", "V", "IV","I"]
    roman_num=''
    i=0
    while  num>0:
        for _ in range(num//val[i]):
            roman_num+=symbol[i]
            num-=val[i]
        i+=1
    return roman_num

def Deci(Rnum):
    new_num=0
    nsize=len(Rnum)-1
    for i in Rnum:
        new_num+=(ord(i)-55)*(34**nsize)
        nsize-=1
    return new_num

def RI(num):
    if num in range(1,4000):
        stg=Roman(num)
        n_num=Deci(stg)
        return RI(n_num)
    else:
        return num

print(RI(int(input(""))))
