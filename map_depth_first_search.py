import random

class MapDepthFirstSearch(object):

    def __init__(self):
        self.__create_map()

    def solve(self, x, y, moves):
        self.visited = [[1 for x in range(21)] for x in range(21)]
        print self.__solve_map(x, y, moves)

    def __create_map(self):
        self.map = [[random.randint(1, 4) for x in range(21)] for x in range(21)]
        self.map[20][20] = 0

    def __solve_map(self, x, y, moves):
        if x > len(self.map) -1 or x < 0 or y > len(self.map) -1 or y < 0:
            return
        if self.visited[x][y] == 0:
            return
        if self.map[x][y]:
            self.visited[x][y] = 0
        if x == 21 and y == 21:
            return moves

        move_value = self.map[x][y]

        self.__solve_map(x , y - move_value, moves + " left")
        self.__solve_map(x , y + move_value, moves + " right")
        self.__solve_map(x - move_value , y, moves + " up")
        self.__solve_map(x + move_value , y, moves + " down")


m = MapDepthFirstSearch()
m.solve(0, 0, "")
