#   DELETING ALL NODE USING FUNCTION

'''
1   Make current head into new object
2   check while node is present
3   make current node next  to new variable
4   delete the current data
5   put the last fetch data to the previous while 
'''


class node:

    def __init__(self, data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

    
    def push(self, new_data):
        
        new_node = node(new_data)

        new_node.next = self.head

        self.head = new_node

## most import function to remove all nodes

##  delete all data using function
    def deleteall(self):
        current = self.head

        while(current):
            new_current = current.next
            
            del current.data

            current = new_current
        print("All data is removed")


# print all data

    def printList(self):

        temp = self.head

        while(temp):
            print(temp.data)
            temp = temp.next

if __name__=="__main__":

    llist = Linkedlist()
    llist.push(2)
    llist.push(3)
    llist.push(4)
    llist.push(5)

    print("before delete:")
    llist.printList()

    #print("after delete:")
    llist.deleteall()
    #llist.printList()

