import tkinter as tk
import copy
'''
    This is the actual GUI object of the form used to
    receive input from the user
'''
class Character_Inquirer:
    def __init__(self, character):
        self.character = character
        self.window = tk.Tk()
        self.labels = []
        self.entries = []
        self.responses = []
        self.ROW_COUNT = 7
        self.COL_COUNT = 3
        self.make_form()
        self.start()

    def get_character(self):
        return self.character

    '''
        Reads in all entries in the UI Grid and stores there values in the responses 2D list
        Reads what is currently in the box. There is no need to press enter, only the submit
        button.
    '''
    def get_form_data(self):
        for i in range(len(self.entries)):
            for j in range(len(self.entries[i])):
                res = self.entries[i][j]
                res_str = res.get()
                self.responses[i][j] = res_str

    def init_grid(self):
        grid = []
        for i in range(self.ROW_COUNT):
            grid.append([None, None, None])
        return grid

    def make_form(self):
        grid = self.init_grid()
        self.labels = copy.deepcopy(grid)
        self.entries = copy.deepcopy(grid)
        self.responses = copy.deepcopy(grid)
        LABEL_STRINGS = ["Character Name", "Class", "Level", "Race", "Background", "Faction", "Player Name", "XP Points",
         "Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma", "Armor Class", "Speed",
         "Personality Traits", "Ideals", "Bonds", "Starting Inventory", "Attacks"]
        index = 0
        row = 0
        for i in range(self.ROW_COUNT):
            col = 1
            for j in range(self.COL_COUNT):
                self.labels[i][j] = label_strings[index]

                new_label = tk.Label(self.window, text=label_strings[index]).grid(row=row, column = col)
                new_entry = tk.Entry(self.window)
                self.entries[i][j] = new_entry
                new_entry.grid(row=row, column=col + 1)
                index+=1
                col+=3
            row+= 2

       # form actions
        submit_button = tk.Button(text="Submit", command=self.get_form_data).grid(row=self.ROW_COUNT*2,column=4, sticky=tk.W,pady=4)
        quit_buttom = tk.Button(text="Quit", command=self.window.quit).grid(row=self.ROW_COUNT*2,column=7, sticky=tk.W,pady=4)

    def start(self):
        self.window.mainloop()
        tk.mainloop()
