# VERSION 1.3.1 <D.E.HEPTA>
# Requires file 'databases.txt'
# Patch notes are included in the source code from this version onwards in function 'show_patches()'

def add_to_database(data_store): 
  while True:
    dataAdd = input("\nAdd data to list (case-sensitive). Type \'stop\' to terminate: ")
    
    if dataAdd.lower() == "stop":
      print("\n")
      break
      
    data_store.append(dataAdd)

def view_database(data_store):
  print("\nDatabase:\n")
  
  if len(data_store) == 0:
    print("Database empty\n")
  else:
    for x in data_store:
      print(x)

def save_to_file(data_store, fileName):
  with open(fileName, "a") as file:
    file.write("NEW DATABASE\n\n")
    
    for item in data_store:
        file.write(item + "\n")
      
    file.write("\nDATABASE END\n")

def show_patches():
  patches = """
  D.E.Quad (v1.0):
  This version was the first version of the Database Editor series, and has not been posted to Replit. Features included:
  > Edit list 'data_store'
  > Check the contents of list 'data_store'
  > Clear list 'data_store' of all values
  > Exit the app gracefully rather than an abprupt stop
  
  If you would like the code for Database Editor QuadFunction, please ask in the comments
  
  D.E.Penta (v1.1):
  Released on 07/18/23
  > Added ability to remove specific items from the database
  
  D.E.Hexa (v1.2):
  Released on 07/26/23
  > All changes made are saved to a file 'databases.txt'. Multiple sessions' worth of files can be stored there



  
  
  LATEST VERSION (08/01/23)
  D.E.Hepta (v1.3.1):
  
  Additions
  >>>>>>>>>>>>> Added the ability to wipe and create a new database session (now you don't have to repeatedly clear and save databases to 'databases.txt' in the same session)
  >>>>>>>>>>>>> Renamed variable 'data' to 'data_store' to avoid readability issues (QoL)
  >>>>>>>>>>>>> User can now view all patch notes within command 'patches' or '_p' when the Editor prompts you to pick an option (QoL)
  >>>>>>>>>>>>> Command to exit the Editor has been changed to 'exit' or 'e' (QoL)

  Bug Fixes
  ------------- Fixed an issue where there was no newline after 'view_database()' printed its contents
  
  Notes
  ............. Yes, even though I said that the ability to view the contents of the 'databases.txt' file would be added in D.E.Hepta, I decided to create other features that would help users to work with the file in a more logical/intuitive way. Hopefully this helps once the actual feature is out, and I apologize for the delay.
  This does mean that all other future plans have been pulled back another version, but I will prioritize working on the viewing function before all else.



  

  Plans for future versions...
  D.E.Octa (v1.4.1):
  MainPatch > Ability to view contents of 'databases.txt'
  
  QoL Patch (v1.4.2):
  QoLPatch > Print the database session number that you are on (updates every time a new database session is created using function 6)
  QoLPatch > Ability to see all patch notes or just the ones for the current version

  D.E.Nona (v1.5.2):
  MainPatch > Clear the 'databases.txt' file
  
  D.E.Deca (v1.6.2):
  MainPatch > Remove certain databases from the 'databases.txt' file

  Into the beyond...
  > Find a way to interface these databases with Excel .csv files
  > Much, much more!
  """
  print(patches)

def main():
  data_store = []
  fileName = "databases.txt"
  print("Entering the Database Editor...\n")
  
  while True:
    print("""
    Database Control Options:\n
    1. Edit the data\n
    2. View the contents of the database\n
    3. Remove select values from the database\n
    4. Clear the database of all data\n
    5. Save this session's database to a file\n
    6. Clear + create a new database session (! NEW !)\n
    7. Check all past and current patch notes (! NEW !)\n\n
    exit OR e -  Exit the Database Editor\n
    """)
    choice = input("Enter one of the five numbers: ")
    if choice == "1":
      add_to_database(data_store)
    elif choice == "2":
      view_database(data_store)
    elif choice == "3":
      view_database(data_store)
      print("\nSelect the value you would like to remove (case-sensitive)\n")
      dataRemove = input()
      data_store.remove(dataRemove)
      print("\nData removed\n")
    elif choice == "4":
      data_store.clear()
      print("\nDatabase wiped\n")
    elif choice == "5":
      save_to_file(data_store, fileName)
      print("\nDatabase saved. If you would like to see the saved values, check the file named 'databases.txt'.\n")
    elif choice == "6":
      data_store.clear()
      print("\nNew session\n")
    elif choice == "7":
      show_patches()
    elif choice == "exit" or "e":
      print("\nExiting Database Editor\n")
      break
    else:
      print("Invalid input, try again. Remember that the inputs are case-sensitive.\n")

main()
