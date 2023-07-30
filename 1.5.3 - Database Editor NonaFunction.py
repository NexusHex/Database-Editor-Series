# D.E.Nona (v1.5.3):

# MainPatch > Clear the 'databases.txt' file
# MainPatch > When Option 'Remove certain items from database' is called, loop till command 'exit' is typed
# QoLPatch > Add graceful error handling to file-related functions, as shown below

'''def comment_to_file(fileName):
    with open(fileName, "a") as file:
        comment = input("Add a comment to the file\n")
        try:
            file.write(f"NEW COMMENT\n\n{comment}\n\nCOMMENT END\n")
        except IOError:
            print("There was an error adding the comment to the file. Please try again or make sure that the file is open in the environment that you are running the code in")
            print("Returning you back to safety...")
            t.sleep(2)
        except FileNotFoundError:
            print("The app cannot find the file. Make sure that the file is open and present in the same directory as the app")
            print("Returning you back to safety...")
            t.sleep(2)
        else:
            print("\nComment added\n")'''