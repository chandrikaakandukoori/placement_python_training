
 


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:


    def __init__(self):
        self.head = None

    def insert_begin(self, data):
        nn = Node(data)

        if self.head is None:
            self.head = nn
            return

        nn.next = self.head
        self.head = nn

    def insert_end(self, data):
        nn = Node(data)

        if self.head is None:
            self.head = nn
            return

        temp = self.head

        while temp.next is not None:
            temp = temp.next

        temp.next = nn

    def insert_at_any_pos(self, pos, data):
        if pos <= 0:
            print("Invalid position")
            return

        if pos == 1:
            self.insert_begin(data)
            return

        temp = self.head
        i = 1

        while i < pos - 1 and temp is not None:
            temp = temp.next
            i += 1

        if temp is None:
            print("Insufficient Elements")
            return

        nn = Node(data)
        nn.next = temp.next
        temp.next = nn

    def count(self):
        temp = self.head
        c = 0

        while temp is not None:
            c += 1
            temp = temp.next

        return c

    def add_at_mid(self, data):
        n = self.count()
        mid = (n // 2) + 1
        self.insert_at_any_pos(mid, data)

    def delete_begin(self):
        if self.head is None:
            print("No Elements in the list")
            return

        self.head = self.head.next

    def delete_end(self):
        if self.head is None:
            print("No Elements in the list to delete")
            return

        if self.head.next is None:
            self.head = None
            return

        temp = self.head
        prev = None

        while temp.next is not None:
            prev = temp
            temp = temp.next

        prev.next = None

    def delete_any_pos(self, pos):
        if pos <= 0:
            print("Invalid Position")
            return

        if pos == 1:
            self.delete_begin()
            return

        temp = self.head
        prev = None
        i = 1

        while i < pos and temp is not None:
            prev = temp
            temp = temp.next
            i += 1

        if temp is None:
            print("Insufficient elements")
            return

        prev.next = temp.next

    def delete_mid(self):
        n = self.count()
        mid = (n // 2) + 1
        self.delete_any_pos(mid)

    def search(self,target):
        pos=1
        temp=self.head
        while temp is not None:
            if temp.data ==target:
                return pos
            temp=temp.next
            pos+=1
        return -1
    
    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def display(self):
        if self.head is None:
            print("List is empty")
            return
        temp = self.head
        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")
        


ll = SinglyLinkedList()

while 1:

    print("\n1. Insert at Beginning")
    print("2. Insert at End")
    print("3. Insert at Any Position")
    print("4. Insert at Middle")
    print("5. Delete at Beginning")
    print("6. Delete at End")
    print("7. Delete at Any Position")
    print("8. Delete at Middle")
    print("9. Count")
    print("10. Search")
    print("11. Display")
    print("12. Reverse") 
    print("13.Exit")

    choice = int(input("Enter your choice: "))

    match choice:

        case 1:
            data = (input("Enter data: "))
            ll.insert_begin(data)

        case 2:
            data = (input("Enter data: "))
            ll.insert_end(data)

        case 3:
            pos = int(input("Enter position: "))
            data = input("Enter data: ")
            ll.insert_at_any_pos(pos, data)

        case 4:
            data = input("Enter data: ")
            ll.add_at_mid(data)

        case 5:
            ll.delete_begin()

        case 6:
            ll.delete_end()

        case 7:
            pos = int(input("Enter position: "))
            ll.delete_any_pos(pos)


        case 8:
            ll.delete_mid()

        case 9:
            print("Number of elements:", ll.count())

        case 10:
            target=input("enter the song to be searched for:")
            v=ll.search(target)
            if v== -1:
                print("target not in list")
            else:
                print("target found at position:",v)
            
        case 11:
            ll.display()

        case 12:
            ll.reverse()
            print("List reversed successfully")
        case 13:
            print("Program terminated")
            break

        case _:
            print("Invalid choice")
