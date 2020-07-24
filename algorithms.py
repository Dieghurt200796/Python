# Sorting algorithms

numbers = [3, 56, 67, 45, 34, 457, 89, 56, 42, 34, 76, 7434, 34, 5, 67, 44, 2, 3]

print(numbers)
numbers.sort()
print(numbers)


numbers = [44, 5, 2, 3]   # [2, 3, 5, 44]

# 1. Compare two numbers that are next to each other
# 2. Swap numbers
# Bubble sort
'''
44  5   2   3
5   44  2   3
5   2   44  3
5   2   3  44

2   5   3  44
2   3   5  44

'''

data = [10,1,2,3,4,5,6,7,8,9]



import random
def shuffle_sort(data: list):
    while True:
        random.shuffle(data)
        return data
attempts = 0
while data != sorted(data):
    data = shuffle_sort(data)
    attempts += 1
    if attempts % 1000 == 0:
        print("   Attempted", attempts, end="\r")
    # print(data)
print("\nFinished!", len(data))
import time
def miracle_sort(data: list):
    while True:
        if data == sorted(data):
            return data
        else:
            time.sleep(1)
    