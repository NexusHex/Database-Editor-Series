import sys
import os
import time

data_store = []


class Editor:
    def __init__(self, data_file, patch_file):
        self.data_file = data_file
        self.patch_file = patch_file

        try:
            with open(data_file, 'r'):
                pass
        except FileNotFoundError:
            print("The file used to store values from the database cannot be found. Please check the program folder")
            sys.exit()

        try:
            with open(patch_file, 'r'):
                pass
        except FileNotFoundError:
            print("The file containing the patch notes couldn't be found. Please check the program folder")
            sys.exit()

        self.data_store = data_store
        self.data_session = 1
        self.fast_mode = False
        self.animations = True

    @staticmethod
    def add_to_database(value):  # Option 1
        data_store.append(value)

    @staticmethod
    def view_database():  # Option 2
        if len(data_store) == 0:
            print("Database Empty")
        else:
            for item in data_store:
                print(item)
        time.sleep(2)

    def delete_certain_values(self):  # Option 3
        if len(data_store) == 0:
            print("Nothing to delete")
        else:
            while True:
                Editor.view_database()
                remove_value = input("\nType out the value you would like to remove from the database. Type 'q' to exit\n")
                if remove_value.lower() == 'q':
                    break
                else:
                    try:
                        data_store.remove(remove_value)
                    except ValueError:
                        print("Invalid input, try again\n")
                    else:
                        print("Data removed\n")
        if self.fast_mode:
            time.sleep(0.5)
        else:
            time.sleep(1)

    def clear_database(self):  # Option 4
        data_store.clear()
        print("Database cleared\n")
        if self.fast_mode:
            time.sleep(0.25)
        else:
            time.sleep(0.5)

    def new_session(self):  # Option 5
        data_store.clear()
        self.data_session += 1
        print(f"New Database Session\nDatabase Session: {self.data_session}")
        if self.fast_mode:
            time.sleep(0.75)
        else:
            time.sleep(1.5)

    def save_to_file(self):  # Option 6
        try:
            with open(self.data_file, 'a') as file:
                file.write("NEW DATABASE\n\n")

                for item in data_store:
                    file.write(item + '\n')

                file.write("\nDATABASE END\n")
        except FileNotFoundError:
            print(f"File {self.data_file} cannot be found. Please check the program's file directory")
            sys.exit()
        if self.fast_mode:
            time.sleep(0.75)
        else:
            time.sleep(1.5)

    def view_file(self):  # Option 7
        file_empty = os.path.getsize(self.data_file)
        try:
            with open(self.data_file, 'r') as file:
                if file_empty == 0:
                    print("File is empty")
                else:
                    for line in file.readlines():
                        print(line)
        except FileNotFoundError:
            print(f"File {self.data_file} cannot be found. Please check the program's file directory")
            sys.exit()
        if self.fast_mode:
            time.sleep(2.5)
        else:
            time.sleep(5)

    def clear_file(self):  # Option 8
        try:
            with open(self.data_file, 'w') as file:
                file.write('')
        except FileNotFoundError:
            print(f"File {self.data_file} cannot be found. Please check the program's file directory")
            sys.exit()
        else:
            file_size = os.path.getsize(self.data_file)
            if file_size != 0:
                try:
                    with open('databases.txt', 'w') as file:
                        pass
                except FileNotFoundError:
                    print(f"File {self.data_file} cannot be found. Please check the program's file directory")
                    sys.exit()
        if self.fast_mode:
            time.sleep(0.25)
        else:
            time.sleep(0.5)

    def comment_to_file(self):  # Option 9
        try:
            with open(self.data_file, 'a') as file:
                comment = input("Type the comment that you would like to add to the file:\n")
                file.write(f"NEW COMMENT\n\n{comment}\n\n COMMENT END")
            print("Comment added")
        except FileNotFoundError:
            print(f"File {self.data_file} cannot be found. Please check the program's file directory")
            sys.exit()
        if self.fast_mode:
            time.sleep(0.25)
        else:
            time.sleep(5)

    def delete_from_file(self): # Option 10
        try:
            with open(self.data_file, "r") as file:  # Try opening the file 'FILENAME'
                lines = file.readlines()  # Store all the lines in 'FILENAME' in a list 'lines'

            databases = []
            db_start_indices = []

            # For every number of database stored - db 1, db 2, db 3... - (idx) and the content within each line of each database (line) in the number of lines
            # (lines) that the whole file has...
            for idx, line in enumerate(lines):
                # Check whether each line says 'NEW DATABASE', takes each instance out of the file and adds that name to the 'databases' list defined earlier.
                # It also appends the value of the database number to list 'db_start_indices'
                if "NEW DATABASE" in line:
                    db_name = line.strip().replace("NEW DATABASE", "")
                    databases.append(db_name)
                    db_start_indices.append(idx)

            # If there are no databases found within the file, say that there aren't any databases to delete and go back to the options menu
            if not databases:
                print("\nNo databases found for deletion.\n")
                return

            # If there were databases to delete, show them to the user by giving them a list of numbers going up by ones (1, 2, 3, 4...)
            print("\nDatabases available for deletion:\n")
            for idx, db in enumerate(databases, start=1):
                print(f"{idx}. {db}")

            # User decides which database to delete based on the number that they input (they can also type 'exit' to cancel last-minute)
            choice = input("\nEnter the number of the database you want to delete (or 'exit' to cancel): ")

            if choice == "exit":
                print("\nDeletion canceled.\n")
                return

            choice_idx = int(
                choice) - 1  # The numerical choice that the user made is assigned to a new variable and subtracted by 1 since list values start
            # from 0 instead of 1

            while True:
                # If the inputted number is more than or equal to 0 and if that number is less than the maximum length of the amount of databases...
                if 0 <= choice_idx < len(databases):
                    db_start = db_start_indices[
                        choice_idx]  # The start point of deletion = the numerical index assigned to a specific database (ex: 3)

                    db_end = None
                    # The program finds the end point of deletion by looking for a line where 'DATABASE END' is present within the range of
                    # start point + 1 (list indexes start from 0) throughout the length of all the lines in the file
                    for idx in range(db_start + 1, len(lines)):
                        # Program makes the end point of deletion = the nearest point to 'db_start' where 'DATABASE END' is present
                        if "DATABASE END" in lines[idx]:
                            db_end = idx
                            break  # Don't repeat the loop again after the condition is fulfilled

                    # If the program found an end point for deletion, delete all values that were stored in the 'lines' list (it included every line of the file)
                    # from the start point to the end point + 1, since list indexes start from 0
                    if db_end is not None:
                        del lines[db_start:db_end + 1]

                    # Reopen the file in write mode to overwrite all old text, and rewrite the contents of the file minus the deleted database
                    with open(self.data_file, "w") as file:
                        file.writelines(lines)

                    print("\nDatabase deleted successfully.\n")
                    break
                else:
                    print("\nInvalid input. Please enter a valid number.\n")

        except FileNotFoundError:
            print(f"File {self.data_file} cannot be found. Please check the program's file directory")
            sys.exit()

    def see_current_patch_notes(self):
        os.system('cls')
        current_patch = """
        LATEST VERSION (08/29/2023)
        D.E.Deca (v1.6.7):

        Additions
        >>>>>>>>>>>>> The program has now been transferred from non-OOP layout to an OOP layout.

        Bug Fixes
        ------------- NO BUG FIXES THIS PATCH
        """
        print(current_patch)
        if self.fast_mode:
            time.sleep(2.5)
        else:
            time.sleep(5)

    def see_all_patch_notes(self):
        try:
            with open(self.patch_file) as file:
                for line in file.readlines():
                    print(line)
        except FileNotFoundError:
            print(f"File {self.patch_file} cannot be found. Please check the program's file directory")
        if self.fast_mode:
            time.sleep(5)
        else:
            time.sleep(10)

    def fast_mode_toggle(self):
        print("\nFast Mode allows you to have shortened wait times between the execution of commands in the Editor. Would you like to turn this feature on?\n")
        print("WARNING: This feature cannot be turned off once it is turned on. You must quit and restart to go back to the normal wait times.")
        while True:
            speed_choice = input("\nTurn on Fast Mode? y/n: ")

            if speed_choice[0] == 'y':
                self.fast_mode = True
                print("\nFast Mode is now ON\n")
                time.sleep(1)
                break
            elif speed_choice[0] == 'n':
                # Fast Mode is False from run, so nothing changes (line 29)
                print("\nFast Mode will remain OFF\n")
                time.sleep(1)
                break
            else:
                print("Invalid input. Try again")
                time.sleep(0.5)

    def low_performance_toggle(self):
        print("Low Performance Mode disables all animations in the app, and is useful for people who have machines that can't handle things like 3D text shapes or ASCII characters.")
        print("WARNING: This feature cannot be turned off once it is turned on. You must quit and restart to get the standard animations again.")
        while True:
            anim_choice = input("\nTurn Low Performance Mode on? y/n: ")

            if anim_choice == "y":
                self.animations = False
                print("\nLow Performance Mode is now ON\n")
                time.sleep(1)
                break
            elif anim_choice == "n":
                print("\nLow Performance Mode will remain OFF\n")
                time.sleep(1)
                break
            else:
                print("\nInvalid response, try again\n")


