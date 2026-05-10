def getAnatomyInfo(partsList, aType):#add the correct cards to a list to get read to be displayed 
   anatomyList = []
   for part in partsList:
       if part.anatomyType == aType:
           anatomyList.append(part)
   return anatomyList
