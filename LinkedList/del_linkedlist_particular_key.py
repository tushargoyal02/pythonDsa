
'''
IF DELETE IS ROOT SIMPLY REMOVE THE NODE
OTHERWISE LOOP TO THE PREVIOUS NODE [RUN LOOP  " POSITION-1  "]
'''
# TO DELETE KEY AT A PARTICULAR LOCATION



'''
1   CHECK LINK LIST PRESENT
2   IF PRESENT CHECK WHETHER PRESENT AT FIRST OR OTHER
'''
class node:
    def __init__(self, data):
        self.data = data
        self.next=None

class Linkedlist:

    def __init__(self):
        self.head=None

    
    def push(self, new_data):


        new_node = node(new_data)

        # new head
        new_node.next=self.head
        self.head = new_node


    def delete1(self, position):

        # checking whether link list is present or not
        if self.head==None:
            return
        
        temp = self.head

        # if element found on the 0 position
        if position==0:
            # assign new head as next node 
            self.head = temp.next
            temp = None
            return
        
        # if not then iterate to the last node before location
        for i in range(position -1):
            temp = temp.next
            # if the temp is found none break up from loop
            if temp is None:
                break
        
        if temp is None:
            return

        if temp.next is None:
            return

        # HERE [temp.next is the node to be deleted]

        # taking address of delete node address to next1
        next1 = temp.next.next

        # making temp as null
        temp.next = None

        temp.next = next1



    def printArray(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next


        
if __name__=="__main__":

    llist = Linkedlist()
    llist.push(2)
    llist.push(3)
    llist.push(4)

    print("before delete")
    llist.printArray()
    llist.delete1(1)

    print("after del")
    llist.printArray()        



