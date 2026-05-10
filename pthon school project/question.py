class Question: # gets question info and organises it
   def __init__(self, questionType, questionText, optionA, optionB, optionC, optionD, correctAnswer):
       self.questionType = questionType
       self.questionText = questionText
       self.optionA = optionA
       self.optionB = optionB
       self.optionC = optionC
       self.optionD = optionD
       self.correctAnswer = correctAnswer
