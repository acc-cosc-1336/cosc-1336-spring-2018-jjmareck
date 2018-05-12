class PieChart:
    def __init__(self, arclist):
        self.arclist = arclist

    def draw(self):
        for arc in self.arclist:
            arc.draw()
