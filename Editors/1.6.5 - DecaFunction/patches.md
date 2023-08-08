This patch included 4 quality-of-life patches:
> Variable 'fileName' has been renamed to FILENAME since it is a constant (QoL)
> 
> The text stored in the 'show_all_patches()' function have been moved into file 'all_patch_notes.txt' (QoL)
> 
> The program is now exited every time the graceful error handling catches an error; this prevents error propagation (QoL)
> 
> The system to check for the files being present/accessible to the program has been moved to function 'check_for_files()' (QoL)
