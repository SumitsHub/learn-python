
##* any() and all() function

n1 = [2, 4, 6, 8, 10]
n2 = [1, 2, 3, 4, 5]

#* all() - Return True if bool(x) is True for all values x in the iterable.
# If the iterable is empty, return True.

print(all([]))  # True
print(all([n % 2 == 0 for n in n1]))  # True
print(all([n % 2 == 0 for n in n2]))  # False


#* any() - Return True if bool(x) is True for any x in the iterable.
# If the iterable is empty, return False.

print(any([]))  # False
print(any([n % 2 == 0 for n in n1]))  # True
print(any([n % 2 == 0 for n in n2]))  # True



##* min() and max()

names = ['Harshit', 'Abhishek', 'Rahul']
print(max(names))  # Rahul
print(min(names))  # Abhishek


students = {
    'Harshit': {'score': 90, 'age': 24},
    'Rahul': {'score': 89, 'age': 35},
    'Rishab': {'score': 70, 'age': 26},
    'Aditya': {'score': 93, 'age': 30},
}

print(max(students, key=lambda item : students[item].get('score')))  # Aditya
print(max(students, key=lambda item : students[item].get('age')))  # Rahul


persons = [
    {'name': 'Harshit', 'score': 90, 'age': 24},
    {'name': 'Rahul', 'score': 89, 'age': 25},
    {'name': 'Rishab', 'score': 70, 'age': 26},
    {'name': 'Aditya', 'score': 93, 'age': 30},
]

print(min(persons, key=lambda p : p.get('score')))  #  {'name': 'Rishab', 'score': 70, 'age': 26}
print(min(persons, key=lambda p : p.get('age')))  #  {'name': 'Harshit', 'score': 90, 'age': 24}



## sort() and sorted()

#* sort() method - Sort the list in ascending order and return None.

fruits = ['grapes', 'orange', 'apple']

fruits.sort()
print(fruits)  # ['apple', 'grapes', 'orange']

fruits = ['grapes', 'orange', 'apple']

# setting reverse flag to True for descending order
fruits.sort(reverse=True)
print(fruits)  # ['orange', 'grapes', 'apple']
print([x for x in range(5)].sort())  # None -> sort() returns None


# using key
people = [
    {'name': 'Alice', 'age': 30},
    {'name': 'Bob', 'age': 25},
    {'name': 'Charlie', 'age': 35}
]

people.sort(key=lambda person : person['age'])
print(people)  # [{'name': 'Bob', 'age': 25}, {'name': 'Alice', 'age': 30}, {'name': 'Charlie', 'age': 35}]


#* sorted() - Return a new list containing all items from the iterable in ascending order.
print(sorted(people, key=lambda p : p['age'], reverse=True))  # [{'name': 'Charlie', 'age': 35}, {'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}]