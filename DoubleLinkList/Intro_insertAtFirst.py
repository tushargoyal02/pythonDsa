
# addding a new _node

class node:
    def __init__(self, data=None, prev=None, next=None):

        # it is the reference to next node in DLL
        self.next = next
        self.data = data

        # refer to prev node in double link list
        self.prev=prev


class DoubleLinkList:

    def __init__(self):

        self.head = None

    def push(self,new_data):
        

        # adding new node 

        new_node = node(new_data)

        new_node.next= self.head
        new_node.prev=None

    # checking the head of the previous node

        if self.head is not None:

            self.head.prev = new_node

        # making a new head as new_node
        self.head = new_node




    def printList(self):

        node= self.head
        while(node is not None):

            print(node.data)
            last = node
            node = node.next


if __name__ == "__main__":


    dll = DoubleLinkList()

    dll.push(2)
    dll.push(3)
    dll.printList()





