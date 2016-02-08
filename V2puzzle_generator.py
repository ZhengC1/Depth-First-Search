#!/usr/bin/env python

"""
Name:  Chun Zheng
Lang:  Python 3.5
Class: Arti Intel
Instruc: M. Parry
"""


class puzzle_generator(object):

    def __init__(self):
        name_file = raw_input("name your file: ")
        map_file = open(str(name_file), "w+")
        for i in range(21):
            for j in range(21):
                map_file.write(str(0))
            map_file.write("\n") 
        map_file.close()

cat = puzzle_generator()

