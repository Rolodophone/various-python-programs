def main():
    num = input("What is the number that you want to test?")
    try:
        n = int(num)
    except:
        print("Please enter an integer.")
        main()
    if n < 1:
        print("The Collatz Conjecture only works with integers higher than 0")
        main()
    i = 0
    while n != 1:
        i += 1
        if n % 2 == 0:
            print("{})  {}  (even)\n\n".format(i, int(n)))
            n /= 2
        else:
            print("{})  {}  (odd)\n\n".format(i, int(n)))
            n *= 3
            n += 1
    print("{})  {}\n\n\n\n".format(i + 1, int(n)))
    main()
    
main()
