ALL PATCHNOTES ARE UPDATED RELATIVE TO WHEN I HAVE POSTED THE VERSION TO AN ONLINE PLATFORM, SOME FUTURE GENERATIONS OF THE SERIES MAY BE MISSING, AND SOME MAY BE ADDED AHEAD OF THE RELEASE DATE

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

Realeased on 08/15/2023
> Added the ability to view contents of 'databases.txt'

> Text at the start of the program + app options text has had a visual overhaul (QoL)

> Gave all past version patch notes titles for the type of change that occured (<new> , -bug- , <QoL>) (QoL)

> Command to exit Editor has been changed to '!' in correspondance with a bug found during testing (QoL)

> Fixed indents in 'patches' var pushing text over onto the next line (Bug Fix)

> Fixed many indent irregularities throughout the code for ease of code reading (Bug Fix)

> Fixed bug causing any string input to the Editor including the designated 'exit' and 'e' inputs to leave the Editor (Bug Fix)

> Added missing newline at the beginng of the input error syntax under 'else:' (Bug Fix)

D.E.Octa - QoL Update (v1.4.3):

Released on 08/31/2023
> Print the database session number that you are on (updates every time a new database session is created using function 6) (QoL)

> Added ability to see all patch notes or just the ones for the current version (QoL)

> Renamed function 'show_patches()' to 'show_all_patches()' (QoL)

> Allow user to add comments like titles, notes etc to the file 'databases.txt' (QoL)

> Keep a short wait between executing a command - checking the contents of a database - and re-printing the options bar (waiting times will vary between different events) (QoL)

> Removed unneccessary newlines from the Edtior options menu (QoL)


END OF CURRENT PATCH NOTES