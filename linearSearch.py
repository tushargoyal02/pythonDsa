#!/usr/bin/python3

def func(arr,n, x):
	
	for i in range(0,n):
		if (arr[i] == x):
			return i
	if(arr[mid] == x):
            return mid

        #if not and value is greater than mid value ignore left part and increase its value 
        elif arr[mid] < x:
            l = mid+1
	return -1




arr =[1,2,3,5,6]

x=10
n = len(arr)

result = func(arr, n,x)

if (result==-1):
	print("value",x," not found in array")

else:
	print("value found here:",result)
