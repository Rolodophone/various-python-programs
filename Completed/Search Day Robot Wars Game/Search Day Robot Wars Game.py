import random

PAGE_SPLIT = "\n" * 60

robotList       = None
players         = None
NUM_OF_PLAYERS  = None
MAX_NAME_LENGTH = 50
WINNING_SCORE   = 5



def main():
    loadRobots()
    loadSettings()
    endGame(cardGame2(NUM_OF_PLAYERS))

    

def loadRobots():
    global robotList
    
    #read robot names into robotList
    with open("robots.txt", "r") as robotsFile:
        robotList = robotsFile.read().splitlines()



def loadSettings():
    global NUM_OF_PLAYERS
    
    #read settings into variables
    with open("settings.txt", "r") as settingsFile:
        settings = settingsFile.read().splitlines()
        
    NUM_OF_PLAYERS = int(settings[0].split("=")[1])
    


def cardGame():
    scores = [None, 0, 0]

    #repeats on a per-round basis
    while scores[1] < 3 and scores[2] < 3:
        
        #set card values to a random value
        (name1, armour1, speed1, weapon1) = (random.choice(robotList), random.randint(0, 100), random.randint(0, 100), random.randint(0, 100))
        robotList.remove(name1)
        (name2, armour2, speed2, weapon2) = (random.choice(robotList), random.randint(0, 100), random.randint(0, 100), random.randint(0, 100))
        robotList.remove(name2)

        print(PAGE_SPLIT + "Your robot is {}. It has {} armour, {} speed, and {} weapon".format(name1, armour1, speed1, weapon1))

        #menu for choosing what property to challenge opponent with
        while True:
            choice = input("Do you choose to challenge your opponent with your [A]rmour, [S]peed, or [W]eapon?\n").lower()
            if choice == "a":
                player1Value = armour1
                player2Value = armour2
                break
            elif choice == "s":
                player1Value = speed1
                player2Value = speed2
                break
            elif choice == "w":
                player1Value = weapon1
                player2Value = weapon2
                break
            else:
                input("'{}' is not an option. Press ENTER to try again.".format(choice))

        #print opponent's values
        print("Player 2 is the robot {}. It has {} armour, {} speed, and {} weapon".format(name2, armour2, speed2, weapon2))

        #evaluate who won the round
        if player1Value > player2Value:
            winningPlayer = 1
        elif player2Value > player1Value:
            winningPlayer = 2
        else:
            winningPlayer = False

        #print who won the round and update scores
        if winningPlayer:
            print("Player {} wins the round! They get 1 point!".format(winningPlayer))
            scores[winningPlayer] += 1
            print("The scores are now: player1 - {}, player2 - {}".format(scores[1], scores[2]))
        else:
            print("It's a draw! No one gets a point.\n\n")

        input("Press ENTER to continue")


    #evaluate and print winner
    print(PAGE_SPLIT + "The game has ended.")
    if scores[1] >= 3:
        print("Player 1 wins!")
    elif scores[2] >= 3:
        print("Player 2 wins!")
    else:
        print("It's a draw!")



class Player:
    def __init__(self, name, score=0):
        self.name  = name
        self.score = score



class Robot:
    def __init__(self, name, armour, speed, weapon):
        self.name   = name
        self.armour = armour
        self.speed  = speed
        self.weapon = weapon



def findPlayerWithHighestAttr(attr):
    valuesList = []
    for player in players:
        valuesList.append(getattr(player, attr))
    
    if len(valuesList) == len(set(valuesList)): #check for duplicates in list
        return players[valuesList.index(max(valuesList))]
    else:
        return None



def printScores():
    for player in players:
        nameLength = len(player.name)
        
        if nameLength < MAX_NAME_LENGTH - 3:
            numOfDots = MAX_NAME_LENGTH - nameLength
        else:
            numOfDots = 0
        
        print("{}{}...{}".format(player.name, "." * numOfDots, player.score))



def cardGame2(NUM_OF_PLAYERS):
    global players
    
    print(PAGE_SPLIT)
    
    #create players
    players = []
    for i in range(NUM_OF_PLAYERS):
        name = input("What would you like player {} to be called?".format(i + 1)) #i + 1 to get from players 0 & 1 to players 1 & 2
        players.append(Player(name))


    #repeat every round until someone wins
    while True:

        #check if there are enough robots for the round
        if len(robotList) < NUM_OF_PLAYERS ** 2:
            input(PAGE_SPLIT + "Oops! We've run out of robot names! Press ENTER to continue.")
            return findPlayerWithHighestAttr("score")


        #repeat every turn
        for playerWhosTurnItIs in players:    
            print(PAGE_SPLIT + "It is {}'s turn".format(playerWhosTurnItIs.name))
            
            #create robots for players
            for player in players:
                player.robot = Robot(random.choice(robotList), random.randint(0, 100), random.randint(0, 100), random.randint(0, 100))
                robotList.remove(player.robot.name)
                    
            print("Your robot is {}. It has {} armour, {} speed, and {} weapon".format(playerWhosTurnItIs.robot.name, playerWhosTurnItIs.robot.armour, playerWhosTurnItIs.robot.speed, playerWhosTurnItIs.robot.weapon))

            #menu for choosing what property to challenge opponent with
            while True:
                choice = input("\nDo you choose to challenge your opponent(s) with your [A]rmour, [S]peed, or [W]eapon?\n").lower()
                if choice == "a":
                    for player in players:
                        player.chosenValue = player.robot.armour
                        
                    break
                elif choice == "s":
                    for player in players:
                        player.chosenValue = player.robot.speed
                        
                    break
                elif choice == "w":
                    for player in players:
                        player.chosenValue = player.robot.weapon
                        
                    break
                else:
                    input("'{}' is not an option. Press ENTER to try again.".format(choice))

            print("\n\n")

            #print opponents' robots
            for player in players:
                if player != playerWhosTurnItIs:
                    print("{} has the robot {}. It has {} armour, {} speed, and {} weapon".format(player.name, player.robot.name, player.robot.armour, player.robot.speed, player.robot.weapon))

            #evaluate who won the round and update scores
            winningPlayer = findPlayerWithHighestAttr("chosenValue")
            if winningPlayer:
                print("\n{} has won this turn.".format(winningPlayer.name))
                winningPlayer.score += 1
            else:
                print("\nIt's a draw! No one gets a point.")

            #print scores
            print("\nThe scores are:")
            printScores()
            input("\nPress ENTER to continue.")

            #check if anyone has won
            for player in players:
                if player.score >= WINNING_SCORE:
                    return player



def endGame(winningPlayer):
    print(PAGE_SPLIT + "The game has ended. Here are the final scores:")
    printScores()
    input("Press ENTER to continue.")

    if winningPlayer != None:
        input(PAGE_SPLIT + "{} has won the game!".format(winningPlayer.name))
    else:
        input("\n\nIt's a tie!")



main()
