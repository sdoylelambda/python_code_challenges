# # Examples
#
#
def asc_des_none(arr, str):
    if str is 'Asc':
        arr.sort()
        print(arr)
        return arr

    if str is 'Des':
        arr.sort(reverse=True)
        print(arr)
        return arr

    if str is 'None':
        return arr


asc_des_none([4, 3, 2, 1], "Asc")  # [1, 2, 3, 4]

asc_des_none([7, 8, 11, 66], "Des")   # [66, 11, 8, 7]

# asc_des_none([1, 2, 3, 4], "None")  # [1, 2, 3, 4]



