import re

with open("data.txt", "r") as file:
    data = file.read()

c = 1

data = data.split(" ")
i=0
for word in data:
    data[i] = "{{c"+str(c)+"::"+word+"}}"
    c += 1
    i += 1

i=0
for word1 in data:
    data[i] = word1.split("<br>")
    j=0
    for word2 in word1:
        data[i][j] = "{{c"+str(c)+"::"+word2+"}}"
        j+=1
        c+=1
    i+=1

print(data)

