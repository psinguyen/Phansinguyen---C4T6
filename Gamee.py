player = {
    "Name": "Zai",
    "Class": "zai",
    "HP": 10,
    "ATK": 10,
    "DEF": 2,
    "AGI": 1,
    "LVL": 1,
}
Opponent = {
    "Name": "Gái",
    "Class": "gai",
    "HP": 50,
    "ATK": 4,
    "DEF": 2,
    "AGI": 1,
    "LVL": 1,
}
while True:
    cmd = input("Your command? ")
    if cmd == "stats player":
        print("Your name: ", player["Name"])
        print("Your class: ", player["Class"])
        print("HP: ", player["HP"])
        print("AGI: ", player["AGI"])
        print("Attack: ", player["ATK"])
        print("Defense: ", player["DEF"])
        print("Level: ", player["LVL"])
    if cmd == "stats Opponent":
        print("Your name: ", Opponent["Name"])
        print("Your class: ", Opponent["Class"])
        print("HP: ", Opponent["HP"])
        print("AGI: ", Opponent["AGI"])
        print("Attack: ", Opponent["ATK"])
        print("Defense: ", Opponent["DEF"])
        print("Level: ", Opponent["LVL"])
    if cmd == "play":
        print ("Chọn một trong mấy cái sau")
        print ("1. Đi chơi")
        print ("2. Đi ăn")
        print ("3. Vào nhà nghỉ a đi vệ sinh tí")
        cmd1 = input("Chọn nhanh trước khi nó dỗi ")
        if cmd1 == "1":
            print ("Đi đâu anh?")
            print ("1. Đi công viên?")
            print ("2. Tocotoco")
            print ("3. Lên phố")
            cmd1_1 = input("Chọn nhanh trước khi nó dỗi ")
            if cmd1_1 == "3":
                print ("Oki, iu thễ")
                DAM = player["ATK"] - Opponent["DEF"]
                if DAM > 0:
                    Opponent["HP"] = Opponent["HP"] - DAM
                print("Op HP: ", Opponent["HP"])
            if cmd1_1 == "2":
                print ("Ứ ừ, hông đi đâu")
                DAM = Opponent["ATK"] - player["DEF"]
                if DAM > 0:
                    player["HP"] = player["HP"] - DAM
                    print("HP: ", player["HP"])
                    if player["HP"] < 0:
                        print("Mình chia tay ik")
            if cmd1_1 == "1":
                print ("Ờ,được thôi")
                if player["HP"] < 0:
                    print("Mình chia tay ik")
        if cmd1 == "2":
            print ("Ăn gì anh?")
            print ("1. Bò?")
            print ("2. Cơm mẹ nấu")
            print ("3. Iem")
            cmd1_2 = input("Chọn nhanh trước khi nó dỗi ")
            if cmd1_2 == "1":
                print ("Ứ ừ, béo nhắm, hông đi đâu")
                print("Ứ ừ, hông đi đâu")
                DAM = Opponent["ATK"] - player["DEF"]
                if DAM > 0:
                    player["HP"] = player["HP"] - DAM
                    print("HP: ", player["HP"])
                    if player["HP"] < 0:
                        print("Mình chia tay ik")
            if cmd1_2 == "2":
                print("Ờ,được thôi")
                if player["HP"] < 0:
                    print("Mình chia tay ik")
            if cmd1_2 == "3":
                print("Oki, iu thễ")
                DAM = player["ATK"] - Opponent["DEF"]
                if DAM > 0:
                    Opponent["HP"] = Opponent["HP"] - DAM
                print("Op HP: ", Opponent["HP"])
        if cmd1 == "3":
            if Opponent["HP"]<0:
                print ("Oki, đi thôi anh")
            if Opponent["HP"]>0:
                print ("Mình chia tay ik")


