#!/usr/bin/env python
# -*- coding: utf-8 -*-
from random import shuffle, randint, choice
from copy import copy
from scrumbler import Scrumbler

# alphabet
apb = list(range(0, 26))


class EnigmaMachine:
    def __init__(self, nocogs, printspecialchars):
        self.printspecialchars = printspecialchars
        self.nocogs = nocogs
        self.cogs = []
        # Create backup of original cog positions for reset
        self.originalCogs = []

        # Create cogs
        for i in range(0, self.nocogs):
            self.cogs.append(Scrumbler())
            self.cogs[i].create(apb)
            self.originalCogs.append(self.cogs[i].transformation)

        # Create reflector
        refabet = copy(apb)
        self.reflector = copy(apb)
        while len(refabet) > 0:
            a = choice(refabet)
            refabet.remove(a)
            b = choice(refabet)
            refabet.remove(b)
            self.reflector[a] = b
            self.reflector[b] = a

    # To print the enigma setup for debugging/replication
    def print_setup(self):
        print("Enigma Setup:\nCogs: ", self.nocogs, "\nCog arrangement:")
        for i in range(0, self.nocogs):
            print(self.cogs[i].transformation)
        print("Reflector arrangement:\n", self.reflector, "\n")

    def reset(self):
        for i in range(0, self.nocogs):
            self.cogs[i].setcog(self.originalCogs[i])

    def encode(self, text):
        ln = 0
        encrypted_text = ""
        for l in text.lower():
            num = ord(l) % 97
            if (num > 25 or num < 0):
                if (self.printspecialchars):
                    encrypted_text += l
                else:
                    pass
            else:
                ln += 1
                # Move through cogs forward
                for i in range(0, self.nocogs):
                    num = self.cogs[i].passthrough(num)
                # Pass through reflector
                num = self.reflector[num]

                # Move back through cogs
                for i in range(0, self.nocogs):
                    num = self.cogs[self.nocogs - i - 1].passthrough_rev(num)
                # add encrypted letter to ciphertext
                encrypted_text += "" + chr(97 + num)
                # Rotate cogs
                for i in range(0, self.nocogs):
                    # in a ticker clock style
                    if (ln % ((i * 6) + 1) == 0):
                        self.cogs[i].rotate()
        return encrypted_text
