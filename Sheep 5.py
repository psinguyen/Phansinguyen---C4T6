list = [5, 7, 300, 90, 24, 50, 75]
for e in range (1,5):
    n = 0
    for c in list:
        if c>n:
            n=c
    print("Now my biggest sheep has size ", n, ". Let's sheer it")
    for c in list:
        if c == n:
            list.remove(c)
    print ("After sheering, this is my flock ")
    print (list)
    for p in list:
        list.remove(p)
        list.append(p+50)
    print ("One month has passed, this is my flock ")
    print (list)