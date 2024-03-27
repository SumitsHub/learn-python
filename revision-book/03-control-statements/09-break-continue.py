
##* 'break' keyword - used to break the loop

## 01 Infinite while loop with break statement -
# Print numbers from 1 to 10 but exit the loop when reaching 7
num = 1
while True:
    print(num)
    if num == 7:
        break
    num += 1
# Output:
# 1
# 2
# 3
# 4
# 5
# 6
# 7
    

## 02: Print numbers from 1 to 10 but exit the loop when reaching 7
for num in range(1, 11):
    print(num)
    if num == 7:
        break

# Output:
# 1
# 2
# 3
# 4
# 5
# 6
# 7



##* 'continue' keyword - used to skip the rest of the loop's code for the current iteration and proceed to the next iteration

## 01: Print even numbers from 1 to 10 using a while loop
num = 1
while num <= 10:
    if num % 2 != 0:
        num += 1
        continue
    print(num)
    num += 1
# Output:
# 2
# 4
# 6
# 8
# 10


## 02: Print odd numbers from 1 to 10 using a for loop
for num in range(1, 11):
    if num % 2 == 0:
        continue
    print(num)

# Output:
# 1
# 3
# 5
# 7
# 9