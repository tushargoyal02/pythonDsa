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


    def search(self, key):

        curr = self.head
        
        while(curr):
            if(curr.data==key):
                return True
            curr = curr.next

        #if data not found
        return False

    
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

if __name__=="__main__":

    llist=Linkedlist()
    llist.push(2)
    llist.push(3)
    llist.printList()

    out=llist.search(3)
    #print(out)
    if out==True:
        print("value found")

    else:
        print("Node with the given value not found")                    