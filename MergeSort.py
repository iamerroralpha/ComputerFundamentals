# Python program for implementation of MergeSort 
def mergeSort(arr): 
    if len(arr) >1: 
        mid = len(arr)//2 #Finding the mid of the array 
        L = arr[:mid] # Dividing the array elements  
        R = arr[mid:] # into 2 halves 
  
        mergeSort(L) # Sorting the first half 
        mergeSort(R) # Sorting the second half 
  
        i = j = k = 0
          
        # Copy data to temp arrays L[] and R[] 
        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                arr[k] = L[i] 
                i+=1
            else: 
                arr[k] = R[j] 
                j+=1
            k+=1
          
        # Checking if any element was left 
        while i < len(L): 
            arr[k] = L[i] 
            i+=1
            k+=1
          
        while j < len(R): 
            arr[k] = R[j] 
            j+=1
            k+=1
    return arr
import time
import random
print('Merge Sort')
def mergeSortComp(n):
	arrS = []
	arrR = []
	arrRdm = []
	for i in range(n):
		arrS.append(i);
		arrRdm.append(random.randint(0,n))
	arrR = arrS[::-1]

	print('Elapsed time for an array of ' +str(n) + ' elements')
	start = time.time()
	Sarray 	= mergeSort(arrS)
	end = time.time()
	print('\t Sorted array '+ str(end - start) + ' s.', end='')
	start = time.time()
	Sarray 	= mergeSort(arrR)
	end = time.time()
	print('\t Reversed array '+ str(end - start) + ' s.', end='')
	start = time.time()
	Sarray 	= mergeSort(arrRdm)
	end = time.time()
	print('\t Random array '+ str(end - start) + ' s.')

mergeSortComp(100)
mergeSortComp(1000)
mergeSortComp(10000)
mergeSortComp(100000)
mergeSortComp(1000000)
mergeSortComp(10000000)


