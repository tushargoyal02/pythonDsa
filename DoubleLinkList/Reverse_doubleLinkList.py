# node of doubly link list
class node:
    
    # Constructor to create a new node 
    def __init__(self, data, prev=None, next=None):

        self.data = data

        self.next = next
        self.prev = prev


class doublelist:
     # Constructor for empty Doubly Linked List 
    def __init__(self):

        self.head = None

     # Given a reference to the head of a list and an 
    # integer,inserts a new node on the front of list 
    def push(self, new_data):

        new_node = node(new_data)

        new_node.next = self.head

        new_node.prev =  None

        if (self.head is not None):

            self.head.prev = new_node

        self.head = new_node    

    # function to reverse

    def reverse(self):
        temp = None
        curr = self.head

        while(curr):

            # assign current previous value to temp
            temp = curr.prev

            # swap the direction by assigning the cureent previous part as next
            curr.prev = curr.next

            # assign the save value in temp to the next of node
            curr.next = temp

            # making current as value in current previous part
            curr = curr.prev

        # changing the head part in last
        if temp is not None:
            self.head = temp.prev






    # Function to print all LinkList 
    def printList(self):

        curr = self.head

        while(curr):
            print(curr.data)
            prev = curr
            curr = curr.next


if __name__ == "__main__":

    dll = doublelist()
    dll.push(3)
    dll.push(2)
    dll.printList()

    print("reversed")
    dll.reverse()
    dll.printList()
    