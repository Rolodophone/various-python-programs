def main():
    global people
    try:
        people = int(input("How many people are in the room?"))
    except:
        print("Please enter a number.")
        main()
    if people < 2:
        print("Number is too small. Please pick a number higher than 2.")
        main()
    else:
        cal_or_sim()


def cal_or_sim():
    birthdays = []
    ans = input('Do you want to calculate the chance or run a simulation? (type "c" for calculate or "s" for simulate)')
    if ans == "c":
        percent = calc()
        print(str(percent) + "% chance that al least 2 people have the same birthday")
        main()
    elif ans == "s":
        for i in range(people):
            month = random.choice(["January", "Febuary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"])
            if month == "January" or month == "March" or month == "May" or month == "July" or month == "August" or month == "October" or month == "December":
                day = random.choice(range(1, 32))
            elif month == "Febuary":
                day = random.choice(range(1, 29))
            else:
                day = random.choice(range(1, 31))
            birthdays.append(str(day) + " " + month)
            print(str(day) + " " + month)
        shared_birthdays = len(birthdays)-len(set(birthdays))
        print("There are " + str(shared_birthdays) + " shared birthdays")
        main()
    else:
        print("I think you have typed something incorrectly, try again.")
        cal_or_sim()


def calc():
    num = 1
    for i in range(people):
        num *= (365-i)/365
    num = (1-num)*100
    return num


import random
print("---------BIRTHDAY PARADOX---------\n\n\n")
birthdays = []
main()
people = 0
