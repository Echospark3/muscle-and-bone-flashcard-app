import csv
from anatomypart import AnatomyPart
from question import Question

def getCsvAnatomyInfo(filename): #loads the CSV file/ card info
   loadedAnatomyList = []
   with open(filename, mode = 'r') as file:
     csvFile = csv.reader(file)
     next(csvFile, None)  # Skip the header.
     for anatomyType, name, location, movement, definition, boneType in csvFile:
         ap = AnatomyPart(anatomyType, name, location, movement, definition, boneType)
         loadedAnatomyList.append(ap)
   return loadedAnatomyList



def getCsvQuestionInfo(filename): #loads the CSV file/ question info
   loadedQuestionList = []
   with open(filename, mode = 'r') as file:
      qcsvFile = csv.reader(file)
      next(qcsvFile, None)  # Skip the header.
      for questionType, questionText, optionA, optionB, optionC, optionD, correctAnswer  in qcsvFile:
         qp = Question(questionType, questionText, optionA, optionB, optionC, optionD, correctAnswer)
         loadedQuestionList.append(qp)
   return loadedQuestionList

def saveResult(markedScore, questionType): #saves the marked results into text file 
   ms = markedScore
   if questionType in ("t", "T"):
      name = input("enter student name: ")
      testMsg = name + "'s score for this test is: "
      with open("score.txt", "a") as file: 
         file.write(testMsg + str(ms))
         file.write('.\n')
