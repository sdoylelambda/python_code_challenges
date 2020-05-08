# Not the most efficient one, but by far the most obvious way to do it is:
# a = [1, 2, 3, 4, 5]
# b = [9, 8, 7, 6, 5]

# returnMatches(a, b)
counter = 0

a = ['a', 'b', 'e', 'c', 'h']
b = ['a', 'b', 'e', 'c', 'g']
# if (set(a) & set(b)):
#     counter += 1
# {5}
# print('counter', counter)
# if order is significant you can do it with list comprehensions like this:

# print('for loop:', [i for i, j in zip(a, b) if i == j])
[5]
x = [i for i, j in zip(a, b) if i == j]
print('x', x)
print('length', len(b))
if len(x) == len(b):
    print('money')
else:
    print('naa')
