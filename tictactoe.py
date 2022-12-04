
import copy 

field = [
['x','_','0'],
['0','x','_'],
['x','_','0']]

#is field full
def is_full(f):
    for i in range(3):
        if '_' in f[i]: 
            return False
    return True


# print('is full', is_full(field))

#defining state: 
def state(f):
    for i in range(3):
        if f[i][0]==f[i][1]==f[i][2] and f[i][0]!='_': 
            return f[i][0]
    #columns
    for i in range(3):
        if f[0][i]==f[1][i]==f[2][i] and f[0][i]!='_': 
            return f[0][i]
    if f[0][0]==f[1][1]==f[2][2] and f[0][0]!='_': 
        return f[0][0]
    elif f[0][2]==f[1][1]==f[2][0] and f[0][2]!='_': 
        return f[0][2]
    # done elif second slope
    elif is_full(f): return 'tie'
    else: return 'continue'

#drawing from array, 
def drawing(f):
    for i in range(len(f)):
        for j in range(3): 
            print (f[i][j], end='')
        print('')

#drawing(field)

#builds array of arrays of arrays of all possible next steps 

def next_step(f, s):
    """
    f: current field 
    s: next step, x or 0 
    """
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

#drawing_all(next_step(field, 'x'))


#drawing all possible next steps in a row 
def drawing_row(f):
    for i in range(3):
        for j in range(len(f)):
            print(''.join(f[j][i]), end = ' ')
        print('')

# drawing_row(next_step(field,'0'))

# print('*'*80)

def minimax(f : [[str]], n : str, depth : int) -> int:
    """
    f — field 
    n — x or 0
    depth — depth of the recursion 
    """ 

    # print('depth', depth)
    # print('current field:') 
    #drawing(f)
    s = state(f)
    # print('state',state(f))
    if s == 'tie':
        # print(f'tie in the termianl branch, depth={depth}')
        return 0

    elif s == 'x': 
        # print(f'1 in the terminal branch, depth= {depth}')
        return 1
        
    elif s == '0':
        # print(f'-1 in the terminal branch, depth={depth}') 
        return -1

    else: 
        scores = []
        # call stack
        for i in next_step(f, n):
            c = minimax(i, ('x' if n == '0' else '0'), depth+1)
            scores.append(c)
            
        # print( f'next_step, depth={depth}')
        #drawing_row(next_step(f,n))
        # print(f'scores={scores}') #todo print elegantly with loop
        if n == 'x': 
            # print('max', max(scores))
            return max(scores)

        elif n == '0': 
            # print('min', min(scores))
            return min(scores)
        # print('a-iter', a)
        # (max if n=='x' else min)(a)

# print('minimax', minimax(field, 'x', 0))


 

def next_turn(field, x): 
    a = []
    for el in next_step(field, x):
        a.append([el, minimax(el, ('x' if x == '0' else '0'), 1)])
    if x == 'x': 
        return a[a.index(max(a, key = lambda k:k[-1]))][0]
    elif x == '0': 
        return a[a.index(min(a, key = lambda k:k[-1]))][0]



#drawing(next_turn(field, 'x'))

#interface with tkinter 









#функция которая берет доску и возвращает релевантную доску. макс — индекс

# won 0 — user - -1
# won x - pc - 1
# tie - 0
# continue





#todo туториалы по минимаксу по тик-так-ту 


        



        







