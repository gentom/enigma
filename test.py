#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
# print(os.getcwd())
sys.path.append(os.getcwd() + "/enigma")
from enigma.enigma import EnigmaMachine

plaintext = """The Enigma machines were a series of electro-mechanical rotor cipher machines developed and used in the early- to mid-20th century to protect commercial, 
diplomatic and military communication. Enigma was invented by the German engineer Arthur Scherbius at the end of World War I. 
Early models were used commercially from the early 1920s, and adopted by military and government services of several countries, 
most notably Nazi Germany before and during World War II. Several different Enigma models were produced, 
but the German military models, having a plugboard, were the most complex. Japanese and Italian models were also in use."""
x = EnigmaMachine(7, True)
x.print_enigma_setup()
print("Plaintext:\n{}\n".format(plaintext))
encrypted_text = x.encode(plaintext)
print("Encrypted text:\n{}\n".format(encrypted_text))
x.reset()
plaintext = x.encode(encrypted_text)
print("Plaintext:\n{}\n".format(plaintext))
