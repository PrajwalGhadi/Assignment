'''Date - 2-6-2021
Author - Prajwal Ghadi
Aim - The length of a month varies from 28 to 31 days. In this exercise you
will create a program that reads the name of a month from the user as a
string. Then your program should display the number of days in that
month. Display “28 or 29 days” for February so that leap years are
addressed.'''

def Day_Calculator(Name_Month):

    month = Name_Month

    if month == 'January':
        print(f"{month} has 31 Days")
    elif month == 'February':
        print(f"{month} has 28 or 29 Days")
    elif month == 'March':
        print(f"{month} has 31 Days")
    elif month == 'April':
        print(f"{month} has 30 Days")
    elif month == 'May':
        print(f"{month} has 31 Days")
    elif month == 'June':
        print(f"{month} has 30 Days")
    elif month == 'July':
        print(f"{month} has 31 Days")
    elif month == 'August':
        print(f"{month} has 31 Days")
    elif month == 'September':
        print(f"{month} has 30 Days")
    elif month == 'October':
        print(f"{month} has 31 Days")
    elif month == 'November':
        print(f"{month} has 30 Days")
    elif month == 'December':
        print(f"{month} has 31 Days")
    else:
        print('Please Enter the proper month!!!')

if __name__ == '__main__':

    Name_Month = input('Enter the Name of Month: ').capitalize()
    Day_Calculator(Name_Month)