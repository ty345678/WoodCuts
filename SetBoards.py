
def SetBoards(boardSetPairs):
    length = len(boardSetPairs)
    count =1
    lastLength = 0
    lengthPairs = []
    lengthPairsTotal = []
    lengthPairsCount=1
    while(count<length):

        boardLength = boardSetPairs[count]
        if(boardLength == lastLength):
            lengthPairsCount+=1
        elif(boardLength!=lastLength and lastLength!=0):
                lengthPairsTotal.append([lastLength,lengthPairsCount])
                lengthPairs = []
                lengthPairsCount = 1
        count+=2
        lastLength = boardLength

    lengthPairsTotal.append([lastLength,lengthPairsCount])
    return lengthPairsTotal

