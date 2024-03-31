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

def start_simulation():
    # Clear list
    for x in range(4):
        PLAYER_STATS[x].clear()

    # Take information from GUI and insert into PLAYER_STATS
    # Player 1
    PLAYER_STATS[0].append(player1_combo.current())
    PLAYER_STATS[0].append(player1_entry.get())

    # Player 2
    PLAYER_STATS[1].append(player2_combo.current())
    PLAYER_STATS[1].append(player2_entry.get())

    # Player 3
    PLAYER_STATS[2].append(player3_combo.current())
    PLAYER_STATS[2].append(player3_entry.get())

    # Player 4
    PLAYER_STATS[3].append(player4_combo.current())
    PLAYER_STATS[3].append(player4_entry.get())

    # Validate user input for Entries
    passed = False
    for x in range(4):

        # Try if Player's level is an int
        check = PLAYER_STATS[x][1]
        try:
            check = int(check)
        except:
            messagebox.showerror("Player " + str(x + 1) + " Error", "Please enter a number for Player "
                                 + str(x + 1) + ".")
        else:
            rank = int(PLAYER_STATS[x][0])
            # No negative integers
            if check < 0:
                messagebox.showerror("Player " + str(x + 1) + " Error", "Player " + str(x + 1)
                                     + " cannot be a negative level.")

            # No larger numbers over 99. Exception is Eggsecutive VP at 999.
            elif rank == 8 and check > 999:
                messagebox.showerror("Player " + str(x + 1) + " Error", "Player " + str(x + 1)
                                     + " has too high level of a level.")
            elif rank != 8 and check > 99:
                messagebox.showerror("Player " + str(x + 1) + " Error", "Player " + str(x + 1)
                                     + " has too high level of a level.")
            else:
                passed = True

    print(*PLAYER_STATS)
    if passed:
        go = startSimulation(PLAYER_STATS)
        go.start()

root = tb.Window(themename="superhero")
# root = Tk()

root.title("Player Select")
root.geometry('600x400')

# Crate Label for entering Rank and Level
rank_label = tb.Label(root, text="Rank", font=("Helvetica", 18))
rank_label.grid(row=1, column=1, padx=5)

level_label = tb.Label(root, text="Level", font=("Helvetica", 18))
level_label.grid(row=1, column=2, padx=5)

# Create Label for Player 1
player1_label = tb.Label(root, text="Player 1", font=("Helvetica", 18))
player1_label.grid(row=2, column=0, padx=5)

# Create Combobox for Player 1
player1_combo = tb.Combobox(root, state="readonly", bootstyle="success", values=JOB_TITLES)
player1_combo.grid(row=2, column=1, padx=5)

# Create Entry for Player 2's Level
player1_entry = tb.Entry(root)
player1_entry.grid(row=2, column=2, padx=5)

# Create Label for Player 2
player2_label = tb.Label(root, text="Player 2", font=("Helvetica", 18))
player2_label.grid(row=3, column=0, padx=5)

# Create Combobox for Player 2
player2_combo = tb.Combobox(root, state="readonly", bootstyle="success", values=JOB_TITLES)
player2_combo.grid(row=3, column=1, padx=5)

# Create Entry for Player 2's Level
player2_entry = tb.Entry(root)
player2_entry.grid(row=3, column=2, padx=5)

# Create Label for Player 3
player3_label = tb.Label(root, text="Player 3", font=("Helvetica", 18))
player3_label.grid(row=4, column=0, padx=5)

# Create Combobox for Player 3
player3_combo = tb.Combobox(root, state="readonly", bootstyle="success", values=JOB_TITLES)
player3_combo.grid(row=4, column=1, padx=5)

# Create Entry for Player 3's Level
player3_entry = tb.Entry(root)
player3_entry.grid(row=4, column=2, padx=5)

# Create Label for Player 4
player4_label = tb.Label(root, text="Player 4", font=("Helvetica", 18))
player4_label.grid(row=5, column=0, padx=5)

# Create Combobox for Player 3
player4_combo = tb.Combobox(root, state="readonly", bootstyle="success", values=JOB_TITLES)
player4_combo.grid(row=5, column=1, padx=5)

# Create Entry for Player 4's Level
player4_entry = tb.Entry(root)
player4_entry.grid(row=5, column=2, padx=5)

# Set Combobox default
player1_combo.current(0)
player2_combo.current(0)
player3_combo.current(0)
player4_combo.current(0)

# Create start button
start_button = tb.Button(root, text="Run", command=start_simulation)
start_button.grid(pady=20)

root.mainloop()
