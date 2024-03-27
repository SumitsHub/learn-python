
##* for loop - used to iterate over iterable objects

## iterating over a list -
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
# Output:
# apple
# banana
# cherry

## iterate over string - 
word = "Python"
for char in word:
    print(char)
# Output:
# P
# y
# t
# h
# o
# n


## using range() function with for loop
for i in range(5):
    print(i)
# Output:
# 0
# 1
# 2
# 3
# 4


## nested for loop
for i in range(3):
    for j in range(2):
        print(i, j)
# Output:
# 0 0
# 0 1
# 1 0
# 1 1
# 2 0
# 2 1


## iterate over dictionary

student_scores = {"John": 85, "Alice": 90, "Bob": 80}
for name, score in student_scores.items():
    print(f"{name}: {score}")
# Output:
# John: 85
# Alice: 90
# Bob: 80


## using 'enumerate' to iterate with index - 
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(index, fruit)
# Output:
# 0 apple
# 1 banana
# 2 cherry


## Using zip() to iterate over multiple sequences simultaneously -
names = ["John", "Alice", "Bob"]
scores = [85, 90, 80]
for name, score in zip(names, scores):
    print(f"{name}: {score}")
# Output:
# John: 85
# Alice: 90
# Bob: 80
