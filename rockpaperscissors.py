from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont, QStandardItemModel, QStandardItem
from PyQt5 import uic
import random as rd

class RPS(QMainWindow):

    def __init__(self):
        super(RPS, self).__init__()
        uic.loadUi("rockpaperscissors.ui", self)
        self.show()

        self.setFixedSize(646, 575)

        self.setWindowTitle("Rock-Paper-Scissors v0.1")
        self.model = QStandardItemModel()
        self.playerDisplay.setFont(QFont("MS Shell", 13))
        self.compDisplay.setFont(QFont("MS Shell", 13))
        self.resultDisplay.setFont(QFont("MS Shell", 12))

        self.rockButton.clicked.connect(self.rock)
        self.paperButton.clicked.connect(self.paper)
        self.scissorsButton.clicked.connect(self.scissors)
        self.playagainButton.clicked.connect(self.play_again)


    def play(self, player_choice):
        computers_choice = rd.choice(['Rock', 'Paper', 'Scissors'])

        comment = ''

        if computers_choice == player_choice:
            comment = f'Both players selected {player_choice}, Its a tie!!!'

        elif (computers_choice == 'Rock' and player_choice == 'Scissors'):
            comment = f'Rock smashes Scissors, You lose!!!'

        elif (computers_choice == 'Scissors' and player_choice == 'Paper'):
            comment = f'Scissors cuts Paper, You lose!!!'

        elif (computers_choice == 'Paper' and player_choice == 'Rock'):
            comment = f'Paper covers Rock, You lose!!!'

        elif (player_choice == 'Paper' and computers_choice == 'Rock'):
            comment = f'Paper covers Rock, You Win!!!'

        elif (player_choice == 'Rock' and computers_choice == 'Scissors'):
            comment = f'Rock smashes Scissors, You Win!!!'

        elif (player_choice == 'Scissors' and computers_choice == 'Paper'):
            comment = f'Scissors cuts Paper, You Win!!!'

        self.playerDisplay.setText(player_choice)
        self.compDisplay.setText(computers_choice)
        self.resultDisplay.setText(comment)

    def rock(self):
        self.play(player_choice = 'Rock')
        

    def paper(self):
        self.play(player_choice = 'Paper')


    def scissors(self):
        self.play(player_choice = 'Scissors')


    def pressed(self, presses):
        if presses == "Play Again!!!":
            self.playerDisplay.setText("")
            self.compDisplay.setText("")
            self.resultDisplay.setText("")

    def play_again(self,presses):
        clicked = self.pressed('Play Again!!!')


app = QApplication([])
window = RPS()
app.exec()








'''
def rock_paper_scissors(comp, user):
    print("Computer:", comp,"and", "User:", user)
    if comp==user:
        print("Tie!!!\n")
    elif (comp == "Rock" and user == "Paper") or (comp == "Scissors" and user == "Rock") or (comp == "Paper" and user == "Scissors"):
        print("User wins :)\n")
    else:
        print("User lose :(\n")

rock_paper_scissors_list = ['Rock','Paper','Scissors']
computers_choice = rd.choice(rock_paper_scissors_list)

while True:
    print("Press\n 1.Rock\n 2.Paper\n 3.Scissors\n")
    user_input = int(input("Enter your choice:"))
    user_choice = rock_paper_scissors_list[user_input - 1]
    rock_paper_scissors(computers_choice, user_choice)
    
'''
