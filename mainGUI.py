from playerStat import enterPlayer
from IDV import *
from startSimulation import *
from tkinter import *
from tkinter import messagebox
from ttkbootstrap.constants import *
import ttkbootstrap as tb

JOB_TITLES = ['Apprentice', 'Part-Timer', 'Go-Getter', 'Overachiever', 'Profreshional Part-Timer',
                'Profreshional +1', 'Profreshional +2', 'Profreshional +3', 'Eggsecutive VP']

# Player stats
# Title (int), level (int), smell (int)
PLAYER_STATS = [[], [], [], []]

# Win rates
# Wave 1 (int), Wave 2 (int), Wave 3 (int), Boss (int)
WIN_RATES = []

def start_simulation():
    # Clear lists
    WIN_RATES.clear()
    for x in range(4):
        PLAYER_STATS[x].clear()

    # Take information from GUI and insert into PLAYER_STATS
    # Player 1
    PLAYER_STATS[0].append(player1_combo.current())
    PLAYER_STATS[0].append(player1_entry.get())
    PLAYER_STATS[0].append(player1_boss.get())

    # Player 2
    PLAYER_STATS[1].append(player2_combo.current())
    PLAYER_STATS[1].append(player2_entry.get())
    PLAYER_STATS[1].append(player2_boss.get())

    # Player 3
    PLAYER_STATS[2].append(player3_combo.current())
    PLAYER_STATS[2].append(player3_entry.get())
    PLAYER_STATS[2].append(player3_boss.get())

    # Player 4
    PLAYER_STATS[3].append(player4_combo.current())
    PLAYER_STATS[3].append(player4_entry.get())
    PLAYER_STATS[3].append(player4_boss.get())

    # Game Stats
    WIN_RATES.append(wave1Winrate_entry.get())
    WIN_RATES.append(wave2Winrate_entry.get())
    WIN_RATES.append(wave3Winrate_entry.get())
    WIN_RATES.append(bossWinrate_entry.get())

    # Validate user input for Entries
    passed = True
    for x in range(4):
        # Try if Player's level is an int
        check = PLAYER_STATS[x][1]
        try:
            check = int(check)
        except:
            messagebox.showerror("Player " + str(x + 1) + " Error", "Please enter a number for Player "
                                 + str(x + 1) + ".")
            passed = False
        else:
            rank = int(PLAYER_STATS[x][0])
            # No negative integers
            if check < 0:
                messagebox.showerror("Player " + str(x + 1) + " Error", "Player " + str(x + 1)
                                     + " cannot be a negative level.")
                passed = False
            # No larger numbers over 99. Exception is Eggsecutive VP at 999.
            elif rank == 8 and check > 999:
                messagebox.showerror("Player " + str(x + 1) + " Error", "Player " + str(x + 1)
                                     + " has too high level of a level.")
                passed = False
            elif rank != 8 and check > 99:
                messagebox.showerror("Player " + str(x + 1) + " Error", "Player " + str(x + 1)
                                     + " has too high level of a level.")
                passed = False
        # Try if player's boss meter is an int
        check = PLAYER_STATS[x][2]
        try:
            check = int(check)
        except:
            messagebox.showerror("Player " + str(x + 1) + " Error", "Please enter a number for Player "
                                 + str(x + 1) + "'s boss meter.")
            passed = False
        else:
            rank = int(PLAYER_STATS[x][2])
            if rank < 0 or rank > 5:
                messagebox.showerror("Player " + str(x + 1) + " Error", "Please enter a number between 0 and 5 "
                                    "for Player " + str(x + 1) + "'s boss meter.")
                passed = False

    # Validate user input for Wave/Boss win rates
    for x in range(4):
        check = WIN_RATES[x]
        try:
            check = int(check)
        except:
            messagebox.showerror("Wave " + str(x + 1) + " Error", "Please enter a number for Wave "
                                 + str(x + 1) + ".")
            passed = False
        else:
            if check < 0 or check > 100:
                messagebox.showerror("Wave " + str(x + 1) + " Error", "Please enter a number"
                                                                      " between 0 and 100.")
                passed = False

    if passed:
        print(*PLAYER_STATS)
        print(*WIN_RATES)
        #go = startSimulation(PLAYER_STATS)
        #go.start()

root = tb.Window(themename="superhero")
# root = Tk()

root.title("Player Select")
root.geometry('600x400')

# Crate Label for entering Rank and Level and Boss Meter
rank_label = tb.Label(root, text="Rank", font=("Helvetica", 18))
rank_label.grid(row=1, column=1, padx=5)

level_label = tb.Label(root, text="Level", font=("Helvetica", 18))
level_label.grid(row=1, column=2, padx=5)

boss_label = tb.Label(root, text="Boss Meter", font=("Helvetica", 18))
boss_label.grid(row=1, column=3, padx=5)

# Create Label for Player 1
player1_label = tb.Label(root, text="Player 1", font=("Helvetica", 18))
player1_label.grid(row=2, column=0, padx=5)

# Create Combobox for Player 1
player1_combo = tb.Combobox(root, state="readonly", bootstyle="success", values=JOB_TITLES)
player1_combo.grid(row=2, column=1, padx=5)

# Create Entry for Player 1's Level
player1_entry = tb.Entry(root)
player1_entry.insert(0, 0)
player1_entry.grid(row=2, column=2, padx=5)

# Create Entry for Player 1's boss meter
player1_boss = tb.Entry(root)
player1_boss.insert(0, 0)
player1_boss.grid(row=2, column=3, padx=5)

# Create Label for Player 2
player2_label = tb.Label(root, text="Player 2", font=("Helvetica", 18))
player2_label.grid(row=3, column=0, padx=5)

# Create Combobox for Player 2
player2_combo = tb.Combobox(root, state="readonly", bootstyle="success", values=JOB_TITLES)
player2_combo.grid(row=3, column=1, padx=5)

# Create Entry for Player 2's Level
player2_entry = tb.Entry(root)
player2_entry.insert(0, 0)
player2_entry.grid(row=3, column=2, padx=5)

# Create Entry for Player 2's boss meter
player2_boss = tb.Entry(root)
player2_boss.insert(0, 0)
player2_boss.grid(row=3, column=3, padx=5)

# Create Label for Player 3
player3_label = tb.Label(root, text="Player 3", font=("Helvetica", 18))
player3_label.grid(row=4, column=0, padx=5)

# Create Combobox for Player 3
player3_combo = tb.Combobox(root, state="readonly", bootstyle="success", values=JOB_TITLES)
player3_combo.grid(row=4, column=1, padx=5)

# Create Entry for Player 3's Level
player3_entry = tb.Entry(root)
player3_entry.insert(0, 0)
player3_entry.grid(row=4, column=2, padx=5)

# Create Entry for Player 3's boss meter
player3_boss = tb.Entry(root)
player3_boss.insert(0, 0)
player3_boss.grid(row=4, column=3, padx=5)

# Create Label for Player 4
player4_label = tb.Label(root, text="Player 4", font=("Helvetica", 18))
player4_label.grid(row=5, column=0, padx=5)

# Create Combobox for Player 4
player4_combo = tb.Combobox(root, state="readonly", bootstyle="success", values=JOB_TITLES)
player4_combo.grid(row=5, column=1, padx=5)

# Create Entry for Player 4's Level
player4_entry = tb.Entry(root)
player4_entry.insert(0, 0)
player4_entry.grid(row=5, column=2, padx=5)

# Create Entry for Player 4's boss meter
player4_boss = tb.Entry(root)
player4_boss.insert(0, 0)
player4_boss.grid(row=5, column=3, padx=5)

# Set Combobox default for Rank and Boss Meter
player1_combo.current(0)
player2_combo.current(0)
player3_combo.current(0)
player4_combo.current(0)

# Create Labels for Waves 1 t0 3
wave1_label = waveWinrate_label = tb.Label(root, text="Wave 1", font=("Helvetica", 18))
wave1_label.grid(row=6, column=1, padx=5, pady=(10, 5))

wave2_label = waveWinrate_label = tb.Label(root, text="Wave 2", font=("Helvetica", 18))
wave2_label.grid(row=6, column=2, padx=5, pady=(10, 5))

wave3_label = waveWinrate_label = tb.Label(root, text="Wave 3", font=("Helvetica", 18))
wave3_label.grid(row=6, column=3, padx=5, pady=(10, 5))


# Create Wave win rate Label
waveWinrate_label = tb.Label(root, text="Wave Win Rate (%)", font=("Helvetica", 10))
waveWinrate_label.grid(row=7, column=0, padx=5, pady=(0, 5))

# Create Wave 1 win rate Entry limit from 0 to 100
wave1Winrate_entry= tb.Entry(root)
wave1Winrate_entry.insert(0, 0)
wave1Winrate_entry.grid(row=7, column=1, padx=5, pady=(0, 5))

# Create Wave 2 win rate Entry limit from 0 to 100
wave2Winrate_entry= tb.Entry(root)
wave2Winrate_entry.insert(0, 0)
wave2Winrate_entry.grid(row=7, column=2, padx=5, pady=(0, 5))

# Create Wave 3 win rate Entry limit from 0 to 100
wave3Winrate_entry= tb.Entry(root)
wave3Winrate_entry.insert(0, 0)
wave3Winrate_entry.grid(row=7, column=3, padx=5, pady=(0, 5))


# Create Boss win rate Label
bossWinrate_label = tb.Label(root, text="Boss Win Rate (%)", font=("Helvetica", 10))
bossWinrate_label.grid(row=8, column=0, padx=5, pady=(20,0))

# Create Boss win rate Entry limit from 0 to 100
bossWinrate_entry= tb.Entry(root)
bossWinrate_entry.insert(0, 0)
bossWinrate_entry.grid(row=8, column=1, padx=5, pady=(20,0))

# Create start button
start_button = tb.Button(root, text="Run", command=start_simulation)
start_button.grid(pady=20)

root.mainloop()
