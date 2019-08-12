class node:
    def __init__(self, data, next=None, prev=None):

        self.data = data
        self.next =next 
        self.prev = prev


class doubleLinklist:

    def __init__(self):

        self.head = None

    

    def push(self, new_data):

        new_node = node(new_data)

        new_node.next = self.head
        new_node.prev = None


        if self.head is not None:

            self.head.prev = new_node
        
        self.head = new_node


    
    def append(self, new_data):

        new_node = node(new_data)

        curr = self.head

        if self.head is None:

            new_node.prev = None 
            self.head = new_node
            return
        
        while(curr.next is not None ):
            curr = curr.next
        
        curr.next =  new_node

        new_node.prev = curr


    def printArray(self):
        curr = self.head
        while(curr):
            print(curr.data)
            prev = curr
            curr =  curr.next


if __name__ == "__main__":


    dll = doubleLinklist()
    dll.append(3)
    dll.append(4)
    dll.printArray()
