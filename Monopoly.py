import random
import string
import json
import os
def StartGame():
    start = input("Start New or Load Game? (N/L) ").lower()
    if start == "n":
        Start()
    elif start == "l":
        Load()
def Start():
    global player_list, prop_mort, player_jail, jailtime, prop_owner, player_cash, player_prop, player_GOOJF, ownedRR, ownedU, player_positions, networth, sortedprop, OrangeMon, RedMon, YellowMon, LightBlueMon, LightPurpleMon, GreenMon, DarkPurpleMon, DarkBlueMon
    player_list = choose_players()
    random.shuffle(player_list)  # Shuffle the player list to randomize the play order
    player_positions = {player: 0 for player in player_list}  # Initialize player positions
    player_jail = {player: False for player in player_list}
    jailtime = {player: 0 for player in player_list}
    player_cash = {player: 1500 for player in player_list}
    player_prop = {player: [] for player in player_list}
    player_GOOJF = {player: 0 for player in player_list}
    ownedRR = {player: 0 for player in player_list}
    ownedU = {player: 0 for player in player_list}
    player_positions = {player: 0 for player in player_list}
    networth = {player: 0 for player in player_list}
    OrangeMon = {player: False for player in player_list}
    RedMon = {player: False for player in player_list}
    YellowMon = {player: False for player in player_list}
    LightBlueMon = {player: False for player in player_list}
    LightPurpleMon = {player: False for player in player_list}
    GreenMon = {player: False for player in player_list}
    DarkPurpleMon = {player: False for player in player_list}
    DarkBlueMon = {player: False for player in player_list}
    prop_mort = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    for i in range(75):
        print()
    print("Players in play order:")
    for i, player in enumerate(player_list, start=1):
        print(f"Position {i}: Player: {player}")
    print("\nGame Start!")
    prop_owner = ['Unowned', 'Unowned', 'Unowned', 'Unowned', 'Unowned', 'Unowned', 'Unowned', 'Unowned', 'Unowned', 'Unowned', 'Unowned', 'Unowned', 'Unowned', 'Unowned', 'Unowned', 'Unowned', 'Unowned', 'Unowned', 'Unowned', 'Unowned', 'Unowned', 'Unowned', 'Unowned', 'Unowned', 'Unowned', 'Unowned', 'Unowned', 'Unowned', 'Unowned', 'Unowned', 'Unowned', 'Unowned', 'Unowned', 'Unowned', 'Unowned', 'Unowned', 'Unowned', 'Unowned', 'Unowned', 'Unowned']
    return
def Load():
    global player_list, player_jail, prop_owner, jailtime, player_cash, player_prop, prop_mort, player_GOOJF, ownedRR, ownedU, player_positions, networth, sortedprop, OrangeMon, RedMon, YellowMon, LightBlueMon, LightPurpleMon, GreenMon, DarkPurpleMon, DarkBlueMon
    files = os.listdir("Monopoly Saves")
    numm = 0
    choices = []
    for file in files:
        numm += 1
        print(f"{numm}. {file}")
        choices.append(file)
    choice = round(float(input("Which File? ")))
    if choice > numm or choice < 1:
        print("Invalid Value")
        Load()
    else:
        choicenum = choice - 1
        print(f"Loading {choices[choicenum]}")
        with open(f"Monopoly Saves/{choices[choicenum]}", "r") as json_file:
            data = json.load(json_file)
    player_list = data["player_list"]
    player_jail = data["player_jail"]
    jailtime = data["jailtime"]
    player_cash = data["player_cash"]
    player_prop = data["player_prop"]
    player_GOOJF = data["player_GOOJF"]
    ownedRR = data["ownedRR"]
    ownedU = data["ownedU"]
    player_positions = data["player_positions"]
    networth = data["networth"]
    OrangeMon = data["OrangeMon"]
    RedMon = data["RedMon"]
    YellowMon = data["YellowMon"]
    LightBlueMon = data["LightBlueMon"]
    LightPurpleMon = data["LightPurpleMon"]
    GreenMon = data["GreenMon"]
    DarkPurpleMon = data["DarkPurpleMon"]
    DarkBlueMon = data["DarkBlueMon"]
    prop_owner = data["prop_owner"]
    prop_mort = data["prop_mort"]
def Save():
    global networth, prop_mort, ownedRR, ownedU, player_list, player_positions, prop_house, player_mort, current_player, player_prop, player_cash, playerGOOJF, Double, jailtime, player_jail, prop_owner, current_turn, OrangeMon, RedMon, YellowMon, LightBlueMon, LightPurpleMon, GreenMon, DarkPurpleMon, DarkBlueMon
    game_state = {
        "player_list": player_list,
        "player_positions": player_positions,
        "prop_house": prop_house,
        "current_player": current_player,
        "player_prop": player_prop,
        "player_cash": player_cash,
        "player_GOOJF": player_GOOJF,
        "Double": Double,
        "jailtime": jailtime,
        "player_jail": player_jail,
        "prop_owner": prop_owner,
        "current_turn": current_turn,
        "DarkPurpleMon": DarkPurpleMon,
        "LightBlueMon": LightBlueMon,
        "LightPurpleMon": LightPurpleMon,
        "OrangeMon": OrangeMon,
        "RedMon": RedMon,
        "YellowMon": YellowMon,
        "GreenMon": GreenMon,
        "DarkBlueMon": DarkBlueMon,
        "ownedU": ownedU,
        "ownedRR": ownedRR,
        "networth": networth,
        "prop_mort": prop_mort
        }
    name = input("Name The File: ")
    if not os.path.exists("Monopoly Saves"):
        os.makedirs("Monopoly Saves")

    with open(f"Monopoly Saves/{name}_gamestate.json", "w") as json_file:
        json.dump(game_state, json_file)
Double = 0
     
def choose_players():
    try:
        player_count = int(input("How many players? "))
        print(f"{player_count} players")
        players = []
        for i in range(player_count):
            name = input(f"Name for Player {i + 1}: ")
            players.append(name)
        return players
    except ValueError:
        print("Invalid number")
        return choose_players()
def endturn():
    global current_turn, player_list, Double
    if Double > 0:
        current_turn = (current_turn + 0) % len(player_list)
    else:
        current_turn = (current_turn + 1) % len(player_list)
ChanceMovement = False
owned_prop = []
current = 0
prop_list = ['GO', 'Mediterranean Avenue(DP)', 'Community Chest', 'Baltic Avenue(DP)', 'Income Tax', 'Reading Railroad(RR)', 'Oriental Avenue(LB)', 'Chance', 'Vermont Avenue(LB)', 'Connecticut Avenue(LB)', 'Just Visiting', 'St. Charles Place(LP)', 'Electric Company(U)', 'States Avenue(LP)', 'Virginia Avenue(LP)', 'Pennsylvania Railroad(RR)', 'St. James Place(O)', 'Community Chest', 'Tennessee Avenue(O)', 'New York Avenue(O)', 'Free Parking', 'Kentucky Avenue(R)', 'Chance', 'Indiana Avenue(R)', 'Illinois Avenue(R)', 'B&O Railroad(RR)', 'Atlantic Avenue(Y)', 'Ventnor Avenue(Y)', 'Water Works(U)', 'Marvin Gardens(Y)', 'Jail', 'Pacific Avenue(G)', 'North Carolina Avenue(G)', 'Community Chest', 'Pennsylvania Avenue(G)', 'Short Line Railroad(RR)', 'Chance', 'Park Place(DB)', 'Luxury Tax', 'Boardwalk(DB)']
prop_house = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
prop_prices = [0, 60, 0, 60, 0, 200, 100, 0, 100, 120, 0, 140, 150, 140, 160, 200, 180, 0, 180, 200, 0, 220, 0, 220, 240, 200, 260, 260, 150, 280, 0, 300, 300, 0, 320, 200, 0, 350, 0, 400]
house_prices = [0, 50, 0, 50, 0, 0, 50, 0, 50, 50, 0, 100, 0, 100, 100, 0, 100, 0, 100, 100, 0, 150, 0, 150, 150, 0, 150, 150, 0, 150, 0, 200, 200, 0, 200, 0, 0, 200, 0, 200]
prop_type = ['GO', 'P', 'CC', 'P', 'IT', 'RR', 'P', 'C', 'P', 'P', 'JV', 'P', 'U', 'P', 'P', 'RR', 'P', 'CC', 'P', 'P', 'FP', 'P', 'C', 'P', 'P', 'RR', 'P', 'P', 'U', 'P', 'Jail', 'P', 'P', 'CC', 'P', 'RR', 'C', 'P', 'LT', 'P']
monopolyDP = ['Mediterranean Avenue(DP)', 'Baltic Avenue(DP)']
monopolyLB = ['Oriental Avenue(LB)', 'Vermont Avenue(LB)', 'Connecticut Avenue(LB)']
monopolyLP = ['St. Charles Place(LP)', 'States Avenue(LP)', 'Virginia Avenue(LP)']
monopolyO = ['St. James Place(O)', 'Tennessee Avenue(O)', 'New York Avenue(O)']
monopolyR = ['Kentucky Avenue(R)', 'Indiana Avenue(R)', 'Illinois Avenue(R)']
monopolyY = ['Atlantic Avenue(Y)', 'Ventnor Avenue(Y)', 'Water Works(U)', 'Marvin Gardens(Y)']
monopolyG = ['Pacific Avenue(G)', 'North Carolina Avenue(G)', 'Pennsylvania Avenue(G)']
monopolyDB = ['Park Place(DB)', 'Boardwalk(DB)']
ownable = [0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1]
rentdue = 0
prop_rentHouse0 = [0, 2, 0, 4, 0, 0, 6, 0, 6, 8, 0, 10, 0, 10, 12, 0, 14, 0, 14, 16, 0, 18, 0, 18, 20, 0, 22, 22, 0, 24, 0, 26, 26, 0, 28, 0, 0, 35, 0, 50]
prop_rentHouseMon = [0, 4, 0, 8, 0, 0, 12, 0, 12, 16, 0, 20, 0, 20, 24, 0, 28, 0, 28, 32, 0, 36, 0, 36, 40, 0, 44, 44, 0, 48, 0, 52, 52, 0, 56, 0, 0, 70, 0, 100]
prop_rentHouse1 = [0, 10, 0, 20, 0, 0, 30, 0, 30, 40, 0, 50, 0, 50, 60, 0, 70, 0, 70, 80, 0, 90, 0, 90, 100, 0, 110, 110, 0, 120, 0, 130, 130, 0, 150, 0, 0, 175, 0, 200]
prop_rentHouse2 = [0, 30, 0, 60, 0, 0, 90, 0, 90, 100, 0, 150, 0, 150, 180, 0, 200, 0, 200, 220, 0, 250, 0, 250, 300, 0, 330, 330, 0, 360, 0, 390, 390, 0, 450, 0, 0, 500, 0, 600]
prop_rentHouse3 = [0, 90, 0, 180, 0, 0, 270, 0, 270, 300, 0, 450, 0, 450, 500, 0, 550, 0, 550, 600, 0, 700, 0, 700, 750, 0, 800, 800, 0, 850, 0, 900, 900, 0, 1000, 0, 0, 1100, 0, 1400]
prop_rentHouse4 = [0, 160, 0, 320, 0, 0, 400, 0, 400, 450, 0, 625, 0, 625, 700, 0, 750, 0, 750, 800, 0, 875, 0, 875, 925, 0, 975, 975, 0, 1025, 0, 1100, 1100, 0, 1200, 0, 0, 1300, 0, 1700]
prop_rentHouse5 = [0, 250, 0, 450, 0, 0, 550, 0, 550, 600, 0, 750, 0, 750, 900, 0, 950, 0, 950, 1000, 0, 1050, 0, 1050, 1100, 0, 1150, 1150, 0, 1200, 0, 1275, 1275, 0, 1400, 0, 0, 1500, 0, 2000]
prop_mortprices = [0, 30, 0, 30, 0, 100, 50, 0, 50, 60, 0, 70, 75, 70, 80, 100, 90, 0, 90, 100, 0, 110, 0, 110, 120, 100, 130, 130, 75, 140, 0, 150, 150, 0, 160, 100, 0, 175, 0, 200]
current_prop = prop_list[0]
current_turn = 0
def Go2Go():
    global current_player, player_cash, player_positions
    print("Chance Card: Advance token to GO. Collect $200.")
    player_cash[current_player] += 200
    print("You got $200 for passing GO.")
    print(f"{current_player} now has ${player_cash[current_player]}.")
    player_positions[current_player] = 0
    movetile = player_positions[current_player]
    tile_list[movetile]()
def Go2Illinois():
    global current_player, player_cash, player_positions
    print("Chance Card: Advance token to Illinois Ave.")
    print("If you pass GO, collect $200.")
    if player_positions[current_player] > 24 or player_positions[current_player] <= 24:
        if player_positions[current_player] > 24 and player_positions[current_player] <= 39:
            player_cash[current_player] += 200
            print("You got $200 for passing GO.")
            print(f"{current_player} now has ${player_cash[current_player]}.")
        player_positions[current_player] = 24
        movetile = player_positions[current_player]
        tile_list[movetile]()
def Go2St():
    global current_player, player_cash, player_positions
    print("Chance Card: Advance token to St. Charles Place.")
    print("If you pass GO, collect $200.")
    if player_positions[current_player] > 11 or player_positions[current_player] <= 11:
        if player_positions[current_player] > 11 and player_positions[current_player] <= 39:
            player_cash[current_player] += 200
            print("You got $200 for passing GO.")
            print(f"{current_player} now has ${player_cash[current_player]}.")
        player_positions[current_player] = 11
        movetile = player_positions[current_player]
        tile_list[movetile]()
def Go2Util():
    global current_player, player_cash, player_positions, ChanceMovement
    print("Chance Card: Advance token to nearest Utility. If unowned, you may buy it from the Bank.")
    print("If owned, throw dice and pay owner a total ten times the amount thrown.")
    print("If you pass GO, collect $200.")
    if player_positions[current_player] > 28 or player_positions[current_player] <= 12:
        if player_positions[current_player] > 28 and player_positions[current_player] <= 39:
            player_cash[current_player] += 200
            print("You got $200 for passing GO.")
            print(f"{current_player} now has ${player_cash[current_player]}.")
        player_positions[current_player] = 12
        movetile = player_positions[current_player]
        ChanceMovement = True
        tile_list[movetile]()
    if player_positions[current_player] <= 28 and player_positions[current_player] > 12:
        player_positions[current_player] = 28
        movetile = player_positions[current_player]
        ChanceMovement = True
        tile_list[movetile]()
def Go2Rail():
    global current_player, player_cash, player_positions, tile_list, movetile
    print("Chance Card: Advance token to the nearest Railroad and pay owner twice the rental to which they are otherwise entitled.")
    print("If Railroad is unowned, you may buy it from the Bank.")
    print("If you pass GO, collect $200.")
    if player_positions[current_player] > 35 or player_positions[current_player] <= 5:
        if player_positions[current_player] > 35 and player_positions[current_player] <= 39:
            player_cash[current_player] += 200
            print("You got $200 for passing GO.")
            print(f"{current_player} now has ${player_cash[current_player]}.")
        player_positions[current_player] = 5
        movetile = player_positions[current_player]
        tile_list[movetile]()
        tile_list[movetile]()
    elif player_positions[current_player] > 5 and player_positions[current_player] <= 15:
        player_positions[current_player] = 15
        movetile = player_positions[current_player]
        tile_list[movetile]()
        tile_list[movetile]()
    elif player_positions[current_player] > 15 and player_positions[current_player] <= 25:
        player_positions[current_player] = 25
        movetile = player_positions[current_player]
        tile_list[movetile]()
        tile_list[movetile]()
    elif player_positions[current_player] > 25 and player_positions[current_player] <= 35:
        player_positions[current_player] = 35
        movetile = player_positions[current_player]
        tile_list[movetile]()
        tile_list[movetile]()
def Go2Reading():
    global current_player, player_cash, player_positions, tile_list, movetile
    print("Chance Card: Advance token to Reading Railroad.")
    print("If you pass GO, collect $200.")
    if player_positions[current_player] <= 39:
        player_cash[current_player] += 200
        print("You got $200 for passing GO.")
        print(f"{current_player} now has ${player_cash[current_player]}.")
    player_positions[current_player] = 5
    movetile = player_positions[current_player]
    tile_list[movetile]()
def Go2BW():
    global current_player, player_cash, player_positions
    print("Chance Card: Advance token to Boardwalk.")
    player_positions[current_player] = 39
    movetile = player_positions[current_player]
    tile_list[movetile]()
def Get50():
    global current_player, player_cash
    player_cash[current_player] += 50
    print("Chance Card: Bank pays you dividend of $50.")
    print(f"{current_player} now has ${player_cash[current_player]}.")
def GOOJF():
    global current_player, player_cash, player_list, player_GOOJF
    player_GOOJF[current_player] += 1
    print("Chance Card: Get Out Of Jail Free!")
def Back3():
    global current_player, player_cash, player_positions
    print("Chance Card: Move token back three spaces.")
    player_positions[current_player] -= 3
    movetile = player_positions[current_player]
    tile_list[movetile]()
def Jail():
    print("Chance Card: Go to Jail.")
    print("Go DIRECTLY to Jail.")
    print("Do NOT pass GO, do NOT collect $200.")
    Jail()
def Repairs():
    global current_player, player_cash, prop_list, player_prop, prop_house
    propcheck = -1
    for i in range(40):
        propcheck += 1
        if prop_list[propcheck] in player_prop:
            housecount = prop_house[propcheck]
            if housecount == 5:
                player_cash[current_player] -= 100
            else:
                player_cash[current_player] -= 25 * housecount
    print("Chance Card: Make general repairs on all your properties.")
    print("Pay $25 per house and $100 per hotel.")
    print(f"{current_player} now has ${player_cash[current_player]}.")
def Poor15():
    global current_player, player_cash
    player_cash[current_player] -= 15
    print("Chance Card: Pay poor tax of $15.")
    print(f"{current_player} now has ${player_cash[current_player]}.")
def Pay50PerP():
    global current_player, player_cash, player_list
    perperson = len(player_list)
    playercost = -1
    for player in player_list:
        playercost += 1
        player_cash[player_list[playercost]] += 50
    player_cash[current_player] -= perperson * 50
    print("Chance Card: You've been elected Chairman of the Board.")
    print("Pay each player $50.")
    print(f"{current_player} now has ${player_cash[current_player]}.")
def Get150():
    global current_player, player_cash
    player_cash[current_player] += 150
    print("Chance Card: Your building and loan matures.")
    print("Collect $150.")
    print(f"{current_player} now has ${player_cash[current_player]}.")
def Get100():
    global current_player, player_cash
    player_cash[current_player] += 100
    print("Chance Card: You have won a crossword competition.")
    print("Collect $100.")
    print(f"{current_player} now has ${player_cash[current_player]}.")
ChanceCards = [Go2Go, Go2Illinois, Go2St, Go2Util, Go2Rail, Go2Reading, Go2BW, Get50, GOOJF, Back3, Jail, Repairs, Poor15, Pay50PerP, Get150, Get100]
ChanceCardsList = ['Go2Go', 'Go2Illinois', 'Go2St', 'Go2Util', 'Go2Rail', 'Go2Reading', 'Go2BW', 'Get50', 'GOOJF', 'Back3', 'Jail', 'Repairs', 'Poor15', 'Pay50PerP', 'Get150', 'Get100']
def Chance():
    random.choice(ChanceCards)()
def CCGo2GO():
    global current_player, player_cash, player_positions
    print("Community Chest: Advance token to GO. Collect $200.")
    player_cash[current_player] += 200
    print("You got $200 for passing GO.")
    print(f"{current_player} now has ${player_cash[current_player]}.")
    player_positions[current_player] = 0
    movetile = player_positions[current_player]
    tile_list[movetile]()
def CCGet200():
    global current_player, player_cash
    player_cash[current_player] += 200
    print("Community Chest: Bank error in your favor.")
    print("Collect $200.")
    print(f"{current_player} now has ${player_cash[current_player]}.")
def CCLose50():
    global current_player, player_cash
    player_cash[current_player] -= 50
    print("Community Chest: Doctor's fee.")
    print("Pay $50.")
    print(f"{current_player} now has ${player_cash[current_player]}.")
def CCGet50():
    global current_player, player_cash
    player_cash[current_player] += 50
    print("Community Chest: From sale of stock you get $50.")
    print(f"{current_player} now has ${player_cash[current_player]}.")
def CCGOOJF():
    global current_player, player_cash, player_list, player_GOOJF
    player_GOOJF[current_player] += 1
    print("Community Chest: Get Out Of Jail Free!")
def CCJail():
    global current_player
    print("Community Chest: Go to Jail.")
    print("Go DIRECTLY to Jail.")
    print("Do NOT pass GO, do NOT collect $200.")
    Jail()
def CCGet50PerP():
    global current_player, player_cash, player_list
    perperson = len(player_list)
    playercost = -1
    for player in player_list:
        playercost += 1
        player_cash[player_list[playercost]] -= 50
    player_cash[current_player] += perperson * 50
    print("Community Chest: Grand Opera Night.")
    print("Collect $50 from every player for opening night seats.")
    print(f"{current_player} now has ${player_cash[current_player]}.")
def CCGet100():
    global current_player, player_cash
    player_cash[current_player] += 100
    print("Community Chest: Holiday Fund matures.")
    print("Receive $100.")
    print(f"{current_player} now has ${player_cash[current_player]}.")
def CCGet20():
    global current_player, player_cash
    player_cash[current_player] += 20
    print("Community Chest: Income tax refund.")
    print("Collect $20.")
    print(f"{current_player} now has ${player_cash[current_player]}.")
def CCGet100Life():
    global current_player, player_cash
    player_cash[current_player] += 100
    print("Community Chest: Life insurance matures.")
    print("Collect $100.")
    print(f"{current_player} now has ${player_cash[current_player]}.")
def CCGet10():
    global current_player, player_cash
    player_cash[current_player] += 10
    print("Community Chest: Its your birthday!")
    print("Collect $10.")
    print(f"{current_player} now has ${player_cash[current_player]}.")
def CCLose100():
    global current_player, player_cash
    player_cash[current_player] -= 100
    print("Community Chest: Pay hospital fees of $100.")
    print(f"{current_player} now has ${player_cash[current_player]}.")
def CCLose150():
    global current_player, player_cash
    player_cash[current_player] -= 150
    print("Community Chest: Pay school fees of $150.")
    print(f"{current_player} now has ${player_cash[current_player]}.")
def CCGet25():
    global current_player, player_cash
    player_cash[current_player] -= 25
    print("Community Chest: Receive $25 consultancy fee.")
    print(f"{current_player} now has ${player_cash[current_player]}.")
def CCRepairs():
    global current_player, player_cash, prop_list, player_prop, prop_house
    propcheck = -1
    for i in range(40):
        propcheck += 1
        if prop_list[propcheck] in player_prop:
            housecount = prop_house[propcheck]
            if housecount == 5:
                player_cash[current_player] -= 115
            else:
                player_cash[current_player] -= 40 * housecount
    print("Community Chest: You are assessed for street repairs.")
    print("Pay $40 per house and $115 per hotel.")
def CCGet10Pretty():
    global current_player, player_cash
    player_cash[current_player] += 10
    print("Community Chest: You have won second prize in a beauty contest.")
    print("Collect $10.")
def CCGet100Inherit():
    global current_player, player_cash
    print("Community Chest: You inherit $100")
    player_cash[current_player] += 100   
CCCards = [CCGo2GO, CCGet200, CCLose50, CCGet50, CCGOOJF, CCJail, CCGet50PerP, CCGet100, CCGet20, CCGet100Life, CCGet10, CCLose100, CCLose150, CCGet25, CCRepairs, CCGet10Pretty, CCGet100Inherit]
CCCardsList = ['CCGo2GO', 'CCGet200', 'CCLose50', 'CCGet50', 'CCGOOJF', 'CCJail', 'CCGet50PerP', 'CCGet100', 'CCGet20', 'CCGet100Life', 'CCGet10', 'CCLose100', 'CCLose150', 'CCGet25', 'CCRepairs', 'CCGet10Pretty', 'CCGet100Inherit']
def CommChest():
    random.choice(CCCards)()
def BankruptCheck():
    if player_cash[current_player] < 0:
        print("You Are Bankrupt.")
        ActionBank()
def CheckNetWorth():
    global check, networth, player_prop, current_player, prop_list, prop_house
    check = -1
    networth[current_player] = 0
    for i in range(40):
        check += 1
        if prop_list[check] in player_prop[current_player]:
            networth[current_player] += int(prop_prices[check])
            networth[current_player] += int(prop_house[check]) * int(house_prices[check])
    networth[current_player] += int(player_cash[current_player])            
def DetermineOwner():
    global player, player_list, owned_prop, player_prop, current_prop, paid_player
    for player in player_list:
        if current_prop in player_prop[player]:
            paid_player = player
            print(f"{current_prop} is owned by {paid_player}.")
def CheckOwned():
    global ownedU, ownedRR, player_list, current_player, player_prop, prop_list
    ownedU[current_player] = 0
    ownedRR[current_player] = 0
    if prop_list[12] in player_prop[current_player]:
        ownedU[current_player] += 1
    if prop_list[28] in player_prop[current_player]:
        ownedU[current_player] += 1
    if prop_list[5] in player_prop[current_player]:
        ownedRR[current_player] += 1
    if prop_list[15] in player_prop[current_player]:
        ownedRR[current_player] += 1
    if prop_list[25] in player_prop[current_player]:
        ownedRR[current_player] += 1
    if prop_list[35] in player_prop[current_player]:
        ownedRR[current_player] += 1
    
def MonopolyCheck():
    global player_prop, sortedprop, current_player, monopolyDB, monopolyDP, monopolyG, monopolyLB, monopolyLP, monopolyO, monopolyR, monopolyY, OrangeMon, RedMon, YellowMon, LightBlueMon, LightPurpleMon, GreenMon, DarkPurpleMon, DarkBlueMon
    if monopolyDB[0] in player_prop[current_player] and monopolyDB[1] in player_prop[current_player]:
        DarkBlueMon[current_player] = True
    else:
        DarkBlueMon[current_player] = False
    if monopolyDP[0] in player_prop[current_player] and monopolyDP[1] in player_prop[current_player]:
        DarkPurpleMon[current_player] = True
    else:
        DarkPurpleMon[current_player] = False
    if monopolyG[0] in player_prop[current_player] and monopolyG[1] in player_prop[current_player] and monopolyG[2] in player_prop[current_player]:
        GreenMon[current_player] = True
    else:
        GreenMon[current_player] = False
    if monopolyLB[0] in player_prop[current_player] and monopolyLB[1] in player_prop[current_player] and monopolyLB[2] in player_prop[current_player]:
        LightBlueMon[current_player] = True
    else:
        LightBlueMon[current_player] = False
    if monopolyLP[0] in player_prop[current_player] and monopolyLP[1] in player_prop[current_player] and monopolyLP[2] in player_prop[current_player]:
        LightPurpleMon[current_player] = True
    else:
        LightPurpleMon[current_player] = False
    if monopolyO[0] in player_prop[current_player] and monopolyO[1] in player_prop[current_player] and monopolyO[2] in player_prop[current_player]:
        OrangeMon[current_player] = True
    else:
        OrangeMon[current_player] = False
    if monopolyR[0] in player_prop[current_player] and monopolyR[1] in player_prop[current_player] and monopolyR[2] in player_prop[current_player]:
        RedMon[current_player] = True
    else:
        RedMon[current_player] = False
    if monopolyY[0] in player_prop[current_player] and monopolyY[1] in player_prop[current_player] and monopolyY[2] in player_prop[current_player]:
        YellowMon[current_player] = True
    else:
        YellowMon[current_player] = False
def DetermineRent():
    global ChanceMovement, current_player, globalmove, player, player_prop, prop_mort, owned_prop, prop_list, prop_prices, current_prop, current, current_prop, current, rentdue, ownedRR, ownedU, monopolyY, monopolyR, monopolyDB, monopolyDP, monopolyLB, monopolyG, monopolyO, monopolyLP
    CheckOwned()
    if prop_type[current] == 'P':
        if prop_house[current] == 0:
            if prop_list[current] in monopolyDB and monopolyDB[0] in player_prop[paid_player] and monopolyDB[1] in player_prop[paid_player]:
                rentdue = prop_rentHouseMon[current]
            elif prop_list[current] in monopolyDP and monopolyDP[0] in player_prop[paid_player] and monopolyDP[1] in player_prop[paid_player]:
                rentdue = prop_rentHouseMon[current]
            elif prop_list[current] in monopolyG and monopolyG[0] in player_prop[paid_player] and monopolyG[1] in player_prop[paid_player] and monopolyG[2] in player_prop[paid_player]:
                rentdue = prop_rentHouseMon[current]
            elif prop_list[current] in monopolyLB and monopolyLB[0] in player_prop[paid_player] and monopolyLB[1] in player_prop[paid_player] and monopolyLB[2] in player_prop[paid_player]:
                rentdue = prop_rentHouseMon[current]
            elif prop_list[current] in monopolyLP and monopolyLP[0] in player_prop[paid_player] and monopolyLP[1] in player_prop[paid_player] and monopolyLP[2] in player_prop[paid_player]:
                rentdue = prop_rentHouseMon[current]
            elif prop_list[current] in monopolyO and monopolyO[0] in player_prop[paid_player] and monopolyO[1] in player_prop[paid_player] and monopolyO[2] in player_prop[paid_player]:
                rentdue = prop_rentHouseMon[current]
            elif prop_list[current] in monopolyR and monopolyR[0] in player_prop[paid_player] and monopolyR[1] in player_prop[paid_player] and monopolyR[2] in player_prop[paid_player]:
                rentdue = prop_rentHouseMon[current]
            elif prop_list[current] in monopolyY and monopolyY[0] in player_prop[paid_player] and monopolyY[1] in player_prop[paid_player] and monopolyY[2] in player_prop[paid_player]:
                rentdue = prop_rentHouseMon[current]
            else:
                rentdue = prop_rentHouse0[current]
        elif prop_house[current] == 1:
            rentdue = prop_rentHouse1[current]
        elif prop_house[current] == 2:
            rentdue = prop_rentHouse2[current]
        elif prop_house[current] == 3:
            rentdue = prop_rentHouse3[current]
        elif prop_house[current] == 4:
            rentdue = prop_rentHouse4[current]
        elif prop_house[current] == 5:
            rentdue = prop_rentHouse5[current]
    elif prop_type[current] == 'RR':
        rentdue = 25 * ownedRR[paid_player]
    elif prop_type[current] == 'U':
        if ChanceMovement == True:
            rroll1 = random.randint(1, 6)
            rroll2 = random.randint(1, 6)
            rrolls = rroll1 + rroll2
            print(f"You rolled a {rroll1} and a {rroll2}.")
            rentdue = 10 * rrolls
            ChanceMovement = False
        else:
            if ownedU[paid_player] == 1:
                rentdue = 4 * globalmove
            elif ownedU[paid_player] == 2:
                rentdue = 10 * globalmove
    Rent()
def Rent():
    global player_cash, player, rentdue, paid_player, current_player
    player_cash[current_player] -= rentdue
    player_cash[paid_player] += rentdue
    print(f"{current_player} paid {paid_player} ${rentdue}.")
    print(f"{current_player} has ${player_cash[current_player]}.")
    rentdue = 0
    BankruptCheck()
def BuyProp():
    global player, player_cash, player_prop, owned_prop, current_player, current_prop, prop_prices, prop_owner, networth
    player_cash[current_player] -= prop_prices[current]
    player_prop[current_player].append(current_prop)
    prop_owner[current] = current_player
    owned_prop.append(current_prop)
    print(f"{current_player} purchased {current_prop} for ${prop_prices[current]}.")
    print(f"{current_player} now has ${player_cash[current_player]}.")
    BankruptCheck()
def RefuseProp():
    print(f"{current_player} passed up the opportunity to purchase {current_prop}.")
def Tile0():
    global current_player, player, player_prop, owned_prop, prop_list, prop_prices, current_prop, current
    print("You landed on GO")
    current = 0
    current_prop = prop_list[current]
def Tile1():
    global current_player, player, player_prop, owned_prop, prop_list, prop_prices, current_prop, current, prop_list, prop_prices, current_prop, current
    print("You landed on Mediterranean Avenue(DP)")
    current = 1
    current_prop = prop_list[current]
    if current_prop in owned_prop and current_prop not in player_prop[current_player]:
        if prop_mort[current]:
            print("This Property Is Mortgaged")
        elif not prop_mort[current]:
            DetermineOwner()
            DetermineRent()
    elif current_prop not in owned_prop:
        buying = input(f"Do you want to buy {current_prop}? for ${prop_prices[current]} (Y/N) ")
        if buying == "yes" or buying == "y":
            BuyProp()
        elif buying == "no" or buying == "n":
            RefuseProp()
        else:
            Tile1()
    elif current_prop in player_prop[current_player]:
        print("You own this property")           
def Tile2():
    global current_player, player, player_prop, owned_prop, prop_list, prop_prices, current_prop, current
    print("You landed on Community Chest")
    current = 2
    current_prop = prop_list[current]
    random.choice(CCCards)()
    BankruptCheck()
def Tile3():
    global current_player, player, player_prop, owned_prop, prop_list, prop_prices, current_prop, current, prop_list, prop_prices, current_prop, current
    print("You landed on Baltic Avenue(DP)")
    current = 3
    current_prop = prop_list[current]
    if current_prop in owned_prop and current_prop not in player_prop[current_player]:
        if prop_mort[current]:
            print("This Property Is Mortgaged")
        elif not prop_mort[current]:
            DetermineOwner()
            DetermineRent()
    elif current_prop not in owned_prop:
        buying = input(f"Do you want to buy {current_prop}? for ${prop_prices[current]} (Y/N) ")
        if buying == "yes" or buying == "y":
            BuyProp()
        elif buying == "no" or buying == "n":
            RefuseProp()
        else:
            Tile3()
    elif current_prop in player_prop[current_player]:
        print("You own this property")
def Tile4():
    global current_player, player, player_prop, owned_prop, prop_list, prop_prices, current_prop, current, prop_list, prop_prices, current_prop, current, networth
    print("You landed on Income Tax")
    current = 4
    current_prop = prop_list[current]
    CheckNetWorth()
    itax = input("Do you want to pay a flat $200 or 10 percent of your net worth? (F/P) ").lower()
    if itax == "flat" or itax == "f":
        player_cash[current_player] -= 200
        print(f"You now have {player_cash[current_player]}.")
    elif itax == "percent" or itax == "p":
        CheckNetWorth()
        tax = 0.1 * networth[current_player]
        player_cash[current_player] -= tax
        print(f"Your net worth is {networth[current_player]}.")
        print(f"You paid {tax}.")
        print(f"You now have {player_cash[current_player]}.")
    else:
        print("Invalid Input")
        Tile4()
    BankruptCheck()        
def Tile5():
    global current_player, player, player_prop, owned_prop, prop_list, prop_prices, current_prop, current, prop_list, prop_prices, current_prop, current
    print("You landed on Reading Railroad(RR)")
    current = 5
    current_prop = prop_list[current]
    if current_prop in owned_prop and current_prop not in player_prop[current_player]:
        if prop_mort[current]:
            print("This Property Is Mortgaged")
        elif not prop_mort[current]:
            DetermineOwner()
            DetermineRent()
    elif current_prop not in owned_prop:
        buying = input(f"Do you want to buy {current_prop}? for ${prop_prices[current]} (Y/N) ")
        if buying == "yes" or buying == "y":
            BuyProp()
        elif buying == "no" or buying == "n":
            RefuseProp()
        else:
            Tile5()
    elif current_prop in player_prop[current_player]:
        print("You own this property")
def Tile6():
    global current_player, player, player_prop, owned_prop, prop_list, prop_prices, current_prop, current, prop_list, prop_prices, current_prop, current
    print("You landed on Oriental Avenue(LB)")
    current = 6
    current_prop = prop_list[current]
    if current_prop in owned_prop and current_prop not in player_prop[current_player]:
        if prop_mort[current]:
            print("This Property Is Mortgaged")
        elif not prop_mort[current]:
            DetermineOwner()
            DetermineRent()
    elif current_prop not in owned_prop:
        buying = input(f"Do you want to buy {current_prop}? for ${prop_prices[current]} (Y/N) ")
        if buying == "yes" or buying == "y":
            BuyProp()
        elif buying == "no" or buying == "n":
            RefuseProp()
        else:
            Tile6()
    elif current_prop in player_prop[current_player]:
        print("You own this property")
def Tile7():
    global current_player, player, player_prop, owned_prop, prop_list, prop_prices, current_prop, current, prop_list, prop_prices, current_prop, current
    print("You landed on Chance")
    current = 7
    current_prop = prop_list[current]
    random.choice(ChanceCards)()
    BankruptCheck()
def Tile8():
    global current_player, player, player_prop, owned_prop, prop_list, prop_prices, current_prop, current, prop_list, prop_prices, current_prop, current
    print("You landed on Vermont Avenue(LB)")
    current = 8
    current_prop = prop_list[current]
    if current_prop in owned_prop and current_prop not in player_prop[current_player]:
        if prop_mort[current]:
            print("This Property Is Mortgaged")
        elif not prop_mort[current]:
            DetermineOwner()
            DetermineRent()
    elif current_prop not in owned_prop:
        buying = input(f"Do you want to buy {current_prop}? for ${prop_prices[current]} (Y/N) ")
        if buying == "yes" or buying == "y":
            BuyProp()
        elif buying == "no" or buying == "n":
            RefuseProp()
        else:
            Tile8()
    elif current_prop in player_prop[current_player]:
        print("You own this property")
def Tile9():
    global current_player, player, player_prop, owned_prop, prop_list, prop_prices, current_prop, current, prop_list, prop_prices, current_prop, current
    print("You landed on Connecticut Avenue(LB)")
    current = 9
    current_prop = prop_list[current]
    if current_prop in owned_prop and current_prop not in player_prop[current_player]:
        if prop_mort[current]:
            print("This Property Is Mortgaged")
        elif not prop_mort[current]:
            DetermineOwner()
            DetermineRent()
    elif current_prop not in owned_prop:
        buying = input(f"Do you want to buy {current_prop}? for ${prop_prices[current]} (Y/N) ")
        if buying == "yes" or buying == "y":
            BuyProp()
        elif buying == "no" or buying == "n":
            RefuseProp()
        else:
            Tile9()
    elif current_prop in player_prop[current_player]:
        print("You own this property")
def Tile10():
    global current_player, player, player_prop, owned_prop, prop_list, prop_prices, current_prop, current, prop_list, prop_prices, current_prop, current
    print("You landed on Just Visiting")
    current = 10
    current_prop = prop_list[current]
def Tile11():
    global current_player, player, player_prop, owned_prop, prop_list, prop_prices, current_prop, current, prop_list, prop_prices, current_prop, current
    print("You landed on St. Charles Place(LP)")
    current = 11
    current_prop = prop_list[current]
    if current_prop in owned_prop and current_prop not in player_prop[current_player]:
        if prop_mort[current]:
            print("This Property Is Mortgaged")
        elif not prop_mort[current]:
            DetermineOwner()
            DetermineRent()
    elif current_prop not in owned_prop:
        buying = input(f"Do you want to buy {current_prop}? for ${prop_prices[current]} (Y/N) ")
        if buying == "yes" or buying == "y":
            BuyProp()
        elif buying == "no" or buying == "n":
            RefuseProp()
        else:
            Tile11()
    elif current_prop in player_prop[current_player]:
        print("You own this property")
def Tile12():
    global current_player, player, player_prop, owned_prop, prop_list, prop_prices, current_prop, current, prop_list, prop_prices, current_prop, current
    print("You landed on Electric Company(U)")
    current = 12
    current_prop = prop_list[current]
    if current_prop in owned_prop and current_prop not in player_prop[current_player]:
        if prop_mort[current]:
            print("This Property Is Mortgaged")
        elif not prop_mort[current]:
            DetermineOwner()
            DetermineRent()
    elif current_prop not in owned_prop:
        buying = input(f"Do you want to buy {current_prop}? for ${prop_prices[current]} (Y/N) ")
        if buying == "y" or buying == "yes":
            BuyProp()
        elif buying == "no" or buying == "n":
            RefuseProp()
        else:
            Tile12()
    elif current_prop in player_prop[current_player]:
        print("You own this property")
def Tile13():
    global current_player, player, player_prop, owned_prop, prop_list, prop_prices, current_prop, current, prop_list, prop_prices, current_prop, current
    print("You landed on States Avenue(LP)")
    current = 13
    current_prop = prop_list[current]
    if current_prop in owned_prop and current_prop not in player_prop[current_player]:
        if prop_mort[current]:
            print("This Property Is Mortgaged")
        elif not prop_mort[current]:
            DetermineOwner()
            DetermineRent()
    elif current_prop not in owned_prop:
        buying = input(f"Do you want to buy {current_prop}? for ${prop_prices[current]} (Y/N) ")
        if buying == "yes" or buying == "y":
            BuyProp()
        elif buying == "no" or buying == "n":
            RefuseProp()
        else:
            Tile13()
    elif current_prop in player_prop[current_player]:
        print("You own this property")
def Tile14():
    global current_player, player, player_prop, owned_prop, prop_list, prop_prices, current_prop, current, prop_list, prop_prices, current_prop, current
    print("You landed on Virginia Avenue(LP)")
    current = 14
    current_prop = prop_list[current]
    if current_prop in owned_prop and current_prop not in player_prop[current_player]:
        if prop_mort[current]:
            print("This Property Is Mortgaged")
        elif not prop_mort[current]:
            DetermineOwner()
            DetermineRent()
    elif current_prop not in owned_prop:
        buying = input(f"Do you want to buy {current_prop}? for ${prop_prices[current]} (Y/N) ")
        if buying == "yes" or buying == "y":
            BuyProp()
        elif buying == "no" or buying == "n":
            RefuseProp()
        else:
            Tile14()
    elif current_prop in player_prop[current_player]:
        print("You own this property")
def Tile15():
    global current_player, player, player_prop, owned_prop, prop_list, prop_prices, current_prop, current, prop_list, prop_prices, current_prop, current
    print("You landed on Pennsylvania Railroad(RR)")
    current = 15
    current_prop = prop_list[current]
    if current_prop in owned_prop and current_prop not in player_prop[current_player]:
        if prop_mort[current]:
            print("This Property Is Mortgaged")
        elif not prop_mort[current]:
            DetermineOwner()
            DetermineRent()
    elif current_prop not in owned_prop:
        buying = input(f"Do you want to buy {current_prop}? for ${prop_prices[current]} (Y/N) ")
        if buying == "yes" or buying == "y":
            BuyProp()
        elif buying == "no" or buying == "n":
            RefuseProp()
        else:
            Tile15()
    elif current_prop in player_prop[current_player]:
        print("You own this property")
def Tile16():
    global current_player, player, player_prop, owned_prop, prop_list, prop_prices, current_prop, current, prop_list, prop_prices, current_prop, current
    print("You landed on St. James Place(O)")
    current = 16
    current_prop = prop_list[current]
    if current_prop in owned_prop and current_prop not in player_prop[current_player]:
        if prop_mort[current]:
            print("This Property Is Mortgaged")
        elif not prop_mort[current]:
            DetermineOwner()
            DetermineRent()
    elif current_prop not in owned_prop:
        buying = input(f"Do you want to buy {current_prop}? for ${prop_prices[current]} (Y/N) ")
        if buying == "yes" or buying == "y":
            BuyProp()
        elif buying == "no" or buying == "n":
            RefuseProp()
        else:
            Tile16()
    elif current_prop in player_prop[current_player]:
        print("You own this property")
def Tile17():
    global current_player, player, player_prop, owned_prop, prop_list, prop_prices, current_prop, current, prop_list, prop_prices, current_prop, current
    print("You landed on Community Chest")
    current = 17
    current_prop = prop_list[current]
    random.choice(CCCards)()
    BankruptCheck()
def Tile18():
    global current_player, player, player_prop, owned_prop, prop_list, prop_prices, current_prop, current, prop_list, prop_prices, current_prop, current
    print("You landed on Tennessee Avenue(O)")
    current = 18
    current_prop = prop_list[current]
    if current_prop in owned_prop and current_prop not in player_prop[current_player]:
        if prop_mort[current]:
            print("This Property Is Mortgaged")
        elif not prop_mort[current]:
            DetermineOwner()
            DetermineRent()
    elif current_prop not in owned_prop:
        buying = input(f"Do you want to buy {current_prop}? for ${prop_prices[current]} (Y/N) ")
        if buying == "yes" or buying == "y":
            BuyProp()
        elif buying == "no" or buying == "n":
            RefuseProp()
        else:
            Tile18()
    elif current_prop in player_prop[current_player]:
        print("You own this property")
def Tile19():
    global current_player, player, player_prop, owned_prop, prop_list, prop_prices, current_prop, current
    print("You landed on New York Avenue(O)")
    current = 19
    current_prop = prop_list[current]
    if current_prop in owned_prop and current_prop not in player_prop[current_player]:
        if prop_mort[current]:
            print("This Property Is Mortgaged")
        elif not prop_mort[current]:
            DetermineOwner()
            DetermineRent()
    elif current_prop not in owned_prop:
        buying = input(f"Do you want to buy {current_prop}? for ${prop_prices[current]} (Y/N) ")
        if buying == "yes" or buying == "y":
            BuyProp()
        elif buying == "no" or buying == "n":
            RefuseProp()
        else:
            Tile19()
    elif current_prop in player_prop[current_player]:
        print("You own this property")
def Tile20():
    global current_player, player, player_prop, owned_prop, prop_list, prop_prices, current_prop, current
    print("You landed on Free Parking")
    current = 20
    current_prop = prop_list[current]
def Tile21():
    global current_player, player, player_prop, owned_prop, prop_list, prop_prices, current_prop, current
    print("You landed on Kentucky Avenue(R)")
    current = 21
    current_prop = prop_list[current]
    if current_prop in owned_prop and current_prop not in player_prop[current_player]:
        if prop_mort[current]:
            print("This Property Is Mortgaged")
        elif not prop_mort[current]:
            DetermineOwner()
            DetermineRent()
    elif current_prop not in owned_prop:
        buying = input(f"Do you want to buy {current_prop}? for ${prop_prices[current]} (Y/N) ")
        if buying == "yes" or buying == "y":
            BuyProp()
        elif buying == "no" or buying == "n":
            RefuseProp()
        else:
            Tile21()
    elif current_prop in player_prop[current_player]:
        print("You own this property")
def Tile22():
    global current_player, player, player_prop, owned_prop, prop_list, prop_prices, current_prop, current
    print("You landed on Chance")
    current = 22
    current_prop = prop_list[current]
    random.choice(ChanceCards)()
    BankruptCheck()
def Tile23():
    global current_player, player, player_prop, owned_prop, prop_list, prop_prices, current_prop, current
    print("You landed on Indiana Avenue(R)")
    current = 23
    current_prop = prop_list[current]
    if current_prop in owned_prop and current_prop not in player_prop[current_player]:
        if prop_mort[current]:
            print("This Property Is Mortgaged")
        elif not prop_mort[current]:
            DetermineOwner()
            DetermineRent()
    elif current_prop not in owned_prop:
        buying = input(f"Do you want to buy {current_prop}? for ${prop_prices[current]} (Y/N) ")
        if buying == "yes" or buying == "y":
            BuyProp()
        elif buying == "no" or buying == "n":
            RefuseProp()
        else:
            Tile23()
    elif current_prop in player_prop[current_player]:
        print("You own this property")
def Tile24():
    global current_player, player, player_prop, owned_prop, prop_list, prop_prices, current_prop, current
    print("You landed on Illinois Avenue(R)")
    current = 24
    current_prop = prop_list[current]
    if current_prop in owned_prop and current_prop not in player_prop[current_player]:
        if prop_mort[current]:
            print("This Property Is Mortgaged")
        elif not prop_mort[current]:
            DetermineOwner()
            DetermineRent()
    elif current_prop not in owned_prop:
        buying = input(f"Do you want to buy {current_prop}? for ${prop_prices[current]} (Y/N) ")
        if buying == "yes" or buying == "y":
            BuyProp()
        elif buying == "no" or buying == "n":
            RefuseProp()
        else:
            Tile24()
    elif current_prop in player_prop[current_player]:
        print("You own this property")
def Tile25():
    global current_player, player, player_prop, owned_prop, prop_list, prop_prices, current_prop, current
    print("You landed on B&O Railroad(RR)")
    current = 25
    current_prop = prop_list[current]
    if current_prop in owned_prop and current_prop not in player_prop[current_player]:
        if prop_mort[current]:
            print("This Property Is Mortgaged")
        elif not prop_mort[current]:
            DetermineOwner()
            DetermineRent()
    elif current_prop not in owned_prop:
        buying = input(f"Do you want to buy {current_prop}? for ${prop_prices[current]} (Y/N) ")
        if buying == "yes" or buying == "y":
            BuyProp()
        elif buying == "no" or buying == "n":
            RefuseProp()
        else:
            Tile25()
    elif current_prop in player_prop[current_player]:
        print("You own this property")
def Tile26():
    global current_player, player, player_prop, owned_prop, prop_list, prop_prices, current_prop, current
    print("You landed on Atlantic Avenue(Y)")
    current = 26
    current_prop = prop_list[current]
    if current_prop in owned_prop and current_prop not in player_prop[current_player]:
        if prop_mort[current]:
            print("This Property Is Mortgaged")
        elif not prop_mort[current]:
            DetermineOwner()
            DetermineRent()
    elif current_prop not in owned_prop:
        buying = input(f"Do you want to buy {current_prop}? for ${prop_prices[current]} (Y/N) ")
        if buying == "yes" or buying == "y":
            BuyProp()
        elif buying == "no" or buying == "n":
            RefuseProp()
        else:
            Tile26()
    elif current_prop in player_prop[current_player]:
        print("You own this property")
def Tile27():
    global current_player, player, player_prop, owned_prop, prop_list, prop_prices, current_prop, current
    print("You landed on Ventnor Avenue(Y)")
    current = 27
    current_prop = prop_list[current]
    if current_prop in owned_prop and current_prop not in player_prop[current_player]:
        if prop_mort[current]:
            print("This Property Is Mortgaged")
        elif not prop_mort[current]:
            DetermineOwner()
            DetermineRent()
    elif current_prop not in owned_prop:
        buying = input(f"Do you want to buy {current_prop}? for ${prop_prices[current]} (Y/N) ")
        if buying == "yes" or buying == "y":
            BuyProp()
        elif buying == "no" or buying == "n":
            RefuseProp()
        else:
            Tile27()
    elif current_prop in player_prop[current_player]:
        print("You own this property")
def Tile28():
    global current_player, player, player_prop, owned_prop, prop_list, prop_prices, current_prop, current
    print("You landed on Water Works(U)")
    current = 28
    current_prop = prop_list[current]
    if current_prop in owned_prop and current_prop not in player_prop[current_player]:
        if prop_mort[current]:
            print("This Property Is Mortgaged")
        elif not prop_mort[current]:
            DetermineOwner()
            DetermineRent()
    elif current_prop not in owned_prop:
        buying = input(f"Do you want to buy {current_prop}? for ${prop_prices[current]} (Y/N) ")
        if buying == "yes" or buying == "y":
            BuyProp()
        elif buying == "no" or buying == "n":
            RefuseProp()
        else:
            Tile28()
    elif current_prop in player_prop[current_player]:
        print("You own this property")
def Tile29():
    global current_player, player, player_prop, owned_prop, prop_list, prop_prices, current_prop, current
    print("You landed on Marvin Gardens(Y)")
    current = 29
    current_prop = prop_list[current]
    if current_prop in owned_prop and current_prop not in player_prop[current_player]:
        if prop_mort[current]:
            print("This Property Is Mortgaged")
        elif not prop_mort[current]:
            DetermineOwner()
            DetermineRent()
    elif current_prop not in owned_prop:
        buying = input(f"Do you want to buy {current_prop}? for ${prop_prices[current]} (Y/N) ")
        if buying == "yes" or buying == "y":
            BuyProp()
        elif buying == "no" or buying == "n":
            RefuseProp()
        else:
            Tile29()
    elif current_prop in player_prop[current_player]:
        print("You own this property")
def Tile30():
    global current_player, player, player_prop, owned_prop, prop_list, prop_prices, current_prop, current
    print("You landed on Go To Jail")
    current = 30
    current_prop = prop_list[current]
    Jail()
def Tile31():
    global current_player, player, player_prop, owned_prop, prop_list, prop_prices, current_prop, current
    print("You landed on Pacific Avenue(G)")
    current = 31
    current_prop = prop_list[current]
    if current_prop in owned_prop and current_prop not in player_prop[current_player]:
        if prop_mort[current]:
            print("This Property Is Mortgaged")
        elif not prop_mort[current]:
            DetermineOwner()
            DetermineRent()
    elif current_prop not in owned_prop:
        buying = input(f"Do you want to buy {current_prop}? for ${prop_prices[current]} (Y/N) ")
        if buying == "yes" or buying == "y":
            BuyProp()
        elif buying == "no" or buying == "n":
            RefuseProp()
        else:
            Tile31()
    elif current_prop in player_prop[current_player]:
        print("You own this property")
def Tile32():
    global current_player, player, player_prop, owned_prop, prop_list, prop_prices, current_prop, current
    print("You landed on North Carolina Avenue(G)")
    current = 32
    current_prop = prop_list[current]
    if current_prop in owned_prop and current_prop not in player_prop[current_player]:
        if prop_mort[current]:
            print("This Property Is Mortgaged")
        elif not prop_mort[current]:
            DetermineOwner()
            DetermineRent()
    elif current_prop not in owned_prop:
        buying = input(f"Do you want to buy {current_prop}? for ${prop_prices[current]} (Y/N) ")
        if buying == "yes" or buying == "y":
            BuyProp()
        elif buying == "no" or buying == "n":
            RefuseProp()
        else:
            Tile32()
    elif current_prop in player_prop[current_player]:
        print("You own this property")
def Tile33():
    global current_player, player, player_prop, owned_prop, prop_list, prop_prices, current_prop, current
    print("You landed on Community Chest")
    current = 33
    current_prop = prop_list[current]
    random.choice(CCCards)()
    BankruptCheck()
def Tile34():
    global current_player, player, player_prop, owned_prop, prop_list, prop_prices, current_prop, current
    print("You landed on Pennsylvania Avenue(G)")
    current = 34
    current_prop = prop_list[current]
    if current_prop in owned_prop and current_prop not in player_prop[current_player]:
        if prop_mort[current]:
            print("This Property Is Mortgaged")
        elif not prop_mort[current]:
            DetermineOwner()
            DetermineRent()
    elif current_prop not in owned_prop:
        buying = input(f"Do you want to buy {current_prop}? for ${prop_prices[current]} (Y/N) ")
        if buying == "yes" or buying == "y":
            BuyProp()
        elif buying == "no" or buying == "n":
            RefuseProp()
        else:
            Tile34()
    elif current_prop in player_prop[current_player]:
        print("You own this property")
def Tile35():
    global current_player, player, player_prop, owned_prop, prop_list, prop_prices, current_prop, current
    print("You landed on Short Line Railroad(RR)")
    current = 35
    current_prop = prop_list[current]
    if current_prop in owned_prop and current_prop not in player_prop[current_player]:
        if prop_mort[current]:
            print("This Property Is Mortgaged")
        elif not prop_mort[current]:
            DetermineOwner()
            DetermineRent()
    elif current_prop not in owned_prop:
        buying = input(f"Do you want to buy {current_prop}? for ${prop_prices[current]} (Y/N) ")
        if buying == "yes" or buying == "y":
            BuyProp()
        elif buying == "no" or buying == "n":
            RefuseProp()
        else:
            Tile35()
    elif current_prop in player_prop[current_player]:
        print("You own this property")
def Tile36():
    global current_player, player, player_prop, owned_prop, prop_list, prop_prices, current_prop, current
    print("You landed on Chance")
    current = 36
    current_prop = prop_list[current]
    random.choice(ChanceCards)()
    BankruptCheck()
def Tile37():
    global current_player, player, player_prop, owned_prop, prop_list, prop_prices, current_prop, current
    print("You landed on Park Place(DB)")
    current = 37
    current_prop = prop_list[current]
    if current_prop in owned_prop and current_prop not in player_prop[current_player]:
        if prop_mort[current]:
            print("This Property Is Mortgaged")
        elif not prop_mort[current]:
            DetermineOwner()
            DetermineRent()
    elif current_prop not in owned_prop:
        buying = input(f"Do you want to buy {current_prop}? for ${prop_prices[current]} (Y/N) ")
        if buying == "yes" or buying == "y":
            BuyProp()
        elif buying == "no" or buying == "n":
            RefuseProp()
        else:
            Tile37()
    elif current_prop in player_prop[current_player]:
        print("You own this property")
def Tile38():
    global current_player, player_cash, player, player_prop, owned_prop, prop_list, prop_prices, current_prop, current
    print("You landed on Luxury Tax")
    current = 38
    current_prop = prop_list[current]
    player_cash[current_player] -= 75
    BankruptCheck()
def Tile39():
    global current_player, player, player_prop, owned_prop, prop_list, prop_prices, current_prop, current
    print("You landed on Boardwalk(DB)")
    current = 39
    current_prop = prop_list[current]
    if current_prop in owned_prop and current_prop not in player_prop[current_player]:
        if prop_mort[current]:
            print("This Property Is Mortgaged")
        elif not prop_mort[current]:
            DetermineOwner()
            DetermineRent()
    elif current_prop not in owned_prop:
        buying = input(f"Do you want to buy {current_prop}? for ${prop_prices[current]} (Y/N) ")
        if buying == "yes" or buying == "y":
            BuyProp()
        elif buying == "no" or buying == "n":
            RefuseProp()
        else:
            Tile39()
    elif current_prop in player_prop[current_player]:
        print("You own this property")
def Jail():
    global Double, jailtime
    print("You're going to Jail")
    player_positions[current_player] = 10
    jailtime[current_player] = 1
    player_jail[current_player] = True
    Double = 0
tile_list = [Tile0, Tile1, Tile2, Tile3, Tile4, Tile5, Tile6, Tile7, Tile8, Tile9, Tile10, Tile11, Tile12, Tile13, Tile14, Tile15, Tile16, Tile17, Tile18, Tile19, Tile20, Tile21, Tile22, Tile23, Tile24, Tile25, Tile26, Tile27, Tile28, Tile29, Tile30, Tile31, Tile32, Tile33, Tile34, Tile35, Tile36, Tile37, Tile38, Tile39]
def Debug():
    global player_positions, tile_list, Double, current_player, player, player_cash
    debuginp = input("Debug Action: ").lower()
    if debuginp == "roll" or debuginp == "r":
        if player_jail[current_player]:
            DJRoll()
        else:
            DRoll()
    elif debuginp == "cash" or debuginp == "c":
        addmoney = round(float(input("Add Cash: ")))
        player_cash[current_player] += addmoney
        print(f"{current_player} now has ${player_cash[current_player]}.")
        AskRoll()
    elif debuginp == "other cash" or debuginp == "other" or debuginp == "o" or debuginp == "oc":
        OtherCashDebug()
    elif debuginp == "chance":
        DChance()
    elif debuginp == "cc" or debuginp == "communitychest":
        DCChest()
    else:
        print("Invalid Response")
        return
        AskRoll()
def OtherCashDebug():
    global player_positions, tile_list, Double, current_player, player, player_cash
    try:
        affected = round(float(input("Who's cash is changing? Input '0' for a list of responses. ")))
        effect = affected - 1
        if affected == 0:
            listing = -1
            for i in player_list:
                listing += 1
                print(f"{listing + 1}. {player_list[listing]}")
            OtherCashDebug()
        elif affected <= len(player_list):
            addmoney = round(float(input("Add Cash: ")))
            player_cash[player_list[effect]] += addmoney
            print(f"{player_list[effect]} now has ${player_cash[player_list[effect]]}.")
            AskRoll()
        else:
            print("Input Number Too Large.")
            OtherCashDebug()
    except ValueError:
        print("Input The Number Associated With The Player.")
        OtherCashDebug()
def DJRoll():
    global player_positions, tile_list, Double, current_player, player, roll1, roll2
    if jailtime[current_player] == 3:
        try:
            print("This is your last turn in jail, if you do not roll doubles you must pay a $50 fee")
            roll1 = round(float(input("Roll 1: ")))
            roll2 = round(float(input("Roll 2: ")))
            move = roll1 + roll2
        except ValueError:
            print("Invaid Input")
            DJRoll()
        if roll1 == roll2:
            print(f"{current_player}, you rolled a {roll1} and a {roll2}.")
            print(f"You will move {move} spaces.")
        else:
            player_cash[current_player] -= 50
            print(f"{current_player}, you rolled a {roll1} and a {roll2}.")
            print(f"You will move {move} spaces.")
        jailtime[current_player] = 0
        player_jail[current_player] = False
        player_positions[current_player] += move
        movetile = player_positions[current_player]
        tile_list[movetile]()
    else:
        try:
            roll1 = round(float(input("Roll 1: ")))
            roll2 = round(float(input("Roll 2: ")))
            move = roll1 + roll2
        except ValueError:
            print("Invaid Input")
            DJRoll()
        if roll1 == roll2:
            jailtime[current_player] = 0
            player_jail[current_player] = False
            print(f"{current_player}, you rolled a {roll1} and a {roll2}.")
            print(f"You will move {move} spaces.")
            player_positions[current_player] += move
            movetile = player_positions[current_player]
            tile_list[movetile]()
        else:
            print(f"You rolled a {roll1} and a {roll2}. You need to roll doubles to get out.")
            jailtime[current_player] += 1
    BankruptCheck()
    endturn()
def DRoll():
    global player_positions, tile_list, Double, current_player, player, roll1, roll2, globalmove
    try:
        roll1 = round(float(input("Roll 1: ")))
        roll2 = round(float(input("Roll 2: ")))
        move = roll1 + roll2
        globalmove = move
    except ValueError:
        print("Invaid Input")
        DRoll()
    print(f"{current_player}, you rolled a {roll1} and a {roll2}.")
    player_positions[current_player] += move
    print(f"You will move {move} spaces.")
    if roll1 == roll2:
        Double += 1
        if Double == 3:
            Jail()
            Double = 0
            endturn()
        else:
            print("You rolled doubles! You get to go again!")
    else:
        Double = 0
    if player_positions[current_player] >= len(tile_list):
        player_positions[current_player] = player_positions[current_player] - 40
        player_cash[current_player] += 200
        print("You got $200 for passing GO.")
        print(f"{current_player} now has ${player_cash[current_player]}.") 
    movetile = player_positions[current_player]
    tile_list[movetile]()
    endturn()
def DChance():
    global ChanceCards, ChanceCardsList
    choice = round(float(input("Which chance card? Input '0' for a list of responses. ")))
    try:
        effect = choice - 1
        if choice == 0:
            listing = -1
            for i in ChanceCards:
                listing += 1
                print(f"{listing + 1}. {ChanceCardsList[listing]}")
            DChance()
        elif effect <= len(ChanceCards):
            ChanceCards[effect]()
            AskRoll()
        else:
            print("Input Number Too Large.")
            DChance()
    except ValueError:
        print("Input The Number Associated With The Chance Card.")
        DChance()
def DCChest():
    global CCCards, CCCardsList
    try:
        choice = round(float(input("Which community chest card? Input '0' for a list of responses. ")))
        effect = choice - 1
        if choice == 0:
            listing = -1
            for i in CCCards:
                listing += 1
                print(f"{listing + 1}. {CCCardsList[listing]}")
            DCChest()
        elif effect <= len(CCCards):
            CCCards[effect]()
            AskRoll()
        else:
            print("Input Number Too Large.")
            DCChest()
    except ValueError:
        print("Input The Number Associated With The Community Chest Card.")
        DCChest()
def BuyHouse():
    global numDP, numLB, numLP, numO, numR, numY, numG, numDB, current_player, OrangeMon, RedMon, YellowMon, LightBlueMon, LightPurpleMon, GreenMon, DarkPurpleMon, DarkBlueMon, prop_house, monopolyDB, monopolyDP, monopolyG, monopolyLB, monopolyLP, monopolyO, monopolyR, monopolyY
    number = 0
    numDP = -1
    numLB = -1
    numLP = -1
    numO = -1
    numR = -1
    numY = -1
    numG = -1
    numDB = -1
    MonopolyCheck()
    print("Monopolies: ")
    if DarkPurpleMon[current_player] == True:
        number += 1
        numDP = number
        print(f"{number}. Dark Purple")
    if LightBlueMon[current_player] == True:
        number += 1
        numLB = number
        print(f"{number}. Light Blue")
    if LightPurpleMon[current_player] == True:
        number += 1
        numLP = number
        print(f"{number}. Light Purple")
    if OrangeMon[current_player] == True:
        number += 1
        numO = number
        print(f"{number}. Orange")
    if RedMon[current_player] == True:
        number += 1
        numR = number
        print(f"{number}. Red")
    if YellowMon[current_player] == True:
        number += 1
        numY = number
        print(f"{number}. Yellow")
    if GreenMon[current_player] == True:
        number += 1
        numG = number
        print(f"{number}. Green")
    if DarkBlueMon[current_player] == True:
        number += 1
        numDB = number
        print(f"{number}. Dark Blue")
    housing = round(float(input("Which Property Set Do You Want To Buy Houses For? ")))
    if housing == numDP:
        house0 = 1
        house1 = 3
        if prop_house[house0] > 4:
            print(f"{monopolyDP[0]} already has a hotel.")
            housefor0 = 0
        else:
            housefor0 = abs(round(float(input(f"How Many Houses on {monopolyDP[0]}?: "))))
        if prop_house[house1] > 4:
            print(f"{monopolyDP[1]} already has a hotel.")
            housefor1 = 0
        else:
            housefor1 = abs(round(float(input(f"How Many Houses on {monopolyDP[1]}?: "))))
        if housefor0 > 5 or housefor1 > 5:
            print("Too many houses on a single property. Max is 5.")
            BuyHouse()
        else:
            houses = [housefor0 + prop_house[house0], housefor1 + prop_house[house1]]
            sortedhouses = sorted(houses, reverse=True)
            if sortedhouses[0] - sortedhouses[1] <= 1:
                total_house = housefor0 * (house_prices[house0]) + housefor1 * (house_prices[house1])
                sure = input(f"Are you sure you want to spend {total_house} on houses? (Y/N). ").lower()
                if sure == "y":
                    prop_house[house0] += housefor0
                    prop_house[house1] += housefor1
                    player_cash[current_player] -= total_house
                    print(f"You now have ${player_cash[current_player]}.")
                if sure == "n":
                    AskRoll()
            else:
                print("Spread too wide.")
                AskRoll()
    elif housing == numLB:
        house0 = 6
        house1 = 8
        house2 = 9
        if prop_house[house0] > 4:
            print(f"{monopolyLB[0]} already has a hotel.")
            housefor0 = 0
        else:
            housefor0 = abs(round(float(input(f"How Many Houses on {monopolyLB[0]}?: "))))
        if prop_house[house1] > 4:
            print(f"{monopolyLB[1]} already has a hotel.")
            housefor1 = 0
        else:
            housefor1 = abs(round(float(input(f"How Many Houses on {monopolyLB[1]}?: "))))
        if prop_house[house2] > 4:
            print(f"{monopolyLB[2]} already has a hotel.")
            housefor2 = 0
        else:
            housefor2 = abs(round(float(input(f"How Many Houses on {monopolyLB[2]}?: "))))
        if housefor0 > 5 or housefor1 > 5 or housefor2 > 5:
            print("Too many houses on a single property. Max is 5.")
            BuyHouse()
        else:
            houses = [housefor0 + prop_house[house0], housefor1 + prop_house[house1], housefor2 + prop_house[house2]]
            sortedhouses = sorted(houses, reverse=True)
            if sortedhouses[0] - sortedhouses[1] <= 1 and sortedhouses[0] - sortedhouses[2] <= 1:
                total_house = housefor0 * (house_prices[house0]) + housefor1 * (house_prices[house1]) + housefor2 * (house_prices[house2])
                sure = input(f"Are you sure you want to spend {total_house} on houses? (Y/N). ").lower()
                if sure == "y":
                    prop_house[house0] += housefor0
                    prop_house[house1] += housefor1
                    prop_house[house2] += housefor2
                    player_cash[current_player] -= total_house
                    print(f"You now have ${player_cash[current_player]}.")
                if sure == "n":
                    AskRoll()
            else:
                print("Spread too wide.")
                AskRoll()
    elif housing == numLP:
        house0 = 11
        house1 = 13
        house2 = 14
        if prop_house[house0] > 4:
            print(f"{monopolyLP[0]} already has a hotel.")
            housefor0 = 0
        else:
            housefor0 = abs(round(float(input(f"How Many Houses on {monopolyLP[0]}?: "))))
        if prop_house[house1] > 4:
            print(f"{monopolyLP[1]} already has a hotel.")
            housefor1 = 0
        else:
            housefor1 = abs(round(float(input(f"How Many Houses on {monopolyLP[1]}?: "))))
        if prop_house[house2] > 4:
            print(f"{monopolyLP[2]} already has a hotel.")
            housefor2 = 0
        else:
            housefor2 = abs(round(float(input(f"How Many Houses on {monopolyLP[2]}?: "))))
        if housefor0 > 5 or housefor1 > 5 or housefor2 > 5:
            print("Too many houses on a single property. Max is 5.")
            BuyHouse()
        else:
            houses = [housefor0 + prop_house[house0], housefor1 + prop_house[house1], housefor2 + prop_house[house2]]
            sortedhouses = sorted(houses, reverse=True)
            if sortedhouses[0] - sortedhouses[1] <= 1 and sortedhouses[0] - sortedhouses[2] <= 1:
                total_house = housefor0 * (house_prices[house0]) + housefor1 * (house_prices[house1]) + housefor2 * (house_prices[house2])
                sure = input(f"Are you sure you want to spend {total_house} on houses? (Y/N). ").lower()
                if sure == "y":
                    prop_house[house0] += housefor0
                    prop_house[house1] += housefor1
                    prop_house[house2] += housefor2
                    player_cash[current_player] -= total_house
                    print(f"You now have ${player_cash[current_player]}.")
                if sure == "n":
                    AskRoll()
            else:
                print("Spread too wide.")
                AskRoll()
    elif housing == numO:
        house0 = 16
        house1 = 18
        house2 = 19
        if prop_house[house0] > 4:
            print(f"{monopolyO[0]} already has a hotel.")
            housefor0 = 0
        else:
            housefor0 = abs(round(float(input(f"How Many Houses on {monopolyO[0]}?: "))))
        if prop_house[house1] > 4:
            print(f"{monopolyO[1]} already has a hotel.")
            housefor1 = 0
        else:
            housefor1 = abs(round(float(input(f"How Many Houses on {monopolyO[1]}?: "))))
        if prop_house[house2] > 4:
            print(f"{monopolyO[2]} already has a hotel.")
            housefor2 = 0
        else:
            housefor2 = abs(round(float(input(f"How Many Houses on {monopolyO[2]}?: "))))
        if housefor0 > 5 or housefor1 > 5 or housefor2 > 5:
            print("Too many houses on a single property. Max is 5.")
            BuyHouse()
        else:
            houses = [housefor0 + prop_house[house0], housefor1 + prop_house[house1], housefor2 + prop_house[house2]]
            sortedhouses = sorted(houses, reverse=True)
            if sortedhouses[0] - sortedhouses[1] <= 1 and sortedhouses[0] - sortedhouses[2] <= 1:
                total_house = housefor0 * (house_prices[house0]) + housefor1 * (house_prices[house1]) + housefor2 * (house_prices[house2])
                sure = input(f"Are you sure you want to spend {total_house} on houses? (Y/N). ").lower()
                if sure == "y":
                    prop_house[house0] += housefor0
                    prop_house[house1] += housefor1
                    prop_house[house2] += housefor2
                    player_cash[current_player] -= total_house
                    print(f"You now have ${player_cash[current_player]}.")
                if sure == "n":
                    AskRoll()
            else:
                print("Spread too wide.")
                AskRoll()
    elif housing == numR:
        house0 = 21
        house1 = 23
        house2 = 24
        if prop_house[house0] > 4:
            print(f"{monopolyR[0]} already has a hotel.")
            housefor0 = 0
        else:
            housefor0 = abs(round(float(input(f"How Many Houses on {monopolyR[0]}?: "))))
        if prop_house[house1] > 4:
            print(f"{monopolyR[1]} already has a hotel.")
            housefor1 = 0
        else:
            housefor1 = abs(round(float(input(f"How Many Houses on {monopolyR[1]}?: "))))
        if prop_house[house2] > 4:
            print(f"{monopolyR[2]} already has a hotel.")
            housefor2 = 0
        else:
            housefor2 = abs(round(float(input(f"How Many Houses on {monopolyR[2]}?: "))))
        if housefor0 > 5 or housefor1 > 5 or housefor2 > 5:
            print("Too many houses on a single property. Max is 5.")
            BuyHouse()
        else:
            houses = [housefor0 + prop_house[house0], housefor1 + prop_house[house1], housefor2 + prop_house[house2]]
            sortedhouses = sorted(houses, reverse=True)
            if sortedhouses[0] - sortedhouses[1] <= 1 and sortedhouses[0] - sortedhouses[2] <= 1:
                total_house = housefor0 * (house_prices[house0]) + housefor1 * (house_prices[house1]) + housefor2 * (house_prices[house2])
                sure = input(f"Are you sure you want to spend {total_house} on houses? (Y/N). ").lower()
                if sure == "y":
                    prop_house[house0] += housefor0
                    prop_house[house1] += housefor1
                    prop_house[house2] += housefor2
                    player_cash[current_player] -= total_house
                    print(f"You now have ${player_cash[current_player]}.")
                if sure == "n":
                    AskRoll()
            else:
                print("Spread too wide.")
                AskRoll()
    elif housing == numY:
        house0 = 26
        house1 = 27
        house2 = 29
        if prop_house[house0] > 4:
            print(f"{monopolyY[0]} already has a hotel.")
            housefor0 = 0
        else:
            housefor0 = abs(round(float(input(f"How Many Houses on {monopolyY[0]}?: "))))
        if prop_house[house1] > 4:
            print(f"{monopolyY[1]} already has a hotel.")
            housefor1 = 0
        else:
            housefor1 = abs(round(float(input(f"How Many Houses on {monopolyY[1]}?: "))))
        if prop_house[house2] > 4:
            print(f"{monopolyY[2]} already has a hotel.")
            housefor2 = 0
        else:
            housefor2 = abs(round(float(input(f"How Many Houses on {monopolyY[2]}?: "))))
        if housefor0 > 5 or housefor1 > 5 or housefor2 > 5:
            print("Too many houses on a single property. Max is 5.")
            BuyHouse()
        else:
            houses = [housefor0 + prop_house[house0], housefor1 + prop_house[house1], housefor2 + prop_house[house2]]
            sortedhouses = sorted(houses, reverse=True)
            if sortedhouses[0] - sortedhouses[1] <= 1 and sortedhouses[0] - sortedhouses[2] <= 1:
                total_house = housefor0 * (house_prices[house0]) + housefor1 * (house_prices[house1]) + housefor2 * (house_prices[house2])
                sure = input(f"Are you sure you want to spend {total_house} on houses? (Y/N). ").lower()
                if sure == "y":
                    prop_house[house0] += housefor0
                    prop_house[house1] += housefor1
                    prop_house[house2] += housefor2
                    player_cash[current_player] -= total_house
                    print(f"You now have ${player_cash[current_player]}.")
                if sure == "n":
                    AskRoll()
            else:
                print("Spread too wide.")
                AskRoll()
    elif housing == numG:
        house0 = 31
        house1 = 32
        house2 = 34
        if prop_house[house0] > 4:
            print(f"{monopolyG[0]} already has a hotel.")
            housefor0 = 0
        else:
            housefor0 = abs(round(float(input(f"How Many Houses on {monopolyG[0]}?: "))))
        if prop_house[house1] > 4:
            print(f"{monopolyG[1]} already has a hotel.")
            housefor1 = 0
        else:
            housefor1 = abs(round(float(input(f"How Many Houses on {monopolyG[1]}?: "))))
        if prop_house[house2] > 4:
            print(f"{monopolyG[2]} already has a hotel.")
            housefor2 = 0
        else:
            housefor2 = abs(round(float(input(f"How Many Houses on {monopolyG[2]}?: "))))
        if housefor0 > 5 or housefor1 > 5 or housefor2 > 5:
            print("Too many houses on a single property. Max is 5.")
            BuyHouse()
        else:
            houses = [housefor0 + prop_house[house0], housefor1 + prop_house[house1], housefor2 + prop_house[house2]]
            sortedhouses = sorted(houses, reverse=True)
            if sortedhouses[0] - sortedhouses[1] <= 1 and sortedhouses[0] - sortedhouses[2] <= 1:
                total_house = housefor0 * (house_prices[house0]) + housefor1 * (house_prices[house1]) + housefor2 * (house_prices[house2])
                sure = input(f"Are you sure you want to spend {total_house} on houses? (Y/N). ").lower()
                if sure == "y":
                    prop_house[house0] += housefor0
                    prop_house[house1] += housefor1
                    prop_house[house2] += housefor2
                    player_cash[current_player] -= total_house
                    print(f"You now have ${player_cash[current_player]}.")
                if sure == "n":
                    AskRoll()
            else:
                print("Spread too wide.")
                AskRoll()
    elif housing == numDB:
        house0 = 37
        house1 = 39
        if prop_house[house0] > 4:
            print(f"{monopolyDB[0]} already has a hotel.")
            housefor0 = 0
        else:
            housefor0 = abs(round(float(input(f"How Many Houses on {monopolyDB[0]}?: "))))
        if prop_house[house1] > 4:
            print(f"{monopolyDB[1]} already has a hotel.")
            housefor1 = 0
        else:
            housefor1 = abs(round(float(input(f"How Many Houses on {monopolyDB[1]}?: "))))
        if housefor0 > 5 or housefor1 > 5:
            print("Too many houses on a single property. Max is 5.")
            BuyHouse()
        else:
            houses = [housefor0 + prop_house[house0], housefor1 + prop_house[house1]]
            sortedhouses = sorted(houses, reverse=True)
            if sortedhouses[0] - sortedhouses[1] <= 1:
                total_house = housefor0 * (house_prices[house0]) + housefor1 * (house_prices[house1])
                sure = input(f"Are you sure you want to spend {total_house} on houses? (Y/N). ").lower()
                if sure == "y":
                    prop_house[house0] += housefor0
                    prop_house[house1] += housefor1
                    player_cash[current_player] -= total_house
                    print(f"You now have ${player_cash[current_player]}.")
                if sure == "n":
                    AskRoll()
            else:
                print("Spread too wide.")
                AskRoll()
    BankruptCheck()
    AskRoll()
        
        
    
    
    AskRoll()
def SellHouse():
    global numDP, numLB, numLP, numO, numR, numY, numG, numDB, current_player, OrangeMon, RedMon, YellowMon, LightBlueMon, LightPurpleMon, GreenMon, DarkPurpleMon, DarkBlueMon, prop_house, monopolyDB, monopolyDP, monopolyG, monopolyLB, monopolyLP, monopolyO, monopolyR, monopolyY
    number = 0
    numDP = -1
    numLB = -1
    numLP = -1
    numO = -1
    numR = -1
    numY = -1
    numG = -1
    numDB = -1
    MonopolyCheck()
    print("Monopolies with Houses: ")
    if DarkPurpleMon[current_player] == True:
        if prop_house[1] >= 1 or prop_house[3] >= 1:
            number += 1
            numDP = number
            print(f"{number}. Dark Purple")
    if LightBlueMon[current_player] == True:
        if prop_house[6] >= 1 or prop_house[8] >= 1 or prop_house[9] >= 1:
            number += 1
            numLB = number
            print(f"{number}. Light Blue")
    if LightPurpleMon[current_player] == True:
        if prop_house[11] >= 1 or prop_house[13] >= 1 or prop_house[14] >= 1:
            number += 1
            numLP = number
            print(f"{number}. Light Purple")
    if OrangeMon[current_player] == True:
        if prop_house[16] >= 1 or prop_house[18] >= 1 or prop_house[19] >= 1:
            number += 1
            numO = number
            print(f"{number}. Orange")
    if RedMon[current_player] == True:
        if prop_house[21] >= 1 or prop_house[23] >= 1 or prop_house[24] >= 1:
            number += 1
            numR = number
            print(f"{number}. Red")
    if YellowMon[current_player] == True:
        if prop_house[26] >= 1 or prop_house[27] >= 1 or prop_house[29] >= 1:
            number += 1
            numY = number
            print(f"{number}. Yellow")
    if GreenMon[current_player] == True:
        if prop_house[31] >= 1 or prop_house[32] >= 1 or prop_house[34] >= 1:
            number += 1
            numG = number
            print(f"{number}. Green")
    if DarkBlueMon[current_player] == True:
        if prop_house[37] >= 1 or prop_house[39] >= 1:
            number += 1
            numDB = number
            print(f"{number}. Dark Blue")
    housing = round(float(input("Which Property Set Do You Want To Sell Houses For? ")))
    if housing == numDP:
        house0 = 1
        house1 = 3
        print(f"Houses on {prop_list[house0]}: {prop_house[house0]}")
        print(f"Houses on {prop_list[house1]}: {prop_house[house1]}")
        if prop_house[house0] == 0:
            print(f"{monopolyDP[0]} has no houses.")
            housefor0 = 0
        else:
            housefor0 = abs(round(float(input(f"Sell How Many Houses on {monopolyDP[0]}?: "))))
        if prop_house[house1] > 4:
            print(f"{monopolyDP[1]} has no houses.")
            housefor1 = 0
        else:
            housefor1 = abs(round(float(input(f"Sell How Many Houses on {monopolyDP[1]}?: "))))
        if prop_house[house0] - housefor0 < 0 or prop_house[house1] - housefor1 < 0:
            print("You cant have less than 0 houses on a property.")
            SellHouse()
        else:
            houses = [prop_house[house0] - housefor0, prop_house[house1] - housefor1]
            sortedhouses = sorted(houses, reverse=True)
            if sortedhouses[0] - sortedhouses[1] <= 1:
                total_house = .5 * (housefor0 * (house_prices[house0]) + housefor1 * (house_prices[house1]))
                sure = input(f"Are you sure you want to lose {housefor0 + housefor1} houses and recieve ${total_house}? (Y/N). ").lower()
                if sure == "y":
                    prop_house[house0] -= housefor0
                    prop_house[house1] -= housefor1
                    player_cash[current_player] += total_house
                    print(f"You now have ${player_cash[current_player]}.")
                if sure == "n":
                    AskRoll()
            else:
                print("Spread too wide.")
                AskRoll()
    elif housing == numLB:
        house0 = 6
        house1 = 8
        house2 = 9
        if prop_house[house0] > 4:
            print(f"{monopolyLB[0]} has no houses.")
            housefor0 = 0
        else:
            housefor0 = abs(round(float(input(f"How Many Houses on {monopolyLB[0]}?: "))))
        if prop_house[house1] > 4:
            print(f"{monopolyLB[1]} has no houses.")
            housefor1 = 0
        else:
            housefor1 = abs(round(float(input(f"How Many Houses on {monopolyLB[1]}?: "))))
        if prop_house[house2] > 4:
            print(f"{monopolyLB[2]} has no houses.")
            housefor2 = 0
        else:
            housefor2 = abs(round(float(input(f"How Many Houses on {monopolyLB[2]}?: "))))
        if prop_house[house0] - housefor0 < 0 or prop_house[house1] - housefor1 < 0 or prop_house[house2] - housefor2 < 0:
            print("You cant have less than 0 houses on a property.")
            SellHouse()
        else:
            houses = [prop_house[house0] - housefor0, prop_house[house1] - housefor1, prop_house[house2] - housefor1]
            sortedhouses = sorted(houses, reverse=True)
            if sortedhouses[0] - sortedhouses[1] <= 1 and sortedhouses[0] - sortedhouses[2] <= 1:
                total_house = .5 * (housefor0 * (house_prices[house0]) + housefor1 * (house_prices[house1]) + housefor2 * (house_prices[house2]))
                sure = input(f"Are you sure you want to lose {housefor0 + housefor1 + housefor2} houses and recieve ${total_house}? (Y/N). ").lower()
                if sure == "y":
                    prop_house[house0] -= housefor0
                    prop_house[house1] -= housefor1
                    prop_house[house2] -= housefor2
                    player_cash[current_player] += total_house
                    print(f"You now have ${player_cash[current_player]}.")
                if sure == "n":
                    AskRoll()
            else:
                print("Spread too wide.")
                AskRoll()
    elif housing == numLP:
        house0 = 11
        house1 = 13
        house2 = 14
        if prop_house[house0] > 4:
            print(f"{monopolyLP[0]} has no houses.")
            housefor0 = 0
        else:
            housefor0 = abs(round(float(input(f"How Many Houses on {monopolyLP[0]}?: "))))
        if prop_house[house1] > 4:
            print(f"{monopolyLP[1]} has no houses.")
            housefor1 = 0
        else:
            housefor1 = abs(round(float(input(f"How Many Houses on {monopolyLP[1]}?: "))))
        if prop_house[house2] > 4:
            print(f"{monopolyLP[2]} has no houses.")
            housefor2 = 0
        else:
            housefor2 = abs(round(float(input(f"How Many Houses on {monopolyLP[2]}?: "))))
        if prop_house[house0] - housefor0 < 0 or prop_house[house1] - housefor1 < 0 or prop_house[house2] - housefor2 < 0:
            print("You cant have less than 0 houses on a property.")
            SellHouse()
        else:
            houses = [prop_house[house0] - housefor0, prop_house[house1] - housefor1, prop_house[house2] - housefor1]
            sortedhouses = sorted(houses, reverse=True)
            if sortedhouses[0] - sortedhouses[1] <= 1 and sortedhouses[0] - sortedhouses[2] <= 1:
                total_house = .5 * (housefor0 * (house_prices[house0]) + housefor1 * (house_prices[house1]) + housefor2 * (house_prices[house2]))
                sure = input(f"Are you sure you want to lose {housefor0 + housefor1 + housefor2} houses and recieve ${total_house}? (Y/N). ").lower()
                if sure == "y":
                    prop_house[house0] -= housefor0
                    prop_house[house1] -= housefor1
                    prop_house[house2] -= housefor2
                    player_cash[current_player] += total_house
                    print(f"You now have ${player_cash[current_player]}.")
                if sure == "n":
                    AskRoll()
            else:
                print("Spread too wide.")
                AskRoll()
    elif housing == numO:
        house0 = 16
        house1 = 18
        house2 = 19
        if prop_house[house0] > 4:
            print(f"{monopolyO[0]} has no houses.")
            housefor0 = 0
        else:
            housefor0 = abs(round(float(input(f"How Many Houses on {monopolyO[0]}?: "))))
        if prop_house[house1] > 4:
            print(f"{monopolyO[1]} has no houses.")
            housefor1 = 0
        else:
            housefor1 = abs(round(float(input(f"How Many Houses on {monopolyO[1]}?: "))))
        if prop_house[house2] > 4:
            print(f"{monopolyO[2]} has no houses.")
            housefor2 = 0
        else:
            housefor2 = abs(round(float(input(f"How Many Houses on {monopolyO[2]}?: "))))
        if prop_house[house0] - housefor0 < 0 or prop_house[house1] - housefor1 < 0 or prop_house[house2] - housefor2 < 0:
            print("You cant have less than 0 houses on a property.")
            SellHouse()
        else:
            houses = [prop_house[house0] - housefor0, prop_house[house1] - housefor1, prop_house[house2] - housefor1]
            sortedhouses = sorted(houses, reverse=True)
            if sortedhouses[0] - sortedhouses[1] <= 1 and sortedhouses[0] - sortedhouses[2] <= 1:
                total_house = .5 * (housefor0 * (house_prices[house0]) + housefor1 * (house_prices[house1]) + housefor2 * (house_prices[house2]))
                sure = input(f"Are you sure you want to lose {housefor0 + housefor1 + housefor2} houses and recieve ${total_house}? (Y/N). ").lower()
                if sure == "y":
                    prop_house[house0] -= housefor0
                    prop_house[house1] -= housefor1
                    prop_house[house2] -= housefor2
                    player_cash[current_player] += total_house
                    print(f"You now have ${player_cash[current_player]}.")
                if sure == "n":
                    AskRoll()
            else:
                print("Spread too wide.")
                AskRoll()
    elif housing == numR:
        house0 = 21
        house1 = 23
        house2 = 24
        if prop_house[house0] > 4:
            print(f"{monopolyR[0]} has no houses.")
            housefor0 = 0
        else:
            housefor0 = abs(round(float(input(f"How Many Houses on {monopolyR[0]}?: "))))
        if prop_house[house1] > 4:
            print(f"{monopolyR[1]} has no houses.")
            housefor1 = 0
        else:
            housefor1 = abs(round(float(input(f"How Many Houses on {monopolyR[1]}?: "))))
        if prop_house[house2] > 4:
            print(f"{monopolyR[2]} has no houses.")
            housefor2 = 0
        else:
            housefor2 = abs(round(float(input(f"How Many Houses on {monopolyR[2]}?: "))))
        if prop_house[house0] - housefor0 < 0 or prop_house[house1] - housefor1 < 0 or prop_house[house2] - housefor2 < 0:
            print("You cant have less than 0 houses on a property.")
            SellHouse()
        else:
            houses = [prop_house[house0] - housefor0, prop_house[house1] - housefor1, prop_house[house2] - housefor1]
            sortedhouses = sorted(houses, reverse=True)
            if sortedhouses[0] - sortedhouses[1] <= 1 and sortedhouses[0] - sortedhouses[2] <= 1:
                total_house = .5 * (housefor0 * (house_prices[house0]) + housefor1 * (house_prices[house1]) + housefor2 * (house_prices[house2]))
                sure = input(f"Are you sure you want to lose {housefor0 + housefor1 + housefor2} houses and recieve ${total_house}? (Y/N). ").lower()
                if sure == "y":
                    prop_house[house0] -= housefor0
                    prop_house[house1] -= housefor1
                    prop_house[house2] -= housefor2
                    player_cash[current_player] += total_house
                    print(f"You now have ${player_cash[current_player]}.")
                if sure == "n":
                    AskRoll()
            else:
                print("Spread too wide.")
                AskRoll()
    elif housing == numY:
        house0 = 26
        house1 = 27
        house2 = 29
        if prop_house[house0] > 4:
            print(f"{monopolyY[0]} has no houses.")
            housefor0 = 0
        else:
            housefor0 = abs(round(float(input(f"How Many Houses on {monopolyY[0]}?: "))))
        if prop_house[house1] > 4:
            print(f"{monopolyY[1]} has no houses.")
            housefor1 = 0
        else:
            housefor1 = abs(round(float(input(f"How Many Houses on {monopolyY[1]}?: "))))
        if prop_house[house2] > 4:
            print(f"{monopolyY[2]} has no houses.")
            housefor2 = 0
        else:
            housefor2 = abs(round(float(input(f"How Many Houses on {monopolyY[2]}?: "))))
        if prop_house[house0] - housefor0 < 0 or prop_house[house1] - housefor1 < 0 or prop_house[house2] - housefor2 < 0:
            print("You cant have less than 0 houses on a property.")
            SellHouse()
        else:
            houses = [prop_house[house0] - housefor0, prop_house[house1] - housefor1, prop_house[house2] - housefor1]
            sortedhouses = sorted(houses, reverse=True)
            if sortedhouses[0] - sortedhouses[1] <= 1 and sortedhouses[0] - sortedhouses[2] <= 1:
                total_house = .5 * (housefor0 * (house_prices[house0]) + housefor1 * (house_prices[house1]) + housefor2 * (house_prices[house2]))
                sure = input(f"Are you sure you want to lose {housefor0 + housefor1} houses and recieve ${total_house}? (Y/N). ").lower()
                if sure == "y":
                    prop_house[house0] -= housefor0
                    prop_house[house1] -= housefor1
                    prop_house[house2] -= housefor2
                    player_cash[current_player] += total_house
                    print(f"You now have ${player_cash[current_player]}.")
                if sure == "n":
                    AskRoll()
            else:
                print("Spread too wide.")
                AskRoll()
    elif housing == numG:
        house0 = 31
        house1 = 32
        house2 = 34
        if prop_house[house0] > 4:
            print(f"{monopolyG[0]} has no houses.")
            housefor0 = 0
        else:
            housefor0 = abs(round(float(input(f"How Many Houses on {monopolyG[0]}?: "))))
        if prop_house[house1] > 4:
            print(f"{monopolyG[1]} has no houses.")
            housefor1 = 0
        else:
            housefor1 = abs(round(float(input(f"How Many Houses on {monopolyG[1]}?: "))))
        if prop_house[house2] > 4:
            print(f"{monopolyG[2]} has no houses.")
            housefor2 = 0
        else:
            housefor2 = abs(round(float(input(f"How Many Houses on {monopolyG[2]}?: "))))
        if prop_house[house0] - housefor0 < 0 or prop_house[house1] - housefor1 < 0 or prop_house[house2] - housefor2 < 0:
            print("You cant have less than 0 houses on a property.")
            SellHouse()
        else:
            houses = [prop_house[house0] - housefor0, prop_house[house1] - housefor1, prop_house[house2] - housefor1]
            sortedhouses = sorted(houses, reverse=True)
            if sortedhouses[0] - sortedhouses[1] <= 1 and sortedhouses[0] - sortedhouses[2] <= 1:
                total_house = .5 * (housefor0 * (house_prices[house0]) + housefor1 * (house_prices[house1]) + housefor2 * (house_prices[house2]))
                sure = input(f"Are you sure you want to lose {housefor0 + housefor1 + housefor2} houses and recieve ${total_house}? (Y/N). ").lower()
                if sure == "y":
                    prop_house[house0] += housefor0
                    prop_house[house1] += housefor1
                    prop_house[house2] += housefor2
                    player_cash[current_player] -= total_house
                    print(f"You now have ${player_cash[current_player]}.")
                if sure == "n":
                    AskRoll()
            else:
                print("Spread too wide.")
                AskRoll()
    elif housing == numDB:
        house0 = 37
        house1 = 39
        if prop_house[house0] > 4:
            print(f"{monopolyDB[0]} has no houses.")
            housefor0 = 0
        else:
            housefor0 = abs(round(float(input(f"How Many Houses on {monopolyDB[0]}?: "))))
        if prop_house[house1] > 4:
            print(f"{monopolyDB[1]} has no houses.")
            housefor1 = 0
        else:
            housefor1 = abs(round(float(input(f"How Many Houses on {monopolyDB[1]}?: "))))
        if prop_house[house0] - housefor0 < 0 or prop_house[house1] - housefor1 < 0:
            print("You cant have less than 0 houses on a property.")
            SellHouse()
        else:
            houses = [prop_house[house0] - housefor0, prop_house[house1] - housefor1]
            sortedhouses = sorted(houses, reverse=True)
            if sortedhouses[0] - sortedhouses[1] <= 1:
                total_house = .5 * (housefor0 * (house_prices[house0]) + housefor1 * (house_prices[house1]))
                sure = input(f"Are you sure you want to lose {housefor0 + housefor1} houses and recieve ${total_house}? (Y/N). ").lower()
                if sure == "y":
                    prop_house[house0] -= housefor0
                    prop_house[house1] -= housefor1
                    player_cash[current_player] += total_house
                    print(f"You now have ${player_cash[current_player]}.")
                if sure == "n":
                    AskRoll()
            else:
                print("Spread too wide.")
                AskRoll()
    AskRoll()
def Mortgage():
    global prop_list, prop_owner, prop_house, prop_prices, prop_mortprices, prop_mort
    view = -1
    num = 0
    mortlist = []
    mortpricelist = []
    mortbetween = []
    print("Mortgageable Properties")
    for i in range(40):
        view += 1
        if ownable[view] == 1 and prop_list[view] in player_prop[current_player] and prop_house[view] == 0 and prop_mort[view] == False:
            num += 1
            filler = " " * (30 - len(prop_list[view]))
            print(f"{num}. {prop_list[view]}{filler}|${prop_mortprices[view]}")
            mortlist.append(prop_list[view])
            mortpricelist.append(prop_mortprices[view])
            mortbetween.append(view)
    num += 1
    print(f"{num}. Cancel")
    try:
        choice = round(float(input("Choose A Property To Mortgage: ")))
        choicereal = choice - 1
        if choice <= 0 or choice > (len(mortlist) + 1): 
            print("Invalid Response. Please Input The Number Associated With The Property You Want To Mortgage.")
            Mortgage()
        elif choicereal == (len(mortlist) + 1):
            return
            AskRoll()
        else:
            morting = mortbetween[choicereal]
            prop_mort[morting] = True
            player_cash[current_player] += mortpricelist[choicereal]
            print(f"You Mortgaged {mortlist[choicereal]} for ${mortpricelist[choicereal]}.")
            print(f"You Now Have ${player_cash[current_player]}.")
    except ValueError:
        print("Invalid Response. Please Input The Number Associated With The Property You Want To Mortgage.")
        return
    return
def UnMortgage():
    global prop_list, prop_owner, prop_house, prop_prices, prop_mortprices, current_player, player_prop
    view = -1
    num = 0
    mortbetween = []
    mortlist = []
    print("Mortgaged Properties")
    for i in range(40):
        view += 1
        if ownable[view] == 1 and prop_mort[view] == True and prop_owner[view] == current_player:
            num += 1
            filler = " " * (30 - len(prop_list[view]))
            print(f"{num}. {prop_list[view]}{filler}|${prop_prices[view]}")
            mortbetween.append(view)
            mortlist.append(prop_list[view])
    num += 1
    print(f"{num}. Cancel")
    try:
        choice = round(float(input("Choose A Property To Unmortgage: ")))
        choicereal = choice - 1
        if choice <= 0 or choice > (len(mortlist) + 1): 
            print("Invalid Response. Please Input The Number Associated With The Property You Want To Unmortgage.")
            UnMortgage()
        elif choicereal == (len(mortlist) + 1):
            return
            AskRoll()
        else:
            morting = mortbetween[choicereal]
            prop_mort[morting] = False
            player_cash[current_player] -= prop_prices[morting]
            print(f"You Unmortgaged {prop_list[morting]} for ${prop_prices[morting]}.")
            print(f"You Now Have ${player_cash[current_player]}.")
    except ValueError:
        print("Invalid Response. Please Input The Number Associated With The Property You Want To Unmortgage.")
        return
    BankruptCheck()
    return
def Trade():
    global target, player_list, current_player, current_turn, prop_list, player_prop, option_list, give_list, trade_list, cashgive, goojfgive, player_GOOJF, player_cash, cashtrade, goojftrade
    playernum = -1
    listnum = 1
    trader_list = []
    print("0. Cancel")
    for i in range(len(player_list)):
        playernum += 1
        if player_list[playernum] != player_list[current_turn]:
            print(f"{listnum}. {player_list[playernum]}")
            trader_list.append(player_list[playernum])
            listnum += 1
    try:
        choiceplayer = round(float(input("Who Do You Want To Trade With? ")))
        if choiceplayer == 0:
            return
        elif choiceplayer > 0 and choiceplayer <= len(trader_list):
            targetplayer = choiceplayer - 1
            target = trader_list[targetplayer]
            print(f"Trading With {target}.")
        elif choiceplayer > len(trader_list):
            print("Invalid Value")
    except ValueError:
        print("Invalid Value")
    done = False
    option_list = []
    trade_list = []
    while done == False:
        propown = -1
        listprop = 2
        print("0. Cancel")
        print("1. Done")
        for i in range(len(prop_list)):
            propown += 1
            if prop_list[propown] in player_prop[target] and prop_list[propown] not in trade_list:
                if prop_list[propown] in player_prop[target]:
                    print(f"{listprop}. {prop_list[propown]}")
                    listprop += 1
                    option_list.append(prop_list[propown])
        try:
            adding = round(float(input("What Properties Do You Want? ")))
            if adding == 0:
                return
            elif adding == 1:
                done = True
            elif adding >= 2 and adding <= (len(option_list)+ 1):
                added = adding - 2
                trade_list.append(option_list[added])
                option_list = []
            else:
                print("Invalid Value")
        except ValueError:
            print("Invalid Value")
    cashdone = False
    while cashdone == False:
        print(f"{target} has ${player_cash[target]}.")
        try:
            cashtrade = round(float(input("How Much Money Do You Want? ")))
            if cashtrade < 0 or cashtrade > player_cash[target]:
                print("Invalid Value")
                cashtrade = 0
            else:
                cashdone = True
        except ValueError:
            print("Invalid Value")
    goojfdone = False
    while goojfdone == False:
        print(f"{target} has {player_GOOJF[target]} get out of jail free cards.")
        try:
            goojftrade = round(float(input("How Many Do You Want? ")))
            if goojftrade < 0 or goojftrade > player_GOOJF[target]:
                print("Invalid Value")
                goojftrade = 0
            else:
                goojfdone = True
        except ValueError:
            print("Invalid Value")
    Give()
def Give():
    global target, player_list, give_notmort_list, give_mort_list, current_player, current_turn, prop_list, player_prop, option_list, give_list, trade_list, cashgive, goojfgive, player_GOOJF, player_cash, cashtrade, goojftrade
    done = False
    option_list = []
    give_list = []
    give_notmort_list = []
    give_mort_list = []
    while done == False:
        propown = -1
        listprop = 2
        print("0. Cancel")
        print("1. Done")
        for i in range(len(prop_list)):
            propown += 1
            if prop_list[propown] in player_prop[current_player]:
                if prop_house[propown] == 0 and prop_list[propown] not in give_list:
                    if prop_list[propown] in player_prop[current_player]:
                        print(f"{listprop}. {prop_list[propown]}")
                        listprop += 1
                        option_list.append(prop_list[propown])
        try:
            adding = round(float(input("What Properties Do You Want To Give? ")))
            if adding == 0:
                return
            elif adding == 1:
                done = True
            elif adding >= 2 and adding <= (len(option_list)+ 1):
                added = adding - 2
                give_list.append(option_list[added])
                option_list = []
        except ValueError:
            print("Invalid Value")
    cashdone = False
    while cashdone == False:
        print(f"You have ${player_cash[current_player]}.")
        try:
            cashgive = round(float(input("How Much Money Do You Want To Give? ")))
            if cashgive < 0 or cashgive > player_cash[current_player]:
                print("Invalid Value")
                cashgive = 0
            else:
                cashdone = True
        except ValueError:
            print("Invalid Value")
    goojfdone = False
    while goojfdone == False:
        print(f"You have {player_GOOJF[current_player]} get out of jail free cards.")
        try:
            goojfgive = round(float(input("How Many Do You Want To Give? ")))
            if goojfgive < 0 or goojfgive > player_GOOJF[current_player]:
                print("Invalid Value")
                goojftrade = 0
            else:
                goojfdone = True
        except ValueError:
            print("Invalid Value")
    TradeConfirm()
def TradeConfirm():
    global target, player_list, current_player, current_turn, prop_list, player_prop, option_list, give_list, trade_list, cashgive, goojfgive, player_GOOJF, player_cash, cashtrade, goojftrade
    for i in range(75):
        print()
    print("Receiving")
    print(trade_list)
    print(f"{current_player}, Are you sure you want to recieve these properties, ${cashtrade} and {goojftrade} get out of jail free cards?")
    print("Giving")
    print(give_list)
    print(f"And give these properties, ${cashgive} and {goojfgive} get out of jail free cards?")
    conf = False
    while conf == False:
        yn = input("Y/N ").lower()
        if yn == "y" or yn == "yes":
            conf = True
        elif yn == "n" or yn == "no":
            return
        else:
            print("Invalid Response")
    TradeConfirm2()
def TradeConfirm2():
    global target, player_list, current_player, current_turn, prop_list, player_prop, option_list, give_list, trade_list, cashgive, goojfgive, player_GOOJF, player_cash, cashtrade, goojftrade
    for i in range(75):
        print()
    print("Receiving")
    print(give_list)
    print(f"{target}, Are you sure you want to recieve these properties, ${cashgive} and {goojfgive} get out of jail free cards?")
    print("Giving")
    print(trade_list)
    print(f"And give these properties, ${cashtrade} and {goojftrade} get out of jail free cards?")
    conf = False
    while conf == False:
        yn = input("Y/N ").lower()
        if yn == "y" or yn == "yes":
            conf = True
        elif yn == "n" or yn == "no":
            return
        else:
            print("Invalid Response")
    TradeExe()
def TradeExe():
    global target, player_list, trade_mort_list, trade_notmort_list, give_mort_list, give_notmort_list, current_player, current_turn, prop_list, player_prop, option_list, give_list, trade_list, cashgive, goojfgive, player_GOOJF, player_cash, cashtrade, goojftrade
    cpt = -1
    for i in range(len(prop_list)):
        cpt += 1
        if prop_list[cpt] in trade_list:
            prop_owner[cpt] = current_player
        elif prop_list[cpt] in give_list:
            prop_owner[cpt] = target
    player_prop[current_player] += trade_list
    player_prop[target] = [item for item in player_prop[target] if item not in trade_list]
    player_prop[target] += give_list
    player_prop[current_player] = [item for item in player_prop[current_player] if item not in give_list]
    player_cash[current_player] += cashtrade
    player_cash[current_player] -= cashgive
    player_cash[target] += cashgive
    player_cash[target] -= cashtrade
    player_GOOJF[current_player] += goojftrade
    player_GOOJF[current_player] -= goojfgive
    player_GOOJF[target] += goojfgive
    player_GOOJF[target] -= goojftrade
    print("Trade Complete")
    return              
def ViewMyProperties():
    global ownedRR, ownedU, prop_mort, prop_list, prop_owner, prop_house, prop_prices, prop_rentHouse0, prop_rentHouseMon, prop_rentHouse1, prop_rentHouse2, prop_rentHouse3, prop_rentHouse4, prop_rentHouse5
    CheckOwned()
    view = -1
    max = 25
    fillerprop = " " * (25 - len('Property'))
    fillername = " " * (25 - len('Rent'))
    fillerhouse = " " * (7 - len('Houses'))
    print(f"Property{fillerprop}|Rent{fillername}|Houses{fillerhouse}|Mortgaged")
    for i in range(40):
        view += 1
        if prop_mort[view]:
            mortcall = "Y"
        elif not prop_mort[view]:
            mortcall = "N"
        fillerprop = " " * (25 - len(prop_list[view]))
        fillerhouse = " " * (7 - len(str(prop_house[view])))
        if prop_list[view] in player_prop[current_player]:
            if ownable[view] == 1:
                if prop_type[view] == 'P':
                    if prop_house[view] == 0:
                        if prop_list[view] in monopolyDB and monopolyDB in player_prop[current_player]:
                            rent = prop_rentHouseMon[view]
                        elif prop_list[view] in monopolyDP and monopolyDP in player_prop[current_player]:
                            rent = prop_rentHouseMon[view]
                        elif prop_list[view] in monopolyG and monopolyG in player_prop[current_player]:
                            rent = prop_rentHouseMon[view]
                        elif prop_list[view] in monopolyLB and monopolyLB in player_prop[current_player]:
                            rent = prop_rentHouseMon[view]
                        elif prop_list[view] in monopolyLP and monopolyLP in player_prop[current_player]:
                            rent = prop_rentHouseMon[view]
                        elif prop_list[view] in monopolyO and monopolyO in player_prop[current_player]:
                            rent = prop_rentHouseMon[view]
                        elif prop_list[view] in monopolyR and monopolyR in player_prop[current_player]:
                            rent = prop_rentHouseMon[view]
                        elif prop_list[view] in monopolyY and monopolyY in player_prop[current_player]:
                            rent = prop_rentHouseMon[view]
                        else:
                            rent = prop_rentHouse0
                    elif prop_house[view] == 1:
                        rent = prop_rentHouse1
                    elif prop_house[view] == 2:
                        rent = prop_rentHouse2
                    elif prop_house[view] == 3:
                        rent = prop_rentHouse3
                    elif prop_house[view] == 4:
                        rent = prop_rentHouse4
                    elif prop_house[view] == 5:
                        rent = prop_rentHouse5
                    fillername = " " * (24 - len(str(rent[view])))
                    print(f"{prop_list[view]}{fillerprop}|${rent[view]}{fillername}|{prop_house[view]}{fillerhouse}|{mortcall}")
                elif prop_type[view] == 'U':
                    fillerhouse = " " * (7 - len('N/A'))
                    if ownedU[current_player] == 1:
                        fillername = " " * (25 - len('4 x Value of Dice Roll'))
                        print(f"{prop_list[view]}{fillerprop}|4 x Value of Dice Roll{fillername}|N/A{fillerhouse}|{mortcall}")
                    elif ownedU[current_player] == 2:
                        fillername = " " * (25 - len('10 x Value of Dice Roll'))
                        print(f"{prop_list[view]}{fillerprop}|10 x Value of Dice Roll{fillername}|N/A{fillerhouse}|{mortcall}")
                elif prop_type[view] == 'RR':
                    fillerhouse = " " * (7 - len('N/A'))
                    if ownedRR[current_player] == 1:
                        fillername = " " * (25 - len('$25'))
                        print(f"{prop_list[view]}{fillerprop}|$25{fillername}|N/A{fillerhouse}|{mortcall}")
                    elif ownedRR[current_player] == 2:
                        fillername = " " * (25 - len('$50'))
                        print(f"{prop_list[view]}{fillerprop}|$50{fillername}|N/A{fillerhouse}|{mortcall}")
                    elif ownedRR[current_player] == 3:
                        fillername = " " * (25 - len('$100'))
                        print(f"{prop_list[view]}{fillerprop}|$100{fillername}|N/A{fillerhouse}|{mortcall}")
                    elif ownedRR[current_player] == 4:
                        fillername = " " * (25 - len('$200'))
                        print(f"{prop_list[view]}{fillerprop}|$200{fillername}|N/A{fillerhouse}|{mortcall}")
    AskRoll()
def ViewAllProperties():
    global prop_list, prop_owner, prop_house, prop_prices, prop_rentHouse0, prop_rentHouseMon, prop_rentHouse1, prop_rentHouse2, prop_rentHouse3, prop_rentHouse4, prop_rentHouse5
    view = -1
    max = 25
    fillerprop = " " * (25 - len('Property'))
    fillername = " " * (25 - len('Owner'))
    print(f"Property{fillerprop}|Owner{fillername}|Houses")
    for i in range(40):
        view += 1
        fillerprop = " " * (25 - len(prop_list[view]))
        fillername = " " * (25 - len(prop_owner[view]))
        if ownable[view] == 1:
            if prop_type[view] == 'P':
                print(f"{prop_list[view]}{fillerprop}|{prop_owner[view]}{fillername}|{prop_house[view]}")
            elif prop_type[view] == 'U':
                print(f"{prop_list[view]}{fillerprop}|{prop_owner[view]}{fillername}|N/A")
            elif prop_type[view] == 'RR':
                print(f"{prop_list[view]}{fillerprop}|{prop_owner[view]}{fillername}|N/A")
    AskRoll()
def Quit():
    quitting = input("Really Quit? (Y/N)").lower()
    if quitting == "y":
        quit()
    if quitting == "n":
        AskRoll()
    else:
        Quit()
def ActionBank():
    global player_positions, tile_list, Double, player_list, player_cash, current_player
    print("Actions: ")
    print("Sell Houses")
    print("Mortgage")
    print("Trade")
    print("Resign")
    Action = input("What will you do? ").lower()
    if Action == "s" or Action == "sell houses" or Action == "sell":
        SellHouse()
    elif Action == "m" or Action == "mortgage":
        Mortgage()
    elif Action == "t" or Action == "trade":
        Trade()
    elif Action == "r" or Action == "resign":
        Resign()
    BankruptCheck()
def Resign():
    global player_positions, current_turn, tile_list, Double, player_list, player_cash, current_player, player_prop, prop_house, player_mort, prop_list
    removal = -1
    for i in range(40):
        removal += 1
        if prop_list[removal] in player_prop[current_player]:
            prop_house[removal] = 0
            player_prop[current_player].remove(prop_list[removal])
            prop_mort[removal] = False
    player_list.remove(player_list[current_turn])
    if len(player_list) == 1:
        Win()
def Win():
    global player_list
    print(f"{player_list[0]} wins.")
    quit()
def AskRoll():
    global player_positions, tile_list, Double, player_list, player_cash, current_player
    BankruptCheck()
    if player_jail[current_player]:
        print("You are in Jail.")
        Action = input("What do you want to do? (Input '?' for actions) ").lower()
        if Action == "?":
            print("Actions:")
            print("Roll")
            print("Leave Jail")
            print("Buy Houses")
            print("Sell Houses")
            print("Mortgage")
            print("Unmortgage")
            print("Trade")
            print("Owned Properties")
            print("All Properties")
            print("Quit")
            print("Resign")
            print("Save")
            AskRoll()
        elif Action == "l" or Action == "leave":
            LeaveJailRoll()
        elif Action == "r" or Action == "roll":
            JailRoll()
        elif Action == "b" or Action == "buy houses" or Action == "buy":
            BuyHouse()
        elif Action == "s" or Action == "sell houses" or Action == "sell":
            SellHouse()
        elif Action == "m" or Action == "mortgage":
            Mortgage()
            AskRoll()
        elif Action == "u" or Action == "unmortgage":
            UnMortgage()
            AskRoll()
        elif Action == "t" or Action == "trade":
            Trade()
        elif Action == "o" or Action == "owned properties" or Action == "owned":
            ViewMyProperties()
        elif Action == "a" or Action == "all properties" or Action == "all":
            ViewAllProperties()
        elif Action == "q" or Action == "quit":
            Quit()
        elif Action == "resign":
            Resign()
        elif Action == "debug":
            Debug()
        elif Action == "save":
            Save()
        else:
            print("Invalid Input")
            AskRoll()
    else:
        Action = input("What do you want to do? (Input '?' for actions) ").lower()
        if Action == "?":
            print("Actions:")
            print("Roll")
            print("Buy Houses")
            print("Sell Houses")
            print("Mortgage")
            print("Unmortgage")
            print("Trade")
            print("Owned Properties")
            print("All Properties")
            print("Quit")
            print("Save")
            AskRoll()
        elif Action == "r" or Action == "roll":
            Roll()
        elif Action == "b" or Action == "buy houses" or Action == "buy":
            BuyHouse()
        elif Action == "s" or Action == "sell houses" or Action == "sell":
            SellHouse()
        elif Action == "m" or Action == "mortgage":
            Mortgage()
            AskRoll()
        elif Action == "u" or Action == "unmortgage":
            UnMortgage()
            AskRoll()
        elif Action == "t" or Action == "trade":
            Trade()
        elif Action == "o" or Action == "owned properties" or Action == "owned":
            ViewMyProperties()
        elif Action == "a" or Action == "all properties" or Action == "all":
            ViewAllProperties()
        elif Action == "q" or Action == "quit":
            Quit()
        elif Action == "resign":
            Resign()
        elif Action == "debug":
            Debug()
        elif Action == "save":
            Save()
        else:
            print("Invalid Input")
            AskRoll() 
def JailRoll():
    global player_positions, tile_list, Double, current_player, player, roll1, roll2, globalmove
    if jailtime[current_player] == 3:
        print("This is your last turn in jail, if you do not roll doubles you must pay a $50 fee")
        roll1 = random.randint(1, 6)
        roll2 = random.randint(1, 6)
        move = roll1 + roll2
        globalmove = move
        if roll1 == roll2:
            print(f"{current_player}, you rolled a {roll1} and a {roll2}.")
            print(f"You will move {move} spaces.")
        else:
            player_cash[current_player] -= 50
            print(f"{current_player}, you rolled a {roll1} and a {roll2}.")
            print(f"You will move {move} spaces.")
        jailtime[current_player] = 0
        player_jail[current_player] = False
        player_positions[current_player] += move
        movetile = player_positions[current_player]
        tile_list[movetile]()
    else:
        roll1 = random.randint(1, 6)
        roll2 = random.randint(1, 6)
        if roll1 == roll2:
            jailtime[current_player] = 0
            player_jail[current_player] = False
            move = roll1 + roll2
            globalmove = move
            print(f"{current_player}, you rolled a {roll1} and a {roll2}.")
            print(f"You will move {move} spaces.")
            player_positions[current_player] += move
            movetile = player_positions[current_player]
            tile_list[movetile]()
        else:
            print(f"You rolled a {roll1} and a {roll2}. You need to roll doubles to get out.")
            jailtime[current_player] += 1
    BankruptCheck()
    endturn()
def LeaveJailRoll():
    global player_positions, tile_list, Double, current_player, player, player_GOOJF, player_cash
    print(f"You have ${player_cash[current_player]} and {player_GOOJF[current_player]} get out of jail free card(s).")
    leave = input("Do you want to leave with a $50 payment or for free with a get out of jail free card? (P/F/CANCEL) ").lower()
    if leave == "cancel" or leave == "c":
        AskRoll()
    if leave == "f" or leave == "free":
        if player_GOOJF[current_player] > 0:
            player_GOOJF[current_player] -= 1
            jailtime[current_player] = 0
            player_jail[current_player] = False
            AskRoll()
        else:
            print("You don't have a get out of jail free card.")
            LeaveJailRoll()
    elif leave == "pay" or leave == "payment" or leave == "p":
        player_cash[current_player] -= 50
        jailtime[current_player] = 0
        player_jail[current_player] = False
        BankruptCheck()
        AskRoll()
def Roll():
    global player_positions, tile_list, Double, player, current_player, roll1, roll2, globalmove
    roll1 = random.randint(1, 6)
    roll2 = random.randint(1, 6)
    move = roll1 + roll2
    globalmove = move
    print(f"{current_player}, you rolled a {roll1} and a {roll2}.")
    player_positions[current_player] += move
    print(f"You will move {move} spaces.")
    if roll1 == roll2:
        Double += 1
        if Double == 3:
            Jail()
            Double = 0
            endturn()
        else:
            print("You rolled doubles! You get to go again!")
            if player_positions[current_player] >= len(tile_list):
                player_positions[current_player] = player_positions[current_player] - 40
                player_cash[current_player] += 200
                print("You got $200 for passing GO.")
                print(f"{current_player} now has ${player_cash[current_player]}.") 
            movetile = player_positions[current_player]
            tile_list[movetile]()
            endturn()
    else:
        Double = 0
        if player_positions[current_player] >= len(tile_list):
            player_positions[current_player] = player_positions[current_player] - 40
            player_cash[current_player] += 200
            print("You got $200 for passing GO.")
            print(f"{current_player} now has ${player_cash[current_player]}.") 
        movetile = player_positions[current_player]
        tile_list[movetile]()
        endturn()
StartGame()
paid_player = player_list[0]
while True:
    current_player = player_list[current_turn]
    print(f"\nIt's {current_player}'s turn.")
    print(f"You have ${player_cash[current_player]}.")
    printcurrent = player_positions[current_player]
    print(f"You are on {prop_list[printcurrent]}.")
    AskRoll()
    input("Press Enter to continue to the next turn...")
