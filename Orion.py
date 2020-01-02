#!/usr/bin/python
from Word_pre_loader import *

class Interpreter:
    def __init__(self, name):
        self.name = name
        self.ignoredCharacters = [","]

    def talk(self, text):
        for remove in range(len(self.ignoredCharacters)):
            text = text.replace(self.ignoredCharacters[remove], "")
        text = text.lower()
        self.text = text.split()

Nouns = FileLoad("Data/Nouns.csv")
Verbs = FileLoad("Data/Verbs.csv")
Adjectives = FileLoad("Data/Adjectives.csv")

Orion = Interpreter("Orion")
Orion.talk("Hello, how are you today?")

print(Orion.text)
