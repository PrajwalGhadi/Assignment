'''
Date - 8-4-2021
Author - Prajwal Ghadigaonkar
Aim : Choose two of the programs you’ve written and add at least one comment
to each. If you don’t have anything specific to write because your programs
are too simple at this point, just add your name and the current date at the
top of each program file. Then write one sentence describing what the
program does
'''

print('''This is a simple and timepass idea...
        if You have Only Brothers enter 1
        if you have only Sister enter 2
        if you have both Brother and sister enter 3''')

Checker = int(input("Enter 1, 2, 3 according to above details:\n"))

if Checker == 1:
    Brother_list = []
    No_Brother = int(input('How many Brother do you have:\n'))
    print('Enter your brothers name:')
    for i in range(No_Brother):
        Brothers = input()
        Brother_list.append(Brothers)

    print('Your Brother names are:')
    for i in Brother_list:
        print(i)
    print('Thank You !!!')

elif Checker == 2:
    Sister_list = []
    No_Sister = int(input('How many Sister do you have:\n'))
    print('Enter your Sister name:')
    for i in range(No_Sister):
        Sisters = input()
        Sister_list.append(Sisters)

    print('Your Sister names are:')
    for i in Sister_list:
        print(i)
    print('Thank You !!!')

else:
    print('There is something wrong')