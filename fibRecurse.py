# def recurse(x):
#    if x > 0:
#        print(x)
#        recurse(x - 1)
#
# recurse(10)

# def fibonacci(n):
#     # Write your code here
#     # E - EXECUTE
#     # LIST TO HOLD VALUES

# n = 10

    # integer_list = []
    # # 0 IS PASSED IN
    # if n == 0:
    #     return integer_list
    # # 1 IS PASSED IN
    # elif n == 1:
    #     return [0]
    # # 2 IS PASSED IN
    # elif n == 2:
    #     return [0, 1]
    # for num in range(0, n):
    #     v.append(num)
    #     print('v', v)
    #


# DETERMINE FIB SEQUENCE
n = 5
fib_infinite = []
a = 0
b = 1
c = 1
fib_infinite.append(a)
fib_infinite.append(b)
fib_infinite.append(c)
v = [0, 1, 2, 3, 4]
print('v', v)
print('v length:', len(v))
    # for num in range(0, n):
    #     v.append(num)
    #     print(v)
# pointer1 = fib_infinite[0]
# print('pointer1', pointer1)
# pointer2 = fib_infinite[1]
# print('pointer12', pointer2)

fib_infinite = []
a = 0
b = 1
c = 1
fib_infinite.append(a)
fib_infinite.append(b)
fib_infinite.append(c)
counter = 0

returnArr = []

def recurse(pointer1, pointer2):
    global counter

    # global pointer1
    # global pointer2
    for i in range(n):
        print('i', i)
        pointer1x = fib_infinite[i]
        print('pointer1', pointer1)
        pointer2x = fib_infinite[i+1]
        print('pointer12', pointer2)
        while counter < 5:
            pos3 = pointer1x + pointer2x
            # x = fib_infinite[i]
            # print('pointer1', pointer1)
            # y = fib_infinite[i+1]
            # print('pointer12', pointer2)
            returnArr.append(pos3)
            # returnArr.append(y)
            print('returnArr', returnArr)
            counter += 1
            print('counter', counter)
            return recurse(pointer1, pointer2)

    else:
        return


recurse(0, 1)
    # FIRST 2 VALUES HARD CODE 0, 1 - ADD TO LIST
    # TO FIND NEXT VALUE ADD PREVIOUS 2
    # ADD TO LIST
    # RETURN FIRST N VALUES FROM SEQUENCE

    # return integer_list
#     return integer_list
#
#
# print(fibonacci(10))


# def recur(n):
#     global counter
#     counter+=1
#     if n==0:
#         return -1
#     else:
#         return recur(n-1)
#
# counter = 0
# recur(100)
# -1
# print(counter)