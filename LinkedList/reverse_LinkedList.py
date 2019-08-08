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

    
    # REVERSE LINKEDLIST

    def reverselist(self):
        
        # new pointer 
        prev=None

        # head to current
        current= self.head

    # loop till current value is NONE
        while(current):
            next = current.next

            current.next = prev

            prev=current

            current=next    

        self.head=prev


    def printList(self):

        temp=self.head
        while(temp):
            print(temp.data)

            temp = temp.next



if __name__=="__main__":

    llist=LinkedList()

    llist.push(2)
    llist.push(3)
    llist.push(4)
    llist.push(5)
    llist.push(6)

    llist.printList()

    # calling function to reverse linked list
    llist.reverselist()
    print("reverse list")
    llist.printList()
