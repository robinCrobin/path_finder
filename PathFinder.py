class PathFinder:
    def __init__(self, matriz):
        self.matriz = matriz
        self.n = len(matriz)      
        self.m = len(matriz[0])   
        self.start_node = None
        self.end_node = None

    def _manhattan_distance(self, pos1, pos2):
        # h(n)=|x atual - x final | + | y atual - y final |
        x1, y1 = pos1
        x2, y2 = pos2
        return abs(x1 - x2) + abs(y1 - y2)
    
    # Função que executa o A*: 
    # def find_path(self, start_pos, end_pos):