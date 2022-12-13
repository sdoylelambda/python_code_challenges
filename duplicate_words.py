import re

str = 'Find the duplicate word in the sentence and return it with number times used.'

def duplicate_words(str):

    regex = "\\b(\\w+)(\\s+\\1\\b)*"
    x = re.finditer(str, str)
    print(x)

    #
    # lst = str.split()
    # output = []
    # print('list:', lst)
    # for word in lst:
    #     print('word', word)
    #     lst.pop(0)
    #     print('list:', lst)
    #     for word_compare in lst:
    #         print('word_compare', word_compare)
    #         if word == word_compare:
    #             print(word_compare, word)
    #             output.append(word)


    # print('output::::', output)

duplicate_words(str)
