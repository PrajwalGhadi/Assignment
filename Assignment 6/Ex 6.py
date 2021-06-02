'''Date - 2-06-2021
Author - Prajwal Ghadi
Aim -  The following table lists the sound level in decibels for several common
noises.

Gas lawnmower 106
Alarm clock 70
Quiet room 40


Write a program that reads a sound level in decibels from the user. If the user
enters a decibel level that matches one of the noises in the table then your
program should display a message containing only that noise. If the user enters a number of decibels between the noises listed then your program
should display a message indicating which noises the level is between. Ensure
that your program also generates reasonable output for a value smaller than
the quietest noise in the table, and for a value larger than the loudest noise in
the table.
'''


def Sound_tracker(Sound_level): # Function to Calculate the Sound level

    Sound = Sound_level

    # Calculating Sound level using if-else statements
    if Sound == 130:
        print(f"{Sound} is an Sound of JackHammer Sound")
    elif Sound == 106:
        print(f'{Sound} is an Sound of Gas Lawnmower')
    elif Sound == 70:
        print(f'{Sound} is an Sound of Alarm Clock')
    elif Sound == 40:
        print(f'{Sound} is an Sound of Quiet Room')

    # Sound which is between the list of sound levels
    elif 130 > Sound > 106:
        print(f'{Sound} is between the level of JackHammer and Gas Lawnmower Sound')
    elif 106 > Sound > 70:
        print(f'{Sound} is between the level of Gas Lawnmower and Alarm Clock Sound')
    elif 70 > Sound > 40:
        print(f'{Sound} is between the level of Alarm Clock and Quiet Room Sound')

    # Sound which is more and less the top and bottom sound level
    elif Sound > 130:
        print(f'{Sound} is more than JackHammer Sound')
    elif Sound < 40:
        print(f'{Sound} is less than Quiet Room Sound')

    else:
        print('Please enter the Proper Value')


if __name__ == '__main__':

    Sound_level = int(input('Enter the Sound Level:')) # It will take an input as a Integer
    # send input to the Sound_tracker function to Calculate the Sound Level
    Sound_tracker(Sound_level)