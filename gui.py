import tkinter as tk
from TicTacToe import *
from TicTacToe_MiniMax import *
from minRiskClassifier import *
import tkinter.font as tkFont
from logisticRegressionClassifier import *
from decisionTreeClassifier import *

class TicTacToeGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tic Tac Toe")
        self.player = "X"
        self.board = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']
        ]
        self.round = 1
        self.predictionsDisplayed = True

        self.buttons = [[" " for _ in range(3)] for _ in range(3)]

        # Create tic tac toe board
        for i in range(3):
            for j in range(3):
                num = ((i*3) + j) + 1
                button = tk.Button(self.root, text=str(num) + "                   \n\n\n\n", font=("Arial", 10), width=10, height=5, command=lambda row=i, col=j: self.clicked(row, col))
                button.grid(row=i, column=j)
                self.buttons[i][j] = button

        # Create Reset Button
        self.resetButton = tk.Button(self.root, text="Reset", width=10, height=5, command=lambda: self.resetGame())
        self.resetButton.grid(row=4, column=0)

        # Label and Value for board map
        self.mapLabel = tk.Label(self.root, text="Map: ")
        self.mapLabel.grid(row=3, column=1)
        self.mapVal = tk.Label(self.root, text="1|2|3\n4|5|6\n7|8|9")
        f = tkFont.Font(self.mapVal, self.mapVal.cget("font"))
        f.configure(underline = True)
        self.mapVal.configure(font=f)
        self.mapVal.grid(row=3, column=2)
        
        # Create Current Round Val and Label
        self.currentRoundLabel = tk.Label(self.root, text="Round:", width=15)
        self.currentRoundLabel.grid(row=0, column=3)
        self.currentRoundVal = tk.Label(self.root, text=self.round, width=10)
        self.currentRoundVal.grid(row=0, column=4)

        # Create Current Turn Val and Label
        self.currentTurnLabel = tk.Label(self.root, text="Current Turn:")
        self.currentTurnLabel.grid(row=1, column=3)
        self.currentTurnVal = tk.Label(self.root, text="X")
        self.currentTurnVal.grid(row=1, column=4)
        
        # Label and Value for Game Status
        self.statusLabel = tk.Label(self.root, text="Status:")
        self.statusLabel.grid(row=2, column=3)
        self.statusVal = tk.Label(self.root, text="Ongoing")
        self.statusVal.grid(row=2, column=4)


        # Label and Value for Classifiers Column
        self.classifierHeaderLabel = tk.Label(self.root, text="Classsifiers for:", width=25, height=5, borderwidth=1, relief="ridge")
        self.classifierHeaderLabel.grid(row=0, column=5)
        self.classifierHeaderVal = tk.Label(self.root, text="X", width=10, height=5, borderwidth=1, relief="ridge")
        self.classifierHeaderVal.grid(row=0, column=6)
        self.classifierHeaderProb = tk.Label(self.root, text="Probability", width=20, height=5, borderwidth=1, relief="ridge")
        self.classifierHeaderProb.grid(row=0, column=7)


        # minRiskMoveAndProb = getNextBestMoveMinRisk([0,0,0,0,0,0,0,0,0], 1)
        minRiskMoveAndProb = minRiskClassifier([0,0,0,0,0,0,0,0,0], 1)

        # Label and Value for Minimum Risk Classifier for X
        self.minRiskXClassifierLabel = tk.Label(self.root, text="MinRisk Classifier:", width=25, height=5, borderwidth=1, relief="ridge")
        self.minRiskXClassifierLabel.grid(row=1, column=5)
        self.minRiskXClassifierVal = tk.Label(self.root, text=str(minRiskMoveAndProb[0]))
        self.minRiskXClassifierVal.grid(row=1, column=6)
        self.minRiskXClassifierProb = tk.Label(self.root, text=str(round(minRiskMoveAndProb[1], 5)))
        self.minRiskXClassifierProb.grid(row=1, column=7)


        logisticRegressionMoveAndProb = logisticRegressionClassifier([0,0,0,0,0,0,0,0,0], 1)
        # Label and Value for Logistic Regression Classifier for X
        self.logRegXClassifierLabel = tk.Label(self.root, text="Logistic Regression Classifier:", width=25, height=5, borderwidth=1, relief="ridge")
        self.logRegXClassifierLabel.grid(row=2, column=5)
        self.logRegXClassifierVal = tk.Label(self.root, text=str(logisticRegressionMoveAndProb[0]))
        self.logRegXClassifierVal.grid(row=2, column=6)
        self.logRegXClassifierProb = tk.Label(self.root, text=str(round(logisticRegressionMoveAndProb[1], 5)))
        self.logRegXClassifierProb.grid(row=2, column=7)


        nextMinimaxMove = get_best_move_minimax(self.board, self.player)
        # Label and Value for Minimax Recommendation
        self.minimaxLabel = tk.Label(self.root, text="Minimax Classifier:", width=25, height=5, borderwidth=1, relief="ridge")
        self.minimaxLabel.grid(row=3, column=5)
        self.minimaxVal = tk.Label(self.root, text=str(self.colRowToVectorVal(nextMinimaxMove[1], nextMinimaxMove[0])))
        self.minimaxVal.grid(row=3, column=6)

        self.decTreeLabel = tk.Label(self.root, text="Decision Tree\nPredicted Winner:", width=15, height=5, borderwidth=1, relief="ridge")
        self.decTreeLabel.grid(row=4, column=3)
        self.decTreeVal = tk.Label(self.root, text=decisionTreeClassifier([0,0,0,0,0,0,0,0,0], 1))
        self.decTreeVal.grid(row=4, column=4)

        self.displayPredictions = tk.Button(self.root, text="Hide\nPredictions", width=10, height=5, command=lambda: self.showHidePredictions())
        self.displayPredictions.grid(row=4, column=7)


    def setPlayer(self, player):
        self.player = player

    def getPlayerNum(self):
        if self.player == "X":
            return 1
        elif self.player == "O":
            return -1
        else:
            return 0

    def clicked(self, row, col):
        
        button = self.buttons[row][col]

        # if button["text"] == "":
        if self.board[row][col] == ' ':
            self.board[row][col] = self.player
            button["text"] = self.player
            # button["font"] = ("Arial", 10)
            # button["height"] = 1
            # button["width"] = 4
            # button["pady"] = 5

            winner = self.has_winner()
            if winner != None:
                self.updateWinnerDisplay(winner)
                # self.setTurnLabel("Winner: " + winner)
            else: 
                if self.player == "X":
                    self.setTurnLabel("O")
                    self.setPlayer("O")
                elif self.player == "O":
                    self.setTurnLabel("X")
                    self.setPlayer("X")
                
                self.updateRoundDisplay()

                # Check if the board is full
                empty = self.has_empty()
                if empty == False:
                    self.setStatusLabel("Draw!")
                    self.setStatusVal("")
                else:
                    self.updateRecs()


    def resetGame(self):
        self.setRound(1)
        self.setRoundVal("1")
        self.setPlayer("X")
        self.setTurnLabel(self.player)
        self.setStatusLabel("Status:")
        self.setStatusVal("Ongoing")
        self.setHeaderVal("X")

        for i in range(3):
            for j in range(3):
                num = ((i*3) + j) + 1
                self.buttons[i][j]["text"] = str(num) + "                   \n\n\n\n"
                # self.buttons[i][j]["font"] = ("Arial", 10)
                # self.buttons[i][j]["height"] = 5
                # self.buttons[i][j]["width"] = 10
                self.board[i][j] = ' '

        # minRiskMoveAndProb = getNextBestMoveMinRisk([0,0,0,0,0,0,0,0,0], 1)
        minRiskMoveAndProb = minRiskClassifier([0,0,0,0,0,0,0,0,0], 1)
        self.setMinRiskXVal(minRiskMoveAndProb[0])
        self.setMinRiskXProb(round(minRiskMoveAndProb[1], 5))

        logisticRegressionMoveAndProb = logisticRegressionClassifier([0,0,0,0,0,0,0,0,0], 1)
        self.setLogRegXVal(logisticRegressionMoveAndProb[0])
        self.setLogRegXProb(round(logisticRegressionMoveAndProb[1], 5))

        nextMinimaxMove = get_best_move_minimax(self.board, self.player)
        self.setMinimaxVal(str(self.colRowToVectorVal(nextMinimaxMove[1], nextMinimaxMove[0])))

        decTreePred = decisionTreeClassifier([0,0,0,0,0,0,0,0,0], 1)
        self.setDecTreeVal(decTreePred)

    def showHidePredictions(self):
        # Hide all prediction stuff
        if self.predictionsDisplayed == True:
            self.predictionsDisplayed = False
            self.setMinRiskXVal("-")
            self.setLogRegXVal("-")
            self.setMinimaxVal("-")
            self.setMinRiskXProb("-")
            self.setLogRegXProb("-")
            self.setDecTreeVal("-")
            self.setDisplayPred("Display\nPredictions")
        else:
            self.setDisplayPred("Hide\nPredictions")
            self.predictionsDisplayed = True
            self.updateRecs()

    def setTurnLabel(self, content):
        self.currentTurnVal["text"] = content

    def setMinRiskXVal(self, content):
        self.minRiskXClassifierVal["text"] = content

    def setMinRiskXProb(self, content):
        self.minRiskXClassifierProb["text"] = content

    def setLogRegXVal(self, content):
        self.logRegXClassifierVal["text"] = content

    def setLogRegXProb(self, content):
        self.logRegXClassifierProb["text"] = content

    def setStatusLabel(self, content):
        self.statusLabel["text"] = content

    def setStatusVal(self, content):
        self.statusVal["text"] = content

    def setRound(self, round):
        self.round = round

    def setRoundVal(self, content):
        self.currentRoundVal["text"] = content

    def setMinimaxVal(self, content):
        self.minimaxVal["text"] = content

    def setDecTreeVal(self, content):
        self.decTreeVal["text"] = content

    def setHeaderVal(self, content):
        self.classifierHeaderVal["text"] = content
    
    def setDisplayPred(self, content):
        self.displayPredictions["text"] = content

    def updateRoundDisplay(self):
        self.setRound(self.round + 1)
        self.setRoundVal(self.round)
        self.setHeaderVal(self.player)

    def updateWinnerDisplay(self, winner):
        self.setStatusLabel("Winner: ")
        self.setStatusVal(str(winner))

    def has_winner(self):
        # check rows for winner
        for row in self.board:
            if row[0] == row[1] == row[2] and row[0] != ' ':
                return row[0]

        # check columns for winner
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] and self.board[0][col] != ' ':
                return self.board[0][col]

        # check diagonals for winner
        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] != ' ':
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] != ' ':
            return self.board[0][2]
        
    def has_empty(self):
        for row in self.board:
            for col in range(3):
                if row[col] == ' ':
                    return True
        return False
    
    def transformBoard(self):
        transformedBoard = list()

        for row in self.board:
            for col in range(3):
                if row[col] == "X":
                    transformedBoard.append(1)
                elif row[col] == "O":
                    transformedBoard.append(-1)
                else:
                    transformedBoard.append(0)
        return transformedBoard
    
    def updateRecs(self):
        if self.predictionsDisplayed == True and self.has_empty() == True:
            board = self.transformBoard()
            if self.player == "X":
                player = 1
            elif self.player == "O":
                player = -1
            else:
                player = 0

            decTreePrediction = decisionTreeClassifier(board, player)
            self.setDecTreeVal(decTreePrediction)

            # nextMoveMinRisk = getNextBestMoveMinRisk(board, player)
            nextMoveMinRisk = minRiskClassifier(board, player)
            nextMoveLogReg = logisticRegressionClassifier(board, player)
            nextMoveMinimax = get_best_move_minimax(self.board, self.player)

            self.setMinRiskXVal(str(nextMoveMinRisk[0]))
            self.setMinRiskXProb(str(round(nextMoveMinRisk[1], 5)))

            self.setLogRegXVal(str(nextMoveLogReg[0]))
            self.setLogRegXProb(str(round(nextMoveLogReg[1], 5)))

            self.setMinimaxVal(str(self.colRowToVectorVal(nextMoveMinimax[1], nextMoveMinimax[0])))
    
    def colRowToVectorVal(self, col, row):
        vectorVal = (row*3) + (col+1)
        return vectorVal


    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    gui = TicTacToeGUI()
    gui.run()
