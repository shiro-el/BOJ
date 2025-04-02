class Stack:
    def __init__(self, Paper, leg):
        self.Paper = Paper
        self.leg = leg
    
    def filp(self, p):
        self.Paper = self.Paper[::-1]
        for i in range(self.leg):
            self.Paper[i] = self.Paper[i][::-1]
        for i in range(self.leg):
            p.Paper[i].extend(self.Paper[i])
    