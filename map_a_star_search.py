from collections import deque
import random
from map_creator import MapCreator

class AStarSearch(MapCreator):

    def __init__(self):
        super(AStarSearch, self).__init__()
        self.solve()

    def solve(self, start):
        for row in self.map:
            print(' '.join([str(i) for i in row]))
        answer = self.__solve_map(start)
        print(answer)

    def __solve_map(self, start):
        open_set = [start]

        for adj in self.__get_adjacent(current):

    def __calculate_heuristic(row, col):

    def __get_adjacent(self, current):
        path = current[0]
        map_coordinates = current[1]
        row = map_coordinates[0]
        col = map_coordinates[1]
        if row < 0 or col < 0 or row > len(self.map) or col > len(self.map):
            return
        value = self.map[row][col]
        adjacent = []
        # up
        if (row - value) >= 0:
            adjacent.append((path + " up", (row - value, col)))
        # down
        if (row + value) < len(self.map):
            adjacent.append((path + " down", (row + value, col)))
        # left
        if (col - value) >= 0:
            adjacent.append((path + " left", (row, col - value)))
        # right
        if (col + value) < len(self.map):
            adjacent.append((path + " right", (row, col + value)))
        return adjacent
