# TIME COMPLEXITY OF INSERTAFTER IS [ O(n)] AS IT DOES CONSTANT  AMOUNT OF WORK

# it involves 5 steps

def afterinsert(self, prev_node, new_data):
    

    # checkif node is present or node
    if prev_node == None:
        print("Given previous node should be a linkedlist:")
        return
    
    new_data = Node(new_data)

    new_data.next = prev_node.next

    prev_node.next = new_node



