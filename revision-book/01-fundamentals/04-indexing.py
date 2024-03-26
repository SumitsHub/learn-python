##* Indexing in Python

# String Indexing
## in Python, indexing is 2-ways, 
## 1. from start to end - index starting with zero to length - 1
## 2. from end to start - index starts with -1 to -length of the string

lang = "Python"

# Index representation
# P  y  t  h  o  n
# 0  1  2  3  4  5
# -6 -5 -4 -3 -2 -1

index = 0
while index < len(lang):
    print(lang[index])
    index += 1

# P
# y
# t
# h
# o
# n

index = -1
while index >= -len(lang):
    print(lang[index])
    index -= 1

# n
# o
# h
# t
# y
# P

index = -len(lang)
while index <= -1:
    print(lang[index])
    index += 1

# P
# y
# t
# h
# o
# n
    
