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


    def findSize(self):
        curr = self.head

        if curr is None:
            print("No node found")
            return
        count = 0

        while(curr is not None):
            count +=1
            curr= curr.next
        
        return count

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
    dll.push(1)
    dll.printArray()


    out=dll.findSize()
    print("size of nodes:", out)