#!/usr/bin/env python

#Name:  Chun Zheng
#Language:  Python 3.5
#Class: Arti. Intel.
#Instructor: M. Parry

#Import Statements
#Import random so that i can populate my list from 1 to 4
import random


class puzzle_generator(object):

    def __init__(self):
        self.lines = [[0 for x in range(21)] for x in range(21)]
        self.table = [[1 for x in range(21)] for x in range(21)]
        #Asking the difficulty of the puzzle that they would like to solve
        name_file = raw_input("puzzle difficulty: ")
        map_file = open("Medium.txt", "w+")
        for i in range(21):
            for j in range(21):
                #This makes the end position zero a goal
                if i == 20 and j == 20 :
                    map_file.write('0')
                else:
                    rand_int = random.randint(1,4)
                    map_file.write(str(rand_int))
                    self.lines.append(rand_int)
            map_file.write("\n")

        map_file.close()

    def solve_generate_puzzle(self, x, y, moves):
        value = int 
        pass
cat = puzzle_generator()

