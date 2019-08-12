
# INSERING A NEW NODE AFTER A GIVEN NODE IN DOUBLY LINK LIST !

class node:
    def __init__(self, data, prev=None, next=None):


        self.data =data
        self.next=next
        self.prev=prev

class DoubleLinkList:

    def __init__(self):

        self.head = None


    def push(self, new_data):

        new_node = node(new_data)

        new_node.next= self.head
        new_node.prev = None

        if self.head is not None:
            self.head.prev = new_node

        self.head = new_node


    
# --------------------------------------------------------------------------------
  # INSERTING A NEW NODE AFTER A GIVEN NODE
  
    def insertAfter(self, prev_node, new_data):

        if prev_node is None:
            print("Prev Node is not found:")
            return
        
        # making new node
        new_node = node(new_data)

        # next of new_node as prev node next value
        new_node.next = prev_node.next

        # prev node next value consist of new Node value
        prev_node.next = new_node


        # New Node prev value consit of prev_node value
        new_node.prev = prev_node



        #   CHANGING THE PREV OF THE LASTED NODE IN DOUBLE LINK LIST

        if new_node.next is not None:

            new_node.next.prev = new_node

# ------------------------------------------------------------------------------------


    def printArray(self):

        curr = self.head
        while(curr):
            print(curr.data)
            prev = curr

            curr = curr.next

if __name__ == "__main__":

    dll = DoubleLinkList()

    dll.push(3)
    dll.push(24)

    dll.printArray()

    # inserting node after the head of next
    dll.insertAfter(dll.head.next,6)

    print("new doubly link list")

    dll.printArray()    





