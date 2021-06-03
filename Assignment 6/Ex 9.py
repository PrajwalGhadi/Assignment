'''Date - 27-05-2021
Author - Prajwal Ghadi
Aim -  The wavelength of visible light ranges from 380 to 750 nanometers
(nm). While the spectrum is continuous, it is often divided into 6 colors
as shown below:
Write a program that reads a wavelength from the user and reports its
color. Display an appropriate error message if the wavelength entered by the
user is outside of the visible spectrum.
'''

'''Color     Wavelength (nm)
Violet      380 to less than 450
Blue        450 to less than 495
Green       495 to less than 570
Yellow      570 to less than 590
Orange      590 to less than 620
Red         620 to 750'''


def Wavelength_Calc(wave):

    wavelenght = wave

    if 450 > wavelenght >= 380:
        print(f'{wavelenght} is an Violet Color Wavelength !!!')
    elif 495 > wavelenght >= 450:
        print(f'{wavelenght} is an Blue Color Wavelength !!!')
    elif 570 > wavelenght >= 495:
        print(f'{wavelenght} is an Green Color Wavelength !!!')
    elif 590 > wavelenght >= 570:
        print(f'{wavelenght} is an Yellow Color Wavelength !!!')
    elif 620 > wavelenght >= 590:
        print(f'{wavelenght} is an Orange Color Wavelength !!!')
    elif 750 > wavelenght >= 620:
        print(f'{wavelenght} is an Red Color Wavelength !!!')
    elif wavelenght > 750:
        print(f'Out of Range !!! \n Your Wavelength is {wavelenght} \n Perfect Range for wavelength is 380 to 750')
    elif wavelenght < 380:
        print(f'Out of Range !!! \n Your Wavelength is {wavelenght} \n Perfect Range for wavelength is 380 to 750')

if __name__ == '__main__':

    print('Please Enter the Wavelenght in Range Between (380 to 750)')
    wave = int(input('Enter the Wavelength:'))
    Wavelength_Calc(wave)