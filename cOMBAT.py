def show_item(object):
    for key, value in object.items():
        print (key, ": ",value)
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
def combat(A, D):
    print(A["Name"], "is beating", D["Name"])
    DAM = A["ATK"] - D["DEF"]
    if DAM > 0:
        D["HP"] = D["HP"] - DAM
    print (D["HP"])
while Opponent["HP"] > 0 or player["HP"] > 0:
    print ("Player HP: ", player["HP"])
    print ("Opponent HP: ", Opponent["HP"])
    combat(player, Opponent)
    combat(Opponent, player)
