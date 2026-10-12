# 1. Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero.

# try:
#     num1 = int(input("Enter numerator: "))
#     num2 = int(input("Enter denominator: "))
#     result = num1 / num2
#     print('Result :', result)
# except ZeroDivisionError:
#     print('Error: Cannot divide by zero !')

# try:
#     a = int(input('Enter numerator :'))
#     b = int(input('Enter denominator :'))
#     print('Result:', a/b)
# except ZeroDivisionError as e:
#     print('Error',e)
# except ValueError:
#     print('Invalid input ! Please enter numbers only.')

##--------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 2. Write a Python program that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer.

# try:
#     num = int(input('Enter an integer :'))
#     print('You entered :', num)
# except ValueError:
#     print('Invalid input ! Please enter a valid integer')

# try:
#     user_input = input('Enter an integer :')
#     if not user_input.isdigit():
#         raise ValueError('Invalid input! Please enter a valid integer')
    
#     num = int(user_input)
#     print('You entered :', num)
# except ValueError as e:
#     print('Error :',e)

##--------------------------------------------------------------------------------------------------------------------------------------------------------------------

# # 3. Write a Python program that opens a file and handles a FileNotFoundError exception if the file does not exist.
# try:
#     file = open('Sample.txt', 'r')
#     content = file.read()
#     print(content)
#     file.close()
# except FileNotFoundError:
#     print('Error : File does not exist')

##--------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 4. Write a Python program that prompts the user to input two numbers and raises a TypeError exception if the inputs are not numerical.

# try:
#     num1 = float(input("Enter first Number"))
#     num2 = float(input('Enter Second Number'))
#     print('sum :', num1 + num2)

# except ValueError:
#     raise TypeError('Input must be numerical values !')

##--------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 5. Write a Python program that opens a file and handles a PermissionError exception if there is a permission issue.

# try:
#     file = open('sample.txt', 'r')
#     content = file.read()
#     print(content)
#     file.close()
# except PermissionError:
#     print('Error : Permission denied! you are not allowed to access this file')

##--------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 6. Write a Python program that executes an operation on a list and handles an IndexError exception if the index is out of range.
# try:
#     lst = [10,20,30,40]

#     index = int(input('Enter index: '))
#     print('Element :', lst[index])

# except IndexError:
#     print('Error : Index out of range!')

# except ValueError:
#     print('Error : Please enter a valid integer index')

##--------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 7. Write a Python program that executes division and handles an ArithmeticError exception if there is an arithmetic error.

# try:
#     a = int(input('Enter numerator :'))
#     b = int(input('Enter denominator :'))

#     result = a/b
#     print('Result:', result)
# except ArithmeticError:
#     print('Error : Arithmetic problem occured')

##--------------------------------------------------------------------------------------------------------------------------------------------------------------------