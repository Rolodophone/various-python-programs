import random
import time

global scores

with open("scores.txt", "r") as scores_txt:
    scores = scores_txt.readlines()
    i = 0
    for val in scores:
        new_val = val.rstrip()
        new_val = new_val.split(":")
        new_val[1] = int(new_val[1])
        scores[i] = new_val
        i += 1
scores = sorted(scores, key = lambda score: score[0])
scores = sorted(scores, key = lambda score: score[1], reverse = True)

def main():
    ans = input("Hello and welcome to Times Tables Time Trials!\n\n\nDo you want to [P]lay, [S]ee the highscores or [Q]uit?\n\n")
    if ans == "P":
        play()
    elif ans == "p":
        play()
    elif ans == "S":
        high_scores()
    elif ans == "s":
        high_scores()
    elif ans == "Q":
        quit()
    elif ans == "q":
        quit()
    else:
        print("{} is not an option".format(ans))
        main()

def play():
    global scores
    
    name = input("What is your name before we start?")
    print("3")
    time.sleep(1)   
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    print("Go!")
    score = 0
    before_time = time.time()
    for i in range(10):
        num1 = random.randrange(3, 12)
        num2 = random.randrange(3, 12)
        ans = input("Question {}\nWhat is {} X {}?".format(i+1, num1, num2))
        if ans == str(num1 * num2):
            score += 10000000
            print("Right!\n")
        else:
            print("Wrong.\nThe correct answer is {}\n".format(num1 * num2))
    after_time = time.time()
    time_spent = after_time - before_time
    score = round(score / (time_spent + 1000))
    print("Your score was...")
    time.sleep(1)
    print(score)
    try:
        if score > max(scores, key = lambda score: score[1])[1]:
            print("New highscore!\n")
    except:
        print("New highscore!\n")
    time.sleep(2)
    scores.append([name, score])
    scores = sorted(scores, key = lambda score: score[1], reverse = True)
    save()
    main()

def high_scores():
    global scores

    if scores != []:
        for val in scores:
            print("{}:  {}".format(val[0], val[1]))
    else:
        print("Nobody has played yet.")
    print("\n\n\n\n")
    main()

def save():
    global scores
    
    with open("scores.txt", "w") as scores_txt:
        for val in scores:
            scores_txt.write("{}:{}\n".format(val[0], val[1]))

main()
