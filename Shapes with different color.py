from turtle import *
n = 3
colors = ['red', 'blue', 'brown', 'yellow', 'grey']
for i in colors:
    color(i)
    for t in range(1,n+1):
        forward(100)
        left(360/n)
    n = n+1
mainloop()
