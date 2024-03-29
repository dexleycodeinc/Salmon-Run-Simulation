from playerStat import enterPlayer
from IDV import *
from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as tb

JOB_TITLES = ['Apprentice', 'Part-Timer', 'Go-Getter', 'Overachiever', 'Profreshional Part-Timer',
                'Profreshional +1', 'Profreshional +2', 'Profreshional +3', 'Eggsecutive VP']

root = tb.Window(themename="superhero")
# root = Tk()

root.title("Player Select")
root.geometry('600x500')

# Create Label for Player 1
player1_label = tb.Label(root, text="Player 1", font=("Helvetica", 18))
player1_label.pack()

# Create Combobox for Player 1
player1_combo = tb.Combobox(root, bootstyle="success", values=JOB_TITLES)
player1_combo.pack(pady=20)

# Create Label for Player 2
player2_label = tb.Label(root, text="Player 2", font=("Helvetica", 18))
player2_label.pack()

# Create Combobox for Player 2
player2_combo = tb.Combobox(root, bootstyle="success", values=JOB_TITLES)
player2_combo.pack(pady=20)

# Create Label for Player 3
player3_label = tb.Label(root, text="Player 3", font=("Helvetica", 18))
player3_label.pack()

# Create Combobox for Player 3
player3_combo = tb.Combobox(root, bootstyle="success", values=JOB_TITLES)
player3_combo.pack(pady=20)

# Create Label for Player 4
player4_label = tb.Label(root, text="Player 4", font=("Helvetica", 18))
player4_label.pack()

# Create Combobox for Player 3
player4_combo = tb.Combobox(root, bootstyle="success", values=JOB_TITLES)
player4_combo.pack(pady=20)

# Set Combobox default
player1_combo.current(0)
player2_combo.current(0)
player3_combo.current(0)
player4_combo.current(0)

root.mainloop()