#HACKPSU spring 2019
#Tyler Mueller
#taran 
#Betsy

import tkinter as tk
from getWoocCuts import getWoodCuts
from SetBoards import SetBoards


global overCutPercent########
class Board:
    def __init__(self,type,sizes):
        self.type = type
        
        self.lengths = []
        self.Lcount = 0
        self.sizes = sizes
        self.boards=[]

    def addLength(self,length):
        if(length>self.sizes[-1] or length <=0):
            print("size must be smaller then Largest board of size: "+str(self.sizes[-1])+"ft")
            #print("If you need a longer board, please add the largest board size you are able to purchase")
        else:
            
            self.lengths.append(length)
            self.Lcount +=1

    def getLengths(self):
        return self.lengths
    def getSizes(self):
        return self.sizes
    def getType(self):
        return self.type
        

    

class window(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        master.title("WoodCuts")
        self.woodImage = tk.PhotoImage(file="wood.ppm")

        self.board2x4 = Board("2x4",[10,12,16])
        self.board2x6 = Board("2x6",[10,12,16])
        self.board2x8 = Board("2x8",[10,12,16])
        #self.board2x8 = Board("2x8",[10,12,16])

        self.createButtons()
        self.pack()



    def createButtons(self):
        self.canvas = tk.Canvas(self.master, width=900, height=900)
               
        self.length2x4 = tk.IntVar() 
        self.amount2x4 = tk.IntVar() 
        self.amount2x4.set(1)
        self.createBOARDButtons(15,self.board2x4.getType(),self.length2x4,self.amount2x4,self.board2x4)

        self.length2x6 = tk.IntVar() 
        self.amount2x6 = tk.IntVar()
        self.amount2x6.set(1)
        self.createBOARDButtons(90,self.board2x6.getType(),self.length2x6,self.amount2x6,self.board2x6)

        self.length2x8 = tk.IntVar() 
        self.amount2x8 = tk.IntVar()
        self.amount2x8.set(1)
        self.createBOARDButtons(165,self.board2x8.getType(),self.length2x8,self.amount2x8,self.board2x8)

        
        #self.createSETBoard()
        self.button = tk.Button(self.master, text="Generate Board Cuts", command=self.generateButton).place(x=(245), y=360,height =50,width = 150)

        #self.showCart()

        self.canvas.pack()

    #def showCart(self):


    def createBOARDButtons(self,PosX,name,lengthVar,amountVar,board):
        self.canvas.create_image((PosX+32), 100,image=self.woodImage)
        self.Wood = tk.Label(self.master,image=self.woodImage)

        #self.label = tk.Label(self.master,text = "2x4").place(x=25,y=50)
        self.canvas.create_text((PosX+30),75,fill="white",font="Times 20 bold",text=name)
               
        self.canvas.create_text((PosX+32),212,fill="black",font="Times 10 bold",text="Length")
        self.textBox = tk.Entry(self.master, textvariable=lengthVar,justify="center").place(x=(PosX+12),y=222,height=30, width=40)
        self.canvas.create_rectangle((PosX+5), 205, (PosX+60), 255)

        self.canvas.create_text((PosX+32),267,fill="black",font="Times 10 bold",text="Amount")
        self.textBox = tk.Entry(self.master, textvariable=amountVar ,justify="center").place(x=(PosX+12),y=277,height=30, width=40)
        self.canvas.create_rectangle((PosX+5), 260, (PosX+60), 312)

        self.button = tk.Button(self.master, text="TEST", command=lambda: self.setLength(lengthVar,amountVar,board)).place(x=(PosX+12), y=320)
     
    def createSETBoard(self):
        self.typeSet = tk.StringVar()
        self.lengthSET = tk.IntVar()
        self.amountSET= tk.IntVar()

        self.canvas.create_rectangle(240, 15, (305), 200, fill="blue")
        self.textBox = tk.Entry(self.master, textvariable=self.typeSet,justify="center").place(x=244,y=50,height=30, width=57)

    def generateButton(self):
        differentBoards=0
        self.canvas.create_rectangle((20), 420, (620), 590)
        if(self.board2x4.getLengths()):
            Set2x4Boards = SetBoards(getWoodCuts(self.board2x4,overCutPercent))
            self.canvas.create_rectangle((25), 425, (75+75*differentBoards), 580)
            self.canvas.create_text((47+75*differentBoards),435,fill="black",font="Times 12 bold",text=self.board2x4.getType())
            count =0
            for x in Set2x4Boards:
                boardString = str(x[0])+"ft-"
                self.canvas.create_text((40+75*differentBoards),(455+20*count),fill="black",font="Times 10 bold",text=boardString)
                self.canvas.create_text((65+75*differentBoards),(455+20*count),fill="black",font="Times 10 bold",text=str(x[1]))
                print(x)
                count+=1
            differentBoards+=1
        if(self.board2x6.getLengths()):
            Set2x6Boards = SetBoards(getWoodCuts(self.board2x6,overCutPercent))
            self.canvas.create_rectangle((25), 425, (75+75*differentBoards), 580)
            self.canvas.create_text((47+75*differentBoards),435,fill="black",font="Times 12 bold",text=self.board2x6.getType())
            count =0
            for x in Set2x6Boards:
                boardString = str(x[0])+"ft-"
                self.canvas.create_text((40+75*differentBoards),(455+20*count),fill="black",font="Times 10 bold",text=boardString)
                self.canvas.create_text((65+75*differentBoards),(455+20*count),fill="black",font="Times 10 bold",text=str(x[1]))
                print(x)
                count+=1
            differentBoards+=1
        if(self.board2x8.getLengths()):
            Set2x8Boards = SetBoards(getWoodCuts(self.board2x8,overCutPercent))
            self.canvas.create_rectangle((25), 425, (75+75*differentBoards), 580)
            self.canvas.create_text((47+75*differentBoards),435,fill="black",font="Times 12 bold",text=self.board2x8.getType())
            count =0
            for x in Set2x8Boards:
                boardString = str(x[0])+"ft-"
                self.canvas.create_text((40+75*differentBoards),(455+20*count),fill="black",font="Times 10 bold",text=boardString)
                self.canvas.create_text((65+75*differentBoards),(455+20*count),fill="black",font="Times 10 bold",text=str(x[1]))
                print(x)
                count+=1
            differentBoards+=1
            

    def setLength(self,lengthVar,amountVar,board):
        for x in range(0,(amountVar).get()):
            board.addLength((lengthVar).get())
            print(board.getLengths())
            print((lengthVar).get())














def main():

    global overCutPercent 
    overCutPercent = False


    #board2x4 = Board("2x4",[6,8,12])
    #board2x4.addLength(4)
    #board2x4.addLength(4)
    #board2x4.addLength(8)
    #board2x4.addLength(10)
    #board2x4.addLength(5)
    #board2x4.addLength(2)
    #board2x4.addLength(7)
    #board2x4.addLength(1) 
    #board2x4.addLength(1) 
    #board2x4.addLength(1) 


    
    #boardSetPairs = getWoodCuts(board2x4,overCutPercent)
    #print(boardSetPairs)
    #boardPairs = SetBoards(boardSetPairs)
    #print(boardPairs)
    

    root = tk.Tk()
    root.geometry("640x600") 
    app = window(root)
    root.mainloop()

if(__name__ == "__main__"):
    main()

#sys.exit(0)