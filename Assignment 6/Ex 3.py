'''Date - 28-05-2021
Author - Prajwal Ghadi
Aim -  Create a program that reads a letter of the alphabet from the user. If the
user enters a, e, i, o or u then your program should display a message
indicating that the entered letter is a vowel. If the user enters y then
your program should display a message indicating that sometimes y is a
vowel, and sometimes y is a consonant. Otherwise your program should
display a message indicating that the letter is a consonant.'''

def Vowel_Checker(user_input):

    user = user_input
    if user == 'a' or user == 'A':
        print(f'{user} is Vowel')
    elif user == 'e' or user == 'E':
        print(f'{user} is Vowel')
    elif user == 'i' or user == "I":
        print(f'{user} is Vowel')
    elif user == 'o' or user == 'O':
        print(f'{user} is Vowel')
    elif user == 'u' or user == 'U':
        print(f'{user} is Vowel')
    elif user == 'y' or user == 'Y':
        print(f'sometimes {user} is vowel and sometimes {user} is consonant')

if __name__ == '__main__':

    user_input = input('Enter the Alphabet :')
    Vowel_Checker(user_input)