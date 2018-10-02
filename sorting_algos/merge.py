def merge_sort(Arr, first, last):
    if first < last:
        middle = (first + last) // 2
    # print(first, middle, last)

        merge_sort(Arr, first, middle)
        merge_sort(Arr, middle + 1, last)
        merge(Arr, first, middle+1, last)


def merge(Arr, first, middle, last):
  
    L = Arr[first:middle]
    # print(L)
    R = Arr[middle:last+1]
    # print(R)
    L.append(99999)
    R.append(99999)
    i = j = 0

    for k in range(first, last+1):
        if L[i] < R[j]:
            Arr[k] = L[i]
            i += 1
        else:
            Arr[k] = R[j]
            j += 1


arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
merge_sort(arr, 0, len(arr)-1)
# print(arr)