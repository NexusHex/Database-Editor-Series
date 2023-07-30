# VERSION 1.4.2 <D.E.OCTA>
# Requires file 'databases.txt'

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
    with open(fileName, "a") as file:
        file.write("NEW DATABASE\n\n")
    
        for item in data_store:
            file.write(item + "\n")
      
        file.write("\nDATABASE END\n")

def view_file(fileName): # Gets called when Option 7 is called (NEW)
    with open(fileName, "r") as file:
        for line in file.readlines():
            print(line)

def show_patches(): # Minimize this, it doesn't need to be looked at in the source code
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
<QoL> Renamed variable 'data' to 'data_store' to avoid readability issues (QoL)
<QoL> User can now view all patch notes within command 'patches' or '_p' when the Editor prompts you to pick an option (QoL)
<QoL> Command to exit the Editor has been changed to 'exit' or 'e' (QoL)
-bug- Fixed an issue where there was no newline after 'view_database()' printed its contents


LATEST VERSION (08/15/2023)
D.E.Octa (v1.4.2):

Additions
>>>>>>>>>>>>> Added the ability to view contents of 'databases.txt'
>>>>>>>>>>>>> Text at the start of the program + app options text has had a visual overhaul (QoL)
>>>>>>>>>>>>> Gave all past version patch notes titles for the type of change that occured (<new> , -bug- , <QoL>) (QoL)
>>>>>>>>>>>>> Command to exit Editor has been changed to '!' in correspondance with a bug found during testing (QoL)

Bug Fixes
------------- Fixed indents in 'patches' var pushing text over onto the next line
------------- Fixed many indent irregularities throughout the code for ease of code reading
------------- Fixed bug causing any string input to the Editor including the designated 'exit' and 'e' inputs to leave the Editor
------------- Added missing newline at the beginng of the input error syntax under 'else:'

Notes
............. Decided that the amount of fixes unrelated to the main addition(s) warranted a new 0.0.___ version


Plans for future versions...

QoL Patch (v1.4.3):
QoLPatch > Print the database session number that you are on (updates every time a new database session is created using function 6)
QoLPatch > Ability to see all patch notes or just the ones for the current version
QoLPatch > Allow user to add comments like titles, notes etc to the file 'databases.txt'
QoLPatch > Keep a short wait between executing a command - checking the contents of a database - and re-printing the options bar (waiting times will vary between different events)

D.E.Nona (v1.5.3):
MainPatch > Clear the 'databases.txt' file
Other patches may be added below this line if I think of something

Visuals Patch (v1.5.4):
VisualsPatch > Add a loading bar for when certain actions happen
VisualsPatch > Add a floating + spinning cube to the screen once the user leaves the editor. It will loop through an animation for 5 seconds before the app auto closes
    
D.E.Deca (v1.6.4):
MainPatch > Remove certain databases from the 'databases.txt' file
Other patches may be added below this line if I think of something
    """
    print(patches)

def main():
    data_store = []
    fileName = "C:/Users/Khizar/Desktop/Coding/Python Projects/Database Editor Series/databases.txt"
    print("Entering the Database Editor...\n")
  
    while True:
        print("""
        Database Editing/Manipulating -\n\n
        1. Edit the data\n
        2. View the contents of the current database\n
        3. Remove select values from the current database\n
        4. Clear the database of all data\n
        5. Clear + create a new database session\n\n
        Files -\n\n
        6. Save the current database to a file\n
        7. View the contents of the file holding all databases (! NEW !)\n\n
        Other -\n\n
        8. Check all past and current patch notes\n
        ! -  Exit the Database Editor\n
        """)
        choice = input("Enter one of the five numbers: ")
        if choice == "1": # Edit the data
            add_to_database(data_store)

        elif choice == "2": # View the current database
            view_database(data_store)

        elif choice == "3": # Remove certain values from the current database
            view_database(data_store)
            print("\nSelect the value you would like to remove (case-sensitive)\n")
            dataRemove = input()
            data_store.remove(dataRemove)
            print("\nData removed\n")

        elif choice == "4": # Clear the database
            data_store.clear()
            print("\nDatabase wiped\n")

        elif choice == "5": # Clear + create a new database session
            data_store.clear()
            print("\nNew session\n")

        elif choice == "6": # Save the current database to a file
            save_to_file(data_store, fileName)
            print("\nDatabase saved. If you would like to see the saved values, check the file named 'databases.txt'.\n")

        elif choice == "7": # View the contents of the file holding all databases (NEW)
            view_file(fileName)

        elif choice == "8": # Check all past and current patch notes
            show_patches()

        elif choice == "!": # Exit the Database Editor
            print("\nExiting Database Editor\n")
            break

        else:
            print("\nInvalid input, try again. Remember that the inputs are case-sensitive.\n")

main()