#!/bin/python3

import math
import os
import random
import re
import sys

def funnyString(s):
  for x in s:
    print(ord(x)) # outputs: 97 98 99

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input() #input>> abc
    
    result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()
    
