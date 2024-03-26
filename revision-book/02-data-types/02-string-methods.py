##* String methods

text = "someThing"

# lower() - returns lowercased copy of string
print(text.lower())  # something

# upper - returns uppercased copy of string
print(text.upper())  # SOMETHING

# capitalize - returns capitalized string
print(text.capitalize())  # Something

# title() - each word gets titlized
print("this is an titlized sentence".title())  # This Is An Titlized Sentence

# count - Return the number of non-overlapping occurrences of substring 'sub' in string
print(text.count("some"))  # 1
print("tell me some thing".count("me"))  # 2

# find() - returns lowest index of input sub string if found else returns -1
print("find me inside".find("me"))  # 5

# index() - similar to find, if substring not found it raises ValueError
print("index of substring".index("substring"))  # 9


name = "        Harshit          "
dots = "........................."

print(name + dots)  #         Harshit          .........................

# strip() - trims leading and trailing whitespaces
print(name.strip() + dots)  # Harshit.........................
# rstrip() - removes trailing whitespaces
print(name.rstrip() + dots)  #         Harshit.........................
# lstrip() - removes leading whitespaces
print(name.lstrip() + dots)  # Harshit          .........................


# replace(old, new[, count]) - replaces old string with new
print("She is a beutiful girl".replace("is", "was")) # She was a beutiful girl


# center(width, fillChar) - returns centered string of width filled with input fill char
print("Preeti".center(20, '*')) # *******Preeti*******
