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
8. print(type(range(10))) - <class 'range'>
9. print(type(my_sum_func)) - <class 'function'>
10. print(type(sum)), print(type(max)) - <class 'builtin_function_or_method'>
11. print(type(type)), print(type(filter)), print(type(map)) - <class 'type'>
12. <class 'dict_keys'>
13. <class 'dict_values'>
14. <class 'dict_items'>
15. <class 'generator'>
16. <class 'map'>


### common methods used with different data types

1. min() & max() - returns smallest and biggest item from the iterables (containing same type of elements)
2. sum() - returns sum of iterables with start value (default = 0)
3. len() - return number of elements in an iterable
4. sorted() - returns new sorted iterable
5. type() - returns the type of input argument