n = 10

def recurse(n):
    # make list with [0,1,2]
    fibList = [0, 1, 2]
    # repeat n number of times
    for loop in n:
        # add positions list[1] + list[2] to list
        position3 = fibList[1] + fibList[2]
        fibList.append(position3)
        # increment list
    print('fibList', fibList)
    return fibList
