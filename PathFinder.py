import heapq
from node import Node

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
    
    def _reconstruct_path(self, current_node):
        path = []
        current = current_node
        while current is not None:
            path.append(current.position)
            current = current.parent
        return path[::-1]
    
    def find_path(self, start_pos, end_pos):
        self.start_node = Node(start_pos)
        self.end_node = Node(end_pos)

        open_list = []
        open_dict = {}
        closed_set = set()

        self.start_node.g = 0
        self.start_node.h = self._manhattan_distance(start_pos, end_pos)
        self.start_node.f = self.start_node.h

        heapq.heappush(open_list, self.start_node)
        open_dict[start_pos] = self.start_node

        while open_list:
            
            current_node = heapq.heappop(open_list)

            if current_node.position in closed_set:
                continue
            
            closed_set.add(current_node.position)
            
            if current_node.position in open_dict:
                 del open_dict[current_node.position]

            if current_node == self.end_node:
                return self._reconstruct_path(current_node)

            moves = [(-1, 0), (1, 0), (0, -1), (0, 1)] 

            for move in moves:
                neighbor_pos = (current_node.position[0] + move[0], 
                                current_node.position[1] + move[1])
                
                if (neighbor_pos[0] < 0 or neighbor_pos[0] >= self.n or
                    neighbor_pos[1] < 0 or neighbor_pos[1] >= self.m):
                    continue

                if self.matriz[neighbor_pos[0]][neighbor_pos[1]] == '1':
                    continue
                    
                if neighbor_pos in closed_set:
                    continue
                
                neighbor_node = Node(neighbor_pos, current_node)
                neighbor_node.g = current_node.g + 1 
                neighbor_node.h = self._manhattan_distance(neighbor_pos, self.end_node.position)
                neighbor_node.f = neighbor_node.g + neighbor_node.h

                if neighbor_pos in open_dict:
                    existing_node = open_dict[neighbor_pos]
                    if neighbor_node.g >= existing_node.g:
                        continue
                    else:
                        existing_node.g = neighbor_node.g
                        existing_node.f = neighbor_node.f
                        existing_node.parent = current_node
                        heapq.heapify(open_list) 
                else:
                    heapq.heappush(open_list, neighbor_node)
                    open_dict[neighbor_pos] = neighbor_node

        return None 