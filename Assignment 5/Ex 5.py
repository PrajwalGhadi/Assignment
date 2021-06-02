'''
Date - 8-4-2021
Author - Prajwal Ghadigaonkar
Aim - Repeat Exercise 4, but this time store the famous person’s name in a
variable called famous_person. Then compose your message and store it in
a new variable called message. Print your message
'''

Author = input('Enter the Author name:\n') #This will take the Author name
Quote = input('Enter the Quote:\n') #This will take a Quote or Message of Author

#I have used fstring here...
print(f'{Author} once said, {Quote}')