import anatomyservice
import questionservice

def chooseCards():
    while True:
        ac = input("enter study type: B) study Bones. M) study Muscles. [B/M]? : ") #ask for user's study preference
        if ac == "B":
            print('bones')
            return ac
        elif ac == "M":
            print ('muscles')
            return ac
        else:
            print("enter B or M")
        
    
def displayCards(chosenInfoList): #displays user chosen info cards
    cardpointer = 0
    navigationChoice = ""
    while navigationChoice not in ("f", 'F'): #loops the question untill 'F' or "f" (finish) is input 
        displayCardStructure(chosenInfoList[cardpointer])
        navigationChoice = input("n (next), p (previous), or f (finish): ")
       
        if cardpointer + 1 < len(chosenInfoList):
            if navigationChoice in ("n", 'N'):
                cardpointer = cardpointer + 1
        if cardpointer > 1:
            if navigationChoice in ("p", 'P'):
                cardpointer = cardpointer - 1
        

def chooseQuestion():
    qc = ""
    while qc not in ('Q','q', "t", "T"): #loops question untill 'Q','q', "t", "T" is input
        qc = input("enter study type: Q) do a Quiz(highscore will not be recorded. T) do a Test(highscore will be recorded) [Q/T]? : ")#ask for user's question preference
        if qc in ('Q','q'):
            print('Quiz')
        elif qc in ("t", "T"):
            print ('Test')
    return qc
       
    
def displayQuestion(chosenQuestionList):
    questionpointer = 0         # index used point to the question in the chosenQuestionList
    responseList = [""] * len(chosenQuestionList)         # this list stores the question's response
    navigationChoice = ""
    while navigationChoice not in ("f", 'F'):
        displayQuestionStructure(chosenQuestionList[questionpointer])

        # get user question response
        responseList[questionpointer]=recordResponse()

        # get user navigation response
        navigationChoice = enterNavigation()

        # given navigation response - decide how to move questionpointer
        if questionpointer + 1 < len(chosenQuestionList):
            if navigationChoice in ("n", 'N'):
                questionpointer = questionpointer + 1
        if questionpointer > 1:
            if navigationChoice in ("p", 'P'):
                questionpointer = questionpointer - 1
    return responseList

def enterNavigation(): # tells the program which question/card to use
    navigationChoice = ""
    while navigationChoice  not in  ("n", 'N',"p", 'P',"c","f", 'F'):
        navigationChoice = input("n (next), p (previous), or f (finish): ")
    return navigationChoice

def recordResponse(): #records user's respone to a question 
    questionResponse="" 
    while questionResponse  not in  ("a", 'A',"b", 'B',"c", 'C',"d", 'D'):
        questionResponse = input('A - D: ')
    return questionResponse
    
def displayResult(markedScore, maxScore): #displays the final result
    print(str(markedScore) +  '/' + str(maxScore))



def displayCardStructure(anatomyPart): # tells program  how to structure info cards
    print('name: '+(anatomyPart.name)) 
    print('location: '+(anatomyPart.location))
    print('defintion: '+(anatomyPart.definition))
    if anatomyPart.movement is not None:
        print('movement type: '+(anatomyPart.movement))
    if anatomyPart.boneType  is not None:
        print('bonetype: '+(anatomyPart.boneType))


def displayQuestionStructure(question): # tells program  how to structure questions
    print('Question: '+(question.questionText))
    print('a: '+(question.optionA))
    print('b: '+(question.optionB))
    print('c: '+(question.optionC))
    print('d: '+(question.optionD))

