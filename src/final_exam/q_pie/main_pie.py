from pie_chart import PieChart
from pie_arc import PieArc

class Main:
    
    def __init__(self):
        
        pie_arcs = [PieArc('one'),PieArc('two'),PieArc('three'),PieArc('four')]
        pie_chart = PieChart(pie_arcs)
        pie_chart.draw()

Main()
