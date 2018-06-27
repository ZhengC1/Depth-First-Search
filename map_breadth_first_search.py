from collections import deque
import random
from map_creator import MapCreator


class MapBreadthFirstSearch(MapCreator):

    def __init__(self):
        super(MapBreadthFirstSearch, self).__init__()
        self.solve((0, 0))

    def solve(self, start):
        for row in self.map:
            print(' '.join([str(i) for i in row]))
        answer = self.__solve_map(start)
        print(answer)

    def __solve_map(self, start):
        queue = deque()
        queue.append(("start", start))
        self.visited[start[0]][start[1]] = True
        while queue:
            current = queue.popleft()
            if current[1] == (len(self.map) - 1, len(self.map) - 1):
                return current
            for direction, adj in self.__get_adjacent(current):
                if self.visited[adj[0]][adj[1]]:
                    continue
                queue.append((direction, adj))
                self.visited[adj[0]][adj[1]] = True
        return "no solution found"

    def __get_adjacent(self, current):
        path = current[0]
        map_coordinates = current[1]
        x = map_coordinates[0]
        y = map_coordinates[1]
        if x < 0 or y < 0 or x > len(self.map) or y > len(self.map):
            return
        value = self.map[x][y]
        adjacent = []
        # up
        if (x - value) >= 0:
            adjacent.append((path + " up", (x - value, y)))
        # down
        if (x + value) < len(self.map):
            adjacent.append((path + " down", (x + value, y)))
        # left
        if (y - value) >= 0:
            adjacent.append((path + " left", (x, y - value)))
        # right
        if (y + value) < len(self.map):
            adjacent.append((path + " right", (x, y + value)))
        return adjacent


m = MapBreadthFirstSearch()
