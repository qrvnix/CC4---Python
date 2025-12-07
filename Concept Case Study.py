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
            print("\nInvalid input. Please try again.\n")        

def choose_operation():
    while True:
        try:
            print(f"\nSelect what operation to do: \n 1 - Traversal (Print all your data)\n 2 - Retrieval\n 3 - Insertion\n 4 - Deletion\n 5 - Length\n 6 - Back to main menu")
            choice = int(input(f"Enter your choice (1-5): "))
            if choice in range(1, 7):
                return choice
            else:
                raise ValueError
        except ValueError:
            print("\nInvalid input. PLease try again.\n")

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

def traversal_SinglyCircular(head):
    if head is None:
        print("Your list is empty.")
        return

    curr = head
    print("Linked List:", end=" ")

    while True:
        print(curr.data, end=" -> ")
        curr = curr.next

        # Stopping point
        if curr == head:
            break
    
    print("(back to head)\n")

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
            print("\nInvalid input. PLease try again.\n")

def insertion():
    while True:
        try:
            print(f"Select where to insert a node:\n 1 - Beginning\n 2 - Middle (Before a node)\n 3 - Middle (After a node)\n 4 - End")
            choice = int(input(f"Enter your choice (1-4): "))
            if choice in range(1, 5):
                return choice
            else:
                raise ValueError
        except ValueError:
            print("\nInvalid input. PLease try again.\n")

def insertion_circular():
    while True:
        try:
            print(f"Select where to insert a node:\n 1 - Beginning\n 2 - Specific Position\n 3 - End")
            choice = int(input(f"Enter your choice (1-3): "))
            if choice in range(1, 4):
                return choice
            else:
                raise ValueError
        except ValueError:
            print("\nInvalid input. PLease try again.\n")

def deletion():
    while True:
        try:
            print(f"Select where to delete a node:\n 1 - Beginning\n 2 - Specific Position\n 3 - End")
            choice = int(input(f"Enter your choice (1-3): "))
            if choice in range(1, 4):
                return choice
            else:
                raise ValueError
        except ValueError:
            print("\nInvalid input. PLease try again.\n")

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
                
                #inserting at the middle-after a node (singly)
                elif insert_choice == 3:
                    print(f"\n                  SINGLY LINKED LIST: Insertion-Middle (After)     \n")
                    target_value = input("Enter data of the node AFTER which to insert: ")
                    newnode_value = str(input("Enter data of new node: "))
                    newnode = Node(newnode_value)

                    #traverse to find the target
                    curr = Head
                    while curr is not None and curr.data != target_value:
                        curr = curr.next
                    
                    if curr is None:
                        print(f"Node '{target_value}' not found. Cannot insert. :( \n")
                    else:
                        #adjust pointers
                        newnode.next = curr.next
                        curr.next = newnode
                
                #inserting at the end (singly)
                elif insert_choice == 4:
                    print(f"\n                  SINGLY LINKED LIST: Insertion-End     \n")
                    newnode_value = str(input("Enter data of new node: "))
                    newnode = Node(newnode_value)

                    #traverse to find tail
                    curr = Head
                    while curr.next is not None:
                        curr = curr.next

                    #adjust pointers
                    curr.next = newnode

            #deletion operation (singly)
            elif user_operation == 4:
                print(f"\n                  SINGLY LINKED LIST: Deletion                  \n")
                delete_choice = deletion()

                #deleting at the beginning (singly)
                if delete_choice == 1:
                    print(f"\n                  SINGLY LINKED LIST: Deletion-Beginning     \n")
                    temp_var = Head     #save to temporary variable
                    Head = Head.next    #adjust pointers
                    temp_var = None     #delete temporary variable
                    print("Successfully deleted the head of the list!\n")
                
                #deleting at specified position (singly)
                elif delete_choice == 2:
                    print(f"\n                  SINGLY LINKED LIST: Deletion-Specified Position     \n")
                    try:
                        delete_pos = int(input("Enter position of the node to be deleted: "))
                    except ValueError:
                        print("\nInvalid input. Please try again.\n")

                    #if list is empty
                    if Head is None:
                        print("List is empty!\n")
                        continue

                    #if user want to delete 1st position/head
                    if delete_pos == 1:
                        Head = Head.next
                        print("Deleted position 1 successfully!\n")
                        continue
                    
                    prev = None
                    curr = Head
                    count_pos = 1

                    while curr is not None and count_pos < delete_pos:
                        prev = curr
                        curr = curr.next
                        count_pos += 1

                    if curr is None:
                        print("Position out of range.\n")
                    else:
                        prev.next = curr.next
                        print(f"Deleted node at position {delete_pos}!\n")
                    
                #deleting at the end (singly)
                elif delete_choice == 3:
                    print(f"\n                  SINGLY LINKED LIST: Deletion-End     \n")
                    
                    # if list is empty
                    if Head is None:
                        print("List is empty!\n")
                    
                    # if list has only 1 node
                    elif Head.next is None:
                        Head = None
                        print("Deleted the only node in the list!\n")

                    else:
                        #traverse
                        curr = Head
                        while curr.next.next is not None:
                            curr = curr.next

                        curr.next = None
                        print(f"Successfully deleted the tail node!\n")

            #count the length of the list
            elif user_operation == 5:
                print(f"\n                  SINGLY LINKED LIST: Length                  \n")
                
                curr = Head
                count = 0

                while curr is not None:
                    count += 1
                    curr = curr.next
                print(f"Length: {count}")

            #returns user to Main Menu
            elif user_operation == 6:
                break

    elif user_choice == 2:
        print(f"\n                  SINGLY-CIRCULAR LINKED LIST                  \n")
        print(f"_______________Let's create your list first!______________")

        #determine the size
        list_size = int(input("Enter list length: "))

        #create the circular list
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
        
        current.next = Head

        #print the created list
        print("\n-----Current List:-----\n")
        traversal_SinglyCircular(Head)
        print("\n-----------------------")

        #Menu of operations under singly-circular
        while True:
            user_operation = choose_operation()
            if user_operation == 1:
                print(f"\n                  SINGLY-CIRCULAR LINKED LIST: Traversal                  \n")
                traversal_SinglyCircular(Head)
            
            elif user_operation == 2:
                print(f"\n                  SINGLY-CIRCULAR LINKED LIST: Retrieval                  \n")
                retri_choice = for_retrieval()
                if retri_choice == 1:       #checking if a value exists
                    user_value = str(input("\nEnter value to check: "))
                    found = False
                    curr = Head

                    if curr is None:
                        print("The list is empty.")
                    else:
                        while True:
                            if curr.data == user_value:
                                print(f"{user_value} exists in the linked list!")
                                found = True
                                break

                            curr = curr.next

                            # stop when we return to head
                            if curr == Head:
                                break

                        if not found:
                            print(f"{user_value} doesn't exist in the linked list. :(")
                
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

                    curr = Head
                    curr_pos = 1        #Head's position is 1

                    if curr is None:
                        print("The list is empty.")
                    else:
                        while True:
                            # If we've reached the position:
                            if curr_pos == retri_pos:
                                print(f"Position {retri_pos} has a data of {curr.data}")
                                break

                            curr = curr.next
                            curr_pos += 1

                            # We've looped back to head → position doesn't exist
                            if curr == Head:
                                print(f"{retri_pos} is out of range.")
                                break

            elif user_operation == 3:
                print(f"\n                  SINGLY-CIRCULAR LINKED LIST: Insertion                  \n")
                insert_choice = insertion_circular()

                #insertion at the beginning (singly-circular)
                if insert_choice == 1:
                    print(f"\n                  SINGLY-CIRCULAR LINKED LIST: Insertion-Beginning                  \n")
                    newnode_value = str(input("Enter data of new node: "))
                    newnode = Node(newnode_value)

                    #empty list
                    if Head is None:
                        Head = newnode
                        newnode.next = Head     # Points to itself

                    else:
                        last = Head             # Find last node
                        while last.next != Head:
                            last = last.next

                        newnode.next = Head     # Point new node to current head
                        last.next = newnode     # Make last node point to new head
                        Head = newnode          # Update head

                    print("Node inserted at the beginning! :)")
                
                #insertion at specified position (singly-circular)
                elif insert_choice == 2:
                    print(f"\n                  SINGLY-CIRCULAR LINKED LIST: Insertion-Specified Position                  \n")
                    newnode_value = str(input("Enter data of new node: "))
                    newnode = Node(newnode_value)

                    while True:
                        try:
                            insert_pos = int(input("Enter position to insert a node: "))
                            if insert_pos < 1:
                                raise ValueError
                            break
                        except ValueError:
                            print("\nInvalid input. Please try again.\n") 
                    
                    if insert_pos == 1:     #same as insertion at the beginning
                        if Head is None:
                            Head = newnode
                            newnode.next = Head     # Points to itself

                        else:
                            last = Head             # Find last node
                            while last.next != Head:
                                last = last.next

                            newnode.next = Head     # Point new node to current head
                            last.next = newnode     # Make last node point to new head
                            Head = newnode          # Update head
                            
                        print("Node inserted at position 1! :)")

                    if insert_pos > 1:    # insertion at positions other than 1
                        if Head is None:
                            print("The list is empty.")

                        else:
                            curr = Head
                            prev = None
                            curr_pos = 1        #Head's position is 1

                            while True:
                                #Stop traversing before the position
                                if curr_pos == insert_pos:
                                    break

                                prev = curr
                                curr = curr.next
                                curr_pos += 1

                                #looped back to head → position doesn't exist
                                if curr == Head:
                                    print(f"{retri_pos} is out of range.")
                                    break

                            prev.next = newnode     #node prior to the position
                            newnode.next = curr     #point new node to the node on target position
                            
                            print(f"Node inserted at position {insert_pos}!")

                elif insert_choice == 3:
                    print(f"\n                  SINGLY-CIRCULAR LINKED LIST: Insertion-End                  \n")
                    newnode_value = str(input("Enter data of new node: "))
                    newnode = Node(newnode_value)

                    #empty list
                    if Head is None:
                        Head = newnode
                        newnode.next = Head     # Points to itself

                    else:
                        last = Head             # Find last node
                        while last.next != Head:
                            last = last.next
      
                        last.next = newnode     # Make last node point to new head
                        newnode.next = Head

                        print("Node inserted at the end! :)")

            elif user_operation == 4:
                print(f"\n                  SINGLY-CIRCULAR LINKED LIST: Deletion                  \n")

            elif user_operation == 5:
                print(f"\n                  SINGLY-CIRCULAR LINKED LIST: Length                  \n")

            elif user_operation == 6:
                break

    elif user_choice == 5:
        break

print(f"\n    Thank you and have a nice day! ^^   ")