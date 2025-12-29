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
    """get_next_state hanterar spelets nuvarande stadie.

    om stadiet har en beskrivning så skrivs den ut,
    varje stadie har minst en valmöjlighet, men om den endast
    har en så väljs den automatiskt annars frågas användaren
    efter ett svar och det alternativet returneras som det nästa stadiet
    """
    desc = gamedata.DESCRIPTIONS.get(state)
    if desc:
        print(desc)

    options = gamedata.ADVENTURE_TREE[state]
    if len(options) == 1:
        return options[0]

    for i, state in enumerate(options):
        print("{} {}".format(i + 1, state))

    inp = None
    while inp is None or inp >= len(options):
        inp = int(input(">> ")) - 1

    return options[inp]


if __name__ == "__main__":
    name = input("What's your name?\n>> ")
    print(
        "Welcome {} to the adventure of your life. \
Try to survive and find the treasure!".format(name.upper())
    )

    current_state = "Start"

    while current_state != "End":
        pictures.print_pic(current_state)
        current_state = get_next_state(current_state)

    pictures.print_pic(current_state)
