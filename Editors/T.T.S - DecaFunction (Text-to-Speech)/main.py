# VERSION T.T.S <D.E.DECA - TTS UPDT>
# Requires files 'databases.txt', 'all_patch_notes.txt' and 'latest_patch_notes.txt'
# Requires external module 'pyttsx4'

# NOTE: Some of the code used in this program has been taken from the responses of ChatGPT, but I have made sure to tweak every non-original response so I 
# have my own code, rather than the copy of a robot (anyways, the responses tend to fail a lot once the context of the code reaches over about 200 lines,
# so I kind of have to change the responses it gives me XD)

# NOTE: This version of the program does not include the modules added in the Visuals Update (v1.5.4), since text-to-speech is designed for people who cannot
# see.

import sys, time, os
try:
    import pyttsx4
except ImportError:
    print("External module 'pyttsx4' does not exist in the environment that you are running this program in. To download pyttsx4 using pip, input the following command into a Command Prompt (Windows) or Terminal window (Mac):")
    print("""py -m pip install pyttsx4 - WINDOWS
python3 -m pip install -U pyttsx4 --user - MAC
          """)
    sys.exit()

def add_to_database(data_store): # Is called when Option 1 is picked
  while True:
    if tts_on:
        tts.say("Add data to list (case-sensitive). Type 'stop' to terminate")
        tts.runAndWait()
    else:
        pass
    dataAdd = input("\nAdd data to list (case-sensitive). Type 'stop' to terminate: ")
    
    if dataAdd.lower() == "stop":
      print("\n")
      break
      
    data_store.append(dataAdd)

def view_database(data_store): # Is called when Option 2 is picked
  print("\nDatabase:\n")
  if tts_on:
      tts.say("Database")
      tts.runAndWait()
  else:
      pass
  
  if len(data_store) == 0:
    print("Database empty\n")
    if tts_on:
        tts.say("Database empty")
        tts.runAndWait()
    else:
        pass
  else:
    for x in data_store:
        print(x)
        if tts_on:
            tts.say(x)
            tts.runAndWait()
        else:
            pass

def save_to_file(data_store, FILENAME): # Is called when Option 6 is called
    try:
        with open(FILENAME, "a") as file:
            file.write("NEW DATABASE\n\n")
    
            for item in data_store:
                file.write(item + "\n")
      
            file.write("\nDATABASE END\n")
    except FileNotFoundError:
        print(f"File '{FILENAME}' does not exist in the directory(ies) listed by the code")
        if tts_on:
            tts.say(f"File '{FILENAME}' does not exist in the directory(ies) listed by the code")
            tts.runAndWait()
        else:
            pass
        sys.exit()
    except Exception as e:
        print(f"Error accessing file, here is the output from the app:\n{e}")
        print("\nIf you keep experiencing issues with the app like this and they do not seem to go away even when you fix the issue, please contact the creator in the comments section of whatever platform you are viewing this code on, thanks.\n")
        if tts_on:
            tts.say(f"Error accessing file, here is the output from the app:{e}")
            tts.runAndWait()
            tts.say("If you keep experiencing issues with the app like this and they do not seem to go away even when you fix the issue, please contact the creator in the comments section of whatever platform you are viewing this code on, thanks.\n")
            tts.runAndWait()
        else:
            pass
        sys.exit()

def view_file(FILENAME): # Is called when Option 7 is called
    file_size = os.path.Isize(FILENAME)
    try:
        with open(FILENAME, "r") as file:
            if file_size == 0:
                print("The file is empty\n")
                if tts_on:
                    tts.say("The file is empty")
                    tts.runAndWait()
                else:
                    pass
            else:
                for line in file.readlines():
                    print(line)
                    if tts_on:
                        tts.say(line)
                        tts.runAndWait()
                    else:
                        pass
    except FileNotFoundError:
        print(f"File '{FILENAME}' does not exist in the directory(ies) listed by the code")
        if tts_on:
            tts.say(f"File '{FILENAME}' does not exist in the directory(ies) listed by the code")
            tts.runAndWait()
        else:
            pass
        sys.exit()
    except Exception as e:
        print(f"Error accessing file, here is the output from the app:\n{e}")
        print("\nIf you keep experiencing issues with the app like this and they do not seem to go away even when you fix the issue, please contact the creator in the comments section of whatever platform you are viewing this code on, thanks.\n")
        if tts_on:
            tts.say(f"Error accessing file, here is the output from the app:{e}")
            tts.runAndWait()
            tts.say("If you keep experiencing issues with the app like this and they do not seem to go away even when you fix the issue, please contact the creator in the comments section of whatever platform you are viewing this code on, thanks.")
            tts.runAndWait()
        else:
            pass
        sys.exit()

def comment_to_file(FILENAME): # Is called when Option $ is called
    try:
        with open(FILENAME, "a") as file:
            if tts_on:
                tts.say("Add a comment to the file")
                tts.runAndWait()
            else:
                pass
            comment = input("Add a comment to the file\n")
            file.write(f"NEW COMMENT\n\n{comment}\n\nCOMMENT END\n")
        print("\nComment added\n")
        if tts_on:
            tts.say("Comment added")
            tts.runAndWait()
        else:
            pass
    except FileNotFoundError:
        print(f"File '{FILENAME}' does not exist in the directory(ies) listed by the code")
        if tts_on:
            tts.say()
            tts.runAndWait()
        else:
            pass
        sys.exit()
    except Exception as e:
        print(f"Error accessing file, here is the output from the app:\n{e}")
        print("\nIf you keep experiencing issues with the app like this and they do not seem to go away even when you fix the issue, please contact the creator in the comments section of whatever platform you are viewing this code on, thanks.\n")
        if tts_on:
            tts.say(f"Error accessing file, here is the output from the app:{e}")
            tts.runAndWait()
            tts.say("If you keep experiencing issues with the app like this and they do not seem to go away even when you fix the issue, please contact the creator in the comments section of whatever platform you are viewing this code on, thanks.")
            tts.runAndWait()
        else:
            pass
        sys.exit()

def clear_file(FILENAME): # Is called when Option 8 is called
    try:
        print("Clearing file...")
        if tts_on:
            tts.say("Clearing file")
            tts.runAndWait()
        else:
            pass

        with open(FILENAME, "w"):
            pass

        print("File cleared!")
        if tts_on:
            tts.say("File cleared!")
            tts.runAndWait()
        else:
            pass
    except FileNotFoundError:
        print(f"File '{FILENAME}' does not exist in the directory(ies) listed by the code")
        if tts_on:
            tts.say(f"File '{FILENAME}' does not exist in the directory(ies) listed by the code")
            tts.runAndWait()
        else:
            pass
        sys.exit()
    except Exception as e:
        print(f"Error accessing file, here is the output from the app:{e}")
        print("\nIf you keep experiencing issues with the app like this and they do not seem to go away even when you fix the issue, please contact the creator in the comments section of whatever platform you are viewing this code on, thanks.\n")
        if tts_on:
            tts.say(f"Error accessing file, here is the output from the app:{e}")
            tts.runAndWait()
            tts.say("If you keep experiencing issues with the app like this and they do not seem to go away even when you fix the issue, please contact the creator in the comments section of whatever platform you are viewing this code on, thanks.")
            tts.runAndWait()
        else:
            pass
        sys.exit()

def delete_from_database_file(FILENAME): # Is called when Option 10 is called (This func is a bit complicated so most lines will have explanations)
    # NOTE: This function was largely made using help from ChatGPT, and I have slightly tweaked the original code that it gave me, since it had errors :p
    try:
        with open(FILENAME, "r") as file: # Try opening the file 'FILENAME'
            lines = file.readlines() # Store all the lines in 'FILENAME' in a list 'lines'

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
            if tts_on:
                tts.say("No databases found for deletion")
                tts.runAndWait()
            else:
                pass
            return

        # If there were databases to delete, show them to the user by giving them a list of numbers going up by ones (1, 2, 3, 4...)
        print("\nDatabases available for deletion:\n")
        if tts_on:
            tts.say("Databases available for deletion")
            tts.runAndWait()
        else:
            pass
        for idx, db in enumerate(databases, start=1):
            print(f"{idx}. {db}")
            if tts_on:
                tts.say(f"{idx}. {db}")
                tts.runAndWait()
            else:
                pass

         # User decides which database to delete based on the number that they input (they can also type 'exit' to cancel last-minute)
        if tts_on:
            tts.say("Enter the number of the database you want to delete, or type 'exit' to cancel")
            tts.runAndWait()
        else:
            pass
        choice = input("\nEnter the number of the database you want to delete (or 'exit' to cancel): ")

        if choice == "exit":
            print("\nDeletion cancelled.\n")
            if tts_on:
                tts.say("Deletion cancelled")
                tts.runAndWait()
            else:
                pass
            return

        try:
            choice_idx = int(choice) - 1 # The numerical choice that the user made is assigned to a new variable and subtracted by 1 since list values start
                                         # from 0 instead of 1
            while True:
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
                    with open(FILENAME, "w") as file:
                        file.writelines(lines)

                    print("\nDatabase deleted successfully.\n")
                    if tts_on:
                        tts.say("Database deleted successfully")
                        tts.runAndWait()
                    else:
                        pass
                    break

                else:
                    print("\nInvalid input. Please enter a valid number.\n")
                    if tts_on:
                        tts.say("Invalid input. Please enter a valid number")
                        tts.runAndWait()
                    else:
                        pass

        # Everything under here handles any issues that the user, computer, or code compiler may make and handles them without crashing the program
        except ValueError:
            print("\nInvalid input. Please enter a valid number.\n")
            if tts_on:
                tts.say("Invalid input. Please enter a valid number")
                tts.runAndWait()
            else:
                pass
            sys.exit()

    except FileNotFoundError:
        print(f"File '{FILENAME}' does not exist in the directory(ies) listed by the code")
        if tts_on:
            tts.say(f"File '{FILENAME}' does not exist in the directory(ies) listed by the code")
            tts.runAndWait()
        else:
            pass
        sys.exit()
    except Exception as e:
        print(f"Error accessing file, here is the output from the app:\n{e}")
        print("\nIf you keep experiencing issues with the app like this and they do not seem to go away even when you fix the issue, please contact the creator in the comments section of whatever platform you are viewing this code on, thanks.\n")
        if tts_on:
            tts.say(f"Error accessing file, here is the output from the app:\n{e}")
            tts.runAndWait()
            tts.say("If you keep experiencing issues with the app like this and they do not seem to go away even when you fix the issue, please contact the creator in the comments section of whatever platform you are viewing this code on, thanks.")
            tts.runAndWait()
        else:
            pass
        sys.exit()

def show_current_patch(): # Is called when Option 0 is called
    current_patch = """
LATEST VERSION (08/07/2023)
D.E.Deca - TTS Update (vT.T.S):

Additions
>>>>>>>>>>>>> Users can choose to have terminal text spoken to them by a text-to-speech module (TTS)
>>>>>>>>>>>>> The program is now exited every time the graceful error handling catches an error; this prevents error propagation (QoL)
>>>>>>>>>>>>> The text stored in the 'show_all_patches()' function have been moved into file 'all_patch_notes.txt' (QoL)
>>>>>>>>>>>>> The system to check for the files being present/accessible to the program has been moved to function 'check_for_files()' (QoL)

Notes
............. Thank you all for using my program, it means a lot to me, and I never thought I would get this far into a project without giving up.
              I hope this can help you find inspiration to complete other projects of your own, and I think that without the hope of someone else seeing your
              projects and using them, no one can go that far in terms of creating new things. I hope you have fun with this last scheduled version,
              which was specifically gauged at the large population of people who struggle to use computers due to blindness, and I hope your own projects can
              reach even better heights than mine.

              And without further ado... Enjoy!"""
    print(current_patch)
    if tts_on:
        tts.say(current_patch)
        tts.runAndWait()

def show_all_patches(ALLPATCHES): # Is called when Option 00 is called
    try:
        with open(ALLPATCHES, "r") as file:
            for line in file.readlines():
                print(line)
                if tts_on:
                    tts.say(line)
                    tts.runAndWait()
                else:
                    pass
    except FileNotFoundError:
        print(f"File {ALLPATCHES} doesn't exist in the directory(ies) listed by the code")
        if tts_on:
            tts.say(f"File '{ALLPATCHES}' does not exist in the directory(ies) listed by the code")
            tts.runAndWait()
        else:
            pass
        sys.exit()
    except Exception as e:
        print(f"Error accessing file, here is the output from the app:{e}")
        print("\nIf you keep experiencing issues with the app like this and they do not seem to go away even when you fix the issue, please contact the creator in the comments section of whatever platform you are viewing this code on, thanks.\n")
        if tts_on:
            tts.say(f"Error accessing file, here is the output from the app:\n{e}")
            tts.runAndWait()
            tts.say("If you keep experiencing issues with the app like this and they do not seem to go away even when you fix the issue, please contact the creator in the comments section of whatever platform you are viewing this code on, thanks.")
            tts.runAndWait()
        else:
            pass
        sys.exit()

def ask_tts(): # Asks the user if they would like text to be read aloud to them
    global tts_on
    global tts
    tts = pyttsx4.init()
    letters = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
    tts.say("Would you like all text to be spoken out loud from now on? Anything other than 'n' will count as yes for ease of accessibility")
    tts.runAndWait()
    tts_on = input("Would you like all text to be spoken out loud from now on? Anything other than 'n' will count as yes for ease of accessibility\n")
    for letter in letters:
        if tts_on.lower() == letter:
            tts_on = True
            break
        else:
            continue
    if tts_on == 'n':
        tts_on = False
        tts = None
    else:
        pass

def check_for_files(FILENAME, ALLPATCHES): # Checks if all infomation files needed to run the program are present
    try:
        with open(FILENAME, "r"):
            pass
    except FileNotFoundError:
        print(f"File 'databases.txt' does not exist in the listed PATH for 'FILENAME':\n{FILENAME}")
        if tts_on:
            tts.say(f"File 'databases.txt' does not exist in the listed PATH for 'FILENAME': {FILENAME}")
            tts.runAndWait()
        else:
            pass
        time.sleep(1)
        sys.exit()
    except Exception as e:
        print(f"There was an error accessing the file 'databases.txt' at {FILENAME}. Please refer to the error and rectify the issue:\n{e}")
        if tts_on:
            tts.say(f"There was an error accessing the file 'databases.txt' at {FILENAME}. Please refer to the error and rectify the issue: {e}")
            tts.runAndWait()
        else:
            pass
        time.sleep(1)
        sys.exit()

    try:
        with open(ALLPATCHES, "r"):
            pass
    except FileNotFoundError:
        print(f"File 'all_patch_notes.txt' does not exist in the listed PATH for 'ALLPATCHES':\n{ALLPATCHES}")
        if tts_on:
            tts.say(f"File 'all_patch_notes.txt' does not exist in the listed PATH for 'ALLPATCHES': {ALLPATCHES}")
            tts.runAndWait()
        else:
            pass
        time.sleep(1)
        sys.exit()
    except Exception as e:
        print(f"There was an error accessing the file 'all_patch_notes.txt' at {ALLPATCHES}. Please refer to the error and rectify the issue:\n{e}")
        if tts_on:
            tts.say(f"There was an error accessing the file 'all_patch_notes.txt' at {ALLPATCHES}. Please refer to the error and rectify the issue: {e}")
            tts.runAndWait()
        else:
            pass
        time.sleep(1)
        sys.exit()

def main():
    FILENAME = "databases.txt"
    ALLPATCHES = "all_patch_notes.txt"
    OPTIONSMENU = """
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
    ? - Fast Mode
    ! -  Exit the Database Editor\n
        """
    data_store = []
    dataSession = 1
    fast = False
    check_for_files(FILENAME, ALLPATCHES)
    print("Entering the Database Editor...\n")

    ask_tts()
    time.sleep(1)
  
    while True:
        print(OPTIONSMENU)
        if tts_on:
            tts.say("""
Database Editing -\n
    1. Edit the data
    2. View the contents of the current database
    3. Remove select values from the current database
    4. Clear the database of all data
    5. Clear + create a new database session
Files -
    6. Save the current database to a file
    7. View the contents of the file holding all databases
    8. Clear the database file of all databases
    9. Write a comment to the database-holding file
    10. Remove certain databases from the database-holding file
Other -
    0. Check patch notes for the current version only
    00. Check all past and current patch notes
    Question mark - Fast Mode
    Exclamation mark -  Exit the Database Editor
        """)
            tts.runAndWait()
        else:
            pass

        if tts_on:
            tts.say("Enter one of the options")
            tts.runAndWait()
        else:
            pass
        choice = input("Enter one of the options: ")

        if choice == "1": # Edit the data
            add_to_database(data_store)

        elif choice == "2": # View the current database
            print(f"\nDatabase Session {dataSession}")
            if tts_on:
                tts.say(f"Database Session {dataSession}")
                tts.runAndWait()
            else:
                pass
            view_database(data_store)

            if fast == True:
                time.sleep(1.5)
            else:
                time.sleep(3)

        elif choice == "3": # Remove certain values from the current database
            while True:
                view_database(data_store)
                print("\nSelect the value you would like to remove. Type '!' to exit (case-sensitive)\n")
                if tts_on:
                    tts.say("Select the value you would like to remove. Type 'exclamation mark' to exit")
                    tts.runAndWait()
                else:
                    pass
                dataRemove = input()

                if dataRemove == "!":
                    break
                else:
                    print("\nRemoving data...\n")
                    if tts_on:
                        tts.say("Removing data")
                        tts.runAndWait()
                    data_store.remove(dataRemove)

                    if fast == True:
                        time.sleep(0.5)
                    else:
                        time.sleep(1)
                    print("\nData removed\n")
                    if tts_on:
                        tts.say("Data removed")
                        tts.runAndWait()
                    else:
                        pass

        elif choice == "4": # Clear the database
            data_store.clear()
            print("\nDatabase wiped\n")
            if tts_on:
                tts.say("Database wiped")
                tts.runAndWait()
            else:
                pass

            if fast == True:
                time.sleep(0.25)
            else:
                time.sleep(0.5)

        elif choice == "5": # Clear + create a new database session
            data_store.clear()
            dataSession += 1
            print(f"\nNew session\nDatabase Session {dataSession}")
            if tts_on:
                tts.say(f"New session: Database session {dataSession}")
                tts.runAndWait()
            else:
                pass

            if fast == True:
                time.sleep(0.25)
            else:
                time.sleep(0.5)

        elif choice == "6": # Save the current database to a file
            save_to_file(data_store, FILENAME)
            print("\nDatabase saved. If you would like to see the saved values, use Option 7 in the Editor menu\n")
            if tts_on:
                tts.say("Database saved. If you would like to see the saved values, use Option 7 in the Editor menu")
                tts.runAndWait()
            else:
                pass

            if fast == True:
                time.sleep(0.75)
            else:
                time.sleep(1.5)

        elif choice == "7": # View the contents of the file holding all databases
            view_file(FILENAME)

            if fast == True:
                time.sleep(2.5)
            else:
                time.sleep(5)
        
        elif choice == "8":
            clear_file(FILENAME)

            if fast == True:
                time.sleep(0.25)
            else:
                time.sleep(0.5)

        elif choice == "9":
            comment_to_file(FILENAME)

            if fast == True:
                time.sleep(0.25)
            else:
                time.sleep(0.5)
        
        elif choice == "10":
            delete_from_database_file(FILENAME)

        elif choice == "0": # Show the patch notes for the current patch
            os.system('cls')
            show_current_patch()
            if fast == True:
                time.sleep(2.5)
            else:
                time.sleep(5)
              
        elif choice == "00":
            os.system('cls')
            show_all_patches(ALLPATCHES)
            if fast == True:
                time.sleep(5)
            else:
                time.sleep(10)

        elif choice == "?":
            print("\nFast Mode allows you to have shortened wait times between the execution of commands in the Editor. Would you like to turn this feature on?\n")
            print("WARNING: This feature cannot be turned off once it is turned on. You must quit and restart the program to go back to the normal wait times.")
            if tts_on:
                tts.say("Fast Mode allows you to have shortened wait times between the execution of commands in the Editor. Would you like to turn this feature on?")
                tts.runAndWait()
                tts.say("Warning: This feature cannot be turned off once it is turned on. You must quit and restart the program to go back to the normal wait times.")
            else:
                pass

            while True:
                if tts_on:
                    tts.say("Turn fast mode on? Type 'y' or 'n' for 'yes' or 'no'")
                    tts.runAndWait()
                else:
                    pass
                speed_choice = input("\nTurn Fast Mode on? y/n: ")

                if speed_choice == "y":
                    fast = True
                    print("\nFast Mode is now ON\n")
                    if tts_on:
                        tts.say("Fast mode is now on")
                        tts.runAndWait()
                    else:
                        pass
                        time.sleep(1)
                    break
                elif speed_choice == "n":
                    print("\nFast Mode will remain OFF\n")
                    if tts_on:
                        tts.say("Fast mode wil remain off")
                        tts.runAndWait()
                    else:
                        pass
                    time.sleep(1)
                    break
                else:
                    print("\nInvalid response, try again\n")
                    if tts_on:
                        tts.say("Invalid response, try again. Type 'y' for yes and 'n' for no")
                        tts.runAndWait()
                    else:
                        pass
                    time.sleep(0.5)

        elif choice == "!": # Exit the Database Editor
            os.system('cls')
            print("\nThank you so much for using my app!\n\nExiting Database Editor...\n")
            if tts_on:
                tts.say("Thank you so much for using my app! The program will now exit the Editor")
                tts.runAndWait()
            else:
                pass
            time.sleep(2.5)
            os.system('cls')
            break

        else:
            print("\nInvalid input, try again. Remember that the inputs are case-sensitive.\n")
            if tts_on:
                tts.say("Invalid input, try again. Remember that the inputs are case-sensitive")
                tts.runAndWait()
            else:
                pass

            if fast == True:
                time.sleep(0.25)
            else:
                time.sleep(0.5)

main()
