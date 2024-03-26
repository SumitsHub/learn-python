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