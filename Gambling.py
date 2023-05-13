import random
import string

for i in range(75):
    print()
jack = False
riggedroll1 = ""
riggedroll2 = ""
riggedroll3 = ""
riggedroll4 = ""
riggedroll5 = ""
riggedroll6 = ""
riggedroll7 = ""
riggedroll8 = ""
riggedroll9 = ""
Rigged = ""
prev = ""
DebugChoice = ""
DebugOutcome = ""
PrevCA = float(0)
turn = float(0)
payout = 0
jackpotmoney = 0
CustomInt = 0
win = False
rollL = None
rollR = None
rollM = None
FreeSpin = 0
Cash = 5000
MachineCash = random.randint(500000, 10000000)
chance_roll = ["Seven", "Cherry", "Cherry", "Cherry", "Cherry", "Cherry", "Lemon", "Lemon", "Lemon", "Lemon", "Lemon", "Orange", "Orange", "Orange", "Orange", "Orange", "Plum", "Plum", "Plum", "Plum", "Plum", "Bell", "Bell", "Bell", "Bar", "Bar", "Bar", "Bar", "Bar", "2Bar", "2Bar", "2Bar", "2Bar", "3Bar", "3Bar", "3Bar", "Diamond", "Diamond", "Watermelon", "Watermelon", "Watermelon", "Grape", "Grape", "Grape", "Grape", "Horseshoe", "Clover", "Horseshoe", "Clover", "Clover", "Horseshoe", "Clover", "Horseshoe", "Heart", "Spade", "Heart", "Spade", "Heart", "Spade", "Heart", "Spade", "LuckySeven", "Jackpot", "Pear", "Pear", "Pear", "Pear", "Nothing", "Nothing", "Nothing"]
SD = ["Seven", "Diamond"]
LF = ["Cherry", "Lemon", "Orange", "Plum"]
B1 = ["Bar"]
B2 = ["2Bar"]
B3 = ["3Bar"]
BW = ["Bell", "Watermelon"]
CH = ["Clover", "Horseshoe"]
M = ["Grape", "Pear", "Heart", "Spade"]
L7 = ["LuckySeven"]
JP = ["Jackpot"]

def DebugC():
    global DebugChoice
    Choices = ["t", "m", "b", "trbl", "brtl"]
    DebugChoice = input("Where Is The Outcome? ").lower()
    if DebugChoice == "?":
        print("T: Top Row")
        print("M: Middle Row")
        print("B: Bottom Row")
        print("TRBL: Diagonal Top Right To Bottom Left")
        print("BRTL: Diagonal Bottom Right To Top Left")
        print("C: Cancel")
        DebugC()
    elif DebugChoice in Choices:
        DebugO()
    elif DebugChoice == "c":
        Choice()
    else:
        print("Invalid Input")
        DebugO()

def DebugM():
    global Cash, CustomAmount, CustomInt
    try:
        CustomAmount = abs(float(input("Custom Bet: ")))
        CustomAmount = round(CustomAmount, 2)
        CustomInt = CustomAmount
        if CustomInt >= 500:
            if Cash >= CustomInt:
                RRoll3()
            else:
                print("Get Some Money Loser.")
                DebugM()
        if CustomInt >= 250 and CustomInt < 500:
            if Cash >= CustomInt:
                RRoll2()
            else:
                print("Get Some Money Loser.")
                DebugM()
        if CustomInt > 0 and CustomInt < 250:
            if Cash >= CustomInt:
                RRoll1()
            else:
                print("Get Some Money Loser.")
                DebugM()
        else:
            print("Invalid Input. Must be a number above 0")
            DebugM()
    except ValueError:
        for i in range(75):
            print()
        print("Invalid Input. Must be a number above 0")
        DebugM()
    for i in range(75):
        print()
    
def DebugO():
    global DebugChoice, Rigged, riggedroll1, riggedroll2, riggedroll3, riggedroll4, riggedroll5, riggedroll6, riggedroll7, riggedroll8, riggedroll9
    DebugOutcome = input("What Goes There? ").lower()
    if DebugOutcome == "?":
        print("Seven")
        print("Diamond")
        print("Cherry")
        print("Lemon")
        print("Orange")
        print("Plum")
        print("Bar")
        print("2Bar")
        print("3Bar")
        print("Bell")
        print("Watermelon")
        print("Clover")
        print("Horseshoe")
        print("Grape")
        print("Pear")
        print("Heart")
        print("Spade")
        print("LuckySeven")
        print("Jackpot")
        print("Nothing")
        DebugO()
    elif DebugOutcome == "seven":
        Rigged = "Seven"
        RiggingStart()
    elif DebugOutcome == "diamond":
        Rigged = "Diamond"
        RiggingStart()
    elif DebugOutcome == "cherry":
        Rigged = "Cherry"
        RiggingStart()
    elif DebugOutcome == "lemon":
        Rigged = "Lemon"
        RiggingStart()
    elif DebugOutcome == "orange":
        Rigged = "Orange"
        RiggingStart()
    elif DebugOutcome == "plum":
        Rigged = "Plum"
        RiggingStart()
    elif DebugOutcome == "bar":
        Rigged = "Bar"
        RiggingStart()
    elif DebugOutcome == "2bar":
        Rigged = "2Bar"
        RiggingStart()
    elif DebugOutcome == "3bar":
        Rigged = "3Bar"
        RiggingStart()
    elif DebugOutcome == "bell":
        Rigged = "Bell"
        RiggingStart()
    elif DebugOutcome == "watermelon":
        Rigged = "Watermelon"
        RiggingStart()
    elif DebugOutcome == "clover":
        Rigged = "Clover"
        RiggingStart()
    elif DebugOutcome == "horseshoe":
        Rigged = "Horseshoe"
        RiggingStart()
    elif DebugOutcome == "grape":
        Rigged = "Grape"
        RiggingStart()
    elif DebugOutcome == "pear":
        Rigged = "Pear"
        RiggingStart()
    elif DebugOutcome == "heart":
        Rigged = "Heart"
        RiggingStart()
    elif DebugOutcome == "spade":
        Rigged = "Spade"
        RiggingStart()
    elif DebugOutcome == "luckyseven":
        Rigged = "LuckySeven"
        RiggingStart()
    elif DebugOutcome == "jackpot":
        Rigged = "Jackpot"
        RiggingStart()
    elif DebugOutcome == "nothing":
        Rigged = "Nothing"
        RiggingStart()
    else:
        print("Invalid Input")
        DebugO()

def RiggingStart():
    global DebugChoice
    if DebugChoice == "t":
        RigT()       
    elif DebugChoice == "m":
        RigM()
    elif DebugChoice == "b":
        RigB()
    elif DebugChoice == "trbl":
        RigTRBL()
    elif DebugChoice == "brtl":
        RigBRTL()
    DebugM()

def RRoll3():
    global rollL, rollR, rollM, Cash, MachineCash, FreeSpin, win, B1, B2, B3, payout, jackpotmoney, CustomInt, turn, jack
    Cash -= CustomInt
    MachineCash += CustomInt
    rollL = riggedL()
    rollR = riggedR()
    rollM = riggedM()
    max_length = 10
    for i in range(75):
        print()
    turn += 1
    print(f"{rollL[0]:<{max_length}} | {rollM[0]:<{max_length}} | {rollR[0]:<{max_length}}")
    print(f"{rollL[1]:<{max_length}} | {rollM[1]:<{max_length}} | {rollR[1]:<{max_length}}")
    print(f"{rollL[2]:<{max_length}} | {rollM[2]:<{max_length}} | {rollR[2]:<{max_length}}")
    if rollL[0] in B1:
        Bar1()
    if rollL[1] in B1:
        Bar1()
    if rollL[2] in B1:
        Bar1()
    if rollM[0] in B1:
        Bar1()
    if rollM[1] in B1:
        Bar1()
    if rollM[2] in B1:
        Bar1()
    if rollR[0] in B1:
        Bar1()
    if rollR[1] in B1:
        Bar1()
    if rollR[2] in B1:
        Bar1()
    if rollL[0] in B2:
        Bar2()
    if rollL[1] in B2:
        Bar2()
    if rollL[2] in B2:
        Bar2()
    if rollM[0] in B2:
        Bar2()
    if rollM[1] in B2:
        Bar2()
    if rollM[2] in B2:
        Bar2()
    if rollR[0] in B2:
        Bar2()
    if rollR[1] in B2:
        Bar2()
    if rollR[2] in B2:
        Bar2()
    if rollL[0] in B3:
        Bar3()
    if rollL[1] in B3:
        Bar3()
    if rollL[2] in B3:
        Bar3()
    if rollM[0] in B3:
        Bar3()
    if rollM[1] in B3:
        Bar3()
    if rollM[2] in B3:
        Bar3()
    if rollR[0] in B3:
        Bar3()
    if rollR[1] in B3:
        Bar3()
    if rollR[2] in B3:
        Bar3()
    if rollL[0] == rollM[0] and rollM[0] == rollR[0]:
        if rollL[0] in SD:
            SevenDiamond()
        if rollL[0] in LF:
            LowFruit()
        if rollL[0] in BW:
            BellWater()
        if rollL[0] in CH:
            Luck()
        if rollL[0] in M:
            Mid()
        if rollL[0] in L7:
            LuckySeven()
        if rollL[0] in JP:
            jack = True
    if rollL[1] == rollM[1] and rollM[1] == rollR[1]:
        if rollL[1] in SD:
            SevenDiamond()
        if rollL[1] in LF:
            LowFruit()
        if rollL[1] in BW:
            BellWater()
        if rollL[1] in CH:
            Luck()
        if rollL[1] in M:
            Mid()
        if rollL[1] in L7:
            LuckySeven()
        if rollL[1] in JP:
            jack = True
    if rollL[2] == rollM[2] and rollM[2] == rollR[2]:
        if rollL[2] in SD:
            SevenDiamond()
        if rollL[2] in LF:
            LowFruit()
        if rollL[2] in BW:
            BellWater()
        if rollL[2] in CH:
            Luck()
        if rollL[2] in M:
            Mid()
        if rollL[2] in L7:
            LuckySeven()
        if rollL[2] in JP:
            jack = True
    if rollL[0] == rollM[1] and rollM[1] == rollR[2]:
        if rollL[0] in SD:
            SevenDiamond()
        if rollL[0] in LF:
            LowFruit()
        if rollL[0] in BW:
            BellWater()
        if rollL[0] in CH:
            Luck()
        if rollL[0] in M:
            Mid()
        if rollL[0] in L7:
            LuckySeven()
        if rollL[0] in JP:
            jack = True
    if rollL[2] == rollM[1] and rollM[1] == rollR[0]:
        if rollL[2] in SD:
            SevenDiamond()
        if rollL[2] in LF:
            LowFruit()
        if rollL[2] in BW:
            BellWater()
        if rollL[2] in CH:
            Luck()
        if rollL[2] in M:
            Mid()
        if rollL[2] in L7:
            LuckySeven()
        if rollL[2] in JP:
            jack = True
    if jack == True:
        payout = MachineCash
        JackpotPayout()
        jack = False
    else:
        payout = payout * CustomInt
        payout = round(payout, 2)
        Cash += payout
        Cash = round(Cash, 2)
        MachineCash -= payout
        MachineCash = round(MachineCash, 2)
    print(f"Payout: ${payout}!")
    Choice()

def RRoll2():
    global rollL, rollR, rollM, Cash, MachineCash, FreeSpin, win, B1, B2, B3, payout, jackpotmoney, CustomInt, turn, jack
    Cash -= CustomInt
    MachineCash += CustomInt
    rollL = riggedL()
    rollR = riggedR()
    rollM = riggedM()
    max_length = 10
    for i in range(75):
        print()
    turn += 1
    print(f"{rollL[0]:<{max_length}} | {rollM[0]:<{max_length}} | {rollR[0]:<{max_length}}")
    print(f"{rollL[1]:<{max_length}} | {rollM[1]:<{max_length}} | {rollR[1]:<{max_length}}")
    print(f"{rollL[2]:<{max_length}} | {rollM[2]:<{max_length}} | {rollR[2]:<{max_length}}")
    if rollL[0] in B1:
        Bar1()
    if rollL[1] in B1:
        Bar1()
    if rollL[2] in B1:
        Bar1()
    if rollM[0] in B1:
        Bar1()
    if rollM[1] in B1:
        Bar1()
    if rollM[2] in B1:
        Bar1()
    if rollR[0] in B1:
        Bar1()
    if rollR[1] in B1:
        Bar1()
    if rollR[2] in B1:
        Bar1()
    if rollL[0] in B2:
        Bar2()
    if rollL[1] in B2:
        Bar2()
    if rollL[2] in B2:
        Bar2()
    if rollM[0] in B2:
        Bar2()
    if rollM[1] in B2:
        Bar2()
    if rollM[2] in B2:
        Bar2()
    if rollR[0] in B2:
        Bar2()
    if rollR[1] in B2:
        Bar2()
    if rollR[2] in B2:
        Bar2()
    if rollL[0] in B3:
        Bar3()
    if rollL[1] in B3:
        Bar3()
    if rollL[2] in B3:
        Bar3()
    if rollM[0] in B3:
        Bar3()
    if rollM[1] in B3:
        Bar3()
    if rollM[2] in B3:
        Bar3()
    if rollR[0] in B3:
        Bar3()
    if rollR[1] in B3:
        Bar3()
    if rollR[2] in B3:
        Bar3()
    if rollL[0] == rollM[0] and rollM[0] == rollR[0]:
        if rollL[0] in SD:
            SevenDiamond()
        if rollL[0] in LF:
            LowFruit()
        if rollL[0] in BW:
            BellWater()
        if rollL[0] in CH:
            Luck()
        if rollL[0] in M:
            Mid()
        if rollL[0] in L7:
            LuckySeven()
        if rollL[0] in JP:
            jack = True
    if rollL[1] == rollM[1] and rollM[1] == rollR[1]:
        if rollL[1] in SD:
            SevenDiamond()
        if rollL[1] in LF:
            LowFruit()
        if rollL[1] in BW:
            BellWater()
        if rollL[1] in CH:
            Luck()
        if rollL[1] in M:
            Mid()
        if rollL[1] in L7:
            LuckySeven()
        if rollL[1] in JP:
            jack = True
    if rollL[2] == rollM[2] and rollM[2] == rollR[2]:
        if rollL[2] in SD:
            SevenDiamond()
        if rollL[2] in LF:
            LowFruit()
        if rollL[2] in BW:
            BellWater()
        if rollL[2] in CH:
            Luck()
        if rollL[2] in M:
            Mid()
        if rollL[2] in L7:
            LuckySeven()
        if rollL[2] in JP:
            jack = True
    if jack == True:
        payout = MachineCash
        JackpotPayout()
        jack = False
    else:
        payout = payout * CustomInt
        payout = round(payout, 2)
        Cash += payout
        Cash = round(Cash, 2)
        MachineCash -= payout
        MachineCash = round(MachineCash, 2)
    print(f"Payout: ${payout}!")
    Choice()
def RRoll1():
    global rollL, rollR, rollM, Cash, MachineCash, FreeSpin, win, B1, B2, B3, payout, jackpotmoney, CustomInt, turn, jack
    Cash -= CustomInt
    MachineCash += CustomInt
    rollL = riggedL()
    rollR = riggedR()
    rollM = riggedM()
    max_length = 10
    for i in range(75):
        print()
    turn += 1
    print(f"{rollL[0]:<{max_length}} | {rollM[0]:<{max_length}} | {rollR[0]:<{max_length}}")
    print(f"{rollL[1]:<{max_length}} | {rollM[1]:<{max_length}} | {rollR[1]:<{max_length}}")
    print(f"{rollL[2]:<{max_length}} | {rollM[2]:<{max_length}} | {rollR[2]:<{max_length}}")
    if rollL[1] in B1:
        Bar1()
    if rollL[1] in B2:
        Bar2()
    if rollL[1] in B3:
        Bar3()
    if rollM[1] in B1:
        Bar1()
    if rollM[1] in B2:
        Bar2()
    if rollM[1] in B3:
        Bar3()
    if rollR[1] in B1:
        Bar1()
    if rollR[1] in B2:
        Bar2()
    if rollR[1] in B3:
        Bar3()
    if rollL[1] == rollM[1] and rollM[1] == rollR[1]:
        if rollL[1] in SD:
            SevenDiamond()
        if rollL[1] in LF:
            LowFruit()
        if rollL[1] in BW:
            BellWater()
        if rollL[1] in CH:
            Luck()
        if rollL[1] in M:
            Mid()
        if rollL[1] in L7:
            LuckySeven()
        if rollL[1] in JP:
            jack = True
    if jack == True:
        payout = MachineCash
        JackpotPayout()
        jack = False
    else:
        payout = payout * CustomInt
        payout = round(payout, 2)
        Cash += payout
        Cash = round(Cash, 2)
        MachineCash -= payout
        MachineCash = round(MachineCash, 2)
    print(f"Payout: ${payout}!")
    Choice()

def RigBRTL():
    global riggedroll1, riggedroll2, riggedroll3, riggedroll4, riggedroll5, riggedroll6, riggedroll7, riggedroll8, riggedroll9
    riggedroll1 = Rigged
    riggedroll2 = random.choice(chance_roll)
    riggedroll3 = random.choice(chance_roll)
    riggedroll4 = random.choice(chance_roll)
    riggedroll5 = Rigged
    riggedroll6 = random.choice(chance_roll)
    riggedroll7 = random.choice(chance_roll)
    riggedroll8 = random.choice(chance_roll)
    riggedroll9 = Rigged
    
def RigTRBL():
    global riggedroll1, riggedroll2, riggedroll3, riggedroll4, riggedroll5, riggedroll6, riggedroll7, riggedroll8, riggedroll9
    riggedroll1 = random.choice(chance_roll)
    riggedroll2 = random.choice(chance_roll)
    riggedroll3 = Rigged
    riggedroll4 = random.choice(chance_roll)
    riggedroll5 = Rigged
    riggedroll6 = random.choice(chance_roll)
    riggedroll7 = Rigged
    riggedroll8 = random.choice(chance_roll)
    riggedroll9 = random.choice(chance_roll)
    
def RigB():
    global riggedroll1, riggedroll2, riggedroll3, riggedroll4, riggedroll5, riggedroll6, riggedroll7, riggedroll8, riggedroll9
    riggedroll1 = random.choice(chance_roll)
    riggedroll2 = random.choice(chance_roll)
    riggedroll3 = random.choice(chance_roll)
    riggedroll4 = random.choice(chance_roll)
    riggedroll5 = random.choice(chance_roll)
    riggedroll6 = random.choice(chance_roll)
    riggedroll7 = Rigged
    riggedroll8 = Rigged
    riggedroll9 = Rigged
    
def RigM():
    global riggedroll1, riggedroll2, riggedroll3, riggedroll4, riggedroll5, riggedroll6, riggedroll7, riggedroll8, riggedroll9
    riggedroll1 = random.choice(chance_roll)
    riggedroll2 = random.choice(chance_roll)
    riggedroll3 = random.choice(chance_roll)
    riggedroll4 = Rigged
    riggedroll5 = Rigged
    riggedroll6 = Rigged
    riggedroll7 = random.choice(chance_roll)
    riggedroll8 = random.choice(chance_roll)
    riggedroll9 = random.choice(chance_roll)

def RigT():
    global riggedroll1, riggedroll2, riggedroll3, riggedroll4, riggedroll5, riggedroll6, riggedroll7, riggedroll8, riggedroll9
    riggedroll1 = Rigged
    riggedroll2 = Rigged
    riggedroll3 = Rigged
    riggedroll4 = random.choice(chance_roll)
    riggedroll5 = random.choice(chance_roll)
    riggedroll6 = random.choice(chance_roll)
    riggedroll7 = random.choice(chance_roll)
    riggedroll8 = random.choice(chance_roll)
    riggedroll9 = random.choice(chance_roll)

def StartGame():
    global FreeSpin, Cash, MachineCash, prev, DebugChoice
    prev = ""
    DebugChoice = ""
    PrevCA = float(0)
    turn = 0
    payout = 0
    FreeSpin = 0
    Cash = 5000
    MachineCash = random.randint(500000, 10000000)
    Choice()
def SevenDiamond():
    #Seven Diamond
    global Cash, MachineCash, payout
    payout += 20

def LowFruit():
    #Cherry Lemon Orange Plum
    global Cash, MachineCash, payout
    payout += 3

def Bar1():
    #Bar
    global Cash, MachineCash, payout
    payout += .1

def Bar2():
    #Bar2
    global Cash, MachineCash, payout
    payout += .5

def Bar3():
    #Bar3
    global Cash, MachineCash, payout
    payout += 1

def BellWater():
    #Bell Watermelon
    global Cash, MachineCash, payout
    payout += 8

def Luck():
    #Clover Horseshoe
    global FreeSpin
    FreeSpin += 2
    print("You Got 2 FREE SPINS!")

def Mid():
    #Grape #Pear #Heart #Spade
    global Cash, MachineCash, payout
    payout += 5

def LuckySeven():
    #LuckySeven
    global Cash, MachineCash, payout
    payout += 200
    
def JackpotPayout():
    global MachineCash, Cash, jackpotmoney
    jackpotmoney = MachineCash
    Cash += jackpotmoney
    MachineCash -= jackpotmoney

def riggedL():
    global riggedroll1, riggedroll4, riggedroll7
    return riggedroll1, riggedroll4, riggedroll7
def riggedR():
    global riggedroll3, riggedroll6, riggedroll9
    return riggedroll3, riggedroll6, riggedroll9
def riggedM():
    global riggedroll2, riggedroll5, riggedroll8
    return riggedroll2, riggedroll5, riggedroll8

def RollL():
    return random.choice(chance_roll), random.choice(chance_roll), random.choice(chance_roll)

def RollR():
    return random.choice(chance_roll), random.choice(chance_roll), random.choice(chance_roll)

def RollM():
    return random.choice(chance_roll), random.choice(chance_roll), random.choice(chance_roll)

def Roll1():
    global rollL, rollR, rollM, Cash, MachineCash, FreeSpin, win, B1, B2, B3, payout, jackpotmoney, turn, jack
    Cash -= 125
    MachineCash += 125
    rollL = RollL()
    rollR = RollR()
    rollM = RollM()
    max_length = 10
    for i in range(75):
        print()
    turn += 1
    print(f"{rollL[0]:<{max_length}} | {rollM[0]:<{max_length}} | {rollR[0]:<{max_length}}")
    print(f"{rollL[1]:<{max_length}} | {rollM[1]:<{max_length}} | {rollR[1]:<{max_length}}")
    print(f"{rollL[2]:<{max_length}} | {rollM[2]:<{max_length}} | {rollR[2]:<{max_length}}")
    if rollL[1] in B1:
        Bar1()
    if rollL[1] in B2:
        Bar2()
    if rollL[1] in B3:
        Bar3()
    if rollM[1] in B1:
        Bar1()
    if rollM[1] in B2:
        Bar2()
    if rollM[1] in B3:
        Bar3()
    if rollR[1] in B1:
        Bar1()
    if rollR[1] in B2:
        Bar2()
    if rollR[1] in B3:
        Bar3()
    if rollL[1] == rollM[1] and rollM[1] == rollR[1]:
        if rollL[1] in SD:
            SevenDiamond()
        if rollL[1] in LF:
            LowFruit()
        if rollL[1] in BW:
            BellWater()
        if rollL[1] in CH:
            Luck()
        if rollL[1] in M:
            Mid()
        if rollL[1] in L7:
            LuckySeven()
        if rollL[1] in JP:
            jack = True
    if jack == True:
        payout = MachineCash
        JackpotPayout()
        jack = False
    else:
        payout = payout * 125
        payout = round(payout, 2)
        Cash += payout
        Cash = round(Cash, 2)
        MachineCash -= payout
        MachineCash = round(MachineCash, 2)
    print(f"Payout: ${payout}!")
    Choice()

def Roll2():
    global rollL, rollR, rollM, Cash, MachineCash, FreeSpin, win, B1, B2, B3, payout, jackpotmoney, turn, jack
    Cash -= 250
    MachineCash += 250
    rollL = RollL()
    rollR = RollR()
    rollM = RollM()
    max_length = 10
    for i in range(75):
        print()
    turn += 1
    print(f"{rollL[0]:<{max_length}} | {rollM[0]:<{max_length}} | {rollR[0]:<{max_length}}")
    print(f"{rollL[1]:<{max_length}} | {rollM[1]:<{max_length}} | {rollR[1]:<{max_length}}")
    print(f"{rollL[2]:<{max_length}} | {rollM[2]:<{max_length}} | {rollR[2]:<{max_length}}")
    if rollL[0] in B1:
        Bar1()
    if rollL[1] in B1:
        Bar1()
    if rollL[2] in B1:
        Bar1()
    if rollM[0] in B1:
        Bar1()
    if rollM[1] in B1:
        Bar1()
    if rollM[2] in B1:
        Bar1()
    if rollR[0] in B1:
        Bar1()
    if rollR[1] in B1:
        Bar1()
    if rollR[2] in B1:
        Bar1()
    if rollL[0] in B2:
        Bar2()
    if rollL[1] in B2:
        Bar2()
    if rollL[2] in B2:
        Bar2()
    if rollM[0] in B2:
        Bar2()
    if rollM[1] in B2:
        Bar2()
    if rollM[2] in B2:
        Bar2()
    if rollR[0] in B2:
        Bar2()
    if rollR[1] in B2:
        Bar2()
    if rollR[2] in B2:
        Bar2()
    if rollL[0] in B3:
        Bar3()
    if rollL[1] in B3:
        Bar3()
    if rollL[2] in B3:
        Bar3()
    if rollM[0] in B3:
        Bar3()
    if rollM[1] in B3:
        Bar3()
    if rollM[2] in B3:
        Bar3()
    if rollR[0] in B3:
        Bar3()
    if rollR[1] in B3:
        Bar3()
    if rollR[2] in B3:
        Bar3()
    if rollL[0] == rollM[0] and rollM[0] == rollR[0]:
        if rollL[0] in SD:
            SevenDiamond()
        if rollL[0] in LF:
            LowFruit()
        if rollL[0] in BW:
            BellWater()
        if rollL[0] in CH:
            Luck()
        if rollL[0] in M:
            Mid()
        if rollL[0] in L7:
            LuckySeven()
        if rollL[0] in JP:
            jack = True
    if rollL[1] == rollM[1] and rollM[1] == rollR[1]:
        if rollL[1] in SD:
            SevenDiamond()
        if rollL[1] in LF:
            LowFruit()
        if rollL[1] in BW:
            BellWater()
        if rollL[1] in CH:
            Luck()
        if rollL[1] in M:
            Mid()
        if rollL[1] in L7:
            LuckySeven()
        if rollL[1] in JP:
            jack = True
    if rollL[2] == rollM[2] and rollM[2] == rollR[2]:
        if rollL[2] in SD:
            SevenDiamond()
        if rollL[2] in LF:
            LowFruit()
        if rollL[2] in BW:
            BellWater()
        if rollL[2] in CH:
            Luck()
        if rollL[2] in M:
            Mid()
        if rollL[2] in L7:
            LuckySeven()
        if rollL[2] in JP:
            jack = True
    if jack == True:
        payout = MachineCash
        JackpotPayout()
        jack = False
    else:
        payout = payout * 250
        payout = round(payout, 2)
        Cash += payout
        Cash = round(Cash, 2)
        MachineCash -= payout
        MachineCash = round(MachineCash, 2)
    print(f"Payout: ${payout}!")
    Choice()

def Roll3():
    global rollL, rollR, rollM, Cash, MachineCash, FreeSpin, win, B1, B2, B3, payout, jackpotmoney, turn, jack
    Cash -= 500
    MachineCash += 500
    rollL = RollL()
    rollR = RollR()
    rollM = RollM()
    max_length = 10
    for i in range(75):
        print()
    turn += 1
    print(f"{rollL[0]:<{max_length}} | {rollM[0]:<{max_length}} | {rollR[0]:<{max_length}}")
    print(f"{rollL[1]:<{max_length}} | {rollM[1]:<{max_length}} | {rollR[1]:<{max_length}}")
    print(f"{rollL[2]:<{max_length}} | {rollM[2]:<{max_length}} | {rollR[2]:<{max_length}}")
    if rollL[0] in B1:
        Bar1()
    if rollL[1] in B1:
        Bar1()
    if rollL[2] in B1:
        Bar1()
    if rollM[0] in B1:
        Bar1()
    if rollM[1] in B1:
        Bar1()
    if rollM[2] in B1:
        Bar1()
    if rollR[0] in B1:
        Bar1()
    if rollR[1] in B1:
        Bar1()
    if rollR[2] in B1:
        Bar1()
    if rollL[0] in B2:
        Bar2()
    if rollL[1] in B2:
        Bar2()
    if rollL[2] in B2:
        Bar2()
    if rollM[0] in B2:
        Bar2()
    if rollM[1] in B2:
        Bar2()
    if rollM[2] in B2:
        Bar2()
    if rollR[0] in B2:
        Bar2()
    if rollR[1] in B2:
        Bar2()
    if rollR[2] in B2:
        Bar2()
    if rollL[0] in B3:
        Bar3()
    if rollL[1] in B3:
        Bar3()
    if rollL[2] in B3:
        Bar3()
    if rollM[0] in B3:
        Bar3()
    if rollM[1] in B3:
        Bar3()
    if rollM[2] in B3:
        Bar3()
    if rollR[0] in B3:
        Bar3()
    if rollR[1] in B3:
        Bar3()
    if rollR[2] in B3:
        Bar3()
    if rollL[0] == rollM[0] and rollM[0] == rollR[0]:
        if rollL[0] in SD:
            SevenDiamond()
        if rollL[0] in LF:
            LowFruit()
        if rollL[0] in BW:
            BellWater()
        if rollL[0] in CH:
            Luck()
        if rollL[0] in M:
            Mid()
        if rollL[0] in L7:
            LuckySeven()
        if rollL[0] in JP:
            jack = True
    if rollL[1] == rollM[1] and rollM[1] == rollR[1]:
        if rollL[1] in SD:
            SevenDiamond()
        if rollL[1] in LF:
            LowFruit()
        if rollL[1] in BW:
            BellWater()
        if rollL[1] in CH:
            Luck()
        if rollL[1] in M:
            Mid()
        if rollL[1] in L7:
            LuckySeven()
        if rollL[1] in JP:
            jack = True
    if rollL[2] == rollM[2] and rollM[2] == rollR[2]:
        if rollL[2] in SD:
            SevenDiamond()
        if rollL[2] in LF:
            LowFruit()
        if rollL[2] in BW:
            BellWater()
        if rollL[2] in CH:
            Luck()
        if rollL[2] in M:
            Mid()
        if rollL[2] in L7:
            LuckySeven()
        if rollL[2] in JP:
            jack = True
    if rollL[0] == rollM[1] and rollM[1] == rollR[2]:
        if rollL[0] in SD:
            SevenDiamond()
        if rollL[0] in LF:
            LowFruit()
        if rollL[0] in BW:
            BellWater()
        if rollL[0] in CH:
            Luck()
        if rollL[0] in M:
            Mid()
        if rollL[0] in L7:
            LuckySeven()
        if rollL[0] in JP:
            jack = True
    if rollL[2] == rollM[1] and rollM[1] == rollR[0]:
        if rollL[2] in SD:
            SevenDiamond()
        if rollL[2] in LF:
            LowFruit()
        if rollL[2] in BW:
            BellWater()
        if rollL[2] in CH:
            Luck()
        if rollL[2] in M:
            Mid()
        if rollL[2] in L7:
            LuckySeven()
        if rollL[2] in JP:
            jack = True
    if jack == True:
        payout = MachineCash
        JackpotPayout()
        jack = False
    else:
        payout = payout * 500
        payout = round(payout, 2)
        Cash += payout
        Cash = round(Cash, 2)
        MachineCash -= payout
        MachineCash = round(MachineCash, 2)
    print(f"Payout: ${payout}!")
    Choice()

def Roll4():
    global rollL, rollR, rollM, Cash, MachineCash, FreeSpin, win, B1, B2, B3, payout, jackpotmoney, CustomInt, turn, jack
    Cash -= CustomInt
    MachineCash += CustomInt
    rollL = RollL()
    rollR = RollR()
    rollM = RollM()
    max_length = 10
    for i in range(75):
        print()
    turn += 1
    print(f"{rollL[0]:<{max_length}} | {rollM[0]:<{max_length}} | {rollR[0]:<{max_length}}")
    print(f"{rollL[1]:<{max_length}} | {rollM[1]:<{max_length}} | {rollR[1]:<{max_length}}")
    print(f"{rollL[2]:<{max_length}} | {rollM[2]:<{max_length}} | {rollR[2]:<{max_length}}")
    if rollL[0] in B1:
        Bar1()
    if rollL[1] in B1:
        Bar1()
    if rollL[2] in B1:
        Bar1()
    if rollM[0] in B1:
        Bar1()
    if rollM[1] in B1:
        Bar1()
    if rollM[2] in B1:
        Bar1()
    if rollR[0] in B1:
        Bar1()
    if rollR[1] in B1:
        Bar1()
    if rollR[2] in B1:
        Bar1()
    if rollL[0] in B2:
        Bar2()
    if rollL[1] in B2:
        Bar2()
    if rollL[2] in B2:
        Bar2()
    if rollM[0] in B2:
        Bar2()
    if rollM[1] in B2:
        Bar2()
    if rollM[2] in B2:
        Bar2()
    if rollR[0] in B2:
        Bar2()
    if rollR[1] in B2:
        Bar2()
    if rollR[2] in B2:
        Bar2()
    if rollL[0] in B3:
        Bar3()
    if rollL[1] in B3:
        Bar3()
    if rollL[2] in B3:
        Bar3()
    if rollM[0] in B3:
        Bar3()
    if rollM[1] in B3:
        Bar3()
    if rollM[2] in B3:
        Bar3()
    if rollR[0] in B3:
        Bar3()
    if rollR[1] in B3:
        Bar3()
    if rollR[2] in B3:
        Bar3()
    if rollL[0] == rollM[0] and rollM[0] == rollR[0]:
        if rollL[0] in SD:
            SevenDiamond()
        if rollL[0] in LF:
            LowFruit()
        if rollL[0] in BW:
            BellWater()
        if rollL[0] in CH:
            Luck()
        if rollL[0] in M:
            Mid()
        if rollL[0] in L7:
            LuckySeven()
        if rollL[0] in JP:
            jack = True
    if rollL[1] == rollM[1] and rollM[1] == rollR[1]:
        if rollL[1] in SD:
            SevenDiamond()
        if rollL[1] in LF:
            LowFruit()
        if rollL[1] in BW:
            BellWater()
        if rollL[1] in CH:
            Luck()
        if rollL[1] in M:
            Mid()
        if rollL[1] in L7:
            LuckySeven()
        if rollL[1] in JP:
            jack = True
    if rollL[2] == rollM[2] and rollM[2] == rollR[2]:
        if rollL[2] in SD:
            SevenDiamond()
        if rollL[2] in LF:
            LowFruit()
        if rollL[2] in BW:
            BellWater()
        if rollL[2] in CH:
            Luck()
        if rollL[2] in M:
            Mid()
        if rollL[2] in L7:
            LuckySeven()
        if rollL[2] in JP:
            jack = True
    if rollL[0] == rollM[1] and rollM[1] == rollR[2]:
        if rollL[0] in SD:
            SevenDiamond()
        if rollL[0] in LF:
            LowFruit()
        if rollL[0] in BW:
            BellWater()
        if rollL[0] in CH:
            Luck()
        if rollL[0] in M:
            Mid()
        if rollL[0] in L7:
            LuckySeven()
        if rollL[0] in JP:
            jack = True
    if rollL[2] == rollM[1] and rollM[1] == rollR[0]:
        if rollL[2] in SD:
            SevenDiamond()
        if rollL[2] in LF:
            LowFruit()
        if rollL[2] in BW:
            BellWater()
        if rollL[2] in CH:
            Luck()
        if rollL[2] in M:
            Mid()
        if rollL[2] in L7:
            LuckySeven()
        if rollL[2] in JP:
            jack = True
    if jack == True:
        payout = MachineCash
        JackpotPayout()
        jack = False
    else:
        payout = payout * CustomInt
        payout = round(payout, 2)
        Cash += payout
        Cash = round(Cash, 2)
        MachineCash -= payout
        MachineCash = round(MachineCash, 2)
    print(f"Payout: ${payout}!")
    Choice()

def Roll5():
    global rollL, rollR, rollM, Cash, MachineCash, FreeSpin, win, B1, B2, B3, payout, jackpotmoney, turn, jack
    FreeSpin -= 1
    rollL = RollL()
    rollR = RollR()
    rollM = RollM()
    max_length = 10
    for i in range(75):
        print()
    turn += 1
    print(f"{rollL[0]:<{max_length}} | {rollM[0]:<{max_length}} | {rollR[0]:<{max_length}}")
    print(f"{rollL[1]:<{max_length}} | {rollM[1]:<{max_length}} | {rollR[1]:<{max_length}}")
    print(f"{rollL[2]:<{max_length}} | {rollM[2]:<{max_length}} | {rollR[2]:<{max_length}}")
    if rollL[0] in B1:
        Bar1()
    if rollL[1] in B1:
        Bar1()
    if rollL[2] in B1:
        Bar1()
    if rollM[0] in B1:
        Bar1()
    if rollM[1] in B1:
        Bar1()
    if rollM[2] in B1:
        Bar1()
    if rollR[0] in B1:
        Bar1()
    if rollR[1] in B1:
        Bar1()
    if rollR[2] in B1:
        Bar1()
    if rollL[0] in B2:
        Bar2()
    if rollL[1] in B2:
        Bar2()
    if rollL[2] in B2:
        Bar2()
    if rollM[0] in B2:
        Bar2()
    if rollM[1] in B2:
        Bar2()
    if rollM[2] in B2:
        Bar2()
    if rollR[0] in B2:
        Bar2()
    if rollR[1] in B2:
        Bar2()
    if rollR[2] in B2:
        Bar2()
    if rollL[0] in B3:
        Bar3()
    if rollL[1] in B3:
        Bar3()
    if rollL[2] in B3:
        Bar3()
    if rollM[0] in B3:
        Bar3()
    if rollM[1] in B3:
        Bar3()
    if rollM[2] in B3:
        Bar3()
    if rollR[0] in B3:
        Bar3()
    if rollR[1] in B3:
        Bar3()
    if rollR[2] in B3:
        Bar3()
    if rollL[0] == rollM[0] and rollM[0] == rollR[0]:
        if rollL[0] in SD:
            SevenDiamond()
        if rollL[0] in LF:
            LowFruit()
        if rollL[0] in BW:
            BellWater()
        if rollL[0] in CH:
            Luck()
        if rollL[0] in M:
            Mid()
        if rollL[0] in L7:
            LuckySeven()
        if rollL[0] in JP:
            jack = True
    if rollL[1] == rollM[1] and rollM[1] == rollR[1]:
        if rollL[1] in SD:
            SevenDiamond()
        if rollL[1] in LF:
            LowFruit()
        if rollL[1] in BW:
            BellWater()
        if rollL[1] in CH:
            Luck()
        if rollL[1] in M:
            Mid()
        if rollL[1] in L7:
            LuckySeven()
        if rollL[1] in JP:
            jack = True
    if rollL[2] == rollM[2] and rollM[2] == rollR[2]:
        if rollL[2] in SD:
            SevenDiamond()
        if rollL[2] in LF:
            LowFruit()
        if rollL[2] in BW:
            BellWater()
        if rollL[2] in CH:
            Luck()
        if rollL[2] in M:
            Mid()
        if rollL[2] in L7:
            LuckySeven()
        if rollL[2] in JP:
            jack = True
    if rollL[0] == rollM[1] and rollM[1] == rollR[2]:
        if rollL[0] in SD:
            SevenDiamond()
        if rollL[0] in LF:
            LowFruit()
        if rollL[0] in BW:
            BellWater()
        if rollL[0] in CH:
            Luck()
        if rollL[0] in M:
            Mid()
        if rollL[0] in L7:
            LuckySeven()
        if rollL[0] in JP:
            jack = True
    if rollL[2] == rollM[1] and rollM[1] == rollR[0]:
        if rollL[2] in SD:
            SevenDiamond()
        if rollL[2] in LF:
            LowFruit()
        if rollL[2] in BW:
            BellWater()
        if rollL[2] in CH:
            Luck()
        if rollL[2] in M:
            Mid()
        if rollL[2] in L7:
            LuckySeven()
        if rollL[2] in JP:
            jack = True
    if jack == True:
        payout = MachineCash
        JackpotPayout()
        jack = False
    else:
        payout = payout * CustomInt
        payout = round(payout, 2)
        Cash += payout
        Cash = round(Cash, 2)
        MachineCash -= payout
        MachineCash = round(MachineCash, 2)
    print(f"Payout: ${payout}!")
    Choice()

def Roll6():
    global rollL, rollR, rollM, Cash, MachineCash, FreeSpin, win, B1, B2, B3, payout, jackpotmoney, CustomInt, turn, jack
    Cash -= CustomInt
    MachineCash += CustomInt
    rollL = RollL()
    rollR = RollR()
    rollM = RollM()
    max_length = 10
    for i in range(75):
        print()
    turn += 1
    print(f"{rollL[0]:<{max_length}} | {rollM[0]:<{max_length}} | {rollR[0]:<{max_length}}")
    print(f"{rollL[1]:<{max_length}} | {rollM[1]:<{max_length}} | {rollR[1]:<{max_length}}")
    print(f"{rollL[2]:<{max_length}} | {rollM[2]:<{max_length}} | {rollR[2]:<{max_length}}")
    if rollL[0] in B1:
        Bar1()
    if rollL[1] in B1:
        Bar1()
    if rollL[2] in B1:
        Bar1()
    if rollM[0] in B1:
        Bar1()
    if rollM[1] in B1:
        Bar1()
    if rollM[2] in B1:
        Bar1()
    if rollR[0] in B1:
        Bar1()
    if rollR[1] in B1:
        Bar1()
    if rollR[2] in B1:
        Bar1()
    if rollL[0] in B2:
        Bar2()
    if rollL[1] in B2:
        Bar2()
    if rollL[2] in B2:
        Bar2()
    if rollM[0] in B2:
        Bar2()
    if rollM[1] in B2:
        Bar2()
    if rollM[2] in B2:
        Bar2()
    if rollR[0] in B2:
        Bar2()
    if rollR[1] in B2:
        Bar2()
    if rollR[2] in B2:
        Bar2()
    if rollL[0] in B3:
        Bar3()
    if rollL[1] in B3:
        Bar3()
    if rollL[2] in B3:
        Bar3()
    if rollM[0] in B3:
        Bar3()
    if rollM[1] in B3:
        Bar3()
    if rollM[2] in B3:
        Bar3()
    if rollR[0] in B3:
        Bar3()
    if rollR[1] in B3:
        Bar3()
    if rollR[2] in B3:
        Bar3()
    if rollL[0] == rollM[0] and rollM[0] == rollR[0]:
        if rollL[0] in SD:
            SevenDiamond()
        if rollL[0] in LF:
            LowFruit()
        if rollL[0] in BW:
            BellWater()
        if rollL[0] in CH:
            Luck()
        if rollL[0] in M:
            Mid()
        if rollL[0] in L7:
            LuckySeven()
        if rollL[0] in JP:
            jack = True
    if rollL[1] == rollM[1] and rollM[1] == rollR[1]:
        if rollL[1] in SD:
            SevenDiamond()
        if rollL[1] in LF:
            LowFruit()
        if rollL[1] in BW:
            BellWater()
        if rollL[1] in CH:
            Luck()
        if rollL[1] in M:
            Mid()
        if rollL[1] in L7:
            LuckySeven()
        if rollL[1] in JP:
            jack = True
    if rollL[2] == rollM[2] and rollM[2] == rollR[2]:
        if rollL[2] in SD:
            SevenDiamond()
        if rollL[2] in LF:
            LowFruit()
        if rollL[2] in BW:
            BellWater()
        if rollL[2] in CH:
            Luck()
        if rollL[2] in M:
            Mid()
        if rollL[2] in L7:
            LuckySeven()
        if rollL[2] in JP:
            jack = True
    if jack == True:
        payout = MachineCash
        JackpotPayout()
        jack = False
    else:
        payout = payout * CustomInt
        payout = round(payout, 2)
        Cash += payout
        Cash = round(Cash, 2)
        MachineCash -= payout
        MachineCash = round(MachineCash, 2)
    print(f"Payout: ${payout}!")
    Choice()
def Roll7():
    global rollL, rollR, rollM, Cash, MachineCash, FreeSpin, win, B1, B2, B3, payout, jackpotmoney, CustomInt, turn, jack
    Cash -= CustomInt
    MachineCash += CustomInt
    rollL = RollL()
    rollR = RollR()
    rollM = RollM()
    max_length = 10
    for i in range(75):
        print()
    turn += 1
    print(f"{rollL[0]:<{max_length}} | {rollM[0]:<{max_length}} | {rollR[0]:<{max_length}}")
    print(f"{rollL[1]:<{max_length}} | {rollM[1]:<{max_length}} | {rollR[1]:<{max_length}}")
    print(f"{rollL[2]:<{max_length}} | {rollM[2]:<{max_length}} | {rollR[2]:<{max_length}}")
    if rollL[1] in B1:
        Bar1()
    if rollL[1] in B2:
        Bar2()
    if rollL[1] in B3:
        Bar3()
    if rollM[1] in B1:
        Bar1()
    if rollM[1] in B2:
        Bar2()
    if rollM[1] in B3:
        Bar3()
    if rollR[1] in B1:
        Bar1()
    if rollR[1] in B2:
        Bar2()
    if rollR[1] in B3:
        Bar3()
    if rollL[1] == rollM[1] and rollM[1] == rollR[1]:
        if rollL[1] in SD:
            SevenDiamond()
        if rollL[1] in LF:
            LowFruit()
        if rollL[1] in BW:
            BellWater()
        if rollL[1] in CH:
            Luck()
        if rollL[1] in M:
            Mid()
        if rollL[1] in L7:
            LuckySeven()
        if rollL[1] in JP:
            jack = True
    if jack == True:
        payout = MachineCash
        JackpotPayout()
        jack = False
    else:
        payout = payout * CustomInt
        payout = round(payout, 2)
        Cash += payout
        Cash = round(Cash, 2)
        MachineCash -= payout
        MachineCash = round(MachineCash, 2)
    print(f"Payout: ${payout}!")
    Choice()

def Choice():
    global Cash, MachineCash, FreeSpin, payout, CustomInt, turn, prev, PrevCA
    payout = 0
    print(f"Cash In Machine: {MachineCash}")
    print(f"Your Cash: {Cash}")
    print(f"Your Free Spins: {FreeSpin}")
    bet = input("How much do you want to bet? (Type '?' for a list of answers and their meanings): ").lower()
    if bet == "debug":
        debugcontent = input("Debug Code: ").lower()
        if debugcontent == "debug.addmoney":
            try:
                debugMoney = float(input("Value: "))
                debugMoney = round(int(debugMoney), 2)
                Cash += debugMoney
                for i in range(75):
                    print()
                Choice()
            except ValueError:
                print("Invalid Value.")
                Choice()
        if debugcontent == "debug.addspins":
            try:
                debugSpins = float(input("Value: "))
                debugSpins = round(int(debugSpins))
                FreeSpin += debugSpins
                for i in range(75):
                    print()
                Choice()
            except ValueError:
                print("Invalid Value.")
                Choice()
        if debugcontent == "debug.choose":
            DebugC()
    elif bet == "?":
        print("List of Bets: Low Medium High Custom Reset")
        print("Low: Only middle row counts")
        print("Medium: All rows count")
        print("High: All rows and diagonals count")
        print("Custom: Must be above 0")
        print("Max: Max Bet")
        print("Free: All rows and diagonals count (Must have free spins)")
        print("Reset: Resets all values")
        Choice()
    elif bet == "x" or bet == "max":
        prev = "x"
        CustomAmount = abs(float(Cash))
        CustomAmount = round(CustomAmount, 2)
        CustomInt = CustomAmount
        if CustomInt >= 500:
            Roll4()
        if CustomInt >= 250 and CustomInt < 500:
            Roll6()
        if CustomInt > 0 and CustomInt < 250:
            Roll7()
        if CustomInt == 0:
            for i in range(75):
                print()
            print("You Have No Money")
            Choice()
    elif bet == "/" or bet == "half":
        prev = "/"
        CustomAmount = abs(float(Cash/2))
        CustomAmount = round(CustomAmount, 2)
        CustomInt = CustomAmount
        if CustomInt >= 500:
            Roll4()
        if CustomInt >= 250 and CustomInt < 500:
            Roll6()
        if CustomInt > 0 and CustomInt < 250:
            Roll7()
        if CustomInt == 0:
            for i in range(75):
                print()
            print("You Have No Money")
            Choice()
        Choice()
    elif bet == "" and turn >= 1:
        if prev == "free" or prev == "f":
            if FreeSpin >= 1:
                Roll5()
            else:
                for i in range(75):
                    print()
                print("You Have No Free Spins")
                Choice()
        elif prev == "max" or prev == "x":
            CustomAmount = abs(float(Cash))
            CustomAmount = round(CustomAmount, 2)
            CustomInt = CustomAmount
            if CustomInt >= 500:
                Roll4()
            if CustomInt >= 250 and CustomInt < 500:
                Roll6()
            if CustomInt > 0 and CustomInt < 250:
                Roll7()
            if CustomInt == 0:
                for i in range(75):
                    print()
                print("You Have No Money")
                Choice()
            Choice()
        elif prev == "half" or prev == "/":
            CustomAmount = abs(float(Cash/2))
            CustomAmount = round(CustomAmount, 2)
            CustomInt = CustomAmount
            if CustomInt >= 500:
                Roll4()
            if CustomInt >= 250 and CustomInt < 500:
                Roll6()
            if CustomInt > 0 and CustomInt < 250:
                Roll7()
            if CustomInt == 0:
                for i in range(75):
                    print()
                print("You Have No Money")
                Choice()
            Choice()
        elif prev == "custom" or prev == "c":
            try:
                CustomInt = PrevCA
                if CustomInt >= 500:
                    if Cash >= CustomInt:
                        Roll4()
                    else:
                        for i in range(75):
                            print()
                        print("Get Some Money Loser.")
                        Choice()
                if CustomInt >= 250 and CustomInt < 500:
                    if Cash >= CustomInt:
                        Roll6()
                    else:
                        for i in range(75):
                            print()
                        print("Get Some Money Loser.")
                        Choice()
                if CustomInt > 0 and CustomInt < 250:
                    if Cash >= CustomInt:
                        Roll7()
                    else:
                        for i in range(75):
                            print()
                        print("Get Some Money Loser.")
                        Choice()
                else:
                    for i in range(75):
                            print()
                    print("Invalid Input. Must be a number above 0")
                    Choice()
            except ValueError:
                for i in range(75):
                    print()
                print("Invalid Input. Must be a number above 0")
                Choice()
        elif prev == "high" or prev == "h":
            if Cash >= 500:
                Roll3()
            else:
                for i in range(75):
                    print()
                print("Get Some Money Loser.")
                Choice()
        elif prev == "medium" or prev == "m":
            if Cash >= 250:
                Roll2()
            else:
                for i in range(75):
                    print()
                print("Get Some Money Loser.")
                Choice()
        elif prev == "low" or prev == "l":
            if Cash >= 125:
                Roll1()
            else:
                for i in range(75):
                    print()
                print("Get Some Money Loser.")
                Choice()
        else:
            for i in range(75):
                print()
            print("Invalid input")
            Choice()
    elif bet == "reset" or bet == "r":
        for i in range(75):
            print()
        StartGame()
    elif bet == "free" or bet == "f":
        prev = "f"
        if FreeSpin >= 1:
            Roll5()
        else:
            for i in range(75):
                print()
            print("You Have No Free Spins")
            Choice() 
    elif bet == "custom" or bet == "c":
        prev = "c"
        try:
            CustomAmount = abs(float(input("Custom Bet: ")))
            CustomAmount = round(CustomAmount, 2)
            CustomInt = CustomAmount
            PrevCA = CustomInt
            if CustomInt >= 500:
                if Cash >= CustomInt:
                    Roll4()
                else:
                    print("Get Some Money Loser.")
                    Choice()
            if CustomInt >= 250 and CustomInt < 500:
                if Cash >= CustomInt:
                    Roll6()
                else:
                    print("Get Some Money Loser.")
                    Choice()
            if CustomInt > 0 and CustomInt < 250:
                if Cash >= CustomInt:
                    Roll7()
                else:
                    print("Get Some Money Loser.")
                    Choice()
            else:
                print("Invalid Input. Must be a number above 0")
                Choice()
        except ValueError:
            for i in range(75):
                print()
            print("Invalid Input. Must be a number above 0")
            Choice()
    elif bet == "high" or bet == "h":
        prev = "h"
        if Cash >= 500:
            Roll3()
        else:
            for i in range(75):
                print()
            print("Get Some Money Loser.")
            Choice()
    elif bet == "medium" or bet == "m":
        prev = "m"
        if Cash >= 250:
            Roll2()
        else:
            for i in range(75):
                print()
            print("Get Some Money Loser.")
            Choice()
    elif bet == "low" or bet == "l":
        prev = "l"
        if Cash >= 125:
            Roll1()
        else:
            for i in range(75):
                print()
            print("Get Some Money Loser.")
            Choice()
    else:
        for i in range(75):
            print()
        print("Invalid input")
        Choice()
Choice()
