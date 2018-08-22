from turtle import *
colors = ['red', 'blue', 'brown', 'yellow', 'grey']
for i in colors:
    color(i)
    begin_fill()
    forward(100)
    left(90)
    forward(200)
    left(90)
    forward(100)
    left(90)
    forward(200)
    left(90)
    forward(100)
    end_fill()
mainloop()
