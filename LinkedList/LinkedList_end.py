# append data at the last


#    TIME COMPLEXITY IS [ O(n) ] where n is the number of nodes in linked list.



def append(self, new_data):


    new_node = Node(new_data)

    # if linkedlist is empty  then make new node as head 
    if self.head=None:
        self.head = new_node
        return

    
    # if not iterate over till last element


    # putting first head into last
    last = self.head

    # checking condition till the last next
    while(last.next):
        last = last.next

    last.next = new_node

    