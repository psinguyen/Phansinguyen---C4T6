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
            command_list[command] = command_list["command + 1"]
            t.left(command)
        if command == "rt":
            command_list[command] = command_list["command + 1"]
            t.left(command)
mainloop()