#User function template for Python

class Solution:
    #Function to partition the array around the range such 
    #that array is divided into three parts.
	def threeWayPartition(self, arr, a, b):
	    # code here 
        n = len(arr)
        
        low = 0
        mid = 0
        high = n - 1
        
        while mid <= high:
            
            # if element < a
            if arr[mid] < a:
                arr[low], arr[mid] = arr[mid], arr[low]
                low += 1
                mid += 1
            
            # if element > b
            elif arr[mid] > b:
                arr[mid], arr[high] = arr[high], arr[mid]
                high -= 1
            
            # if element btw a and b
            else:
                mid += 1
        
        return arr
	    
