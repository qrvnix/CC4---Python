class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

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
    question = str(input("Do you want to link another data?: "))

Curr = Head
print(f"\nLinked List Data:\n")
while Curr is not None:
    print(Curr.data, end=" ")
    Curr = Curr.next