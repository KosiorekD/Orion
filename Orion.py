#!/usr/bin/python
from Word_pre_loader import *

class Interpreter:
    def __init__(self, name):
        self.name = name
        self.ignoredCharacters = [","]

    def talkTo(self, text):
        for remove in range(len(self.ignoredCharacters)):
            text = text.replace(self.ignoredCharacters[remove], "")
        text = text.lower()
        self.text = text.split()

    def response(self):
        print(":Under Consturction - Unable to communicate yet:")

Nouns = FileLoad("Data/Nouns.csv")
Verbs = FileLoad("Data/Verbs.csv")
Adjectives = FileLoad("Data/Adjectives.csv")

Orion = Interpreter("Orion")
print("-- A conversation has begun with", Orion.name, "--")

while True:
    try:
        print(" User : ", end="", flush=True)
        userText = input("")

        Orion.talkTo(userText)
        Orion.response()
    except KeyboardInterrupt:
        print("\n", Orion.name ,": Goodbye")
        break
