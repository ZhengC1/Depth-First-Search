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
        #Asking the difficulty of the puzzle that they would like to solve
        name_file = raw_input("puzzle difficulty: ")
        map_file = open("Medium.txt", "w+")
        for i in range(21):
           for j in range(21):
               if (i == 0 and j == 0) or (i == 20 and j == 20 ):
                   map_file.write('0')
               else:
                   rand_int = random.randint(1,4)
                   map_file.write(str(rand_int))
           map_file.write("\n")
        
        map_file.close()

    def generate_puzzle(self):
       pass
cat = puzzle_generator()

