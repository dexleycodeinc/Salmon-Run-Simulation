"""
playerStat.py is used to enter the Player's information.
Pass in the player number and job titles.
"""

def enterPlayer(playerNum, jobTitle):
    playerInfo = []
    
    # Display the list job titles
    print('\n\n 1) Apprentice, 2) Part-Timer, 3) Go-Getter, 4) Overachiever, 5) Profreshional Part-Timer, ' +
          '6) Profreshional + 1, 7) Profreshional +2, 8) Profreshional +3, 9) Eggsecutive VP')

    # While loop to check input for player's title
    checker = False
    while checker == False:

        # Input the player's title by number
        playerTitle = input('Player ' + str(playerNum) + '\'s job title: ')
        
        # Verify that input is a digit
        if playerTitle.isdigit():
            
            # Check if the digit is between 1 and 9
            if int(playerTitle) - 1 >= 0 and int(playerTitle) - 1 <= 8:
                # Append job title
                playerInfo.append(jobTitle[int(playerTitle) - 1])
                checker = True
             
        else:
            print("Please enter a value between 1 to 9")

        # Verify that input matches a job title
        """"
        for i in range(len(jobTitle)):
            titleCheck = jobTitle[i]
            if playerTitle.lower() == titleCheck.lower():
                #print('Player ' + str(playerNum) + ' is a(n) ' + jobTitle[i])
                
                # Add player's title to list
                playerInfo.append(playerTitle)
                checker = True
                break
        """
    # While loop to check input for player's rank
    checker = False
    while checker == False:
        
        # Input the player's Rank
        playerRank = input('Player ' + str(playerNum) + '\'s rank: ')

        # Error checking to make sure it's an int passed as input
        if playerRank.isnumeric() == False:
            print("Invalid input.")
        else:
            # Pass playerRank as int
            playerRank = int(playerRank)

            # Check if player is Eggsecutive VP as rank can range from 0-999
            # Rank can also be 999
            if int(playerTitle)-1 == 8:
                if  playerRank > 999 or playerRank < 0: 
                    print("Eggsecutive VP ranks range from 0-999")
                else:
                    # Add player's rank to list
                    playerInfo.append(playerRank)
                    checker = True

            # Otherwise check for range from 0-99 for other ranks
            elif playerRank > 99 or playerRank < 0:
                print("Ranks can range from 0-99 (except for Eggsecutive VP)")
            else:
                # Add player's rank to list
                playerInfo.append(playerRank)
                checker = True
#    print('Player ' + str(playerNum) + ' is ' + playerTitle + ' rank ' + str(playerRank))
    
    # Input the player's Salmonmeter level. Level between 0 and 5, inclusive
    checker = False
    while checker == False:
        playerSalmon = input('Player ' + str(playerNum) + '\'s Salmonmeter: ')
        if playerSalmon.isdigit() and int(playerSalmon) >= 0 and int(playerSalmon) <= 5:

            # Add player's Salmonmeter to list
            playerInfo.append(playerSalmon)
            checker = True
        else:
            print("Invalid input. Salmonmeter ranges from 0 to 5.")

    # Return the player's title and rank and Salmonmeter level
    return playerInfo
    
            
       