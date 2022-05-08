import math
import os
import random
import re
import sys

# Complete the 'squares' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER a
#  2. INTEGER b

def squares(a, b):
    # Write your code here
    sq = int(a**0.5)
    if(sq**2 != a):
        sq += 1
    else:
        sq = sq
    c = 0
    A = sq
    sq = A**2
    while(sq<=b):
        c += 1
        A += 1
        sq = A**2
    return c
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input().strip())
    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()
        a = int(first_multiple_input[0])
        b = int(first_multiple_input[1])
        result = squares(a, b)
        fptr.write(str(result) + '\n')
    fptr.close()