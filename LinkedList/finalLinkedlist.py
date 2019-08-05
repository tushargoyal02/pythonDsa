class Node:

    def __init__(self, data):
        self.data =data
        self.next=None

class LinkedList:

    def __init__(self):

        self.head=None

    ##  1.
    # starting of linkedlist
    def push(self, new_data):

        new_node = Node(new_data)

        new_node.next = self.head

        self.head = new_node

    ##  2.
    # at mid position linkedlist

    def after(self, prev_node, new_data):


        #checking if the prev_node is   exist or not
        if prev_node.next == None:
            print("No LinkedList found")
            return
        
        
        new_node = Node(new_data)

        # assign previous node next to the new_data node [next]
        new_node.next = prev_node.next

        #given head of new to next of previous
        prev_node.next = new_node  

    ##  3.
    # appending the node at the last


    def append(self, new_data):

        new_node = Node(new_data)

        # checking if node is empty or not
        if self.head==None:
            self.head=new_node

        # if condition is false iterate to last element of the list
        last = self.head
        while(last.next):
            last = last.next

        
    ## 4 
    # function to print the linked list
    def printList(self):
            # taking head node to temp
            temp = self.head

            # loop till we have elements in temp
            while(temp):
                print(temp.data)
                temp = temp.next


# code execution to start

if __name__ == "__main__":
    
    llist = LinkedList()

    llist.append(6)

    llist.push(2)

    llist.push(3)

    llist.after(llist.head.next, 8)


    #printing the list

    llist.printList()