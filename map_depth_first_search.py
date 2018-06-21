import random

class MapDepthFirstSearch(object):

    def __init__(self, map_size):
        self.__create_map(map_size)

    def solve(self, x, y, moves):
        for row in self.map:
            print(' '.join([str(i) for i in row]))

        answer = self.__solve_map(x, y, moves)
        if answer:
            print(answer)
        else:
            print("no solution was found")

    def __create_map(self, map_size):
        self.map = [[random.randint(1, 4) for x in range(map_size)] for x in range(map_size)]
        self.visited = [[False for x in range(map_size)] for x in range(map_size)]
        # set destination
        self.map[map_size -1][map_size -1] = 0

    def __solve_map(self, x, y, moves):
        if x > len(self.map) -1 or x < 0 or y > len(self.map) -1 or y < 0:
            return ""
        if self.visited[x][y]:
            return ""
        self.visited[x][y] = True
        if self.map[x][y] == 0:
            return moves

        move_value = self.map[x][y]

        return self.__solve_map(x , y - move_value,  moves + " left ") \
                + self.__solve_map(x , y + move_value, moves + "right ") \
                + self.__solve_map(x - move_value , y,  moves + "up ") \
                + self.__solve_map(x + move_value , y,  moves + "down ")


map_size = input("map size: ")
m = MapDepthFirstSearch(int(map_size))
m.solve(0, 0, "")
