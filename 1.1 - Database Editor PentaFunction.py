# VERSION 1.1 <D.E.PENTA>

def add_to_database(data):
  while True:
    dataAdd = input("Add data to list. Type \'stop\' to terminate: ")
    print("\n")
    if dataAdd.lower() == "stop":
      break
    data.append(dataAdd)

def view_database(data):
  print("\nDatabase:\n")
  for x in data:
    print(x)

def main():
  data = []
  print("Entering the Database Editor...\n")
  while True:
    print("Database Control Options:\n1. Edit the data\n2. View the contents of the database\n3. Remove select values from the database\n4. Clear the database of all data\n5. Exit the Database Editor")
    choice = input("Enter one of the five numbers: ")
    if choice == "1":
      add_to_database(data)
    elif choice == "2":
      view_database(data)
      if len(data) == 0:
        print("Database empty")
      print("\n")
    elif choice == "3":
      view_database(data)
      print("\nSelect the value you would like to remove (case-sensitive)\n")
      dataRemove = input()
      data.remove(dataRemove)
      print("\nData removed\n")
    elif choice == "4":
      data.clear()
      print("\n")
      print("Database wiped\n")
    elif choice == "5":
      print("\nExiting Database Editor\n")
      break
    else:
      print("Invalid input, try again\n")

main()
