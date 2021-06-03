'''
Date - 3-06-2021
Author - Prajwal Ghadi
Aim -
'''

def Remove_Largest_Smallest(list):

    Original_list = list
    Original_list.sort() # Sorting of list to remove element from both end

    # This will create a copy of list by removing the First 2 and Last 2 Elements from Original list
    New_list = Original_list[2:-2]

    print(f'Original List is {Original_list} \n New List is {New_list}')


if __name__ == '__main__':

    # This Will take the input range which must be more than 4
    Number_Count = int(input('How many number you want in List:'))

    # This if statement will Check that Input is Greater than 4 or not
    if Number_Count < 4:
        print('List Stores more than 4 Integers')
        exit()

    Original_list = []  # It's an Empty list

    # This loop will generate the Items to store in list
    for i in range(Number_Count):
        Number_List = (int(input()))

        Original_list.append(Number_List)  # This will append all values in list

    Remove_Largest_Smallest(Original_list) # Calling Function