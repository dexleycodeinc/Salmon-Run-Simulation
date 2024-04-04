from IDV import *

class startSimulation:
    def __init__(self, playerStats, winRates, gameCount):
        self.playerStats = playerStats
        self.winRates = winRates
        self.gameCount = gameCount


    def start(self):
        IDV = calculateIDV(self.playerStats)
        print(IDV)