D.E.Quad (v1.0):

Code wasn't posted online at release, so no date is available

> Edit list 'data_store'

> Check the contents of list 'data_store'

> Clear list 'data_store' of all values

> Exit the app gracefully rather than an abprupt stop
  
D.E.Penta (v1.1):

Released on 07/18/23
> Added ability to remove specific items from the database
  
D.E.Hexa (v1.2):

Released on 07/26/23
> All changes made are saved to a file 'databases.txt'. Multiple sessions' worth of files can be stored there



  
  
LATEST VERSION (08/01/23)

D.E.Hepta (v1.3.1):
  
Additions
> Added the ability to wipe and create a new database session (now you don't have to repeatedly clear and save databases to 'databases.txt' in the same session)

> Renamed variable 'data' to 'data_store' to avoid readability issues (QoL)

> User can now view all patch notes within command 7 when the Editor prompts you to pick an option (QoL)

> Command to exit the Editor has been changed to 'exit' or 'e' (QoL)
  
Bug Fixes
> Fixed an issue where there was no newline after 'view_database()' printed its contents
  
Notes

Yes, even though I said that the ability to view the contents of the 'databases.txt' file would be added in D.E.Hepta, I decided to create other features that would help users to work with the file in a more logical/intuitive way. Hopefully this helps once the actual feature is out, and I apologize for the delay.
This does mean that all other future plans have been pulled back another version, but I will prioritize working on the viewing function before all else.

Plans for future versions...

D.E.Octa (v1.4.1):

> MainPatch - Ability to view contents of 'databases.txt'

  
QoL Patch (v1.4.2):

> QualityOfLifePatch - Print the database session number that you are on (updates every time a new database session is created using function 6)

> QualityOfLifePatch - Ability to see all patch notes or just the ones for the current version


D.E.Nona (v1.5.2):

> MainPatch - Clear the 'databases.txt' file

  
D.E.Deca (v1.6.2):

> MainPatch - Remove certain databases from the 'databases.txt' file


Into the beyond...

> Find a way to interface these databases with Excel .csv files

> Much, much more!
