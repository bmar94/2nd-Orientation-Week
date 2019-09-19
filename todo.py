import fileinput
file_path = "todo.txt"

command = input("Choose what u wanna do? [list, add, mark, archive]: ")


if command == "list":

    lines = [line.rstrip('\n') for line in open(file_path)]
    print("You saved the following to-do items:")
    for element in lines:
        print(3 *" ",lines.index(element)+1, element)

elif command == "add":

    text = input("Add an item: ")

    with open(file_path, "a" ) as file:
        file.write("[ ]" +" " + text + "\n")

    print("Item added.")

elif command == "mark":

    lines = [line.rstrip('\n') for line in open(file_path)]
    print("You saved the following to-do items:")
    for element in lines:
        print(3 *" ",lines.index(element)+1, element)
    
    text = input("Which one you want to mark as completed? ")
    a = int(text) - 1
    mark = open(file_path, 'r').readlines()
    with open (file_path, 'w') as file:
        for index,line in enumerate(mark):
            if index == a:
                file.write("[X] " +line[4:])
                print(line[4:-1] + " is completed.")
            else:
                file.write(line)
        

elif command == "archive":
    
    print("All completed task got deleted.")
    arc = open(file_path, "r").readlines()
    with open (file_path, "w") as file:
        for index, line in enumerate(arc):
            if line.startswith("[X]"):
                pass
            else:
                file.write(line)