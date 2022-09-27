#!/bin/python3

import math
import os
import random
import re
import sys
import string

# Complete the solve function below.
def solve(s):
    # print(s.title())
    # return s.title()
    print(' '.join(elem.capitalize() for elem in s.split(' ')))
    # print(string.capwords(s))
    # print(s[0].upper()+s[1:])
    return

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    # fptr.write(result + '\n')

    # fptr.close()
