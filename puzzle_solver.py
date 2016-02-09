#!usr/bin/python

'''
Author: Chun Zheng
Assignment: Backtracking Treasure Hunt
Lang - python 2.7
Class - Artificial Intelligence
'''
class treasure_hunt(object):
    """
    Initilize Function
    reads maps that are 11 by 11
    @ param map_file - takes a file string and then reads through it.
    """
    def __init__(self, map_file):
        self.lines = [[0 for x in  range(11)] for x in range(11)]
        self.table = [[1 for x in range(11)] for x in range(11)]
        """
        The last couple lines strips the spaces in the file and
        readlines so that you can index everything in a list in python
        """
        treasure_map = open(map_file, "r")
        self.lines = treasure_map.readlines()
        self.lines = [l.replace(" ", "") for l in self.lines]
        treasure_map.close()
        print self.lines
    """
    takes the x and y coordinate in the list
    moves is the moves you have made in the map throughout
    the recursive calls.
    """
    def backtrack(self, x, y, moves):
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

#Prints and asks what file you would like to read in
file_name = raw_input("Name of file :")

solution = treasure_hunt(file_name)
#Prints the recursive solution
print solution.backtrack(5, 5, "")
