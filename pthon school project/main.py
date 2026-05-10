import csvservice
import questionservice
import uiservice
import anatomyservice

#get anatomy info 
anatomyPartList = csvservice.getCsvAnatomyInfo('muscles_and_bones_data.csv')

#choose card type muscle/bone
anatomyChoice=uiservice.chooseCards()

#tells correct anatomy choice
chosenInfoList = anatomyservice.getAnatomyInfo(anatomyPartList, anatomyChoice)

#display cards
uiservice.displayCards(chosenInfoList)

#get question info 
questionList = csvservice.getCsvQuestionInfo('question_list.csv')

#choose question type quiz/test
questionType=uiservice.chooseQuestion()

#tells correct question choice
chosenQuestionList = questionservice.getQuestionInfo(questionList, anatomyChoice)

#display questions
responseList=uiservice.displayQuestion(chosenQuestionList)

#mark the question 
markedScore = questionservice.markQuestions(chosenQuestionList,responseList)

#record result (assuming test) - score
csvservice.saveResult(markedScore, questionType)

#display result  - score
uiservice.displayResult(markedScore, len(chosenQuestionList))




# i used gemini ai on 1/5/2026 to write the data in the questionlist csv file
