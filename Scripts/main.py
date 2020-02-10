from character import Character
from character_inquirer import Character_Inquirer
import tkinter as tk

def get_character_count():
    return int(input("How many character are you keeping track of?\n"))

def assert_num(string_res):
    if(not string_res.isnumeric()):
        print("ENTER NUMBERS ONLY")
        exit(1)
'''
    Function gathers all information about the character from the user
'''
def character_inquiry(character):
    iq = Character_Inquirer(character)
    return iq

'''
    Builds each character the user wants to keep track of. Once each character is made,
    they are stored in a list, which is returned at the end of this function
'''
def build_characters(count):
    characters = []
    for i in range(count):
        character = Character(0,0,0,0,0,0)
        character_inquiry(character)
        characters.append(character)
    return characters

def print_stats(characters):
    for character in characters:
        print(character.__str__(), end="")

'''
Startup is in charge of loading the program up and to a state in which
is ready to be interact with users
'''
def startup():
    #character_count = get_character_count()
    characters = build_characters(1)
    #print_stats(characters)

def main():
    startup()

main()
