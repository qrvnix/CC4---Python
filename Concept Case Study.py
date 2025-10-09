class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def choose():
    print(f"Select which list you want to create: \n 1 - Singly\n 2 - Singly Circular\n 3 - Doubly\n 4 - Doubly Circular")
    choice = int(input(f"Enter your choice (1-4): "))
    return choice

def choose_operation():
    print(f"\nSelect what operation to do: \n 1 - Traversal\n 2 - Retrieval\n 3 - Insertion\n 4 - Deletion")
    choice = int(input(f"Enter your choice (1-4): "))
    return choice

user_choice = choose()
if user_choice == 1:
    print(f"\n                  SINGLY LINKED LIST                  \n")
    Head_data = str(input("\nEnter head's data: "))
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
        question = str(input("\nDo you want to link another data?: "))

    user_operation = choose_operation()
    if user_operation == 1:
        print(f"\n                  SINGLY LINKED LIST: Traversal                  \n")
        Curr = Head
        print(f"\nLinked List Data:\n")
        while Curr is not None:
            print(Curr.data, end=" ")
            Curr = Curr.next