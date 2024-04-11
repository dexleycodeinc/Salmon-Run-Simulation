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
        self.setBossChance()

    def printGameStat(self):
        print("Game " + str(self.gameNumber))

        #print("Player " + str(1) + ": " + JOB_TITLES[int(self.playerStats[0][0])] + " " +
              #self.playerStats[0][1])

        # Print each player's stats
        for x in range(4):
            print("Player " + str(x+1) + ": " + JOB_TITLES[int(self.playerStats[x][0])] + " " +
                  self.playerStats[x][1])

    def setBossChance(self):
        # The chance of a Boss wave (Xtrawave) is based off of the statistics provided by:
        # https://splatoonwiki.org/wiki/Xtrawave#Salmometer
        meterStats = [0, 0, 0, 0, 0, 1.5625, 3.75, 6.5625, 10, 14.0625, 18.75, 24.0625,
                      30, 36.5625, 43.75, 51.5625, 60, 69.0625, 78.75, 89.0625, 100]
        meterTotal = 0
        for x in range(4):
            meterTotal += int(self.playerStats[x][2])
        print("Meter total is " + str(meterTotal))
        print("Boss chance is: " + str(meterStats[meterTotal]) + "%")