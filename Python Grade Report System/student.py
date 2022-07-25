# function that calculates average score
def calculateAverages(scores):
    summa = 0
    # loop that find average of scores
    for score in scores:
        summa += score
    average = summa / 3
    averagelist.append(average)

# function that sort scores        
def sortScores(scores):
    scores.sort()

# function that takes name and scores and append them to list
def getNameScore(name,scores,namelist,scoreslist):
    namelist.append(name)
    scoreslist.append(scores)
    

# function that returns letter grades of scores
def getLetterGrade(score):
    if score >= 90:
        numberOfLetter[0] += 1
        return "A"
    elif score >= 80 and score < 90:
        numberOfLetter[1] += 1
        return "B"
    elif score >= 70 and score < 80:
        numberOfLetter[2] += 1
        return "C"
    elif score >= 60 and score < 70:
        numberOfLetter[3] += 1
        return "D"
    else:
        numberOfLetter[4] += 1
        return "F"
    
#function that display results
def display(namelist,scoreslist,averagelist,numberOfLetter,numberOfStudent):
    ave = 0
    for score in averagelist:
        ave += score
    ave = ave / numberOfStudent

    for i in range(5):
        numberOfLetter.append(0)
        
    print("\nSemester Grades Summary")
    print("\tTotal Number of Students: {}\n".format(numberOfStudent))
    print("\tName\t\t\tScores\t\t\tAverage\t\tLetter Grade")
    for i in range(numberOfStudent):
        print("\t{}\t\t\t{}\t\t{:.2f}\t\t{}".format(namelist[i],", ".join(str(x) for x in scoreslist[i]),averagelist[i],getLetterGrade(averagelist[i])))
        

    print("_____________________________________________")
    print("Average Grade of all students\t\t{:.2f}".format(ave))
    print("Number of A's\t\t\t\t\t\t{}".format(numberOfLetter[0]))
    print("Number of B's\t\t\t\t\t\t{}".format(numberOfLetter[1]))
    print("Number of C's\t\t\t\t\t\t{}".format(numberOfLetter[2]))
    print("Number of D's\t\t\t\t\t\t{}".format(numberOfLetter[3]))
    print("Number of F's\t\t\t\t\t\t{}".format(numberOfLetter[4]))

    
namelist = []
scoreslist = []
averagelist = []
numberOfLetter = []

print("Instructor’s Entry",end="")

numberOfStudent = int(input("How many students: "))

#for loop that performs operations with functions
for i in range(numberOfStudent):
    print("\nStudent #{}".format(i+1),end="")
    name = input("Enter the name: ")
    scores = []
    for j in range(3):
        while True:
            score = int(input("Enter grade for Exam {}: ".format(j+1)))
            if score >= 0 and score <= 110:
                break
            else:
                print("Invalid score.")
        scores.append(score)
    calculateAverages(scores)
    sortScores(scores)
    getNameScore(name, scores, namelist, scoreslist)
    
display(namelist, scoreslist, averagelist, numberOfLetter, numberOfStudent)



    
        
    
    