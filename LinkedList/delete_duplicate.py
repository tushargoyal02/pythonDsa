class node:

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):

        self.head=None


    def push(self, new_data):

        new_node = node(new_data)

        new_node.next=self.head

        self.head = new_node

    
    #    DUPLICATE REMOVE FUNCTION
    def duplicateremove(self):
        temp=self.head

        # checking if starting is null then return
        if(temp is None):
            return

        # make new loop until next is present
        while(temp.next):
            if(temp.data == temp.next.data ):

                #assign next values address 
                new = temp.next.next
                #making the current node value as 0
                temp.next = None

                # assign new node address to current next
                temp.next = new

            else:

                temp=temp.next
        return self.head

    def printList(self):

        temp=self.head
        while(temp):
            print(temp.data)

            temp = temp.next

if __name__ == "__main__":
    
    llist=LinkedList()
    llist.push(2)
    llist.push(3)
    llist.push(2)
    llist.push(2)
    llist.printList()

    llist.duplicateremove()
    print("after delete")
    llist.printList()

    

