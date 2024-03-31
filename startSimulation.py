from IDV import *

class startSimulation:
    def __init__(self, playerStats):
        self.playerStats = playerStats




    def start(self):
        IDV = calculateIDV(self.playerStats)
        print(IDV)