class node:
    def __init__(self, data):
        self.data= data
        self.next = None

class Linkedlist:
    def __init__(self):

        self.head = None
        

    def push(self, new_data):

        new_node =  node(new_data)

        new_node.next = self.head
        self.head = new_node

    
    def totalCount(self):
        temp = self.head
        val =0
        while(temp):
            val +=1
            temp= temp.next
        return val
    
    def printArray(self):

        temp = self.head

        while(temp):
            print(temp.data)
            temp = temp.next

if __name__ == "__main__":

    llist = Linkedlist()

    llist.push(2)
    llist.push(3)
    llist.push(4)
    print("Linkedlist:")
    llist.printArray()
    output=llist.totalCount()

    print("total node:",output)
