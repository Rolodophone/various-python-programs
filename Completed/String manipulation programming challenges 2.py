while True:
    string = input("\n\nEnter a string")

    option = input("Would you like to:\nFind the [N]umber of characters in "
                   "the string\n[R]everse the string\nConvert the string "
                   "to [U]ppercase\nConvert the string to [L]owercase\n")
    if option == "n":
        print(len(string))
    elif option == "r":
        print(string[::-1])
    elif option == "u":
        print(string.upper())
    elif option == "l":
        print(string.lower())

    option = input("Would you like to input [A]nother string or [L]eave?")
    if option == "l":
        exit()
    elif option == "a":
        continue
    else:
        break
