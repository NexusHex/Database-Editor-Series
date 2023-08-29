import Editor
import os
import time
import sys

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

file_name = 'databases.txt'
patches_name = 'all_patch_notes.txt'

editor = Editor.Editor(file_name, patches_name)

loadingBar.bar()

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
    8. Clear the database file of all databases (excludes comments)
    9. Write a comment to the database-holding file
    10. Remove certain databases from the database-holding file\n
Other -\n
    0. Check patch notes for the current version only
    00. Check all past and current patch notes
    ? - Fast Mode
    ~ - Low Performance Mode
    ! -  Exit the Database Editor\n
        """)

    action = input("Select an action from the menu: ")

    if action == '1':
        while True:
            add_value = input("Type the value you would like to add to the database. Type 'q' to exit\n")
            if add_value.lower() == 'q':
                break
            else:
                editor.add_to_database(add_value)
    elif action == '2':
        editor.view_database()
    elif action == '3':
        editor.delete_certain_values()
    elif action == '4':
        editor.clear_database()
    elif action == '5':
        editor.new_session()
    elif action == '6':
        editor.save_to_file()
    elif action == '7':
        editor.view_file()
    elif action == '8':
        editor.clear_database()
    elif action == '9':
        editor.comment_to_file()
    elif action == '10':
        editor.delete_from_file()
    elif action == '0':
        editor.see_current_patch_notes()
    elif action == '00':
        editor.see_all_patch_notes()
    elif action == '?':
        editor.fast_mode_toggle()
    elif action == '~':
        editor.low_performance_toggle()
    elif action == '!':
        os.system('cls')
        print("\nThank you so much for using my app!\n\nExiting Database Editor...\n")
        time.sleep(2.5)
        if editor.animations:
            rotatingCube.cube()
        else:
            pass
        sys.exit()
    else:
        print("Invalid input. Try again\n")
