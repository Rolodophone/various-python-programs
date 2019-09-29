a = input()
b = a.split(".")
c = b[0] + b[1]
print(str(int("".join(b)) - int(c)) + "/" + "9" * int(b[2]) + "0" * int(b[1]))
