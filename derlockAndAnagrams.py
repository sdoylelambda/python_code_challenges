def sherlockAndAnagrams(str1, str2):
    print(sorted(str1))
    print(sorted(str2))
    sortedStr1 = sorted(str1)
    sortedStr2 = sorted(str2)

    x = [i for i, j in zip(sortedStr1, sortedStr2) if i == j]
    print(x)

    if len(x) == len(sortedStr1):
        print('money')
        return 'Anagram'
    else:
        print('naa')
        return 'Not an anagram'

sherlockAndAnagrams('mom', 'mmo')  # anagram
sherlockAndAnagrams('mom', 'oom')  # not anagram

    # counter = 0
    #
    # a = ['a', 'b', 'e', 'c', 'h']
    # b = ['a', 'b', 'e', 'c', 'g']
    # if (set(a) & set(b)):
    #     counter += 1
    # {5}
    # print('counter', counter)
    # if order is significant you can do it with list comprehensions like this:

    # print('for loop:', [i for i, j in zip(a, b) if i == j])
    # [5]
    # x = [i for i, j in zip(a, b) if i == j]
    # print('x', x)
    # print('length', len(b))
    # if len(x) == len(b):
    #     print('money')
    # else:
    #     print('naa')



    # >> > a = [1, 2, 3, 4, 5]
    # >> > b = [9, 8, 7, 6, 5]
    # >> > set(a) & set(b)
    # {5}
    # if order is significant you can do it with list comprehensions like this:
    #
    # >> > [i for i, j in zip(a, b) if i == j]
    # [5]













    # counter = 0
    # # the two strings won't be anagrams if their lengths don't match
    # if len(sortedStr1) != len(sortedStr2):
    #     print("Not an anagram")
    #     return "Not an anagram"
    #
    # for l in sortedStr1:
    #     # print('l', l)
    #     for k in sortedStr1:
    #         # print('k', k)
    #         # print('222l', l)
    #         if l == k:
    #             print('matchdddddd')
    #             counter += 1
    # print('counter:', counter)
    # print('len(str1)', len(str1))
    # if counter == len(str1) - 1:
    #     print('anagram')
    # else:
    #     print('not anagram')





    # for strOne in sortedStr1:
    #     for strTwo in sortedStr2:
    #         print('strOne', strOne)
    #         print('strTwo', strTwo)
    #         # for l in str1:
    #         if strOne == strTwo:
    #             print("match", strOne)
    #         # elif str1 == str2:
    #         #     return 'maybe'
    #         else:
    #             print("Not an anagram")
    #             return "Not an anagram"

    # we want to look for chars that repeat
    # figure out how those repeated chars might be rearranged
    # order doesn't matter

    # given two strings, how can we figure out that those two strings
    # are anagrams of one another?

    # mom, omm -> mmo, mmo
    # we could sort both strings and then check both sorted strings
    # character by character

    # use a dict to count the occurrences of letters in the strings
    # { m: 0, o: 0 }
    # loop through the other string and decrement the value in the dict
    # for each character we come across
    # we know there was a match when all of the characters in the dict
    # were "spent"



    # if we see any repeated characters, then those will definitely count
    # towards the number of anagrammatic pairs

    # use a map to keep track of sorted substrings that we've seen as we
    # iterate through the input string with different length substrings
    # store sorted substrings in a map if they aren't in the map
    # otherwise, sort the substring, then check if it's in the map
    # if it is, then increment our counter by 1

# sherlockAndAnagrams('mom', 'mmo') # anagram
# sherlockAndAnagrams('mom', 'oom') # not anagram