class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def choose():
    print(f"\nSelect which list you want to create: \n 1 - Singly\n 2 - Singly Circular\n 3 - Doubly\n 4 - Doubly Circular\n 5 - Exit")
    choice = int(input(f"Enter your choice (1-5): "))
    return choice

def choose_operation():
    print(f"\nSelect what operation to do: \n 1 - Traversal (Print all your data)\n 2 - Retrieval\n 3 - Insertion\n 4 - Deletion")
    choice = int(input(f"Enter your choice (1-4): "))
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

        question = str(input(f"\nDo you want to link another data? (Hit enter to skip): "))
        while question.lower() == "yes":
            next_data = str(input("Enter next data: "))
            new_node = Node(next_data)
            current.next = new_node
            current = new_node
            question = str(input("\nDo you want to link another data? (Hit enter to skip): "))

        user_operation = choose_operation()
        if user_operation == 1:
            print(f"\n                  SINGLY LINKED LIST: Traversal                  \n")
            Curr = Head
            print(f"Your Linked List Data:\n")
            while Curr is not None:
                print(Curr.data, " ")
                Curr = Curr.next

    if user_choice == 5:
        break

print(f"    Thank you and have a nice day! ^^   ")