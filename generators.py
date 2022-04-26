def interval(min, max): #A function that returns the steps to go from one number to another. This is for the sake of trying out generators.
    temp = min
    while temp < max - 1:
        temp += 1
        yield temp

numbers = list(interval(0,10)) #Creating a variable forces the generator to run
numbers_interleaved = list(zip(interval(0,9), interval(1,10))) # Interleaving between each generator using the zip() function to save it to only one variable

print(numbers)

numbers_sum = sum(interval(0,1_000_000_000))

print(numbers_sum)