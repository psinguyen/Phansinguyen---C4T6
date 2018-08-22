list = []
while True:
    command = input("Welcome to our shop, what do you want (C, R, U, D)? ")
    if command == "C":
        new = input("Enter new item: ")
        list.append(new)
        for c in list:
            print("*", c)
    if command == "R":
        for c in list:
            print("*", c)
    if command == "U":
        update = int(input("Update position? "))
        trade = input("Enter new item: ")
        n = 1
        listed = list
        for c in list:
            list.remove(c)
            list.append(n)
            n=n+1
        for e in list:
            if e==update:
                list.remove(e)
                list.append(trade)
        for m in listed:
            for n in list:
                if n == trade:
                    list.remove(n)
                    list.append(trade)
                else:
                    list.remove(n)
                    list.append(m)
        for y in list:
            print("*", y)
        list=listed
    if command == "D":
        remove = input("Delete position? ")
        list.remove(remove)
        for c in color_list:
            print("*", c)


