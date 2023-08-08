This patch had 6 quality-of-life changes:
> Print the database session number that you are on (updates every time a new database session is created using function 6) (QoL)
> 
> Added ability to see all patch notes or just the ones for the current version (QoL)
> 
> Renamed function 'show_patches()' to 'show_all_patches()' (QoL)
> 
> Allow user to add comments like titles, notes etc to the file 'databases.txt' (QoL)
> 
> Keep a short wait between executing a command - checking the contents of a database - and re-printing the options bar (waiting times will vary between different events) (QoL)
> 
> Removed unneccessary newlines from the Edtior options menu (QoL)

This patch was the result of me finding a lot of problems in the execution of the code in a short amount of time, meaning that I had to make a whole new patch just to fix them rather than fixing them in small bunches.
