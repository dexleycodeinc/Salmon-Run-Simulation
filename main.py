from playerStat import enterPlayer
from IDV import *
from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as tb

import numpy as np

PLAYERS_INFO = []
JOB_TITLES = ['Apprentice', 'Part-Timer', 'Go-Getter', 'Overachiever', 'Profreshional Part-Timer', 
                'Profreshional +1', 'Profreshional +2', 'Profreshional +3', 'Eggsecutive VP']
IDV = 0
HAZARD_LEVEL = 0

# Main function to start off everything
def main():
    global IDV
    global HAZARD_LEVEL
    global PLAYERS_INFO
    # Input the title and ranks of the 4 players
    for i in range(4):
        PLAYERS_INFO.append(enterPlayer((i+1), JOB_TITLES))

    IDV = calculateIDV(PLAYERS_INFO, JOB_TITLES)
    HAZARD_LEVEL = calculateHazardLevel(IDV)

    # Check information of players
    playerInfoCheck()
'''
    #Ask how many bosses to encounter before ending simulation
    bossCount = 0
    bossCountCheck = False
    while bossCountCheck == False:
        #bossCount = input('# of King Salmonds to encounter: ')
        if bossCount.isdigit():
            bossCountCheck = True
            break
'''

    
# Function to display all 4 player's title, rank, and Salmonmeter    
def playerInfoCheck():
    global IDV
    global HAZARD_LEVEL
    for x in PLAYERS_INFO:
        print(x)
    print(IDV)
    print(HAZARD_LEVEL)

def tkinerWindow():

    root = tb.Window(themename="superhero")
    #root = Tk()

    root.title("Player Select")
    root.geometry('500x350')

    # Create Label for Player 1
    player1_label = tb.Label(root, text="Player 1", font=("Helvetica", 18))
    player1_label.pack()

    # Create Combobox for Player 1
    player1_combo = tb.Combobox(root, bootstyle="success", values=JOB_TITLES)
    player1_combo.pack(pady=20)

    
    root.mainloop()

#main()
tkinerWindow()