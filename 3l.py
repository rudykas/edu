[5,7,9,1,3,2,6,0,4]
[1,3,2,0,4]
[7,9,6]
[0,1,2,3,4]
[6,7,9]
[0,1,2,3,4,5,6,7,9]

def qsort(a):
    if a==[]:
        return []
    b=[]
    c=[]
    for i in range(1,len(a)):
        if a[i]<a[0]:
            b.append(a[i])
        if a[i]>=a[0]:
            c.append(a[i])
    return qsort(b)+[a[0]]+qsort(c)


a=[5,3,9,1,10]

def qsort2(a):
    if len(a)<=1:
        return a
    b=[]
    c=[]
    for i in range(1,len(a)):
        if a[i]<a[0]:
            b.append(a[i])
        else: 
            c.append(a[i])
    return qsort2(b)+[a[0]]+qsort2(c)


a=[5,3,9,1,10]

print(qsort2(a))
    
# x,y,z
# i,j,k
# a,b,c
# bar, foo, foobar (lurkmore)
# spam
# f,g,h