import question

def getQuestionInfo(questionList, qType): #gets questions and adds them to list to be read
    quizList = []
    for question in questionList:
        if question.questionType == qType:
            quizList.append(question)
    return quizList




def markQuestions(chosenInfoList,responseList): # marks question to see if you got them correct
    score = 0
    for q in range(len(chosenInfoList)):
        print (str(chosenInfoList[q].correctAnswer.lower()) + "-=" + str(responseList[q].lower()))
        if chosenInfoList[q].correctAnswer.lower() == responseList[q].lower():
            score = score + 1
    return score


