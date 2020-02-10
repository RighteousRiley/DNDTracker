class Character():
    def __init__(self):
        self.strength = -1
        self.dexterity = -1;
        self.constitution = -1
        self.intellect = -1
        self.wisdom = -1
        self.charisma = -1
        self.class_str = ""
        self.level = 0
        self.background = None
        self.race = ""
        self.alignment = ""
        self.xp = 0
        self.armor_class = None
        self.speed = None
        self.current_hitpoints = None
        self.temp_hit_points = None
        self.inventory = None
        self.proficiences = []
        self.character_name = ""
        self.player_name = ""
        self.character_sheet = None

    def __init__(self, strength, dexterity, constitution, intellect, wisdom, charisma):
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intellect = intellect
        self.wisdom = wisdom
        self.charisma = charisma
        self.class_str = ""
        self.level = 0
        self.background = None
        self.race = ""
        self.alignment = ""
        self.xp = 0
        self.armor_class = None
        self.speed = None
        self.current_hitpoints = None
        self.temp_hit_points = None
        self.inventory = None
        self.proficiences = []
        self.character_name = ""
        self.player_name = ""

    def set_strength(self, strength):
        self.strength = strength

    def get_strength(self):
        return self.strength

    def set_dexterity(self, dexterity):
        self.dexterity = dexterity

    def get_dexterity(self):
        return self.dexterity

    def set_constitution(self, num):
        self.constitution = num

    def get_constitution(self):
        return self.constitution

    def set_intellect(self, num):
        self.intellect = num

    def get_intellect(self):
        return self.intellect

    def set_wisdom(self, num):
        self.wisdom = num

    def get_wisdom(self):
        return self.wisdom

    def set_charisma(self, num):
        self.character_name = num

    def get_charisma(self):
        return self.charisma

    def set_class(self, class_str):
        self.charachter_class = class_str

    def get_class(self):
        return self.class_str

    def set_level(self, num):
        self.level = num

    def get_level(self):
        return self.level

    def set_background(self, background_story_str):
        self.background = background_story_str

    def get_background(self):
        return self.background

    def set_race(self, race):
        self.race = race

    def get_race(self):
        return self.race

    def set_alignment(self, alignment):
        self.alignment = alignment

    def get_alignment(self):
        return self.alignment

    def set_xp(self, num):
        self.xp = num

    def get_curr_xp(self):
        return self.xp

    def set_armor_class(self, class_name):
        self.armor_class = class_name

    def get_armor_class(self):
        return self.armor_class

    def set_speed(self, speed):
        self.speed = speed

    def get_speed(self):
        return self.speed

    def set_current_hitpoints(self, num):
        self.current_hitpoints = num

    def get_current_hp(self):
        return self.current_hitpoints

    def set_temp_hitpoints(self, num):
        self.temp_hit_points = num

    def get_temp_hp(self):
        return self.temp_hit_points

    def set_inventory(self, inventory_obj):
        self.inventory = inventory_obj

    def get_inventory(self):
        return inventory

    def add_proficiency(self, skill):
        self.proficiences.append(skill)

    def set_character_name(self, name):
        self.character_name = name

    def get_character_name(self):
        return self.character_name

    def set_player_name(self, name):
        self.player_name = name

    def get_player_name(self):
        return self.player_name

    def __str__(self):
        return ("" + "Character Name: " + str(self.get_character_name() + "\n") + \
        "-----------------------------------------" + "\n" + \
         "Strength: " + str(self.get_strength()) + "\n" + \
         "Dexterity: " + str(self.get_dexterity()) + "\n" + \
         "Constitution: " + str(self.get_constitution()) + "\n" + \
         "Intellect: " + str(self.get_intellect()) + "\n" + \
         "Wisdom: " + str(self.get_wisdom()) + "\n" + \
         "Charisma: " + str(self.get_charisma()) + "\n" + "\n")
