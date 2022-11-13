from curses import *
import random
import snake_score as sc

name = input('What is your name? ')

#changing terminall to raw  mode 
s = initscr()




try: 
    #creating letter for snake
    snake_char = random.choice(['a','b','q','z','s','n','m','d'])

    #print letter 
    s.addstr(0,0,snake_char)

    y=0
    x=0

    # score of user
    score = 0

    #finding screen size 
    h,w = s.getmaxyx()

    def create_apple():
        global ya,xa,apple
        apple=random.choice(['a','b','q','z','s','n','m','d']) 
        ya=random.randint(0,h-1) #h-1 because last argument included by randint
        xa=random.randint(0,w-1)
        
        s.addstr(ya,xa,apple)
        
        while [ya,xa] in snake:
            ya=random.randint(0,h-1)
            xa=random.randint(0,w-1)
            s.addstr(ya,xa,apple)
        
    #start point of snake
    snake=[[0,0]]

    create_apple()

    dy=0
    dx=1

    halfdelay(1)
    while True:
        key=s.getch() #waits a key to be pressed 
        s.erase() # erase everything from the screen 
        # if key==-1: 
        #    y=y+dy
        #    x=x+dx

        #moving snake with keys s,w,a,d
        if key == ord('d'):
            dx=1
            dy=0
        elif key == ord('s'):
            dy=1
            dx=0
        elif key == ord('a'):
            dx=-1
            dy=0
        elif key ==ord('w'):
            dy=-1
            dx=0
        y=y+dy
        x=x+dx
        
        s.addstr(ya,xa,apple) #renew apple due to previous erasure 
        
        if y==ya and x==xa:  # [y,x]==apple
            score += 1
            snake_char = apple # changing letter of snake to apple letter 
            create_apple()

        else:
            del snake[0]

        #returning to screen from outer space
        if y == h:
            y = 0
        elif x == w:
            x = 0
        elif y < 0:
            y = h-1
        elif x < 0:
            x = w-1
        #new coordinates of snake's head
        head=[y,x]
        
        if head in snake: #check of colision 
            endwin()
            exit()
        snake.append(head)
        #drawing the snake 
        for k in range(len(snake)): 
            s.addstr(snake[k][0],snake[k][1],snake_char)
        
        
    s.getch()


# from curses import wrapper
# wrapper(main)
# endwin()

finally: 
    endwin()
    
    #name = input('What is your name? ')
    sc.add_participant(name, score)
    winner = sc.findMaxScoreFromFile('score2.csv')
    print(f'Thanks, {name}, your score is {score}. The winner is {winner[0]}, with score {winner[1]}')





#try — весь код
# finally — выполнится в любом случае 

# выход  ctrl-c

#? что делает getch? erase? 
#? 
