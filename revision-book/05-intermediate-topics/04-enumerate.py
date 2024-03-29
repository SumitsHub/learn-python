# We use enumerate function with loop to track position of our item in iterable
# enumerate() also returns an iterable

names = ['Raj', 'Sham', 'Chinmay']
## Without enumerate function

pos = 0
for name in names:
    print(f'{pos}: {name}')
    pos += 1

# Output:
# 0: Raj
# 1: Sham
# 2: Chinmay

## With enumerate()
for pos, name in enumerate(names):
    print(f'{pos}: {name}')

# Output:
# 0: Raj
# 1: Sham
# 2: Chinmay
    
print(enumerate(names))  # enumerate object
print(list(enumerate(names)))  # [(0, 'Raj'), (1, 'Sham'), (2, 'Chinmay')]