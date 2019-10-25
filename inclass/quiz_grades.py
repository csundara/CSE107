

grade = [[78, 76, 90], [90, 87, 76]]

for i in range(len(grade)):
    print('Student ' + str(i + 1) + ':')
    printGrade = ' '
    for j in range(len(grade[i])):
        printGrade = printGrade + str(grade[i][j]) + ' '
    print(printGrade)

# now print average grade for each Student
count = 1
for i in grade:
    avgGrade = 0
    for j in i:
        avgGrade = avgGrade + float(j)
    avgGrade = avgGrade / len(i)
    print('Student ' + str(count) + ': ' + str(avgGrade))
    count = count + 1

#class average of each quiz

for quiz in range(len(grade[0])):
    sumQuiz = 0
    for std in range(len(grade)):
        sumQuiz = sumQuiz + grade[std][quiz]
    print('The average of Quiz ' + str(quiz + 1) + ' is ' + str(sumQuiz/len(grade)))
