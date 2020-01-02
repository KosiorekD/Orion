class Bot:
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
