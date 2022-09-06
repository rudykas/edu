
#[ ][*][ ] 
#[ ][ ][*] 
#[*][*][*]    


a = [[0,1,0,0],
    [0,0,1,0],
    [1,1,1,0],
    [0,0,0,0]]
    
# i — x, j — y
# первый индекс это строчка, второй — столбец 

#отрисовка звездочек по кортежу
def show(a):
    for j in range(len(a)):
        for i in range(len(a[j])):
            print('[',end='')
            if a[j][i]==0:
                print(' ',end='')
            if a[j][i]==1:
                print('*',end='')
            print(']',end='')
        print('')


# проверяет, не вышли ли за границы. 
# что значит te?          
def te(y,x,a):
    if x<0 or y <0 or x > len(a[0])-1 or y > len(a)-1:return 0 
    else:return a[y][x]
        
def count_alive(x,y,a):
    return te(y-1,x-1,a)+\
    te(y-1,x,a)+\
    te(y-1,x+1,a)+\
    te(y,x-1,a)+\
    te(y,x+1,a)+\
    te(y+1,x-1,a)+\
    te(y+1,x,a)+\
    te(y+1,x+1,a)
    
print('Alive neighbours — ', count_alive(1,1,a))

show(a)

def live_or_die(x : int,y : int,a : [[int]]):
  if a[y][x] == 1:
    if count_alive(x,y,a) < 2 or count_alive(x,y,a) > 3:
      return 0
    else: return 1
  elif a[y][x] == 0 and count_alive(x,y,a) == 3: return 1
  else: return 0

print('Does exist star? —', a[1][1])

print('Will be alive? — ', live_or_die(0,1,a))

def build_new(a):
    c=[]
    for y in range(len(a)):
        b=[]
        for x in range(len(a[0])):
             b.append(live_or_die(x,y,a))
        c.append(b)
    return c

show(build_new(build_new(build_new(a))))
    
import re 


file = open('life.txt', 'r')

text=file.read()

text = text.split('\n')
print(text)


print(re.match(r'(\[ \]|\[\*\])+$', "[ ][*][*][][ ]"))


# проверка строк на валидность
def check(a):
    text_array = a.split('\n') 
    for i in range(len(text_array)-2):
        if not (len(text_array[i]) == len(text_array[i+1])): return False
    for j in range(len(text_array)-1):
        if not re.match(r'(\[ \]|\[\*\])+$', text_array[j]): return False
    return True



def check(a):
    text_array = a.split('\n') 
    for i in range(len(text_array)-2):
        if not (len(text_array[i]) == len(text_array[i+1])): return False
    return all(re.match(r'(\[ \]|\[\*\])+$', k) for k in text_array)
    
            
        
a = """[ ][*][ ]
[ ][ ][ ]
[*][*][*]"""

print(check(a))
    

#check (
    #for i in range(len(text_array))
    #    re.match(r'(\[ \]|\[\*\])+$', text_array[i])
        
        

#"[ ][*][*][ ][ ]"
#[\[\] *] and 
#(\[ \]|\[\*\])


#for i in range(1,10): print(i)

#i=0
#while i<10:
#    print(i)