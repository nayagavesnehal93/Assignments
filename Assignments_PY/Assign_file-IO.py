# 1. Write a Python program to read an entire text file.

# file = open('sample.txt', 'r')
# content = file.read()
# print(content)
# file.close()

# with open('sample.txt', 'r') as file:
#     content = file.read()
#     print(content)

##-----------------------------------------------------------------------------------------------------------------------

# 2. Write a Python program to read first n lines of a file.

# n = int(input('Enter number of lines to read: '))
# with open('sample.txt', 'r') as file:
#     for i in range(n):
#         line = file.readline()
#         if not line:          # Stop if file ends before n lines
#             break
#         print(line, end='')


# n = int(input('Enter number of lines to read: '))
# with open('sample.txt' , 'r') as file:
#     lines = file.readlines()
#     for line in lines[:n]:
#         print(line,end='')

##-----------------------------------------------------------------------------------------------------------------------

# 3. Write a Python program to append text to a file and display the text.

# text = input('Enter text to append :')
# with open ('sample.txt', 'r') as file:
#     file.write(text + '\n')             # Add new line after text
# with open('sample.txt', 'r') as file:
#     content = file.read()
#     print('\n updated file content :')
#     print(content)

##-----------------------------------------------------------------------------------------------------------------------

# 4. Write a Python program to read last n lines of a file.

# n = int(input('Enter number of last lines to read :'))
# with open('sample.txt', 'r') as file:
#     lines = file.readlines()       # Read all lines into a list
# last_lines = lines[-n:]
# for line in last_lines:
#     print(line, end='')

##-----------------------------------------------------------------------------------------------------------------------

# 5. Write a Python program to read a file line by line and store it into a list.

# lines_lst = []
# with open('sample.txt', 'r') as file:
#     for line in file:
#         lines_lst.append(line.strip())   # Remove extra newline
# print(lines_lst)
G
##-----------------------------------------------------------------------------------------------------------------------

# 6. Write a Python program to read a file line by line store it into a variable.

# content = ''
# with open('sample.txt', 'r') as file:
#     for line in file:
#         content += line      # Append each line to variable
# print(content)

##-----------------------------------------------------------------------------------------------------------------------

# 7. Write a python program to find the longest words.
# with open ('sample.txt', 'r') as file:
#     words = file.read().split()

# max_length = 0
# for word in words:
#     if len(word) > max_length:
#         max_length = len(word)

# longest_word = []
# for word in words:
#     if len(word) == max_length:
#         longest_word.append(word)

# print('Longesh word length :', max_length)
# print('Longest word (s) :' , longest_word)

##-----------------------------------------------------------------------------------------------------------------------

# 8. Write a Python program to count the number of lines in a text file.

# count = 0
# with open ('sample.txt' ,'r') as file:
#     for line in file:
#         count += 1 
# print('Number of lines in files',count)

# with open ('sample.txt', 'r') as file:
#     lines = file.readlines()
# print('Number of lines:', len(lines))

##-----------------------------------------------------------------------------------------------------------------------

# 9. Write a Python program to count the frequency of words in a file.

# word_count = {}
# with open('sample.txt', 'r') as file:
#     for line in file:
#         words = line.split()    # split linne into words
#         for word in words:
#             if word in word_count:
#                 word_count[word] += 1
#             else:
#                 word_count[word] = 1
# print('Wrods frequency :')
# for word, count in word_count.items():
#     print(word, ':', count)

# word_count = {}
# with open('Sample.txt', 'r') as file:
#     for line in file:
#         for word in line.split():
#             word_count[word] = word_count.get(word,0) + 1
# print(word_count)


##-----------------------------------------------------------------------------------------------------------------------

# 10. Write a Python program to get the file size of a plain file.

# import os 
# file_name = 'sample.txt'
# size =os.path.getsize(file_name)
# print('File size', size, 'bytes')

##-----------------------------------------------------------------------------------------------------------------------

# 11. Write a Python program to write a list to a file.

# list = [1,2,3,4,5,6,7,8,9,0]
# with open('sample.txt', 'w') as file:
#     for item in list:
#         file.write(str (item) + '\n')
# print('List written to file succesfully !')

# list = [1,2,3,4,5,6,7,8,9,0]
# with open('Sample.txt', 'w') as file:
#     file.write('\n'.join(map(str, list)))
# print('succesfully written')

##-----------------------------------------------------------------------------------------------------------------------

# 12. Write a Python program to copy the contents of a file to another file .

# with open ('source.txt', 'r') as src,open('destination.txt', 'w') as dest:
#     for line in src:
#         dest.write(line)
# print('File copied succesfully')

##-----------------------------------------------------------------------------------------------------------------------

# 13. Write a Python program to read a random line from a file.

# import random

# with open('sample.txt', 'r') as file:
#     lines = file.readines()
# if lines:
#     print(random.choice(lines))
# else:
#     print('file is empty')

##-----------------------------------------------------------------------------------------------------------------------

# 14. Write a Python program to assess if a file is closed or not.

# file = open('sample.txt', 'r')
# print('is file closed', file.closed)
# file.close()
# print('Is file closed after closing', file.closed)

##-----------------------------------------------------------------------------------------------------------------------

# 15.Write a Python program that takes a text file as input and returns the number of words of a given text file.

# file_name = input('Enter file name')
# with open (file_name,'r') as file:
#     content = file.read()
#     words = content.split()
#     count = len(words)
# print('total number of wrods :', count)

##-----------------------------------------------------------------------------------------------------------------------
