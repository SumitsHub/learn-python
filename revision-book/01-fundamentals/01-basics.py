# This is commente and will be ignored by python interpreter
# Comment starts with # symbol in Python

##* print function

print("Hello")  # single quote string

print("Hello")  # double quote string

print("Hey I't me..")  # single quote inside double quote

print('Hey I am "BIG" start..')  # double quote inside single quote

##* Escape  Sequences
# \" - double quote
print(
    'Heyy there "listen" to me'
)  # using double quotes inside duoble quote using escape sequences

# \' - single quote
print("Heyy thete ' listen' to me")

# \\
print("This is example of \\back slash")

# \n
print("This will be print on \nnew line")

# \t
print("This is \t tab")

# \b
print("This is \b backspace")


##* Escape sequence as normal text
print("Line A \\n Line B")  # Output: Line A \n Line B


##* Raw Strings - string starting with letter 'r', treats escape sequences as normal text

print(r"Line A \n Line B")  # Output: Line A \n Line B
