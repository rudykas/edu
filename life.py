#[ ][*][ ] 
#[ ][ ][*] 
#[*][*][*]    


a = [[0,1,0],
    [0,0,1],
    [1,1,1]]
    
# i — x, j — y

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
        
def te(y,x,a):
    if x<0 or y <0 or x > len(a) or y > len(a[0]):return 0 
    else:return a[y][x]
        

def count_alive(x,y,a):
    return te((y-1,x-1,a)+\
    te(y-1,x,a)+\
    te(y-1,x+1,a)+\
    te(y,x-1,a)+\
    te(y,x,a)+\
    te(y,x+1,a)+\
    te(y+1,x-1,a)+\
    te(y+1,x,a)+\
    te(y+1,x+1),a)
    
print(count_alive(1,1,a))

show(a)