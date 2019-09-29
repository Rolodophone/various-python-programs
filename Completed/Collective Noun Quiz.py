import time
import random
animals = {"ants":["colony", "army"], "bats":["cloud", "colony"], "bears":["sleuth", "sloth"], "bees":["hive", "swarm"], "birds":["flock", "flight"], "buffalo":["herd"], "cats":["clutter"], "chickens":["brood", "flock"], "cows":["herd"], "dogs":["pack"], "dolphins":["school"], "ducks":["raft"], "elephants":["herd"], "fish":["school"], "foxes":["troop", "earth"], "frogs":["army", "colony"], "geese":["flock", "gaggle"], "goats":["flock", "herd"], "horses":["herd", "team", "string"] ,"kangaroos":["mob", "troop"], "lions":["pride"], "monkeys":["troop"], "owls":["parliament"], "penguins":["colony"], "humans":["crowd"], "pigs":["herd"], "rabbits":["colony", "nest", "warren"], "sheep":["flock"], "tigers":["streak"], "whales":["school", "shoal", "pod"], "wolves":["pack", "herd"], "zebras":["cohort", "herd"]} 
Questions = list(animals)
Answers = list(animals.values())
def Main():
    Que = random.sample(Questions, 10)
    Ans = []
    for i in range(10):
        Ans.append(animals[Que[i]])

    print("Hello!")
    time.sleep(1)
    print("My name is Quiz.")
    time.sleep(2)
    print("I will test you on your knowledge on the collective nouns of animals.")
    time.sleep(2)

    for i in range(10):
        print("Question " + str(i+1) + ":")
        time.sleep(2)
        print("What is the collective noun for...")
        time.sleep(2)
        reply = input("..." + Que[i] + "?")
        if reply in Ans[i]:
            print("Well done.\nYou got it right!")
        else:
            print("Oh no!\nYou got it wrong.")
            print("Answer:     " + str(Ans[i]))
            break
    print("Congratulations!\nYou finished the quiz!")
    m = input("press enter to restart")
    Main()
    
Main()
