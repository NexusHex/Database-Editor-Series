This patch included one text-to-speech addition and 3 quality-of-life patches:
> Users can choose to have terminal text spoken to them by a text-to-speech module (text-to-speech)
> 
> The program is now exited every time the graceful error handling catches an error; this prevents error propagation (QoL)
> 
> The text stored in the 'show_all_patches()' function have been moved into file 'all_patch_notes.txt' (QoL)
> 
> The system to check for the files being present/accessible to the program has been moved to function 'check_for_files()' (QoL)

This version of the Editor was created specifically for blind people, since they struggle to interact with machines that mainly show things using text on a screen. It was also an opportunity for me to try out dealing with text-to-speech coding, albeit a very shallow introduction to the topic.
