class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def choose():
    print(f"\nSelect which list you want to create: \n 1 - Singly\n 2 - Singly Circular\n 3 - Doubly\n 4 - Doubly Circular\n 5 - Exit")
    choice = int(input(f"Enter your choice (1-5): "))
    return choice

def choose_operation():
    print(f"\nSelect what operation to do: \n 1 - Traversal (Print all your data)\n 2 - Retrieval\n 3 - Insertion\n 4 - Deletion\n 5 - Back to main menu")
    choice = int(input(f"Enter your choice (1-5): "))
    return choice

def for_retrieval():
    print(f"Do you want to:\n 1 - Check if a specific value exists on the list\n 2 - Retrieve from a specified position?")
    choice = int(input(f"Enter your choice (1-2): "))
    return choice

status = True
while status:
    user_choice = choose()
    if user_choice == 1:
        print(f"\n                  SINGLY LINKED LIST                  \n")
        print(f"_______________Let's create your list first!______________")
        Head_data = str(input("Enter head's data: "))
        Head = Node(Head_data)
        current = Head

        next_data = str(input("Enter next data: "))
        new_node = Node(next_data)
        current.next = new_node
        current = new_node

        question = str(input(f"\nDo you want to link another data? (y/n): "))
        while question.lower() == "y":
            next_data = str(input("Enter next data: "))
            new_node = Node(next_data)
            current.next = new_node
            current = new_node
            question = str(input("\nDo you want to link another data? (y/n): "))

        while True:
            user_operation = choose_operation()
            if user_operation == 1:
                print(f"\n                  SINGLY LINKED LIST: Traversal                  \n")
                Curr = Head
                print(f"Your Linked List Data:\n")
                while Curr is not None:
                    print(Curr.data, " ")
                    Curr = Curr.next

            elif user_operation == 2:
                print(f"\n                  SINGLY LINKED LIST: Retrieval                  \n")
                retri_choice = for_retrieval()
                if retri_choice == 1:
                    user_value = str(input("\nEnter value to check: "))
                    found = False
                    Curr = Head
                    while Curr is not None:
                        if Curr.data == user_value:
                            print(f"{user_value} exists in the linked list!")
                            found = True
                            break
                        Curr = Curr.next
                    if not found:
                        print(f"{user_value} doesn't exist in the linked list. :(")

                elif retri_choice == 2:
                    retri_pos = int(input("\nEnter position to retrieve: "))
                    Curr_pos = 0
                    Curr = Head
                    while Curr is not None:
                        Curr_pos += 1
                        if Curr_pos == retri_pos:
                            print(f"{retri_pos} has a data of {Curr.data}")
                            break
                        Curr = Curr.next
                    else:
                        print(f"{retri_pos} is out of range.")
                
            elif user_operation == 5:
                break

    elif user_choice == 5:
        break

print(f"    Thank you and have a nice day! ^^   ")