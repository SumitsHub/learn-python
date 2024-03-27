## Useful Commands

1. "code filename.py" - opens VS Code with newly created file open
2. "code ." - opens current directory with VS Code
3. "python filename.py" OR "py filenam.py" - command to run python file


## 01-fundamentals

### Printing Emojis

- [unicodes.org] - website to get unicode of an emoji
- example emoji - 🥰 unicode - U+1F970
- To print an emoji follow 2 step process mentioned below:
  - 1. Replace '+' in the unicode with 3 zeros i.e. '000' -> e.g. U0001F970
  - 2. Prefix result with backshlash ('\') -> e.g. '\U0001F970'
  - ```py 
        print('\U0001F970')  # Output: 🥰
    ```


### Operator precedence and associativity

|Operators|Precedence & Associativity |
|--|--|
|Paranthesis|Highest|
|Exponent (**)|Right to Left|
|*, /, //, %|Left to Right|
|+, -|Left to Right|


### Types returned by python -

1. print(type(0)) - <class 'int'>
2. print(type("abc")) - <class 'str'>
3. print(type([1, 2])) - <class 'list'>
4. print(type({1, 2, 3})) - <class 'set'>
5. print(type(True)) - <class 'bool'>
6. print(type({'k1': 'v1'})) - <class 'dict'>
7. print(type(0.4)) - <class 'float'>