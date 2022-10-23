field = [['_','_','_'],
['_','_','x'],
['_','_','_']]

#is field full
def is_full(f):
    for i in range(3):
        if '_' not in f[i]: 
            return False
    return True

#defining state: 
def state(f):
    for i in range(3):
        if f[i][0]==f[i][1]==f[i][2] and f[i][0]!='_': 
            return f[i][0]
    #done: columns
    for i in range(3):
        if f[0][i]==f[1][i]==f[2][i] and f[i][0]!='_': 
            return f[i][0]
    if f[0][0]==f[1][1]==f[2][2] and f[i][0]!='_': 
        return f[0][0]
    elif f[0][2]==f[1][1]==f[2][0] and f[i][0]!='_': 
        return f[0][0]
    # done elif second slope
    elif is_full(f): return 'tie'
    else: return 'continue'

#done: define function for drawing, 
def drawing(f):
    for i in range(len(f)):
        for j in range(3): 
            print (f[i][j], end='')
        print('')


drawing(field)

#define function2 which builds array of arrays of arrays of all possible options

import copy 

def next_step(f, s):
    f_return = []
    for y in range(3):
        for x in range(3): 
            if f[y][x] == '_':
                f_iter = copy.deepcopy(f)
                f_iter[y][x] = s
                f_return.append(f_iter)
    return f_return

# drawing fields with all next steps
def drawing_all(f):
    for i in range(len(f)):
        drawing(f[i])


drawing_all(next_step(field, 'x'))

# won 0 — user - -1
# won x - pc - 1
# tie - 0
# continue


def minimax(f : [[str]], n : str) -> int:
    s = state(f)
    if s == 'tie': return 0
    elif s == 'x': return 1
    elif s == '0': return -1
    else: 
        a = []
        for i in nextstep(f, n):
            c = minimax(i, ('x' if n == '0' else '0'))
            a.append(c)
        if n == 'x': return max(a)
        elif n == '0': return min(a)
        # (max if n=='x' else min)(a)

print(minimax(field, '0'))

#todo функция, которая печатает доски из массива в строчку
#todo туториалы по минимаксу по тик-так-ту 


        



        







