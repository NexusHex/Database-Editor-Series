# VERSION 1.2.1 <D.E.HEXA>
# Requires file 'databases.txt'

def add_to_database(data):
  while True:
    dataAdd = input("\nAdd data to list. Type \'stop\' to terminate: ")
    if dataAdd.lower() == "stop":
      break
    data.append(dataAdd)

def view_database(data):
  print("\nDatabase:\n")
  for x in data:
    print(x)

def save_to_file(data, fileName):
  with open(fileName, "a") as file:
    file.write("NEW DATABASE\n\n")
    for item in data:
        file.write(item + "\n")
    file.write("\nDATABASE END\n")

def main():
  data = []
  fileName = "C:/Users/Khizar/Desktop/Coding/Python Projects/Database Editor Series/databases.txt"
  print("Entering the Database Editor...\n")
  while True:
    print("Database Control Options:\n1. Edit the data\n2. View the contents of the database\n3. Remove select values from the database\n4. Clear the database of all data\n5. Save this session's database to a file\n6. Exit the Database Editor")
    choice = input("Enter one of the five numbers: ")
    if choice == "1":
      add_to_database(data)
    elif choice == "2":
      view_database(data)
      if len(data) == 0:
        print("Database empty\n")
    elif choice == "3":
      view_database(data)
      print("\nSelect the value you would like to remove (case-sensitive)\n")
      dataRemove = input()
      data.remove(dataRemove)
      print("\nData removed\n")
    elif choice == "4":
      data.clear()
      print("\nDatabase wiped\n")
    elif choice == "5":
      save_to_file(data, fileName)
      print("\nDatabase saved. If you would like to see the saved values, check the file named 'databases.txt'.\n")
    elif choice == "6":
      print("\nExiting Database Editor\n")
      break
    else:
      print("Invalid input, try again\n")

main()
