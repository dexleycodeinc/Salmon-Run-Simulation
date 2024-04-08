from IDV import *

class startSimulation:
    # Constructor
    def __init__(self, playerStats, winRates, scaleCount, gameCount):
        self.playerStats = playerStats
        self.winRates = winRates
        self.scaleCount = scaleCount
        self.gameCount = gameCount
        self.IDV = 0
        self.hazardLevel = 0

        self.IDV = calculateIDV(self.playerStats)
        self.hazardLevel = calculateHazardLevel(self.IDV)

        print(*self.playerStats)
        print(*self.winRates)
        print(self.scaleCount)
        print(self.gameCount)
        print("IDV: " + str(self.IDV))
        print("Hazard level: " + str(self.hazardLevel))


    def start(self):
        print('pass')