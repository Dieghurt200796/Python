#A short look at mapping using generators.

def number_iteration(start, finish):
    temp = start
    yield temp
    while temp < finish:
        temp += 1
        yield temp

numbers = list(number_iteration(1,10))

def squared(x):
    return 2 ** x

numbers_squared = list(map(squared, numbers))

print(numbers_squared)