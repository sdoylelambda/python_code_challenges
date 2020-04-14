def sherlockAndAnagrams(s):
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

    # the two strings won't be anagrams if their lengths don't match

    # if we see any repeated characters, then those will definitely count
    # towards the number of anagrammatic pairs

    # use a map to keep track of sorted substrings that we've seen as we
    # iterate through the input string with different length substrings
    # store sorted substrings in a map if they aren't in the map
    # otherwise, sort the substring, then check if it's in the map
    # if it is, then increment our counter by 1 