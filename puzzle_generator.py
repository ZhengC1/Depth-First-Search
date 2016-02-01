#!/usr/bin/env python

"""
Name:  Chun Zheng
Lang:  Python 3.5
Class: Arti Intel
Instruc: M. Parry
"""


class puzzle_generator(object):

  def __init__(self):
    name_file = input("name your file: ")
    map_file = open(name_file, "a")
    for i in range(21):
      for j in range(21):
        map_file.write(str(0))
  map_file.write("\n") 
        map_file.close()

        def generate_solution(self);



        ca is the offset used in the file
#Also prints offset
    value = int(self.lines[x][y])
    print "Offset: %s" % value

#Marks whether or not you have been to this location already
  if self.table[x][y] == 0:
    return False

#Returns the solution and stops the recursion
    if (x == 0 or x == 10) and (y == 0 or y == 10):

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
return Falsegg=G= puzzle_generator()

