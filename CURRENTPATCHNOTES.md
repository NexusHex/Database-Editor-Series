All versions listed here are available in this repo

D.E.Quad (v1.0):

Code wasn't posted online at release, so no date is available

> Edit list 'data_store'

> Check the contents of list 'data_store'

> Clear list 'data_store' of all values

> Exit the app gracefully rather than an abprupt stop
  
D.E.Penta (v1.1):

Released on 07/18/2023
> Added ability to remove specific items from the database
  
D.E.Hexa (v1.2):

Released on 07/26/2023
> All changes made are saved to a file 'databases.txt'. Multiple sessions' worth of files can be stored there

D.E.Hepta (v1.3.1):

Released on 08/01/2023
> Added the ability to wipe and create a new database session (now you don't have to repeatedly clear and save databases to 'databases.txt' in the same session)

> Renamed variable 'data' to 'data_store' to avoid readability issues (QoL)

> User can now view all patch notes within command 'patches' or '_p' when the Editor prompts you to pick an option (QoL)

> Command to exit the Editor has been changed to 'exit' or 'e' (QoL)

> Fixed an issue where there was no newline after 'view_database()' printed its contents (Bug Fix)

D.E.Octa (v1.4.2):

Realeased on 08/02/2023
> Added the ability to view contents of 'databases.txt'

> Text at the start of the program + app options text has had a visual overhaul (QoL)

> Gave all past version patch notes titles for the type of change that occured (QoL)

> Command to exit Editor has been changed to '!' in correspondance with a bug found during testing (QoL)

> Fixed indents in 'patches' var pushing text over onto the next line (Bug Fix)

> Fixed many indent irregularities throughout the code for ease of code reading (Bug Fix)

> Fixed bug causing any string input to the Editor including the designated 'exit' and 'e' inputs to leave the Editor (Bug Fix)

> Added missing newline at the beginng of the input error syntax under 'else:' (Bug Fix)

D.E.Octa - QoL Update (v1.4.3):

Released on 08/03/2023
> Print the database session number that you are on (updates every time a new database session is created using function 6) (QoL)

> Added ability to see all patch notes or just the ones for the current version (QoL)

> Renamed function 'show_patches()' to 'show_all_patches()' (QoL)

> Allow user to add comments like titles, notes etc to the file 'databases.txt' (QoL)

> Keep a short wait between executing a command - checking the contents of a database - and re-printing the options bar (waiting times will vary between different events) (QoL)

> Removed unneccessary newlines from the Edtior options menu (QoL)

D.E.Nona (v1.5.3):

Released on 08/04/2023
> Users can now clear the 'databases.txt' file

> The option to delete certain items from the database is now a loop to allow multiple specific items to be removed in one go

> Added graceful error handling for all file-related functions (QoL)

> Added graceful error handling at the start of the 'main()' function to check if the file exists (QoL)


D.E.Nona - Visuals Update (v1.5.4):

Released on 08/05/2023
> Added a loading bar at the start of the program to simulate the app loading up (Visual)

> Add a floating + spinning cube to the screen once the user leaves the editor. It can be cancelled by pressing Ctrl + C (Visual)

> Changed the indent levels of titles within the option select text (QoL)

> App now clears the shell of all text for Operations 90 (show all patches), 91 (show current patch) and ! (exit the editor) (QoL)

D.E.Deca (v1.6.4):

Released on 08/06/2023
> Remove certain databases from the 'databases.txt' file

> User can shorten the wait time between events by using an in-built command (QoL)

> Flavor text printed after saving a database to the file has been rewritten (QoL)

> Users have the option to turn off the animations in the Editor menu (QoL)

> Options for checking current/all patch notes have been renamed to '0' and '00 (QoL)

> Function 'view_file()' now returns 'The file is empty' if there are no databases or comments within the file (QoL)

D.E.Deca - TTS Update (vT.T.S):

Released on 08/07/2023
> Users can choose to have terminal text spoken to them by a text-to-speech module (TTS)

> Users can now inspect the documentation of the Database Editor

> The program is now exited every time the graceful error handling catches an error; this prevents error propagation (QoL)

> The text stored in the 'show_all_patches()' function have been moved into file 'all_patch_notes.txt' (QoL)

> The system to check for the files being present/accessible to the program has been moved to function 'check_for_files()' (QoL)


ALL UPDATES OF THE EDITOR (TERMINAL-BASED) WILL BE PUT ONTO DATABASE EDTIOR DECAFUNCTION FROM HERE

D.E.Deca (v1.6.5):

Released on 08/08/2023
> Variable 'fileName' has been renamed to FILENAME since it is a constant (QoL)

> The text stored in the 'show_all_patches()' function have been moved into file 'all_patch_notes.txt' (QoL)

> The program is now exited every time the graceful error handling catches an error; this prevents error propagation (QoL)

> The system to check for the files being present/accessible to the program has been moved to function 'check_for_files()' (QoL)

D.E.Deca (v1.6.5):

Released on 08/08/2023
> Variable 'fileName' has been renamed to FILENAME since it is a constant (QoL)

> The text stored in the 'show_all_patches()' function have been moved into file 'all_patch_notes.txt' (QoL)

> The program is now exited every time the graceful error handling catches an error; this prevents error propagation (QoL)

> The system to check for the files being present/accessible to the program has been moved to function 'check_for_files()' (QoL)

D.E.Deca (v1.6.6):

Released on 08/09/2023
> Constants have now been moved to the top of the program (QoL)

> Error handling has been added to Option 3 (Remove certain values from the database) (QoL)

D.E.Deca - TTS Update (vT.T.S):

Released on 08/07/2023
> Users can choose to have terminal text spoken to them by a text-to-speech module (TTS)

> The program is now exited every time the graceful error handling catches an error; this prevents error propagation (QoL)

> The text stored in the 'show_all_patches()' function have been moved into file 'all_patch_notes.txt' (QoL)

> The system to check for the files being present/accessible to the program has been moved to function 'check_for_files()' (QoL)
