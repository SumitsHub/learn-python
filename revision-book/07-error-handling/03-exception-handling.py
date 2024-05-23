
#* try except - exception handling

##* catch all type of errors
try:
    age = int(input('Enter your age: '))
except: # catch all errors
    print('Invalid input age')


##* except particular error type
try:
    age = int(input('Enter your age: '))
except ValueError: # catch all errors
    print('Invalid input age')
except:
    print('Something went wrong')


##* taking valid input using loop and exception
while True:
    try:
        age = int(input('Enter age: '))
        break
    except ValueError:
        print('Please enter valid age')
    except:
        print('Un-expected error')
    

while True:
    try:
        age = int(input('Enter age: '))
        # shifted below code to else block
        # print('Well done!')
        # break
    except ValueError:
        print('Please enter valid age')
    except:
        print('Un-expected error')
    else:
        print('Well done!')
        break
    finally:
        print('Ends well all well!')