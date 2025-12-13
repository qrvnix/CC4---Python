class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Doubly_Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

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
            print(f"\nSelect what operation to do: \n 1 - Traversal (Print all your data)\n 2 - Retrieval\n 3 - Insertion\n 4 - Deletion\n 5 - Length\n 6 - Sort\n 7 - Back to main menu")
            choice = int(input(f"Enter your choice (1-7): "))
            if choice in range(1, 8):
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

def traversal_Doubly(head):
    if head is None:
        print("Your list is empty.")
        return
    
    curr = head
    print("Linked List:", end=" ")

    while curr:
        print(curr.data, end=" <-> " if curr.next else "")
        curr = curr.next

    print("\n")

def traversal_DoublyCircular(head):
    if head is None:
        print("Your list is empty.")
        return
    
    curr = head
    print("Linked List:", end=" ")

    while True:
        print(curr.data, end="")
        curr = curr.next

        # Stopping point
        if curr == head:
            break
        else:
            print(" <-> ", end="")

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

def insertion_doubly():
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

def sorting_operation():
    while True:
        try:
            print(f"Select how to sort: \n 1 - Lowest to highest\n 2 - Highest to lowest")
            choice = int(input(f"Enter your choice (1-2): "))
            if choice in range(1, 3):
                return choice
            else:
                raise ValueError
        except ValueError:
            print("\nInvalid input. PLease try again.\n")

def selection_sort_S(head, ascending = True):
    if head is None:
        return head

    current_node = head     # Node being sorted

    while current_node is not None:
        selected_node = current_node             # Node with the smallest value found in the current pass
        search_node = current_node.next     # Node used to find the minimum value ahead

        while search_node is not None:
            if ascending:
                if search_node.data < selected_node.data:
                    selected_node = search_node
            else:
                if search_node.data > selected_node.data:
                    selected_node = search_node
            search_node = search_node.next

        # Swap data
        current_node.data, selected_node.data = selected_node.data, current_node.data
        current_node = current_node.next

    return head

def selection_sort_SC(head, ascending = True):
    if head is None or head.next == head:
        return head

    current_node = head
    while True:
        selected_node = current_node
        search_node = current_node.next

        while search_node != head:
            if ascending:
                if search_node.data < selected_node.data:
                    selected_node = search_node
            else:
                if search_node.data > selected_node.data:
                    selected_node = search_node
            search_node = search_node.next

        # Swap data
        current_node.data, selected_node.data = selected_node.data, current_node.data
        current_node = current_node.next

        if current_node == head:
            break

    return head

def selection_sort_D(head, ascending = True):
    if head is None:
        return head

    current_node = head
    while current_node is not None:
        selected_node = current_node
        search_node = current_node.next

        while search_node is not None:
            if ascending:
                if search_node.data < selected_node.data:
                    selected_node = search_node
            else:
                if search_node.data > selected_node.data:
                    selected_node = search_node
            search_node = search_node.next

        # Swap data
        current_node.data, selected_node.data = selected_node.data, current_node.data
        current_node = current_node.next

    return head

def selection_sort_DC(head, ascending = True):
    if head is None or head.next == head:
        return head

    current_node = head
    while True:
        selected_node = current_node
        search_node = current_node.next

        while search_node != head:
            if ascending:
                if search_node.data < selected_node.data:
                    selected_node = search_node
            else:
                if search_node.data > selected_node.data:
                    selected_node = search_node
            search_node = search_node.next

        current_node.data, selected_node.data = selected_node.data, current_node.data
        current_node = current_node.next

        if current_node == head:
            break

    return head

#Main Code
while True:
    user_choice = choose()
    if user_choice == 1:
        print(f"\n                  SINGLY LINKED LIST                  \n")
        print(f"_______________Let's create your list first!______________")

        while True:
            try:
                list_size = int(input("Enter list length: "))
                break
            except ValueError:
                print("\nInvalid input. Please try again.\n")

        #creates the head
        Head_data = int(input("\nEnter head's data: "))
        Head = Node(Head_data)
        current = Head

        nodeCount = 1
        while nodeCount < list_size:
            next_data = int(input("Enter next data: "))
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
                    while True:
                        try:
                            user_value = int(input("\nEnter value to check: "))
                            break
                        except ValueError:
                            print("Invalid input. Please try again.")
                    
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
                    while True:
                        try:
                            newnode_value = int(input("Enter data of new node: "))
                            break
                        except ValueError:
                            print("\nInvalid input. Please try again.\n")
                    
                    newnode = Node(newnode_value)
                    newnode.next = Head
                    Head = newnode

                    print(f"{newnode_value} was successfully inserted!")
                
                #inserting at the middle-before a node (singly)
                elif insert_choice == 2:
                    print(f"\n                  SINGLY LINKED LIST: Insertion-Middle (Before)     \n")
                    while True:    
                        try:
                            target_value = int(input("Enter data of the node BEFORE which to insert: "))
                            newnode_value = int(input("Enter data of new node: "))
                            break
                        except ValueError:
                            print("\nInvalid input. Please try again.\n")

                    newnode = Node(newnode_value)

                    if Head.data == target_value:
                        newnode.next = Head
                        Head = newnode
                        print(f"{newnode_value} was successfully inserted!")

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
                            print(f"{newnode_value} was successfully inserted!")
                
                #inserting at the middle-after a node (singly)
                elif insert_choice == 3:
                    print(f"\n                  SINGLY LINKED LIST: Insertion-Middle (After)     \n")
                    while True:    
                        try:    
                            target_value = int(input("Enter data of the node AFTER which to insert: "))
                            newnode_value = int(input("Enter data of new node: "))
                            break
                        except ValueError:
                            print("\nInvalid input. Please try again.\n")
                    
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
                        print(f"{newnode_value} was successfully inserted!")
                
                #inserting at the end (singly)
                elif insert_choice == 4:
                    print(f"\n                  SINGLY LINKED LIST: Insertion-End     \n")
                    while True:
                        try:
                            newnode_value = int(input("Enter data of new node: "))
                            break
                        except ValueError:
                            print("\nInvalid input. Please try again.\n")
                    
                    newnode = Node(newnode_value)

                    #traverse to find tail
                    curr = Head
                    while curr.next is not None:
                        curr = curr.next

                    #adjust pointers
                    curr.next = newnode
                    print(f"{newnode_value} was successfully inserted!")

            #deletion operation (singly)
            elif user_operation == 4:
                print(f"\n                  SINGLY LINKED LIST: Deletion                  \n")
                delete_choice = deletion()

                #deleting at the beginning (singly)
                if delete_choice == 1:
                    print(f"\n                  SINGLY LINKED LIST: Deletion-Beginning     \n")
                    
                    if Head is None:        # Empty list
                        print("List is empty!\n")
                        continue
                    
                    elif Head.next is None:  # only one node
                        Head = None

                    else:
                        temp_var = Head     # save to temporary variable
                        Head = Head.next    # adjust pointers
                        temp_var = None     # delete temporary variable
                        
                        print("Successfully deleted the head of the list!\n")
                
                #deleting at specified position (singly)
                elif delete_choice == 2:
                    print(f"\n                  SINGLY LINKED LIST: Deletion-Specified Position     \n")
                    
                    while True:
                        try:
                            delete_pos = int(input("Enter position of the node to be deleted: "))
                            if delete_pos <= 0:
                                raise ValueError
                            break
                        except ValueError:
                            print("\nInvalid input. Please try again.\n")

                    # If list is empty
                    if Head is None:
                        print("List is empty!\n")

                    # If user want to delete 1st position/head
                    elif delete_pos == 1:
                        Head = Head.next
                        print("Deleted position 1 successfully!\n")
                    
                    else:
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
                    
                # Deleting at the end (singly)
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
                        # Traverse
                        curr = Head
                        while curr.next.next is not None:
                            curr = curr.next

                        curr.next = None
                        print(f"Successfully deleted the tail node!\n")

            # Count the length of the list
            elif user_operation == 5:
                print(f"\n                  SINGLY LINKED LIST: Length                  \n")
                
                curr = Head
                count = 0

                while curr is not None:
                    count += 1
                    curr = curr.next
                
                print(f"Length: {count}")

            # Performs selection sort
            elif user_operation == 6:
                print(f"\n                  SINGLY LINKED LIST: Sort                  \n")
                sort_choice = sorting_operation()

                if sort_choice == 1:
                    print(f"\n                  SINGLY LINKED LIST: Sort (Lowest - Highest)                  \n")
                    Head = selection_sort_S(Head, ascending = True)
                    print(f"Successfully sorted the list: LOWEST to HIGHEST")
                    
                    print("\n-----Current List:-----\n")
                    traversal(Head)
                    print("\n-----------------------")
                
                elif sort_choice == 2:
                    print(f"\n                  SINGLY LINKED LIST: Sort (Highest - Lowest)                  \n")
                    Head = selection_sort_S(Head, ascending = False)
                    print(f"Successfully sorted the list: HIGHEST to LOWEST")
                    
                    print("\n-----Current List:-----\n")
                    traversal(Head)
                    print("\n-----------------------")

            # Returns user to Main Menu
            elif user_operation == 7:
                break

    elif user_choice == 2:
        print(f"\n                  SINGLY-CIRCULAR LINKED LIST                  \n")
        print(f"_______________Let's create your list first!______________")

        # Determine the size
        while True:
            try:
                list_size = int(input("Enter list length: "))
                break
            except ValueError:
                print("\nInvalid input. Please try again.\n")

        # Create the circular list
        Head_data = int(input("\nEnter head's data: "))
        Head = Node(Head_data)
        current = Head

        nodeCount = 1
        while nodeCount < list_size:
            next_data = int(input("Enter next data: "))
            new_node = Node(next_data)
            current.next = new_node
            current = new_node
            nodeCount += 1
        
        current.next = Head

        # Print the created list
        print("\n-----Current List:-----\n")
        traversal_SinglyCircular(Head)
        print("\n-----------------------")

        # Menu of operations under singly-circular
        while True:
            user_operation = choose_operation()
            
            if user_operation == 1:
                print(f"\n                  SINGLY-CIRCULAR LINKED LIST: Traversal                  \n")
                traversal_SinglyCircular(Head)
            
            elif user_operation == 2:
                print(f"\n                  SINGLY-CIRCULAR LINKED LIST: Retrieval                  \n")
                retri_choice = for_retrieval()
                if retri_choice == 1:       #checking if a value exists
                    while True:    
                        try:
                            user_value = int(input("\nEnter value to check: "))
                            break
                        except ValueError:
                            print("\nInvalid input. Please try again.\n")

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

                # Insertion at the beginning (singly-circular)
                if insert_choice == 1:
                    print(f"\n                  SINGLY-CIRCULAR LINKED LIST: Insertion-Beginning                  \n")
                    while True:
                        try:
                            newnode_value = int(input("Enter data of new node: "))
                            break
                        except ValueError:
                            print("\nInvalid input. Please try again.\n")
                    
                    newnode = Node(newnode_value)

                    # Empty list
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
                
                # Insertion at specified position (singly-circular)
                elif insert_choice == 2:
                    print(f"\n                  SINGLY-CIRCULAR LINKED LIST: Insertion-Specified Position                  \n")
                    while True:
                        try:
                            newnode_value = int(input("Enter data of new node: "))
                            break
                        except ValueError:
                            print("\nInvalid input. Please try again.\n")

                    newnode = Node(newnode_value)

                    while True:
                        try:
                            insert_pos = int(input("Enter position to insert a node: "))
                            if insert_pos < 1:
                                raise ValueError
                            break
                        except ValueError:
                            print("\nInvalid input. Please try again.\n") 
                    
                    if insert_pos == 1:     # Same as insertion at the beginning
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

                    elif insert_pos > 1:    # Insertion at positions other than 1
                        if Head is None:
                            print("The list is empty.")

                        else:
                            curr = Head
                            prev = None
                            curr_pos = 1        #Head's position is 1

                            while True:
                                # Stop traversing before the position
                                if curr_pos == insert_pos:
                                    break

                                prev = curr
                                curr = curr.next
                                curr_pos += 1

                                # Looped back to head → position doesn't exist
                                if curr == Head:
                                    print(f"{insert_pos} is out of range.")
                                    break

                            prev.next = newnode     # node prior to the position
                            newnode.next = curr     # point new node to the node on target position
                            
                            print(f"Node inserted at position {insert_pos}!")

                # Insertion at the end (singly-circular)
                elif insert_choice == 3:
                    print(f"\n                  SINGLY-CIRCULAR LINKED LIST: Insertion-End                  \n")
                    while True:
                        try:
                            newnode_value = int(input("Enter data of new node: "))
                            break
                        except ValueError:
                            print("\nInvalid input. Please try again.\n")
                    
                    newnode = Node(newnode_value)

                    # empty list
                    if Head is None:
                        Head = newnode
                        newnode.next = Head     # Points to itself
                        print("Node inserted at the end! :)")

                    else:
                        last = Head             # Find last node
                        while last.next != Head:
                            last = last.next
      
                        last.next = newnode     # Make last node point to new head
                        newnode.next = Head

                        print("Node inserted at the end! :)")

            elif user_operation == 4:
                print(f"\n                  SINGLY-CIRCULAR LINKED LIST: Deletion                  \n")
                delete_choice = deletion()

                # deleting at the beginning (singly-circular)
                if delete_choice == 1:
                    print(f"\n                  SINGLY-CIRCULAR LINKED LIST: Deletion-Beginning     \n")
                    
                    #empty list
                    if Head is None:
                        print("The list is empty. There is nothing to delete.\n")
                    
                    #One node only
                    elif Head.next == Head:     # Head pointing to it self (circular)
                        Head = None
                        print("Successfully deleted the head of the list!\n")
                    
                    # More than one node
                    else:
                        temp_var = None
                        last = Head
                        while last.next != Head:
                            temp_var = last
                            last = last.next

                        last.next = Head.next       # Tail points to the node next to head
                        Head = Head.next            # Adjust the head
                        temp_var = None             # Dispose temporary variable
                        print("Successfully deleted the head of the list!\n")
                
                elif delete_choice == 2:
                    print(f"\n                  SINGLY-CIRCULAR LINKED LIST: Deletion-Specified Position     \n")
                    while True:    
                        try:
                            delete_pos = int(input("Enter position of the node to be deleted: "))
                            if delete_pos <= 0:
                                raise ValueError
                            break
                        except ValueError:
                            print("\nInvalid input. Please try again.\n")
                    
                    if Head is None:
                        print("The list is empty. There is nothing to delete.\n")
                    
                    else:
                        if delete_pos == 1:      # Same as deleting the front node
                            temp_var = Head
                            if Head.next == Head:
                                Head = None

                            else:
                                last = Head
                                while last.next != Head:
                                    temp_var = last
                                    last = last.next

                                last.next = Head.next       # Tail points to the node next to head
                                Head = Head.next            # Adjust the head
                            
                            temp_var = None             # Dispose temporary variable
                            print("Successfully deleted position 1!\n")
                    
                        else:
                            curr = Head         # Current node during traversal
                            prev = None         # Node before the current node
                            temp_var = None
                            curr_pos = 1

                            while True:
                                #Stop traversing before the position
                                if curr_pos == delete_pos:
                                    break

                                prev = curr
                                temp_var = curr
                                curr = curr.next
                                curr_pos += 1

                                #looped back to head → position doesn't exist
                                if curr == Head:
                                    curr = None
                                    break
                            
                            if curr is None:
                                print(f"{delete_pos} is out of range.")
                            else:
                                temp_var = curr
                                prev.next = curr.next       # Adjust the previous node's pointer
                                temp_var = None         # Dispose temporary variable
                                print(f"Successfully deleted position {delete_pos}!\n")
                
                elif delete_choice == 3:
                    print(f"\n                  SINGLY-CIRCULAR LINKED LIST: Deletion-End     \n")
                    
                    #empty list
                    if Head is None:
                        print("The list is empty. There is nothing to delete.\n")

                    #One node only
                    elif Head.next == Head:     # Head pointing to it self (circular)
                        temp_var = Head         # Save the node to be deleted
                        Head = None
                        temp_var = None         # Dispose
                        print("Successfully deleted the head of the list!\n") 

                    #More than one node
                    else:
                        prev = None
                        last = Head

                        # Traverse to find the tail
                        while last.next != Head:
                            prev = last
                            last = last.next

                        temp_var = last         # Save in temporary variable
                        prev.next = Head        # Previous node points to head
                        temp_var = None         # Dispose
                        print("Successfully deleted the tail of the list!\n")  

            elif user_operation == 5:
                print(f"\n                  SINGLY-CIRCULAR LINKED LIST: Length                  \n")

                # Empty list
                if Head is None:
                    print("The list is empty!\n")

                else:
                    count = 1
                    curr = Head

                    while curr.next != Head:        # Traverse until the current node points to the head
                        count += 1
                        curr = curr.next
                    
                    print(f"Length: {count}.\n")

            # Sorting operation (Singly-circular)
            elif user_operation == 6:
                print(f"\n                  SINGLY-CIRCULAR LINKED LIST: Sort                  \n")
                sort_choice = sorting_operation()

                if sort_choice == 1:
                    print(f"\n                  SINGLY-CIRCULAR LINKED LIST: Sort (Lowest - Highest)                  \n")
                    Head = selection_sort_SC(Head, ascending = True)
                    print(f"Successfully sorted the list: LOWEST to HIGHEST")
                    
                    print("\n-----Current List:-----\n")
                    traversal_SinglyCircular(Head)
                    print("\n-----------------------")
                
                elif sort_choice == 2:
                    print(f"\n                  SINGLY-CIRCULAR LINKED LIST: Sort (Highest - Lowest)                  \n")
                    Head = selection_sort_SC(Head, ascending = False)
                    print(f"Successfully sorted the list: HIGHEST to LOWEST")
                    
                    print("\n-----Current List:-----\n")
                    traversal_SinglyCircular(Head)
                    print("\n-----------------------")

            # Returns user to Main Menu
            elif user_operation == 7:
                break

    elif user_choice == 3:
        print(f"\n                  DOUBLY LINKED LIST                  \n")
        print(f"_______________Let's create your list first!______________")

        while True:
            try:
                list_size = int(input("Enter list length: "))
                break
            except ValueError:
                print("\nInvalid input. Please try again.\n")

        #creates the head
        Head_data = int(input("\nEnter head's data: "))
        Head = Doubly_Node(Head_data)
        current = Head

        nodeCount = 1
        while nodeCount < list_size:
            next_data = int(input("Enter next data: "))
            new_node = Doubly_Node(next_data)
            current.next = new_node
            new_node.prev = current
            current = new_node
            nodeCount += 1

        #print the created list
        print("\n-----Current List:-----\n")
        traversal_Doubly(Head)
        print("\n-----------------------")

        while True:
            user_operation = choose_operation()
            #traversal operation (singly)
            if user_operation == 1:
                print(f"\n                  DOUBLY LINKED LIST: Traversal                  \n")
                traversal_Doubly(Head)
            
            elif user_operation == 2:
                print(f"\n                  DOUBLY LINKED LIST: Retrieval                  \n")
                retri_choice = for_retrieval()
                
                    #checks if a particular value exists
                if retri_choice == 1:
                    while True:    
                        try:
                            user_value = int(input("\nEnter value to check: "))
                            break
                        except ValueError:
                            print("\nInvalid input. Please try again.\n")

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
                            break

                        except ValueError:
                            print("\nInvalid input. Please try again.\n")

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

            elif user_operation == 3:
                print(f"\n                  DOUBLY LINKED LIST: Insertion                  \n")

                insert_choice = insertion_doubly()

                #inserting at beginning (singly)
                if insert_choice == 1:
                    print(f"\n                  DOUBLY LINKED LIST: Insertion-Beginning      \n")
                    while True:
                        try:
                            newnode_value = int(input("Enter data of new node: "))
                            break
                        except ValueError:
                            print("\nInvalid input. Please try again.\n")

                    newnode = Doubly_Node(newnode_value)

                    if Head is not None:        # This makes sure that the previous pointer is only set if list is not empty
                        Head.prev = newnode

                    newnode.next = Head
                    Head = newnode
                
                elif insert_choice == 2:
                    print(f"\n                  DOUBLY LINKED LIST: Insertion-Specific Position      \n")
                    while True:
                        try:
                            newnode_value = int(input("Enter data of new node: "))
                            break
                        except ValueError:
                            print("\nInvalid input. Please try again.\n") 

                    newnode = Doubly_Node(newnode_value)

                    while True:
                        try:
                            insert_pos = int(input("Enter position to insert a node: "))
                            if insert_pos < 1:
                                raise ValueError
                            break
                        except ValueError:
                            print("\nInvalid input. Please try again.\n") 
                    
                    if insert_pos == 1:     # Insertion at the beginning
                        if Head is not None:
                            Head.prev = newnode
                        newnode.next = Head     # Points to itself
                        newnode.prev = None
                        Head = newnode
                        print("Node inserted at position 1!")
                    
                    else:                   # Insert at positions > 1
                        if Head is None:    #checks if list is empty
                            print("The list is empty.")
                        else:
                            curr = Head
                            curr_pos = 1

                            # Traverse to the node currently at insert_pos
                            while curr is not None and curr_pos < insert_pos:
                                prev = curr
                                curr = curr.next
                                curr_pos += 1

                            # Insert newnode between prev and curr
                            newnode.prev = prev
                            newnode.next = curr
                            prev.next = newnode
                            if curr is not None:
                                curr.prev = newnode

                            print(f"Node inserted at position {insert_pos}!")

                # Insertion at the end (doubly)
                elif insert_choice == 3:
                    print(f"\n                  DOUBLY LINKED LIST: Insertion-End      \n")
                    while True:   
                        try:
                            newnode_value = int(input("Enter data of new node: "))
                            break
                        except ValueError:
                            print("\nInvalid input. Please try again.\n")

                    newnode = Doubly_Node(newnode_value)

                    # Traverse to find tail
                    curr = Head
                    while curr.next is not None:
                        curr = curr.next

                    # Adjust pointers
                    curr.next = newnode
                    newnode.prev = curr

                    print(f"Successfully inserted {newnode.data}! :)")

            elif user_operation == 4:
                print(f"\n                  DOUBLY LINKED LIST: Deletion      \n")
                delete_choice = deletion()

                # Deletion at the beginning (Doubly)
                if delete_choice == 1:
                    print(f"\n                  DOUBLY LINKED LIST: Deletion-Beginning      \n")

                    if Head is None:        # Empty list
                        print("The list is empty. Nothing to delete.\n")

                    elif Head.next is None: # One element only
                        Head = None
                        print("Successfully deleted the head (list is now empty)!\n")
                    
                    else:
                        temp_var = Head     # Save to temporary variable
                        Head = Head.next    # Adjust pointer
                        Head.prev = None
                        temp_var = None     # Delete temporary variable

                        print("Successfully deleted the head of the list!\n")

                # Deletion at specified position (Doubly)
                elif delete_choice == 2:
                    print(f"\n                  DOUBLY LINKED LIST: Deletion-Specific Position      \n")
                    while True:
                        try:
                            delete_pos = int(input("Enter position of the node to be deleted: "))
                            if delete_pos <= 0:
                                raise ValueError
                            break
                        except ValueError:
                            print("\nInvalid input. Please try again.\n")
                    
                    if Head is None:        # Empty list
                        print("List is empty!\n")
                    
                    elif delete_pos == 1:
                        temp_var = Head     # Save to temporary variable

                        if Head.next is None:       # Only one node
                            Head = None
                        
                        else:
                            Head = Head.next    # Adjust pointer
                            Head.prev = None
                        
                        temp_var = None     # Delete temporary variable

                        print(f"Successfully deleted position {delete_pos}!\n")
                        continue

                    else:
                        curr = Head
                        count_pos = 1

                        # Traverse to reach the position
                        while curr is not None and count_pos < delete_pos:
                            curr = curr.next
                            count_pos += 1

                        if curr is None:    # Reached None, therefore, position is invalid
                            print("Position out of range.\n")
                        
                        else:
                            curr.prev.next = curr.next      # Connect previous node to next node

                            if curr.next is not None:
                                curr.next.prev = curr.prev

                            print(f"Deleted node at position {delete_pos}!\n")

                # Deletion at the end (Doubly)
                elif delete_choice == 3:
                    print(f"\n                  DOUBLY LINKED LIST: Deletion-End     \n")

                    # if list is empty
                    if Head is None:
                        print("List is empty!\n")
                    
                    # if list has only 1 node
                    elif Head.next is None:
                        Head = None
                        print("Deleted the only node in the list!\n")

                    else:
                        # Traverse
                        curr = Head
                        while curr.next.next is not None:
                            curr = curr.next

                        last = curr.next

                        curr.next = None
                        last.prev = None

                        print(f"Successfully deleted the tail node!\n")

            elif user_operation == 5:       # Counts the length of the list
                print(f"\n                  DOUBLY LINKED LIST: Length                  \n")
            
                curr = Head
                count = 0

                while curr is not None:
                    count += 1
                    curr = curr.next
                print(f"Length: {count}")

            # Returns user to Main Menu
            elif user_operation == 6:
                print(f"\n                  DOUBLY LINKED LIST: Sort                  \n")
                sort_choice = sorting_operation()

                if sort_choice == 1:
                    print(f"\n                  DOUBLY LINKED LIST: Sort (Lowest - Highest)                  \n")
                    Head = selection_sort_D(Head, ascending = True)
                    print(f"Successfully sorted the list: LOWEST to HIGHEST")
                    
                    print("\n-----Current List:-----\n")
                    traversal_Doubly(Head)
                    print("\n-----------------------")
                
                elif sort_choice == 2:
                    print(f"\n                  DOUBLY LINKED LIST: Sort (Highest - Lowest)                  \n")
                    Head = selection_sort_D(Head, ascending = False)
                    print(f"Successfully sorted the list: HIGHEST to LOWEST")
                    
                    print("\n-----Current List:-----\n")
                    traversal_Doubly(Head)
                    print("\n-----------------------")

            # Returns user to Main Menu
            elif user_operation == 7:
                break

    elif user_choice == 4:
        print(f"\n                  DOUBLY-CIRCULAR LINKED LIST                  \n")
        print(f"_______________Let's create your list first!______________")
        
        #determine the size
        while True:
            try:
                list_size = int(input("Enter list length: "))
                break
            except ValueError:
                print("\nInvalid input. Please try again.\n")

        #create the circular list
        Head_data = int(input("\nEnter head's data: "))
        Head = Doubly_Node(Head_data)
        current = Head

        nodeCount = 1
        while nodeCount < list_size:
            next_data = int(input("Enter next data: "))
            new_node = Doubly_Node(next_data)

            current.next = new_node
            new_node.prev = current

            current = new_node
            nodeCount += 1
        
        current.next = Head
        Head.prev = current

        # Print the created list
        print("\n-----Current List:-----\n")
        traversal_DoublyCircular(Head)
        print("\n-----------------------")

        # Menu of operations under doubly-circular
        while True:
            user_operation = choose_operation()
            if user_operation == 1:
                print(f"\n                  DOUBLY-CIRCULAR LINKED LIST: Traversal                  \n")
                traversal_DoublyCircular(Head)
            
            elif user_operation == 2:
                print(f"\n                  DOUBLY-CIRCULAR LINKED LIST: Retrieval                  \n")
                retri_choice = for_retrieval()

                # Checking if a value exists
                if retri_choice == 1:  
                    while True:     
                        try:
                            user_value = int(input("\nEnter value to check: "))
                            break
                        except ValueError:
                            print("\nInvalid input. Please try again.\n")

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

                            # Stop when we return to head
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
                            break
                        except ValueError:
                            print("\nInvalid input. Please try again.\n")

                    curr = Head
                    curr_pos = 1        #Head's position is 1

                    if curr is None:
                        print("The list is empty.")
                        continue

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
                print(f"\n                  DOUBLY-CIRCULAR LINKED LIST: Insertion                  \n")
                insert_choice = insertion_doubly()
                
                # Insertion at the beginning (doubly-circular)
                if insert_choice == 1:
                    print(f"\n                  DOUBLY-CIRCULAR LINKED LIST: Insertion-Beginning                  \n")
                    while True:    
                        try:    
                            newnode_value = int(input("Enter data of new node: "))
                            break
                        except ValueError:
                            print("\nInvalid input. Please try again.\n")

                    newnode = Doubly_Node(newnode_value)

                    # Checks if user has an empty list
                    if Head is None:
                        Head = newnode
                        newnode.next = Head     # Points to itself
                        newnode.prev = Head

                    else:
                        last = Head             # Find last node
                        while last.next != Head:
                            last = last.next

                        newnode.next = Head     # Ajust pointers
                        newnode.prev = last
                        Head.prev = newnode
                        last.next = newnode     # Make last node point to new head
                        Head = newnode          # Update head

                    print("Node inserted at the beginning! :)")

                # Insertion at specified position (doubly-circular)
                elif insert_choice == 2:
                    print(f"\n                  DOUBLY-CIRCULAR LINKED LIST: Insertion-Specific Position                  \n")
                    while True:
                        try:
                            newnode_value = int(input("Enter data of new node: "))
                            break
                        except ValueError:
                            print("\nInvalid input. Please try again.\n")
                    
                    newnode = Doubly_Node(newnode_value)
                    
                    while True:
                        try:
                            insert_pos = int(input("Enter position to insert a node: "))
                            if insert_pos < 1:
                                raise ValueError
                            break
                        except ValueError:
                            print("\nInvalid input. Please try again.\n")

                    if insert_pos == 1:
                        
                        # Checks if user has an empty list
                        if Head is None:
                            Head = newnode
                            newnode.next = Head     # Points to itself
                            newnode.prev = Head
                        
                        else:
                            last = Head             # Find last node
                            while last.next != Head:
                                last = last.next

                            newnode.next = Head     # Adjust pointers
                            newnode.prev = last
                            Head.prev = newnode
                            last.next = newnode     # Make last node point to new head
                            Head = newnode          # Update head
                        
                        print("Node inserted at position 1! :)")
                    
                    else:       # Insert at position > 1
                        
                        # Checks if user has an empty list
                        if Head is None:
                            print("The list is empty.")

                        else:
                            curr = Head
                            curr_pos = 1        #Head's position is 1

                            while curr_pos < insert_pos - 1:
                                curr = curr.next
                                curr_pos += 1

                                # If we looped back to head → position doesn't exist
                                if curr == Head:
                                    print(f"{insert_pos} is out of range.")
                                    break
                            
                            # Insert newnode after curr
                            newnode.next = curr.next        # Adjust pointers
                            newnode.prev = curr
                            curr.next.prev = newnode
                            curr.next = newnode

                            print(f"Node inserted at position {insert_pos}!")

                elif insert_choice == 3:
                    print(f"\n                  DOUBLY-CIRCULAR LINKED LIST: Insertion-End                  \n")
                    while True:
                        try:
                            newnode_value = int(input("Enter data of new node: "))
                            break
                        except ValueError:
                            print("\nInvalid input. Please try again.\n")
                    
                    newnode = Doubly_Node(newnode_value)

                    # Checks if user has an empty list
                    if Head is None:
                        Head = newnode
                        newnode.next = Head     # Points to itself
                        newnode.prev = Head

                    else:
                        last = Head             # Find last node
                        while last.next != Head:
                            last = last.next

                        newnode.next = Head     # Ajust pointers
                        newnode.prev = last
                        last.next = newnode     # Make last node point to new head
                        Head.prev = newnode

                    print("Node inserted at the end! :)")

            elif user_operation == 4:
                print(f"\n                  DOUBLY-CIRCULAR LINKED LIST: Deletion                  \n")
                delete_choice = deletion()
                
                # Deletion at the beginning (Doubly-circular)
                if delete_choice == 1:
                    print(f"\n                  DOUBLY-CIRCULAR LINKED LIST: Deletion-Beginning                  \n")

                    # Empty list
                    if Head is None:
                        print("The list is empty. There is nothing to delete.\n")
                    
                    # One node only
                    elif Head.next == Head:     #Head pointing to it self (circular)
                        Head = None
                        print("Successfully deleted the head of the list!\n")
                    
                    # More than one node
                    else:
                        last = Head
                        while last.next != Head:
                            last = last.next

                        last.next = Head.next       # Tail points to the node next to head
                        Head.next.prev = last
                        Head = Head.next            # Adjust the head

                        print("Successfully deleted the head of the list!\n")

                # Deletion at specified position (Doubly-circular)
                elif delete_choice == 2:
                    print(f"\n                  DOUBLY-CIRCULAR LINKED LIST: Deletion-Specific Position                  \n")
                    while True:    
                        try:
                            delete_pos = int(input("Enter position of the node to be deleted: "))
                            if delete_pos <= 0:
                                raise ValueError
                            break                       
                        except ValueError:
                            print("\nInvalid input. Please try again.\n")
                        
                    if Head is None:
                        print("The list is empty. There is nothing to delete.\n")
                    
                    else:
                        if delete_pos == 1:
                            # One node only
                            if Head.next == Head:     #Head pointing to it self (circular)
                                Head = None
                                print("Successfully deleted the head of the list!\n")
                            
                            # More than one node
                            else:
                                last = Head
                                while last.next != Head:
                                    last = last.next

                                last.next = Head.next       # Tail points to the node next to head
                                Head.next.prev = last
                                Head = Head.next            # Adjust the head

                                print("Successfully deleted position 1!\n")
                        
                        else:
                            curr = Head         # Current node during traversal
                            curr_pos = 1

                            while curr_pos == delete_pos - 1:       # Stop at node before the target position
                                curr = curr.next
                                curr_pos += 1

                                #looped back to head → position doesn't exist
                                if curr.next == Head:
                                    print(f"{delete_pos} is out of range.")
                                    break 
                                
                            else:
                                node_to_delete = curr.next      # This only runs if no breaks happened

                                # If deleting the last node
                                if node_to_delete.next == Head:
                                    curr.next = Head
                                    Head.prev = curr

                                else:
                                    curr.next = node_to_delete.next      # Adjust pointers
                                    node_to_delete.next.next.prev = curr
                                    
                                    print(f"Successfully deleted position {delete_pos}!\n")

                # Deletion at the end (Doubly-circular)
                elif delete_choice == 3:
                    print(f"\n                  DOUBLY-CIRCULAR LINKED LIST: Deletion-End                  \n")

                    # Checks if list is empty
                    if Head is None:
                        print("The list is empty. There is nothing to delete.\n")

                    # One node only
                    elif Head.next == Head:     #Head pointing to it self (circular)
                        Head = None
                        print("Successfully deleted the head of the list!\n")
                    
                    # More than one node
                    else:
                        last = Head
                        while last.next != Head:
                            last = last.next

                        last.prev.next = Head       # Adjust pointers
                        Head.prev = last.prev
                        last = None

                        print("Successfully deleted the tail of the list!\n")

            elif user_operation == 5:
                print(f"\n                  DOUBLY-CIRCULAR LINKED LIST: Length                  \n")
                
                # Empty list
                if Head is None:
                    print("The list is empty!\n")

                else:
                    count = 0
                    curr = Head

                    while True:        # Traverse until the current node points to the head
                        count += 1
                        curr = curr.next
                        if curr == Head:  # Stop after completing full circle
                            break
                    
                    print(f"Length: {count}.\n")
            
            elif user_operation == 6:
                print(f"\n                  DOUBLY-CIRCULAR LINKED LIST: Sort                  \n")
                sort_choice = sorting_operation()

                if sort_choice == 1:
                    print(f"\n                  DOUBLY-CIRCULAR LINKED LIST: Sort (Lowest - Highest)                  \n")
                    Head = selection_sort_DC(Head, ascending = True)
                    print(f"Successfully sorted the list: LOWEST to HIGHEST")
                    
                    print("\n-----Current List:-----\n")
                    traversal_DoublyCircular(Head)
                    print("\n-----------------------")
                
                elif sort_choice == 2:
                    print(f"\n                  DOUBLY-CIRCULAR LINKED LIST: Sort (Highest - Lowest)                  \n")
                    Head = selection_sort_DC(Head, ascending = False)
                    print(f"Successfully sorted the list: HIGHEST to LOWEST")
                    
                    print("\n-----Current List:-----\n")
                    traversal_DoublyCircular(Head)
                    print("\n-----------------------")

            # Returns user to Main Menu
            elif user_operation == 7:
                break

    # Exits the Main Menu
    elif user_choice == 5:
        break

print(f"\n    Thank you and have a nice day! ^^   ")