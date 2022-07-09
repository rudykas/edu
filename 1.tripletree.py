from turtle import*

width(3)
def angle3(side):
    if (side < 17):
        return
    left(30)
    forward(side)
    angle3(side*2/3)
    back(side)
    right(30)
    forward(side)
    angle3(side*2/3)
    back(side)
    right(30)
    forward(side)
    angle3(side*2/3)
    back(side)
    left(30)

    
left(90)
back(150)
forward(150)
angle3(100)
