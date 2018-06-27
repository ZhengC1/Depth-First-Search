import random
from map_creator import MapCreator


class MapDepthFirstSearch(MapCreator):

    def __init__(self):
        super(MapDepthFirstSearch, self).__init__()
        self.solve(0, 0, "")

    def solve(self, x, y, moves):
        for row in self.map:
            print(' '.join([str(i) for i in row]))

        answer = self.__solve_map(x, y, moves)
        if answer:
            print(answer)
        else:
            print("no solution was found")

    def __solve_map(self, x, y, moves):
        if x > len(self.map) - 1 or x < 0 or y > len(self.map) - 1 or y < 0:
            return ""
        if self.visited[x][y]:
            return ""
        self.visited[x][y] = True
        if self.map[x][y] == 0:
            return moves

        move_value = self.map[x][y]

        return self.__solve_map(x, y - move_value,  moves + " left ") \
            + self.__solve_map(x, y + move_value, moves + "right ") \
            + self.__solve_map(x - move_value, y,  moves + "up ") \
            + self.__solve_map(x + move_value, y,  moves + "down ")


m = MapDepthFirstSearch()
