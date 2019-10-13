#!/usr/bin/python3

def func(arr,n, x):
	
	for i in range(0,n):
		if (arr[i] == x):
			return i
	return -1




arr =[1,2,3,5,6]

x=10
n = len(arr)

result = func(arr, n,x)
if(arr[mid] == x):
            return mid

        #if not and value is greater than mid value ignore left part and increase its value 
        elif arr[mid] < x:
            l = mid+1


        # if value less than mid value ignore right part and decrease right value by -1
        else: 
            r= mid-1
       

else:
	print("value found here:",result)
