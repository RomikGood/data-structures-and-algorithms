def binary_search(arr, key):
    start = 0
    end = len(arr) - 1
    
    while start <= end:
 
        mid = (start + end) // 2
         
        # Check if key == mid
        if arr[mid] == key:
            return mid
            
 
        # If key is greater, ignore left half
        elif arr[mid] < key:
            start = mid + 1
 
        # If key is smaller, ignore right half
        elif arr[mid] > key:
            end = mid - 1
        
    return -1
     

    
# arr = [1,4,6,8,14,45]
# key = 11
# print(binary_search(arr, key))