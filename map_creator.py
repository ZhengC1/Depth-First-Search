import random


class MapCreator(object):

    def __init__(self):
        map_size = input("map size: ")
        self.__create_map(map_size)

    def __create_map(self, map_size):
        self.map = [[random.randint(1, 4) for x in range(map_size)]
                    for x in range(map_size)]
        self.visited = [[False for x in range(
            map_size)] for x in range(map_size)]
        # set destination
        self.map[map_size - 1][map_size - 1] = 0
