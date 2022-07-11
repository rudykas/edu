#найдите максимальный элемент массива
x=[-1,-2,-12,-7,-3,-4,-8, -2]

y = x[0]

for i in x:
    if y<=i:
        y=i

#print(y)

#Функция count_element(2,[1,8,9,2,5,2,2]) -> 3, подсчитывает кол-во элементов массива равных первому аргументу



def count_element(c,d):
    z = 0
    for i in d:
        if i==c:
            z=z+1
    return z

# c = input('элемент ')
# d = input('массив ')
            
# print(count_element(int(c),eval(d)))


#2. Функция equal_elements([2,2,2,2]) -> True, возвращает истину если все элементы массива одинаковы, ложь, если хотя бы один элемент не равен остальным

# a = eval(input('массив для проверки одинаковости '))

def equal_element(a):
    for i in a:
        z=0
        c=a[0]
        if i==c:
           z=z+1
    return z==len(a)-1
   
# print(equal_element(a))

#3. Функция merge([2,5,9],[1,4,8]) -> [1,2,4,5,8,9], сливающая два отсортированных массива так, чтобы результриующий массив был отсортирован.



def merge(a,b):
    c = []
    for i in range(len(a)):
        if a[i]>b[i]:
            c.append(b[i])
            c.append(a[i])
        else:
            c.append(a[i])
            c.append(b[i])
    return c

a = [2,5,9]
#eval(input('массив для merge a '))
b = [1,4,8]
#eval(input('массив для merge b '))

#print(merge(a,b))

#3.1. Функция merge оба упорядоченны, но относительно друг друга они не упорядоченны. т.е. [1,4,8,9] [2,5,7]

#не (a и b) = (не a) или (не b)
#не (a или b) = (не a) и (не b)

def merge2(a,b):
    c=[]
    while not (a == [] or b == []):
        if a[0] < b[0]:
            c.append(a[0])
            a.pop(0)
        else:
            c.append(b[0])
            b.pop(0)
    c.extend(a)
    c.extend(b)
    return c

a = [1,4,8,9]
b = [2,5,7]
            
print(merge2(a,b))
    

#4. Функция is_sorted([3,7,9]) -> True, если массив отсортирован по возрастанию, False в противном случае.


def is_sorted(a):
    c=0
    for i in range(len(a)-1):
       if a[i+1]>a[i]: c=c+1
    return c==len(a)-1

a=[3,7,5]
print(is_sorted(a))


def merge_sort(a):
    if len(a)>1:
        e=len(a)//2
        return merge2(merge_sort(a[e:]),merge_sort(a[:e]))
    else:return a
    
a=[1,4,2,7,8,5]
print(merge_sort(a))

