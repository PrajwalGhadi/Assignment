'''Date - 27-05-2021
Author - Prajwal Ghadi
Aim -  Write a program that reads an integer from the user. Then your
program should display a message indicating whether the integer is
even or odd'''

def EvenOdd(UserInput):
    User = UserInput
    if User % 2 == 0:
        print(f"{User} is Even")
    else:
        print(f"{User} is Odd")


if __name__ == "__main__":
    UserInput = int(input("Enter the Number to check Even Or Odd:" ))
    EvenOdd(UserInput)