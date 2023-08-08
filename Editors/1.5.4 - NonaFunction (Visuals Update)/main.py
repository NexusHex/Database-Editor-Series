# VERSION 1.5.4 <D.E.NONA - Visuals Update>
# Requires file 'databases.txt'
# Requires modules 'loadingBar.py' and 'rotatingCube.py'

import loadingBar, rotatingCube, sys, time, os
def add_to_database(data_store): # Gets called when Option 1 is picked
  while True:
    dataAdd = input("\nAdd data to list (case-sensitive). Type \'stop\' to terminate: ")
    
    if dataAdd.lower() == "stop":
      print("\n")
      break
      
    data_store.append(dataAdd)

def view_database(data_store): # Gets called when Option 2 is picked
  print("\nDatabase:\n")
  
  if len(data_store) == 0:
    print("Database empty\n")
  else:
    for x in data_store:
      print(x)

def save_to_file(data_store, fileName): # Gets called when Option 6 is called
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

def view_file(fileName): # Gets called when Option 7 is called
    try:
        with open(fileName, "r") as file:
            for line in file.readlines():
                print(line)
    except FileNotFoundError:
        print(f"File '{fileName}' does not exist in the directory(ies) listed by the code")
    except Exception as e:
        print(f"Error accessing file, here is the output from the app:\n{e}")
        print("\nIf you keep experiencing issues with the app like this and they do not seem to go away even when you fix the issue, please contact the creator in the comments section of whatever platform you are viewing this code on, thanks.\n")

def comment_to_file(fileName): # Gets called when Option $ is called
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

def clear_file(fileName): # Gets called when Option 8 is called
    try:
        print("Clearing file...")
        with open(fileName, "w"):
            pass
        time.sleep(1)
        print("File cleared!")
    except FileNotFoundError:
        print(f"File '{fileName}' does not exist in the directory(ies) listed by the code")
    except Exception as e:
        print(f"Error accessing file, here is the output from the app:\n{e}")
        print("\nIf you keep experiencing issues with the app like this and they do not seem to go away even when you fix the issue, please contact the creator in the comments section of whatever platform you are viewing this code on, thanks.\n")


def show_all_patches(): # Gets called when Option 90 is called
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

LATEST VERSION (08/05/2023)
D.E.Nona - Visuals Update (v1.5.4):

Additions

>>>>>>>>>>>>> Added a loading bar at the start of the program to simulate the app loading up (Visual)
>>>>>>>>>>>>> Add a floating + spinning cube to the screen once the user leaves the editor. It can be cancelled by pressing Ctrl + C (Visual)
>>>>>>>>>>>>> Changed the indent levels of titles within the option select text (QoL)
>>>>>>>>>>>>> App now clears the shell of all text for Operations 90 (show all patches), 91 (show current patch) and ! (exit the editor) (QoL)

Bug Fixes
------------- NO BUG FIXES THIS PATCH

Notes
............. Time to add some flair to this boring terminal window app and make things look nice! Many thanks to Al Sweigart for making both the Loading Bar base code and the Rotating Cube base code, both of which I had much fun editing for my own purposes.


Plans for future versions...
   
D.E.Deca (v1.6.4):
MainPatch > Remove certain databases from the 'databases.txt' file
Other patches may be added below this line if I think of something

Text-to-Speech Update (v1.6.5):
TTSPatch > Users can choose to have the responses of the code read aloud to them
    """
    print(patches)

def show_current_patch(): # Gets called when Option 91 is called
    current_patch = """
LATEST VERSION (08/05/2023)
D.E.Nona - Visuals Update (v1.5.4):

Additions

>>>>>>>>>>>>> Added a loading bar at the start of the program to simulate the app loading up (Visual)
>>>>>>>>>>>>> Add a floating + spinning cube to the screen once the user leaves the editor. It can be cancelled by pressing Ctrl + C (Visual)
>>>>>>>>>>>>> Changed the indent levels of titles within the option select text (QoL)
>>>>>>>>>>>>> App now clears the shell of all text for Operations 90 (show all patches), 91 (show current patch) and ! (exit the editor) (QoL)

Bug Fixes
------------- NO BUG FIXES THIS PATCH

Notes
............. Time to add some flair to this boring terminal window app and make things look nice! Many thanks to Al Sweigart for making both the Loading Bar base code and the Rotating Cube base code, both of which I had much fun editing for my own purposes.
    """
    print(current_patch)

def main():
    fileName = "databases.txt"
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
    print("Entering the Database Editor...\n")
    loadingBar.bar() # A loading bar that appears whenever the program is started
    print('\n')
    time.sleep(1)
  
    while True:
        print("""
Database Editing -\n
    1. Edit the data
    2. View the contents of the current database
    3. Remove select values from the current database (! UPDATED !)
    4. Clear the database of all data
    5. Clear + create a new database session\n
Files -\n
    6. Save the current database to a file
    7. View the contents of the file holding all databases
    8. Clear the database file of all databases (! NEW !)
    $. Write a comment to the database-holding file\n
Other -\n
    90. Check patch notes for the current version only
    91. Check all past and current patch notes
    ! -  Exit the Database Editor\n
        """)
        choice = input("Enter one of the options: ")
        if choice == "1": # Edit the data
            add_to_database(data_store)

        elif choice == "2": # View the current database
            print(f"\nDatabase Session {dataSession}")
            view_database(data_store)
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
                    time.sleep(1)
                    print("\nData removed\n")

        elif choice == "4": # Clear the database
            data_store.clear()
            print("\nDatabase wiped\n")
            time.sleep(0.5)

        elif choice == "5": # Clear + create a new database session
            data_store.clear()
            dataSession += 1
            print(f"\nNew session\nDatabase Session {dataSession}")
            time.sleep(0.5)

        elif choice == "6": # Save the current database to a file
            save_to_file(data_store, fileName)
            print("\nDatabase saved. If you would like to see the saved values, check the file named 'databases.txt'.\n")
            time.sleep(1.5)

        elif choice == "7": # View the contents of the file holding all databases
            view_file(fileName)
            time.sleep(5)
        
        elif choice == "8": # NEW
            clear_file(fileName)
            time.sleep(0.5)

        elif choice == "$":
           comment_to_file(fileName)
           time.sleep(0.5)
        
        elif choice == "90": # Show the patch notes for the current patch
           os.system('cls')
           show_current_patch()
           time.sleep(5)
              
        elif choice == "91":
            os.system('cls')
            show_all_patches()
            time.sleep(10)

        elif choice == "!": # Exit the Database Editor
            os.system('cls')
            print("\nThank you so much for using my app!\n\nExiting Database Editor...\n")
            time.sleep(2.5)
            rotatingCube.cube()
            os.system('cls')
            break

        else:
            print("\nInvalid input, try again. Remember that the inputs are case-sensitive.\n")
            time.sleep(0.5)

main()
