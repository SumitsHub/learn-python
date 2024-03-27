
##* while loop

## 01: 
# Print numbers from 1 to 5 using a while loop
num = 1
while num <= 5:
    print(num)
    num += 1
# Output:
# 1
# 2
# 3
# 4
# 5
    

## 02: Using a while loop with user input -
# Ask the user to enter a number until a negative number is entered
num = int(input("Enter a number (negative to stop): "))
while num >= 0:
    print("Entered number:", num)
    num = int(input("Enter another number (negative to stop): "))


## 03: Nested while loops
# Print a multiplication table using nested while loops
i = 1
while i <= 5:
    j = 1
    while j <= 10:
        print(i * j, end="\t")
        j += 1
    print()  # Move to the next line after printing each row
    i += 1
# Output:
# 1  2  3  4  5  6  7  8  9  10
# 2  4  6  8  10 12 14 16 18 20
# 3  6  9  12 15 18 21 24 27 30
# 4  8  12 16 20 24 28 32 36 40
# 5  10 15 20 25 30 35 40 45 50
