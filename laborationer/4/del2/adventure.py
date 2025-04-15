#!/usr/bin/env python3
#
# A text-based adventure game, based on
# https://github.com/codinggrace/text_based_adventure_game
#
# MIT License
# Copyright (c) 2020 Coding Grace
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import gamedata
import pictures

def get_next_state(state):
    desc = gamedata.DESCRIPTIONS.get(state)
    if desc:
        print(desc)

    options = gamedata.ADVENTURE_TREE[state]
    if len(options) == 1:
        return options[0]
    
    for i, state in enumerate(options):
        print("{} {}".format(i + 1, state))

    inp = None
    while inp == None or inp >= len(options):
        inp = int(input(">> ")) - 1
    
    return options[inp]

def main():
    name = input("What's your name?\n>> ")
    print("Welcome {} to the adventure of your life. Try to survive and find the treasure!".format(name.upper()))

    current_state = "Start"

    while current_state != "End":
        pictures.print_pic(current_state)
        current_state = get_next_state(current_state)

    pictures.print_pic(current_state)

# if __name__ == "__main__":
#     name = input("What's your name?\n>> ")
#     print("Welcome {} to the adventure of your life. Try to survive and find the \
#     treasure!".format(name.upper()))

#     current_state = "Start"
#     succ_states = gamedata.ADVENTURE_TREE[current_state]

#     while (current_state != "End"):
#         print(gamedata.DESCRIPTIONS[current_state])
#         for i, state in enumerate(succ_states):
#             print("{} {}".format(i + 1, state))

#         inp = None
#         while not inp or inp >= len(succ_states):
#             inp = int(input(">> "))
        
#         current_state = succ_states[inp]
    

#     if inp == "1":
#         text_box = "{}\n{}  {}\n{}  {}".format(gamedata.DESCRIPTIONS["Blue"],
#                                             "1", gamedata.OPTIONS["Chest"],
#                                             "2", gamedata.OPTIONS["Guard"])
#         print(text_box)
#         inp = input(">> ")

#         if inp == "1":
#             text_box = "{}\n{}  {}\n{}  {}".format(gamedata.DESCRIPTIONS["Chest"],
#                                                 "1", gamedata.OPTIONS["Take"],
#                                                 "2", gamedata.OPTIONS["Leave"])
#             pictures.print_treasure()
#             print(text_box)
#             inp = input(">> ")

#             if inp == "1":
#                 text_box = "{}\n{}  {}\n{}  {}".format(gamedata.DESCRIPTIONS["Take"],
#                                                     "1", gamedata.OPTIONS["Sneak"],
#                                                     "2", gamedata.OPTIONS["Talk"])
#                 print(text_box)
#                 inp = input(">> ")

#                 if inp == "1":
#                     pictures.print_guard()
#                     text_box = "{}".format(gamedata.DESCRIPTIONS["Direction"])
#                     print(text_box)
#                     inp = input(">> ")

#                     if inp == "left":
#                         text_box = "{}".format(gamedata.DESCRIPTIONS["Sneak"])
#                         print(text_box)
#                     else:
#                         pictures.print_game_over()

                        
#                 elif inp == "2":
#                     text_box = "{}".format(gamedata.DESCRIPTIONS["Talk"])
#                     pictures.print_guard()
#                     print(text_box)
#                     pictures.print_game_over()

#             elif inp == "2":
#                 text_box = "{}\n{}  {}\n{}  {}".format(gamedata.DESCRIPTIONS["Leave"],
#                                                     "1", gamedata.OPTIONS["Sneak"],
#                                                     "2", gamedata.OPTIONS["Talk"])
#                 print(text_box)
#                 inp = input(">> ")

#                 if inp == "1":
#                     pictures.print_guard()
#                     text_box = "{}".format(gamedata.DESCRIPTIONS["Direction"])
#                     print(text_box)
#                     inp = input(">> ")

#                     if inp == "left":
#                         text_box = "{}".format(gamedata.DESCRIPTIONS["Sneak"])
#                         print(text_box)
#                     else:
#                         pictures.print_game_over()

#                 elif inp == "2":
#                     text_box = "{}".format(gamedata.DESCRIPTIONS["Talk"])
#                     pictures.print_guard()
#                     print(text_box)
#                     pictures.print_game_over()

#         elif inp == "2":
#             text_box = "{}\n{}  {}\n{}  {}".format(gamedata.DESCRIPTIONS["Guard"],
#                                                 "1", gamedata.OPTIONS["Sneak"],
#                                                 "2", gamedata.OPTIONS["Talk"])
#             print(text_box)
#             inp = input(">> ")

#             if inp == "1":
#                 pictures.print_guard()
#                 text_box = "{}".format(gamedata.DESCRIPTIONS["Direction"])
#                 print(text_box)
#                 inp = input(">> ")

#                 if inp == "left":
#                     text_box = "{}".format(gamedata.DESCRIPTIONS["Sneak"])
#                     print(text_box)
#                 else:
#                     pictures.print_game_over()

#             elif inp == "2":
#                 text_box = "{}".format(gamedata.DESCRIPTIONS["Talk"])
#                 pictures.print_guard()
#                 print(text_box)
#                 pictures.print_game_over()

#     elif inp == "2":
#         text_box = "{}\n{}  {}\n{}  {}".format(gamedata.DESCRIPTIONS["Red"],
#                                             "1", gamedata.OPTIONS["Flee"],
#                                             "2", gamedata.OPTIONS["Attack"])
#         pictures.print_dragon()
#         print(text_box)
#         inp = input(">> ")

#         if inp == "1":
#             text_box = "{}".format(gamedata.DESCRIPTIONS["Flee"])
#             print(text_box)

#         elif inp == "2":
#             text_box = "{}".format(gamedata.DESCRIPTIONS["Attack"])
#             print(text_box)
#             pictures.print_game_over()

main()