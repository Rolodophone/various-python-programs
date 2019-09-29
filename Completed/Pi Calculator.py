import random, math, re

def main():
    ans = input("PRESS ENTER TO START")
    if ans != 0:
        menu()

def menu():
    ans = input("[I]ndividually or [Q]uick iterations?").lower()
    if ans == "i":
        ind()
    elif ans == "q":
        qui()
    else:
        print("{} is not an option\n".format(ans))
        menu()

def options():
    ans = input("[S]tart again or [Q]uit?").lower()
    if ans == "s":
        main()
    elif ans == "q":
        quit()
    else:
        print("{} is not an option\n".format(ans))
        options()

def ind():
    iternum = 0
    num1 = 0
    num2 = 0
    what = ""
    coprimes = 0
    cofactors = 0
    hcf = 0
    prob = 0.0
    calcpi = 0
    while True:
        ans = input("").lower()
        if ans != "q":
            iternum += 1
            print("iteration number: {}".format(iternum))
            
            num1 = random.randint(1, 1000000000000000000000000000)
            num2 = random.randint(1, 1000000000000000000000000000)
            print("first number: {}\nsecond number: {}".format(str(num1), str(num2)))

            hcf = math.gcd(num1, num2)
            if hcf == 1:
                what = "coprime"
                coprimes += 1
            else:
                what = "cofactor"
                cofactors += 1
            print("HCF: {}\nso they are: {}".format(str(hcf), what))

            prob = coprimes / (coprimes + cofactors)
            try:
                calcpi = math.sqrt(6 / prob)
            except:
                calcpi = "undefined (division by 0)"
            print("probabilty of being coprime: {}\ncalculated pi: {}\nreal pi:       {}\n\n".format(str(prob), str(calcpi), math.pi))

        else:
            options()

def qui():
    iternum = 0
    num1 = 0
    num2 = 0
    coprimes = 0
    cofactors = 0
    hcf = 0
    prob = 0.0
    calcpi = 0

    try:
        enditer = int(input("How many iterations?"))
    except:
        print("Please enter a number\n")
        
    while iternum < enditer:
        iternum += 1
        
        num1 = random.randint(1, 1000000)
        num2 = random.randint(1, 1000000)

        hcf = math.gcd(num1, num2)
        if hcf == 1:
            coprimes += 1
        else:
            cofactors += 1

        prob = coprimes / (coprimes + cofactors)
        try:
            calcpi = math.sqrt(6 / prob)
        except:
            calcpi = "undefined (division by 0)"
        print("{}\n".format(str(calcpi)))

    options()
            
main()
