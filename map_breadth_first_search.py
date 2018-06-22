from collections import deque
import random
from map_creator import MapCreator

class MapBreadthFirstSearch(MapCreator):

    def __init__(self):
        super(MapBreadthFirstSearch, self).__init__()
        self.solve((0,0))

    def solve(self, start):
        for row in self.map:
            print(' '.join([str(i) for i in row]))

        answer = self.__solve_map(start)
        if answer:
            print(answer)
        else:
            print("no solution was found")

    def __solve_map(self, start):
      edge_to = {}
      queue = deque()
      queue.append(start)
      self.visited[start[0]][start[1]] = True;
      while queue:
          current = queue.popleft()
          for adj in self.__get_adjacent(current):
              if self.visited[adj[0]][adj[1]]:
                  continue
              queue.append(adj)
              self.visited[adj[0]][adj[1]] = True
              edge_to[adj] = current
      return edge_to

    def __get_adjacent(self, map_coordinates):
       x = map_coordinates[0]
       y = map_coordinates[1]
       if x < 0 or y < 0 or x > len(self.map) or y > len(self.map):
         return
       value = self.map[x][y]
       adjacent = []
       # up
       if (x - value) >= 0:
          adjacent.append((x - value, y))
       # down
       if (x + value) < len(self.map):
          adjacent.append((x + value, y))
       if (y - value) >= 0:
          adjacent.append((x, y - value))
       if (y + value) < len(self.map):
          adjacent.append((x, y + value))
       return adjacent

m = MapBreadthFirstSearch()
