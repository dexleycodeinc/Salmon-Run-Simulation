"""
Hazard level is taking the average of 4 players' IDV and multiply by 0.2%. 
Result should then be displayed as a percentage
https://splatoonwiki.org/wiki/Salmon_Run_Next_Wave_data#:~:text=The%20quota%20and%20Hazard%20Level,equivalent%20to%20Eggsecutive%20VP%20865.

"""

def calculateIDV(playerInfo, job_title):
    IDV = 0
    for x in range(len(playerInfo)):
        # Get the player's title 
        title = playerInfo[x][0]
        titleIndex = job_title.index(title)

        IDV = IDV + (100 * titleIndex) + playerInfo[x][1]
    
    return IDV

def calculateHazardLevel(IDV):
    hazardLevel = IDV * .2
    return hazardLevel