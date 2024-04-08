from IDV import *

class startSimulation:
    def __init__(self, playerStats, winRates, scaleCount, gameCount):
        self.playerStats = playerStats
        self.winRates = winRates
        self.scaleCount = scaleCount
        self.gameCount = gameCount
        print(*self.playerStats)
        print(*self.winRates)
        print(self.scaleCount)
        print(self.gameCount)


    def start(self):
        IDV = calculateIDV(self.playerStats)
        print(IDV)