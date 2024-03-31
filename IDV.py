"""
Hazard level is taking the average of 4 players' IDV and multiply by 0.2%. 
Result should then be displayed as a percentage
https://splatoonwiki.org/wiki/Salmon_Run_Next_Wave_data#:~:text=The%20quota%20and%20Hazard%20Level,equivalent%20to%20Eggsecutive%20VP%20865.

"""
JOB_TITLES = ['Apprentice', 'Part-Timer', 'Go-Getter', 'Overachiever', 'Profreshional Part-Timer',
                'Profreshional +1', 'Profreshional +2', 'Profreshional +3', 'Eggsecutive VP']
def calculateIDV(playerInfo):
    IDV = 0
    for x in range(4):
        # Get the player's title 
        title = playerInfo[x][0]

        IDV = IDV + (100 * title) + int(playerInfo[x][1])
    
    return IDV

def calculateHazardLevel(IDV):
    hazardLevel = IDV * .2
    return hazardLevel