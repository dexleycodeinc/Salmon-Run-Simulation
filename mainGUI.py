from playerStat import enterPlayer
from IDV import *
from tkinter import *
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
    PLAYER_STATS[0].append(player1_combo.current())
    PLAYER_STATS[0].append(player1_entry.get())
    print(*PLAYER_STATS)




root = tb.Window(themename="superhero")
# root = Tk()

root.title("Player Select")
root.geometry('800x700')

# Create Label for Player 1
player1_label = tb.Label(root, text="Player 1", font=("Helvetica", 18))
player1_label.pack()

# Create Combobox for Player 1
player1_combo = tb.Combobox(root, bootstyle="success", values=JOB_TITLES)
player1_combo.pack(pady=20)

# Create Entry for Player 1's Level
player1_entry = tb.Entry(root)
player1_entry.pack(pady=10)

# Create Label for Player 2
player2_label = tb.Label(root, text="Player 2", font=("Helvetica", 18))
player2_label.pack()

# Create Combobox for Player 2
player2_combo = tb.Combobox(root, bootstyle="success", values=JOB_TITLES)
player2_combo.pack(pady=20)

# Create Entry for Player 2's Level
player2_entry = tb.Entry(root)
player2_entry.pack(pady=10)

# Create Label for Player 3
player3_label = tb.Label(root, text="Player 3", font=("Helvetica", 18))
player3_label.pack()

# Create Combobox for Player 3
player3_combo = tb.Combobox(root, bootstyle="success", values=JOB_TITLES)
player3_combo.pack(pady=20)

# Create Entry for Player 3's Level
player3_entry = tb.Entry(root)
player3_entry.pack(pady=10)

# Create Label for Player 4
player4_label = tb.Label(root, text="Player 4", font=("Helvetica", 18))
player4_label.pack()

# Create Combobox for Player 3
player4_combo = tb.Combobox(root, bootstyle="success", values=JOB_TITLES)
player4_combo.pack(pady=20)

# Create Entry for Player 4's Level
player4_entry = tb.Entry(root)
player4_entry.pack(pady=10)

# Set Combobox default
player1_combo.current(0)
player2_combo.current(0)
player3_combo.current(0)
player4_combo.current(0)

# Create start button
start_button = tb.Button(root, text="Run", command=start_simulation)
start_button.pack(pady=20)

root.mainloop()
