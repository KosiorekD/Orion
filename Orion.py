#!/usr/bin/python
import csv
from Pre_Loader import *
from Bot import *

Nouns = Load("Data/Nouns.csv")
Verbs = Load("Data/Verbs.csv")
Adjectives = Load("Data/Adjectives.csv")

Orion = Bot("Orion")
print("-- A conversation has begun with", Orion.name, "--")

while True:
    try:
        print(" User : ", end="", flush=True)
        userText = input("")

        Orion.talkTo(userText)
        Orion.response()
        print(Orion.text)

    except KeyboardInterrupt:
        print("\n", Orion.name ,": Goodbye")
        del Orion
        del Nouns
        del Verbs
        del Adjectives
        break
