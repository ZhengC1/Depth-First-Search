#!/usr/bin/env python

#Name:  Chun Zheng
#Language:  Python 3.5
#Class: Arti. Intel.
#Instructor: M. Parry

#Import Statements
#Import random so that i can populate my list from 1 to 4
import random


class puzzle_generator(object):

    #My init function, it's rather long
    def __init__(self):
        #A lines list and a tables list to keep track of my moves.
        self.lines = [[0 for x in range(21)] for x in range(21)]
        self.table = [[1 for x in range(21)] for x in range(21)]

        #Asking the difficulty of the puzzle that they would like to solve
        name_file = raw_input("puzzle difficulty: ")
        map_file = open("Medium.txt", "w+")
        for i in range(21):
            for j in range(21):
                #This makes the end position zero a goal
                if i == 20 and j == 20:
                    map_file.write('0')
                else:
                    rand_int = random.randint(1, 4)
                    map_file.write(str(rand_int))
                    self.lines.append(rand_int)
            map_file.write("\n")
        map_file.close()
        treasure_map = open("Medium.txt", "r")
        self.lines = treasure_map.readlines()
        treasure_map.close()
        print self.lines
"""
    def solve_generate_puzzle(self, x, y, moves):
        #Values is the offset used in the file
        #Also prints offset
        value = int(self.lines[x][y])
        print "Offset: %s" % value

        #Marks whether or not you have been to this location already
        if self.table[x][y] == 0:
            return False

        #Returns the solution and stops the recursion
        if (x == 0 or x == 10) and (y == 0 or y == 10):
            print "Solution : %s" % moves
            print "Found a solution %d %d Return it!" %(x, y)
            return True
        #Else, does the recursive function calls
        else:
            #Sets the visited location in another table
            self.table[x][y] = 0
            if (x - value) > -1 and (x - value) < 11:
                print "Try moving up %d spaces" %value
                print "Current position %d %d %s" %(x, y, moves)
                if self.backtrack(x - value, y, moves + " up"):
                    print 'Found a solution at %d %d. Return it!' %(x, y)
                    return True
                else:
                    self.table[x][y] = 0
            if (x + value) > -1 and (x + value) < 11:
                print "Try moving down %d spaces" %value
                print "Current position %d %d %s" %(x, y, moves)
                if self.backtrack(x + value, y, moves + " down"):
                    print 'Found a solution at %d %d, Return it!' %(x, y)
                    return True
                else:
                    self.table[x][y] = 0
            if (y - value) > -1 and (y - value) < 11:
                print "Try moving left %d spaces" %value
                print "Current position %d %d %s" %(x, y, moves)
                if self.backtrack(x, y - value, moves + " left"):
                    print 'Found a solution at %d %d, Return it!' %(x, y)
                    return True
                else:
                    self.table[x][y] = 0
            if (y + value) > -1 and (y + value) < 11:
                print "Try moving right %d spaces" %value
                print "Current position %d %d %s" %(x, y, moves)
                if self.backtrack(x, y + value, moves + " right"):
                    print 'Found a solution at %d %d, Return it!' %(x, y)
                    return True
                else:
                    self.table[x][y] = 0
        #Returns false if all else fails.
        return False
"""
#solution = treasure_hunt(file_name)
#Prints the recursive solution
#print solution.backtrack(0, 0)
cat = puzzle_generator()
