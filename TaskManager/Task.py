class Task(object):
    def __init__(self, name, text):
        self.name = name
        self.text = text

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getText(self):
        return self.text

    def setText(self, text):
        self.text = text
