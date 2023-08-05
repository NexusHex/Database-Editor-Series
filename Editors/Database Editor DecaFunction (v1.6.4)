# VERSION 1.6.4 <D.E.DECA>
# Requires file 'databases.txt'
# Requires modules 'loadingBar.py' and 'rotatingCube.py'

# NOTE: Some of the code used in this program has been taken from the responses of ChatGPT, but I have made sure to tweak every non-original response so I 
# have my own code, rather than the copy of a robot (anyways, the responses tend to fail a lot once the context of the code reaches over about 200 lines,
# so I kind of have to change the responses it gives me XD)

# NOTE: The modules 'loadingBar' and 'rotatingCube' are both altered versions of projects listed in the book 'The Big Book Of Small Python Projects'
# (Al Sweigart, No Starch Press), so look at those files directly to get a more specific idea of what I copied, deleted or edited

import sys, time, os
try:
    import loadingBar
except ImportError:
    print("Module 'loadingBar' does not exist in the same directory as the app. Please check the app directory and make sure that the module is there")
    sys.exit()

try:
    import rotatingCube
except ImportError:
    print("Module 'rotatingCube' does not exist in the same directory as the app. Please check the app directory and make sure that the module is there")
    sys.exit()

def add_to_database(data_store): # Is called when Option 1 is picked
  while True:
    dataAdd = input("\nAdd data to list (case-sensitive). Type \'stop\' to terminate: ")
    
    if dataAdd.lower() == "stop":
      print("\n")
      break
      
    data_store.append(dataAdd)

def view_database(data_store): # Is called when Option 2 is picked
  print("\nDatabase:\n")
  
  if len(data_store) == 0:
    print("Database empty\n")
  else:
    for x in data_store:
      print(x)

def save_to_file(data_store, fileName): # Is called when Option 6 is called
    try:
        with open(fileName, "a") as file:
            file.write("NEW DATABASE\n\n")
    
            for item in data_store:
                file.write(item + "\n")
      
            file.write("\nDATABASE END\n")
    except FileNotFoundError:
        print(f"File '{fileName}' does not exist in the directory(ies) listed by the code")
    except Exception as e:
        print(f"Error accessing file, here is the output from the app:\n{e}")
        print("\nIf you keep experiencing issues with the app like this and they do not seem to go away even when you fix the issue, please contact the creator in the comments section of whatever platform you are viewing this code on, thanks.\n")

def view_file(fileName): # Is called when Option 7 is called
    file_empty = os.path.Isize(fileName)
    try:
        with open(fileName, "r") as file:
            if file_empty == 0:
                print("The file is empty\n")
            else:
                for line in file.readlines():
                    print(line)
    except FileNotFoundError:
        print(f"File '{fileName}' does not exist in the directory(ies) listed by the code")
    except Exception as e:
        print(f"Error accessing file, here is the output from the app:\n{e}")
        print("\nIf you keep experiencing issues with the app like this and they do not seem to go away even when you fix the issue, please contact the creator in the comments section of whatever platform you are viewing this code on, thanks.\n")

def comment_to_file(fileName): # Is called when Option $ is called
    try:
        with open(fileName, "a") as file:
            comment = input("Add a comment to the file\n")
            file.write(f"NEW COMMENT\n\n{comment}\n\nCOMMENT END\n")
        print("\nComment added\n")
    except FileNotFoundError:
        print(f"File '{fileName}' does not exist in the directory(ies) listed by the code")
    except Exception as e:
        print(f"Error accessing file, here is the output from the app:\n{e}")
        print("\nIf you keep experiencing issues with the app like this and they do not seem to go away even when you fix the issue, please contact the creator in the comments section of whatever platform you are viewing this code on, thanks.\n")

def clear_file(fileName): # Is called when Option 8 is called
    try:
        print("Clearing file...")
        with open(fileName, "w"):
            pass
        print("File cleared!")
    except FileNotFoundError:
        print(f"File '{fileName}' does not exist in the directory(ies) listed by the code")
    except Exception as e:
        print(f"Error accessing file, here is the output from the app:\n{e}")
        print("\nIf you keep experiencing issues with the app like this and they do not seem to go away even when you fix the issue, please contact the creator in the comments section of whatever platform you are viewing this code on, thanks.\n")

def delete_from_database_file(fileName): # Is called when Option 10 is called (This func is a bit complicated so most lines will have explanations)
    # NOTE: This function was largely made using help from ChatGPT, and I have slightly tweaked the original code that it gave me, since it had errors :p
    try:
        with open(fileName, "r") as file: # Try opening the file 'fileName'
            lines = file.readlines() # Store all the lines in 'fileName' in a list 'lines'

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

        try:
            choice_idx = int(choice) - 1 # The numerical choice that the user made is assigned to a new variable and subtracted by 1 since list values start
                                         # from 0 instead of 1

            # If the inputted number is more than or equal to 0 and if that number is less than the maximum length of the amount of databases...
            if 0 <= choice_idx < len(databases):
                db_start = db_start_indices[choice_idx] # The start point of deletion = the numerical index assigned to a specific database (ex: 3)

                db_end = None
                # The program finds the end point of deletion by looking for a line where 'DATABASE END' is present within the range of
                # start point + 1 (list indexes start from 0) throughout the length of all the lines in the file
                for idx in range(db_start + 1, len(lines)):
                    # Program makes the end point of deletion = the nearest point to 'db_start' where 'DATABASE END' is present
                    if "DATABASE END" in lines[idx]:
                        db_end = idx
                        break # Don't repeat the loop again after the condition is fulfilled
                
                # If the program found an end point for deletion, delete all values that were stored in the 'lines' list (it included every line of the file)
                # from the start point to the end point + 1, since list indexes start from 0
                if db_end is not None:
                    del lines[db_start:db_end + 1]

                #Reopen the file in write mode to overwrite all old text, and rewrite the contents of the file minus the deleted database
                with open(fileName, "w") as file:
                    file.writelines(lines)

                print("\nDatabase deleted successfully.\n")

            else:
                print("\nInvalid input. Please enter a valid number.\n")

        # Everything under here handles any issues that the user, computer, or code compiler may make and handles them without crashing the program
        except ValueError:
            print("\nInvalid input. Please enter a valid number.\n")

    except FileNotFoundError:
        print(f"File '{fileName}' does not exist in the directory(ies) listed by the code")
    except Exception as e:
        print(f"Error accessing file, here is the output from the app:\n{e}")
        print("\nIf you keep experiencing issues with the app like this and they do not seem to go away even when you fix the issue, please contact the creator in the comments section of whatever platform you are viewing this code on, thanks.\n")

def show_all_patches(): # Is called when Option 90 is called
    patches = """
D.E.Quad (v1.0):
No date available

<new> Edit list 'data_store'
<new> Check the contents of list 'data_store'
<new> Clear list 'data_store' of all values
<new> Exit the app gracefully rather than an abprupt stop


D.E.Penta (v1.1):
Released on 07/18/2023

<new> Added ability to remove specific items from the database


D.E.Hexa (v1.2):
Released on 07/26/2023

<new> All changes made are saved to a file 'databases.txt'. Multiple sessions' worth of files can be stored there


D.E.Hepta (v1.3.1):
Released on 08/01/2023

<new> Added the ability to wipe and create a new database session (now you don't have to repeatedly clear and save databases to 'databases.txt' in the same session)
<QoL> Renamed variable 'data' to 'data_store' to avoid readability issues 
<QoL> User can now view all patch notes within command 'patches' or '_p' when the Editor prompts you to pick an option 
<QoL> Command to exit the Editor has been changed to 'exit' or 'e' 
-bug- Fixed an issue where there was no newline after 'view_database()' printed its contents


D.E.Octa (v1.4.2):
Released on 08/02/2023

<new> Added the ability to view contents of 'databases.txt'
<QoL> Text at the start of the program + app options text has had a visual overhaul
<QoL> Gave all past version patch notes titles for the type of change that occured (<new> , -bug- , <QoL>)
<QoL> Command to exit Editor has been changed to '!' in correspondance with a bug found during testing
-bug- Fixed indents in 'patches' var pushing text over onto the next line
-bug- Fixed many indent irregularities throughout the code for ease of code reading
-bug- Fixed bug causing any string input to the Editor including the designated 'exit' and 'e' inputs to leave the Editor
-bug- Added missing newline at the beginng of the input error syntax under 'else:'


D.E.Octa - QoL Update (v1.4.3):
Released on 08/03/2023

<QoL> Print the database session number that you are on (updates every time a new database session is created using function 6)
<QoL> Added ability to see all patch notes or just the ones for the current version
<QoL> Renamed function 'show_patches()' to 'show_all_patches()'
<QoL> Allow user to add comments like titles, notes etc to the file 'databases.txt'
<QoL> Keep a short wait between executing a command - checking the contents of a database - and re-printing the options bar (waiting times will vary between different events)
<QoL> Removed unneccessary newlines from the Edtior options menu


D.E.Nona (v1.5.3):
Released on 08/04/2023

<new> Users can now clear the 'databases.txt' file
<QoL> The option to delete certain items from the database is now a loop to allow multiple specific items to be removed in one go
<QoL> Added graceful error handling for all file-related functions
<QoL> Added graceful error handling at the start of the 'main()' function to check if the file exists


D.E.Nona - Visuals Update (v1.5.4):
Released on 08/05/2023

<visual> Added a loading bar at the start of the program to simulate the app loading up
<visual> Add a floating + spinning cube to the screen once the user leaves the editor. It can be cancelled by pressing Ctrl + C
<QoL> Changed the indent levels of titles within the option select text
<QoL> App now clears the shell of all text for Operations 90 (show all patches), 91 (show current patch) and ! (exit the editor)


LATEST VERSION (08/06/2023)
D.E.Deca (v1.6.4):

>>>>>>>>>>>>> Remove certain databases from the 'databases.txt' file
>>>>>>>>>>>>> User can shorten the wait time between events by using an in-built command (QoL)
>>>>>>>>>>>>> Flavor text printed after saving a database to the file has been rewritten (QoL)
>>>>>>>>>>>>> Users have the option to turn off the animations in the Editor menu (QoL)
>>>>>>>>>>>>> Options for checking current/all patch notes have been renamed to '0' and '00' (QoL)
>>>>>>>>>>>>> Function 'view_file()' now returns 'The file is empty' if there are no databases or comments within the file (QoL)

Bug Fixes
------------- NO BUG FIXES THIS PATCH

Notes
............. Hi! In this new version of the editor, you can now delete certain databases that have been stored within the .txt file using an in-built command! There have also been some changes to other cosmetic features of the editor. Enjoy!


Plans for future versions...

Text-to-Speech Update (v1.6.5):
TTSPatch > Users can choose to have the responses of the code read aloud to them
    """
    print(patches)

def show_current_patch(): # Is called when Option 91 is called
    current_patch = """
LATEST VERSION (08/06/2023)
D.E.Deca (v1.6.4):

>>>>>>>>>>>>> Remove certain databases from the 'databases.txt' file
>>>>>>>>>>>>> User can shorten the wait time between events by using an in-built command (QoL)
>>>>>>>>>>>>> Flavor text printed after saving a database to the file has been rewritten (QoL)
>>>>>>>>>>>>> Users have the option to turn off the animations in the Editor menu (QoL)
>>>>>>>>>>>>> Options for checking current/all patch notes have been renamed to '0' and '00' (QoL)
>>>>>>>>>>>>> Function 'view_file()' now returns 'The file is empty' if there are no databases or comments within the file (QoL)

Bug Fixes
------------- NO BUG FIXES THIS PATCH

Notes
............. Hi! In this new version of the editor, you can now delete certain databases that have been stored within the .txt file using an in-built command! There have also been some changes to other cosmetic features of the editor. Enjoy!
    """
    print(current_patch)

def main():
    fileName = "C:/Users/Khizar/Desktop/Coding/Python Projects/Database Editor Series/databases.txt"
    try: # Checking to make sure that 'databases.txt' is accessible to the app at the start of the program
        with open(fileName, "r"):
            pass
    except FileNotFoundError:
        print(f"File 'databases.txt' does not exist in the listed PATH for 'fileName':\n{fileName}")
        time.sleep(1)
        sys.exit()
    except Exception as e:
        print(f"There was an error accessing the file 'databases.txt' at {fileName}. Please refer to the error and rectify the issue:\n{e}")
        time.sleep(1)
        sys.exit()

    data_store = []
    dataSession = 1
    fast = False
    animations = True
    print("Entering the Database Editor...\n")

    if animations == True:
        loadingBar.bar() # A loading bar that appears whenever the program is started
    else:
        pass

    print('\n')
    time.sleep(1)
  
    while True:
        print("""
Database Editing -\n
    1. Edit the data
    2. View the contents of the current database
    3. Remove select values from the current database
    4. Clear the database of all data
    5. Clear + create a new database session\n
Files -\n
    6. Save the current database to a file
    7. View the contents of the file holding all databases
    8. Clear the database file of all databases
    9. Write a comment to the database-holding file
    10. Remove certain databases from the database-holding file\n
Other -\n
    0. Check patch notes for the current version only
    00. Check all past and current patch notes
    ? - Fast Mode (! NEW !)
    ~ - Low Performance Mode (! NEW !)
    ! -  Exit the Database Editor\n
        """)
        choice = input("Enter one of the options: ")
        if choice == "1": # Edit the data
            add_to_database(data_store)

        elif choice == "2": # View the current database
            print(f"\nDatabase Session {dataSession}")
            view_database(data_store)

            if fast == True:
                time.sleep(1.5)
            else:
                time.sleep(3)

        elif choice == "3": # Remove certain values from the current database
            while True:
                view_database(data_store)
                print("\nSelect the value you would like to remove. Type '!' to exit (case-sensitive)\n")
                dataRemove = input()

                if dataRemove == "!":
                    break
                else:
                    print("\nRemoving data...\n")
                    data_store.remove(dataRemove)

                    if fast == True:
                        time.sleep(0.5)
                    else:
                        time.sleep(1)
                    print("\nData removed\n")

        elif choice == "4": # Clear the database
            data_store.clear()
            print("\nDatabase wiped\n")

            if fast == True:
                time.sleep(0.25)
            else:
                time.sleep(0.5)

        elif choice == "5": # Clear + create a new database session
            data_store.clear()
            dataSession += 1
            print(f"\nNew session\nDatabase Session {dataSession}")

            if fast == True:
                time.sleep(0.25)
            else:
                time.sleep(0.5)

        elif choice == "6": # Save the current database to a file
            save_to_file(data_store, fileName)
            print("\nDatabase saved. If you would like to see the saved values, use Option 7 in the Editor menu\n")

            if fast == True:
                time.sleep(0.75)
            else:
                time.sleep(1.5)

        elif choice == "7": # View the contents of the file holding all databases
            view_file(fileName)

            if fast == True:
                time.sleep(2.5)
            else:
                time.sleep(5)
        
        elif choice == "8":
            clear_file(fileName)

            if fast == True:
                time.sleep(0.25)
            else:
                time.sleep(0.5)

        elif choice == "9":
            comment_to_file(fileName)

            if fast == True:
                time.sleep(0.25)
            else:
                time.sleep(0.5)
        
        elif choice == "10":
            delete_from_database_file(fileName)

        elif choice == "0": # Show the patch notes for the current patch
            os.system('cls')
            show_current_patch()

            if fast == True:
                time.sleep(2.5)
            else:
                time.sleep(5)
              
        elif choice == "00":
            os.system('cls')
            show_all_patches()

            if fast == True:
                time.sleep(5)
            else:
                time.sleep(10)

        elif choice == "?":
            print("\nFast Mode allows you to have shortened wait times between the execution of commands in the Editor. Would you like to turn this feature on?\n")
            print("WARNING: This feature cannot be turned off once it is turned on. You must quit and restart to go back to the normal wait times.")

            while True:
                speed_choice = input("\nTurn Fast Mode on? y/n: ")

                if speed_choice == "y":
                    fast = True
                    print("\nFast Mode is now ON\n")
                    time.sleep(1)
                    break
                elif speed_choice == "n":
                    print("\nFast Mode will remain OFF\n")
                    time.sleep(1)
                    break
                else:
                    print("\nInvalid response, try again\n")
                    time.sleep(0.5)

        elif choice == "~":
            print("Low Performance Mode disables all animations in the app, and is useful for people who have machines that can't handle things like 3D text shapes or ASCII characters.")
            print("WARNING: This feature cannot be turned off once it is turned on. You must quit and restart to get the standard animations again.")

            while True:
                anim_choice = input("\nTurn Low Performance Mode on? y/n: ")

                if anim_choice == "y":
                    animations = False
                    print("\nLow Performance Mode is now ON\n")
                    time.sleep(1)
                    break
                elif anim_choice == "n":
                    print("\nLow Performance Mode will remain OFF\n")
                    time.sleep(1)
                    break
                else:
                    print("\nInvalid response, try again\n")

        elif choice == "!": # Exit the Database Editor
            os.system('cls')
            print("\nThank you so much for using my app!\n\nExiting Database Editor...\n")
            time.sleep(2.5)

            if animations == True:
                rotatingCube.cube()
                os.system('cls')
                break
            else:
                os.system('cls')
                break

        else:
            print("\nInvalid input, try again. Remember that the inputs are case-sensitive.\n")

            if fast == True:
                time.sleep(0.25)
            else:
                time.sleep(0.5)

main()
