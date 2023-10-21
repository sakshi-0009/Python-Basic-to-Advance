playerList = ["VIrat","Rohit","KLRahul","Dhoni"]
playerName = input("Enter player name : ")
for player in playerList:
    if(player==playerName):
        print(player," is present in the list")
        break
else:
    print(player," is not present in the list")
