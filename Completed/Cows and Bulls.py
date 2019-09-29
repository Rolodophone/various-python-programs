from random import randint
from time import clock

def main():
    print("Welcome to Cows and Bulls!\n")
    while True:
        ans = input("Would you like to hear how the game is played?\n")
        if ans.lower() == "yes" or ans.lower() == "y":
            print("\nOk, here are the instructions:\n")
            print("I will generate a random number with no duplicate digits.")
            print("YOU have got to try to guess it!")
            print("You can do this by entering a 4-digit number and seeing how close you are.")
            print("I will say how many bulls and cows you have.")
            print("A bull is when you have guessed the right digit and it IS in the right place.")
            print("A cow is when you have guessed the right digit and it ISN'T in the right place.")
            print("You have got to use this information to work out my number.")
            print("I won't help you with that part :-)")
            
            print("\nOh, and I almost forgot!")
            print("If at an point you want to give up (which you should never do), just type \"exit\"")
            print("Good luck!")
            break

        elif ans.lower() == "no" or ans.lower() == "n":
            break

        else:
            print("{} is not an option\n".format(ans))
            
        
    input("\nPress enter to begin")
    play()


def play():
    difficulty = input("Please choose a difficulty (this will be how many digits the number has)\n")
    try:
        difficulty = int(difficulty)
    except:
        print("Please enter an integer\n\n")
        play()

    if difficulty < 1:
        print("Please enter a number above 0\n\n")
        play()

    num = ""
    for i in range(difficulty):
        while True:
            digit = str(randint(0, 9))
            if not digit in num:
                num += digit
                break

    legit = True

    guesses = 0
    clock()
    while True:
        guesses += 1
        
        ans = input("\n\nEnter a guess or type \"exit\" to exit:\n")
        if ans.lower() == "exit":
            legit = False
            break
        elif len(ans) == difficulty:
            bulls = 0
            cows = 0
            i = 0
            for digit in ans:
                if digit in num:
                    if digit == num[i]:
                        bulls += 1
                    else:
                        cows += 1
                i += 1

            if ans == num:
                break
            else:
                print("Your number was {} and it had {} bull(s) and {} cow(s)\n\n".format(ans, bulls, cows))
        else:
            print("Please enter a {}-digit number\n".format(difficulty))

    time = clock()
    if legit == True:
        score = round(1000000000 - (time + (guesses * 20)))
        if score < 0:
            score = 0
        
        print("\nWell done! You guessed the number! It was {}".format(num))
        print("Your score is {}".format(score))
    else:
        print("\nOh no, you gave up :-(")
        print("The number was {}".format(num))

    ans = input("\n\nWould you like to play again?")
    if ans.lower() == "yes" or ans.lower() == "y":
        play()
    else:
        quit()


main()
