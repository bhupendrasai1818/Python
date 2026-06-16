import math as m
s=0
d=1
l=[]
m=0
#n=int(input("enter the size"))
'''for i in range(0,n):
    l.append(int(input("enter list element")))
    s+=l[i]
print(l,s)'''
x=input("enter string")
for i in range(0,len(x)-1):
    for j in range(i+1,len(x)-1):
        if x[i]==x[j] and [j]!=x[j+1]:
            if d>m:
                print(d,"---")
                m=d
                d=1
                print(x[i:j])
                break
            else:
                d=1
                break
        else:
            d+=1
#print(l)
#c='helfdbfvnsjfo'
#c=tuple(c)
#print(type(c),c)
#c=set(c)
#print(type(c),c)
#c=list(c)
#print(type(c),c)
