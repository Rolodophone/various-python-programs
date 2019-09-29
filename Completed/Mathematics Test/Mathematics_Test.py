import random, os.path
#import the random module for later use

global scores
#globalise the scores variable

if not os.path.isfile("scores.txt"):
    with open("scores.txt", "w") as tmp:
        tmp.close()

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
#read and sort the scores

questions = [["What is the next prime number after 7?", "11"],
             ["The perimeter of a circle is also known as what?", "CIRCUMFERENCE"],
             ["65 – 43 = ?", "22"],
             ["True or false? A convex shape curves outwards.", "TRUE"],
             ["What does the square root of 144 equal?", "12"],
             ["True or false? Pi can be correctly written as a fraction.", "FALSE"],
             ["What comes after a million, billion and trillion?", "QUADRILLION"],
             ["52 divided by 4 equals what?", "13"],
             ["What is the bigger number, a googol or a billion?", "GOOGOL"],
             ["True or false? Opposite angles of a parallelogram are equal.", "TRUE"],
             ["divide 21 in the ratio 1:2:4.", "3:6:12"],
             ["6 ÷ -0.5 = ?", "-12"],
             ["87 + 56 = ?", "143"],
             ["How many sides does a nonagon have?", "9"],
             ["True or false? -2 is an integer.", "TRUE"],
             ["What is the next number in the Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ?", "55"],
             ["True or false? In an isosceles triangle all sides are unequal.", "FALSE"],
             ["In statistics, the middle value of an ordered set of values is called what?", "MEDIAN"],
             ["What does 3 squared equal?", "9"],
             ["True or false? -4 is a natural number.", "FALSE"],
             ["5 to the power of 0 equals what?", "1"]
            ]
#define the questions

def main():
    ans = input("Mathematics Test\n\n\nDo you want to [T]ake the test, [S]ee the highscores or [Q]uit?\n\n")
    if ans == "T":
        test()
    elif ans == "t":
        test()
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
#main menu

def test():
    global scores

    name = input("What is your name before we start?")
    Q = random.sample(questions, 15)
    score = 0
    print("ANSWER IN CAPITALS")
    for i in range(15):
        ans = input(Q[i][0])
        #input the question
        if ans == Q[i][1]:
            score += 1
            print("Right!\n")
        else:
            print("Wrong.\nThe correct answer is {}\n".format(Q[i][1]))
        #check the answer
    print("Your score was {} out of 15".format(score))
    #print score
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
        print("Nobody has taken the test yet.")
    #print highscores
        
    print("\n\n\n\n")
    main()

def save():
    global scores
    
    with open("scores.txt", "w") as scores_txt:
        for val in scores:
            scores_txt.write("{}:{}\n".format(val[0], val[1]))
            #save scores

main()
#call main function to start the main menu
