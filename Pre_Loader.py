#!/usr/bin/python
import csv

class Load:
    def __init__(self, file):
        self.file = file
        self.data = []

    def readFile(self):
        with open(self.file, "r") as csvFile:
            reader = csv.reader(csvFile, delimiter=',', quotechar='|')
            for row in reader:
                self.data.append(row)
