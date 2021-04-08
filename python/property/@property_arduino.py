class Arduino:
    def __init__(self, com, baud):
        self.com = com
        self.baud = baud

    def connect(self):
        return f"{self.com}.{self.baud}"
