class Node:
    def __init__(self, data):
        #assign data
        self.data = data
        # initalize next as null
        self.next = None

class LinkedList:
    def __init__(self):
        self.head  = None


    def printList(self):

        temp = self.head 
        while (temp): 
            print(temp.data) 
            temp = temp.next

if __name__ == '__main__':

    # creating an empty list
    llist = LinkedList()

    #creating the first head node
    llist.head = Node(1)
    
    #second note with data =2
    second = Node(2)
    third = Node(3)

    llist.head.next = second
    second.next = third

    llist.printList()
