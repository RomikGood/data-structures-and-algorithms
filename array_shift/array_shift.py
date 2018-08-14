'''takes value and inserts in the middle of the array
    '''
def insert_shift_array(arr, val):
    ind = len(arr)//2 + len(arr)%2
    return ((arr[:ind]+ [val] + arr[ind:]))

# insert_shift_array([1,2,3,4], 5)