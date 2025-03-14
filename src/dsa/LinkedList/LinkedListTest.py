from src.dsa.LinkedList.LinkedList import LinkedList

def linked_list_test1():
    first_linked_list = LinkedList()
    print(f"The head of an empty linked list : {first_linked_list.head}")

    first_linked_list.insert_at_beginning(4)
    first_linked_list.insert_at_beginning(7)
    first_linked_list.insert_at_end(2)
    first_linked_list.insert_at_end(1)

    current_node = first_linked_list.head
    while current_node:
        print(current_node.data, end=" -> ")
        current_node = current_node.next

    print(f"\nDoes this linked list contain the number 7 ? {first_linked_list.does_contain(7)}")
    print(f"Does this linked list contain the number 17 ? {first_linked_list.does_contain(17)}")


if __name__ == '__main__':
    linked_list_test1()
