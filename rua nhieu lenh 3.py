from turtle import*
turtle_list = []
for i in range(5):
    t = Turtle()
    turtle_list.append(t)
while True:
    position = int(input("Turtle position? "))
    colour = (input("Turtle color? "))
    shapes = (input("Turtle shape? "))
    command = (input("Turtle command? "))
    command_list = command.split(" ")
    turtle_list[position] = t
    t.color(colour)
    t.shape(shapes)
    for command in command_list:
        if command == "fd":
            t.forward(100)
        if command == "bd":
            t.backward(100)
        if command == "lt":
            t.left(90)
        if command == "rt":
            t.right(90)
mainloop()