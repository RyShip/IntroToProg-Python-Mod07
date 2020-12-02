# ---------------------------------------------------------------------------- #
# Title: Assignment 07
# Description: Time to make some pickles!  I basically re-purposed the assignment 6 script to allow the user to add
# colors and rate them.
# the data is then pickled into a file and then reloaded from the file.
# I chose to do this to really cement everything from mod 5, mod 6, and mod 7 together.  Hope you liked it.
# ChangeLog (Who,When,What):
# RShip,12/01/20,Modified code to complete assignment 7
# ---------------------------------------------------------------------------- #


# Defining Variables#
lstTable = []
strFileName = "pickled_color_choice.txt"



class Processor:

    @staticmethod
    def read_pickled_data_from_file(file_name):
        import pickle
        file = open(file_name, 'rb')
        new_dic = pickle.load(file)
        file.close()
        return new_dic, 'success'

    @staticmethod
    def add_data_to_list(task, priority, list_of_rows):
        row = {'Task': task, 'Priority': priority}
        list_of_rows.append(row)
        return list_of_rows, 'Success'

    @staticmethod
    def pickle_data_to_file(file_name, list_of_rows):
        import pickle
        file = open(file_name, 'wb')
        pickle.dump(list_of_rows, file)
        file.close()
        return list_of_rows, 'Success'


class IO:

    @staticmethod
    def print_menu_Tasks():
        print('''
        Menu of Options
        1) Add a new Color
        2) Pickle all Data to File        
        3) Reload all Pickled Data from File
        4) Exit Program
        ''')
        print()

    @staticmethod
    def print_current_Tasks_in_list(list_of_rows):
        print("------- The current Tasks ToDo are: -------")
        for row in list_of_rows:
            print(row["Task"] + " (" + row["Priority"] + ")")
        print("--------------------------------------------")
        print()

    @staticmethod
    def input_menu_choice():
        choice = str(input("Which option would you like to perform? [1 to 4] - ")).strip()
        print()
        return choice

    @staticmethod
    def input_new_task_and_priority():
        task = str(input('please enter a Color: '))
        priority = str(input('please rate this color [10 = I like!]  [1 = Not my style]: '))
        return task, priority

    @staticmethod
    def input_press_to_continue(optional_message=''):
        print(optional_message)
        input('Press the [Enter] key to continue.')

    @staticmethod
    def input_yes_no_choice(message):
        return str(input(message)).strip().lower()

    @staticmethod
    def pickle_data_from_file(new_dict):
        print('\n' + 'Your un-pickled data is -' + '\n')
        for row in new_dict:
            print(row["Task"] + " (" + row["Priority"] + ")")
        print(type(new_dict))
        print('\n' + '-' * 50)


while True:
    IO.print_current_Tasks_in_list(lstTable)
    IO.print_menu_Tasks()
    strChoice = IO.input_menu_choice()

    if strChoice.strip() == '1':
        strTask, strPriority = IO.input_new_task_and_priority()
        lstTable, strStatus = Processor.add_data_to_list(strTask, strPriority, lstTable)
        IO.input_press_to_continue(strStatus)


    elif strChoice == '2':
        strChoice = IO.input_yes_no_choice("Pickle this data to file? (y/n) - ")
        if strChoice.lower() == "y":
            lstTable, strStatus = Processor.pickle_data_to_file(strFileName, lstTable)
            IO.input_press_to_continue(strStatus)
        else:
            IO.input_press_to_continue("Save Cancelled!")


    elif strChoice == '3':
        print("Reloading Pickled Data")
        strChoice = IO.input_yes_no_choice("Are you sure you want to reload pickled data from file? (y/n) -  ")
        if strChoice.lower() == 'y':
            lst_table, strStatus = Processor.read_pickled_data_from_file(strFileName)
            IO.input_press_to_continue(strStatus)
            IO.pickle_data_from_file(lst_table)
        else:
            IO.input_press_to_continue("File Reload  Cancelled!")


    elif strChoice == '4':
        print("Goodbye!")
        break