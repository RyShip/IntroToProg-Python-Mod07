# ---------------------------------------------------------------------------- #
# Title: Assignment 07 Try and Except demo
# Description: a quick and easy demo for try and except blocks
# This script was whipped up from scratch
# I chose to do this to really cement everything from mod 5, mod 6, and mod 7 together.  Hope you liked it.
# ChangeLog (Who,When,What):
# RShip,12/1/20,Modified code to complete assignment 7
# ---------------------------------------------------------------------------- #

def process_open_file(file):
    try:
        open_file = open(file, 'r')
    except FileNotFoundError:
        print('-'*50)
        print('Remember file name is case sensitive')
        print('-'*50)
        raise
    return open_file

def io_File_name():
    user_input = input('Please type in \'TestFile.txt\' to open it and read the data: ')
    return user_input, 'success'

def io_presentation_menu():
    print('Please press [1] to enter file name and retrieve data\nPlease press [2] to exit.')

def io_presentation_menu_choice():
    choice = input('Enter number here: ')
    return choice

while True:
    io_presentation_menu()
    input_choice = io_presentation_menu_choice()

    if input_choice == '1':
        try:
            file_choice, status = io_File_name()
            opened_file = process_open_file(file_choice)
        except:
            print('-' * 50)
            print('Please try again and don\'t forget the \'.txt\'!')
            print('-' * 50)
            file_choice, status = io_File_name()
            opened_file = process_open_file(file_choice)
            for row in opened_file:
                print('\n' + 'Your data:')
                print(row + '\n')
            continue
    else:
        print('\n' + 'C\'ya!')
        break
