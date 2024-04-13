from IDV import *

import random

JOB_TITLES = ['Apprentice', 'Part-Timer', 'Go-Getter', 'Overachiever', 'Profreshional Part-Timer',
                'Profreshional +1', 'Profreshional +2', 'Profreshional +3', 'Eggsecutive VP']

class startSimulation:
    # Constructor
    def __init__(self, playerStats, winRates, scaleCount, gameCount):
        # Player stats
        # Title (int), level (int), smell (int)
        self.playerStats = playerStats

        # Win rates
        # Wave 1 (int), Wave 2 (int), Wave 3 (int), Boss (int)
        self.winRates = winRates
        self.scaleCount = scaleCount
        self.gameCount = gameCount
        self.IDV = 0
        self.hazardLevel = 0
        self.gameNumber = 0

        # Types of scales earned
        # Bronze (int), Silver (int), Gold (int)
        self.scaleType = []

        self.IDV = calculateIDV(self.playerStats)
        self.hazardLevel = calculateHazardLevel(self.IDV)
        # random.seed()

        #self.printGameStat()

        self.start()

    def start(self):
        random.seed()
        #print('pass')
        #self.printGameStat()
       # print(self.playerStats)

        # Set the Xtrawave/Boss chance before starting
        self.setBossChance()
        self.printGameStat()

        print()

        # Cycle through the number of games
        gameSuccess = True
        for x in range(self.gameCount):
            self.gameNumber += 1

            # Go through Waves 1 to 3
            for y in range(1, 4):
                # Set the probability of winning Wave y
                randNum = random.randint(0, 100)

                # If the winRate for Wave y is less than the randomly generated number
                if int(self.winRates[y-1]) < randNum:
                    self.waveLoss(y)
                    gameSuccess = False
                    # Break out of loop if loss at a wave
                    break
            # If the team wins all 3 waves, then go to waveWon()
            if gameSuccess:
                self.waveWon()

            # Reset gameSuccess to True
            gameSuccess = True



    def printGameStat(self):
        print("Game " + str(self.gameNumber))

        #print("Player " + str(1) + ": " + JOB_TITLES[int(self.playerStats[0][0])] + " " +
              #self.playerStats[0][1])

        # Print each player's stats
        for x in range(4):
            print("Player " + str(x+1) + ": " + JOB_TITLES[int(self.playerStats[x][0])] + " " +
                  str(self.playerStats[x][1]))

    def setBossChance(self):
        # The chance of a Boss wave (Xtrawave) is based off of the statistics provided by:
        # https://splatoonwiki.org/wiki/Xtrawave#Salmometer
        meterStats = [0, 0, 0, 0, 0, 1.5625, 3.75, 6.5625, 10, 14.0625, 18.75, 24.0625,
                      30, 36.5625, 43.75, 51.5625, 60, 69.0625, 78.75, 89.0625, 100]
        meterTotal = 0
        for x in range(4):
            meterTotal += int(self.playerStats[x][2])
        #print("Meter total is " + str(meterTotal))
        #print("Boss chance is: " + str(meterStats[meterTotal]) + "%")

    def increaseBossChance(self):
        # Increase each player's boss chance by 1 up to a max of 5
        for x in range(4):
            if int(self.playerStats[x][2]) < 5:
                self.playerStats[x][2] = int(self.playerStats[x][2]) + 1
        # Set the new boss chance
        self.setBossChance()

    def resetBossChance(self):
        # Reset all player's 'smell' to 0
        for x in range(4):
            self.playerStats[x][2] = 0
        # Set the new boss chance
        self.setBossChance()

    def waveLoss(self, waveNum):
        # Lost at wave 1
        if waveNum == 1:
            # Decrease level by 20 for all players
            for x in range(4):
                self.playerStats[x][1] = int(self.playerStats[x][1]) - 20
                if int(self.playerStats[x][1]) < 0:
                    self.demote(x)

        # Lost at wave 2
        elif waveNum == 2:
            for x in range(4):
                self.playerStats[x][1] = int(self.playerStats[x][1]) - 10
                if int(self.playerStats[x][1]) < 0:
                    self.demote(x)

        # Lost at Wave 3
        # Do nothing

        # Increase "smell" meter after determing wave loss
        self.increaseBossChance()
        self.printGameStat()

    def waveWon(self):
        # Determine a chance for a boss to appear

        # If boss appears, reset all 'smell' to 0 and startup Xtrawave

        # If boss does not appear, increase 'smell' meter

        # Increase all player's level by 20
        for x in range(4):
            self.playerStats[x][1] = int(self.playerStats[x][1]) + 20
            # Only promote ranks other than Eggsecutive VP
            if int(self.playerStats[x][1]) > 99 and int(self.playerStats[x][0]) != 8:
                self.promote(x)
            # Prevent going above Eggsecutive VP 999
            elif int(self.playerStats[x][1] > 999 and int(self.playerStats[x][0]) == 8):
                self.playerStats[x][1] = 999

        self.printGameStat()

    def demote(self, playerNumber):
        # Can't go below Apprentice
        if int(self.playerStats[playerNumber][0]) == 0:
            self.playerStats[playerNumber][1] = 0
        else:
            # Demote and set new rank to 40
            self.playerStats[playerNumber][0] = int(self.playerStats[playerNumber][0]) - 1
            self.playerStats[playerNumber][1] = 40

    def promote(self, playerNumber):
        self.playerStats[playerNumber][0] = int(self.playerStats[playerNumber][0]) + 1
        self.playerStats[playerNumber][1] = 40
