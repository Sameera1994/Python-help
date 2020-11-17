#!/bin/python3

import math
import os
import random
import re
import sys

def twoStrings(s1):
    print(set(s1))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s1 = input()

        result = twoStrings(s1)

        fptr.write(result + '\n')

    fptr.close()

