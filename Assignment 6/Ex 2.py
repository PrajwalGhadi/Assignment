'''Date - 27-05-2021
Author - Prajwal Ghadi
Aim -   Write a program that implements the conversion from human years to
dog years described in the previous paragraph. Ensure that your
program works correctly for conversions of less than two human years
and for conversions of two or more human years. Your program should
display an appropriate error message if the user enters a negative
number.'''


Human_year = int(input())

if Human_year == 1:
    print('dog year is 1 month')