class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def choose():
    while True:
        try:
            print(f"\nSelect which list you want to create: \n 1 - Singly\n 2 - Singly Circular\n 3 - Doubly\n 4 - Doubly Circular\n 5 - Exit")
            choice = int(input(f"Enter your choice (1-5): "))
            if choice in range(1,6):
                return choice
            else:
                raise ValueError
        except ValueError:
            print("Invalid input. Please try again.")        

def choose_operation():
    while True:
        try:
            print(f"\nSelect what operation to do: \n 1 - Traversal (Print all your data)\n 2 - Retrieval\n 3 - Insertion\n 4 - Deletion\n 5 - Back to main menu")
            choice = int(input(f"Enter your choice (1-5): "))
            if choice in range(1, 6):
                return choice
            else:
                raise ValueError
        except ValueError:
            print("Invalid input. PLease try again.")

def traversal(head):
    if head is None:
        print("Your list is empty.")
        return
    curr = head
    print("Linked List:", end=" ")
    while curr:
        print(curr.data, end=" -> " if curr.next else "")
        curr = curr.next
    print("\n")

def for_retrieval():
    while True:
        try:
            print(f"Do you want to:\n 1 - Check if a specific value exists on the list\n 2 - Retrieve from a specified position?")
            choice = int(input(f"Enter your choice (1-2): "))
            if choice in range(1, 3):
                return choice
            else:
                raise ValueError
        except ValueError:
            print("Invalid input. PLease try again.")

def insertion():
    while True:
        try:
            print(f"Select where to insert a node:\n 1 - Beginning\n 2 - Middle (Before a node)\n 3 - Middle (After a node)\n 4 - End")
            choice = int(input(f"Enter your choice (1-4): "))
            if choice in range(1, 3):
                return choice
            else:
                raise ValueError
        except ValueError:
            print("Invalid input. PLease try again.")

#Main Code
status = True
while status:
    user_choice = choose()
    if user_choice == 1:
        print(f"\n                  SINGLY LINKED LIST                  \n")
        print(f"_______________Let's create your list first!______________")

        list_size = int(input("Enter list length: "))

        #creates the head
        Head_data = str(input("\nEnter head's data: "))
        Head = Node(Head_data)
        current = Head

        nodeCount = 1
        while nodeCount < list_size:
            next_data = str(input("Enter next data: "))
            new_node = Node(next_data)
            current.next = new_node
            current = new_node
            nodeCount += 1

        #print the created list
        print("\n-----Current List:-----\n")
        traversal(Head)
        print("\n-----------------------")

        while True:
            user_operation = choose_operation()
            #traversal operation (singly)
            if user_operation == 1:
                print(f"\n                  SINGLY LINKED LIST: Traversal                  \n")
                traversal(Head)

            #retrieval operation (singly)
            elif user_operation == 2:
                print(f"\n                  SINGLY LINKED LIST: Retrieval                  \n")
                retri_choice = for_retrieval()

                #checks if a particular value exists
                if retri_choice == 1:
                    user_value = str(input("\nEnter value to check: "))
                    found = False
                    curr = Head
                    while curr is not None:
                        if curr.data == user_value:
                            print(f"{user_value} exists in the linked list!")
                            found = True
                            break
                        curr = curr.next
                    if not found:
                        print(f"{user_value} doesn't exist in the linked list. :(")

                #retrieve the position of particular value
                elif retri_choice == 2:
                    while True:
                        try:
                            retri_pos = int(input("\nEnter position to retrieve: "))
                            if retri_pos <= 0:
                                raise ValueError
                                continue
                            break
                        except ValueError:
                            print("Invalid input. Please try again.")

                        curr_pos = 0
                        curr = Head
                        while curr is not None:
                            curr_pos += 1
                            if curr_pos == retri_pos:
                                print(f"Position {retri_pos} has a data of {curr.data}")
                                break
                            curr = curr.next
                        else:
                            print(f"{retri_pos} is out of range.")
            
            #insertion operation (singly)
            elif user_operation == 3:
                print(f"\n                  SINGLY LINKED LIST: Insertion                  \n")
                insert_choice = insertion()

                #inserting at beginning (singly)
                if insert_choice == 1:
                    print(f"\n                  SINGLY LINKED LIST: Insertion-Beginning      \n")
                    newnode_value = str(input("Enter data of new node: "))
                    newnode = Node(newnode_value)
                    newnode.next = Head
                    Head = newnode
                
                #inserting at the middle-before a node (singly)
                elif insert_choice == 2:
                    print(f"\n                  SINGLY LINKED LIST: Insertion-Middle (Before)     \n")
                    target_value = input("Enter data of the node BEFORE which to insert: ")
                    newnode_value = str(input("Enter data of new node: "))
                    newnode = Node(newnode_value)

                    if Head.data == target_value:
                        newnode.next = Head
                        Head = newnode
                    else:
                        prev = None
                        curr = Head 
                        while curr is not None and curr.data != target_value:
                            prev = curr
                            curr = curr.next
                        if curr is None:
                            print(f"Node with data '{target_value}' is not found.")
                        else:
                            prev.next = newnode
                            newnode.next = curr

            #returns user to Main Menu
            elif user_operation == 5:
                break

    elif user_choice == 5:
        break

print(f"\n    Thank you and have a nice day! ^^   ")