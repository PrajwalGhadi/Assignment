'''Date - 2-06-2021
Author - Prajwal Ghadi
Aim -  Write a program that determines the name of a shape from its number
of sides. Read the number of sides from the user and then report the
appropriate name as part of a meaningful message. Your program
should support shapes with anywhere from 3 up to (and including) 10
sides. If a number of sides outside of this range is entered then your
program should display an appropriate error message.'''


def shapes(a):

    sides = a
    if sides == 3:
        print(f'{sides} sided shape is Triangle')
    elif sides == 4:
        print(f'{sides} sided shape is Square')
    elif sides == 5:
        print(f'{sides} sided shape is Pentagon')
    elif sides == 6:
        print(f'{sides} sided shape is Hexagon')
    elif sides == 7:
        print(f'{sides} sided shape is Heptagon')
    elif sides == 8:
        print(f'{sides} sided shape is Octagon')
    elif sides == 9:
        print(f'{sides} sided shape is Nanogon')
    elif sides == 10:
        print(f'{sides} sided shape is Decagon')
    elif sides < 3:
        print('Please Enter Side More than 3 or 3')
    elif sides > 10:
        print('Please Enter Side less than 10 or 10')
    else:
        print("Please Enter only Numbers")
if __name__ == "__main__":

    print('Sides of shape must be in a range of 3 to 10')
    Sides = int(input("How many side of shape do you want:"))
    shapes(Sides)
