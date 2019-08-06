class node:

    def __init__(self, data):

        self.data = data
        self.next = None

class Linkedlist:

    def __init__(self):

        self.head=None


    def push(self, new_data):

        new_node = node(new_data)

        new_node.next = self.head

        self.head = new_node

# TO DELETE A NODE IN A LINKEDLIST
    def dele(self, key):

        #head value ink temp
        temp = self.head

        # checking whether temp is not null 
        if(temp is not  None):

            # if true check whether key is same or not
            if (temp.data == key):

                # the new head will be new_node next
                self.head = temp.next
                # declaring the delete node as null
                temp=None
                return 
        while(temp is not None):
            if(temp.data == key):
                break        
                # will keep the next of current node into prev
            prev = temp

            # new temp consist of next address of node
            temp = temp.next

        if(temp ==None):
            return
        
        prev.next = temp.next


    #printing array
    def printArray(self):
        # head value in temp
        temp = self.head

        # loop till temp value is present
        while(temp):
            # printing the data
            print(temp.data)
            temp = temp.next


if __name__ == "__main__":

    llist = Linkedlist()

    llist.push(2)
    llist.push(3)
    llist.push(4)
    print("Linkedlist before delete:","\n")
    llist.printArray()
    print("after delete:","\n")
    llist.dele(3)
    llist.printArray()





        


