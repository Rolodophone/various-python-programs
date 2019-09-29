import random

REVISION_LENGTH = 5



def main():
    global revisionData
        
    with open("data/revisionData.txt", "r") as revisionFile:
        rawData = revisionFile.read().split("\n\n")

    for i in range(len(rawData)):
        rawData[i] = rawData[i].split("\n")

    for i in range(len(rawData)):
        for j in range(len(rawData[i])):
            rawData[i][j] = rawData[i][j].split(":")
            
            if len(rawData[i][j]) > 1:
                rawData[i][j][2] = float(rawData[i][j][2])


    revisionData = {}

    for section in rawData:
        revisionData[section[0][0]] = section[1:]



def menu():
    while True:
        option = input("Choose a subject: ").upper()

        if option in revisionData:
            assert len(revisionData[option]) >= REVISION_LENGTH, "Revision subject must contain more revision points than REVISION_LENGTH"
            revise(option, REVISION_LENGTH)
            
            break

        else:
            print("That subject has no revision data. Try again for another subject\n")



def revise(subject, length):
    answers = answerQuestions(subject, getRandomIndexes(subject, length))
    incorrectIndexes = reviseAnswers(subject, answers, True)
    
    while incorrectIndexes != []:
        print("\n\nOh no! you got some wrong! Let's try again")
        answers = answerQuestions(subject, incorrectIndexes)
        incorrectIndexes = reviseAnswers(subject, answers, False)

    print("\n\nSession complete!")



def answerQuestions(subject, indexes):
    lastRevisionAnswers = []

    for index in indexes:
        answer = input(("\n" * 50) + revisionData[subject][index][0] + "\n")

        lastRevisionAnswers.append([index, answer])


    return lastRevisionAnswers



def reviseAnswers(subject, answers, changeProbs):
    global revisionData
    
    incorrectIndexes = []
    
    print(("\n" * 50) + "Here are your answers:\n\n")

    for answer in answers:
        print("\n\n\n\n{}\nYou answered: '{}'".format(revisionData[subject][answer[0]][0], answer[1]))
        
        if answer[1].lower() == revisionData[subject][answer[0]][1].lower():
            print("CORRECT!")

            if changeProbs:
                prevTotal = 0
                for point in revisionData[subject]:
                    if point != revisionData[subject][answer[0]]:
                        prevTotal += point[2]

                revisionData[subject][answer[0]][2] /= 2
                
                newTotal = 100 - revisionData[subject][answer[0]][2]
                multiplier = newTotal / prevTotal
                
                for point in revisionData[subject]:
                    if point != revisionData[subject][answer[0]]:
                        point[2] *= multiplier
            
        else:
            print("INCORRECT\nThe correct answer was '{}'".format(revisionData[subject][answer[0]][1]))
            incorrectIndexes.append(answer[0])


    with open("data/revisionData.txt", "w") as revisionFile:
        subjectList = []
        for subject in revisionData.items():
            pointList = []
            for point in subject[1]:
                newPoint = point[:]     # using list slicing to clone the list
                newPoint[2] = str(point[2])
                pointList.append(":".join(newPoint))

            subjectList.append(subject[0] + "\n" + "\n".join(pointList))

        rawData = "\n\n".join(subjectList)
        revisionFile.write(rawData)

    input()
    return incorrectIndexes



def getRandomIndexes(subject, length):
    result = []
    
    for i in range(length):
        while True:
            randNum = random.random() * 100

            cumulativeProb = 0
            for i in range(len(revisionData[subject]) - 1):
                cumulativeProb += revisionData[subject][i][2]
                if randNum <= cumulativeProb:
                    randomIndex = i
                    break
            
            if not randomIndex in result:
                result.append(randomIndex)
                break

    return result



main()
menu()
