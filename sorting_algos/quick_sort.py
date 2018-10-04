def quick_sort(Arr):
    """
    """
    _helper(Arr, 0, len(Arr)-1)


def _helper(Arr, low, hi):
    """helper recursive function
    """
    if low < hi:
        p = partition(Arr, low, hi)
        _helper(Arr, low, p-1)
        _helper(Arr, p+1, hi)


def get_pivot(Arr, low, hi):
    """function gets a pivot
    """
    mid = (hi + low) // 2
    pivot = hi
    if Arr[low] < Arr[mid]:
        if Arr[mid] > Arr[hi]:
            pivot = mid
    elif Arr[low] < Arr[hi]:
        pivot = low
    return pivot


def partition(Arr, low, hi):
    """function gets pivot index and pivot values 
    and swaps the value of low and border indexes
    """
    pivotIndex = get_pivot(Arr, low, hi)
    pivotValue = Arr[pivotIndex]
    Arr[pivotIndex], Arr[low] = Arr[low], Arr[pivotIndex]
    border = low

    for i in range(low, hi+1):
        if Arr[i] < pivotValue:
            border += 1
            Arr[i], Arr[border] = Arr[border], Arr[i]
    Arr[low], Arr[border] = Arr[border], Arr[low]

    return (border)

