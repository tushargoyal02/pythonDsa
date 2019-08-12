# DELETE NODE AT FIRST OR ANY POSITION

import gc

class node:

    def __init__(self, data, prev=None, next=None):

        self.data = data

        self.next = next
        self.prev = prev

    
class doublelist:
    def __init__(self):

        self.head = None


    def push(self, new_data):

        new_node = node(new_data)

        new_node.next = self.head

        new_node.prev =  None

        if (self.head is not None):

            self.head.prev = new_node

        self.head = new_node    


# MAIN FUNCTION TO DELETE ANY DATA
    def delete(self, dele):

        # checking whether the given node is present or not
        if self.head is None  or dele is None:
            print("no node are found or " +dele+ " is not found")

            return

        # if the head is the node to be deleted
        if self.head == dele:
            # assign new head as next node
            self.head = dele.next

        # check that next node should be null
        if dele.next is not None:
            # making next node prev as current node prev value
            dele.next.prev =  dele.prev

        # check whether current node previous node is empty or not
        if dele.prev is not None:

            dele.prev.next = dele.next

        gc.collect()
        

    def printArray(self):

        curr = self.head

        while(curr):
            print(curr.data)
            prev = curr
            curr = curr.next

if __name__ == "__main__":
    
    dll = doublelist()
    dll.push(2)
    dll.push(4)
    dll.push(5)
    dll.printArray()


    print("after delete")
    dll.delete(dll.head)
    
    # deleting the next node of head
    #dll.delete(dll.head.next)

    dll.printArray()