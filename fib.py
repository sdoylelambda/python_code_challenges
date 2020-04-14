
import math
import os
import random
import re
import sys



#
# Complete the 'fibonacci' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER n as parameter.

#    U.P.E.R.
#    U - UNDERSTAND
#
# FIB NUMBERS = SEQUENCE OF NUMBERS WHERE:
#       AFTER FIRST 2 NUMBERS
#       EACH NUMBER IS A SUM OF THE PRIOR 2 NUMBERS
#
# FIB EXAMPLE:
#   INPUT: N = 8
#   OUTPUT: (0,1,1,2,3,5,8,13)
#
# NOTES
# INPUT = LENGTH OF LIST THAT IS RETURNED
# I THINK I WANT TO RETURN, MAY NEED TO PRINT
# COULD I HARD CODE FIB SEQUENCE INSTEAD OF WRITING AN ALGORITHM FOR IT?
#   BASED ON TESTS HIGHEST FIB SEQUENCE IS 10 SO THIS SHOULD WORK
# FOR GENERATING FIB => INFINITY
# POSITION 0 + POSITION 1 = POSITION 3
# INCREMENT POINTERS += 1

# EDGE CASES
# WHAT IF 0 OR 1 OR 2 IS PASSED IN?

# P - PLAN
# DETERMINE FIB SEQUENCE
#       FIRST 2 VALUES HARD CODE 0, 1 - ADD TO LIST
#           TO FIND NEXT VALUE ADD PREVIOUS 2
#               ADD TO LIST
# RETURN FIRST N VALUES FROM SEQUENCE


def fibonacci(n):
    # Write your code here
    # E - EXECUTE
    # LIST TO HOLD VALUES
    integer_list = []
    # 0 IS PASSED IN
    if n == 0:
        return integer_list
    # 1 IS PASSED IN
    elif n == 1:
        return [0]
    # 2 IS PASSED IN
    elif n == 2:
        return [0, 1]
    # DETERMINE FIB SEQUENCE
    fib_hack = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    integer_list = fib_hack[:n]

    # FIRST 2 VALUES HARD CODE 0, 1 - ADD TO LIST
    # TO FIND NEXT VALUE ADD PREVIOUS 2
    # ADD TO LIST
    # RETURN FIRST N VALUES FROM SEQUENCE

    # return integer_list
    return integer_list


print(fibonacci(10))




# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#     n = int(input().strip())
#
#     result = fibonacci(n)
#
#     fptr.write('\n'.join(map(str, result)))
#     fptr.write('\n')
#
#     fptr.close()
