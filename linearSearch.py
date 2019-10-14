#!/usr/bin/python3
class doubleLinklist:

    def __init__(self):

        self.head = None

    

    def push(self, new_data):

        new_node = node(new_data)

        new_node.next = self.head
        new_node.prev = None


        if self.head is not None:

            self.head.prev = new_node
        
        self.head = new_node
n = len(arr)

result = func(arr, n,x)

if (result==-1):
	print("value",x," not found in array")

else:
	print("value found here:",result)
