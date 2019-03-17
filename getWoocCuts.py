


def getWoodCuts(board,overCutPercent):
    lengths = board.getLengths()
    sizes = board.getSizes()
    boardSetPairs = []
   

    while(lengths):
        totalBoard = 0
        boardSets = []
        for x in lengths:#gets first board
            if(x>totalBoard):
                totalBoard = x
        try:
            boardSets.append(totalBoard)
            lengths.remove(totalBoard)
        except:
            print("error in removing board from list")
            break

        #totalBoard = firstBoard
        secBoardMax =0
        secBoard = 0

        size = maxSize(sizes,lengths)

        while(totalBoard<(size-overCutPercent)):
            #firstBoard = totalBoard #works but could be cleaned if time
            for x in lengths:
                
                        

                secBoard =  x + totalBoard #firstBoard
                if((secBoard)<=(size-overCutPercent)):
                    if((secBoard)>secBoardMax):
                        secBoardMax = secBoard#checkboard
                if(totalBoard>size):
                    totalBoard = totalBoard
            try:            
                lengths.remove(secBoardMax-totalBoard)                
                boardSets.append(secBoardMax-totalBoard)
            except:
                break
            totalBoard = secBoardMax
            if(not lengths):
                break

        boardSetPairs.append(boardSets)
        boardSetPairs.append(size)
    return boardSetPairs

    
 


def maxSize(sizes,lengths):
    total = 0
    for x in lengths:
        total = total +x
    for x in sizes:
        if(total<x):
            return x
       

    return sizes[-1]