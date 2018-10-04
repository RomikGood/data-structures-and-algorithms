def radix_sort(arr):
    """function return a different array
    """
    if len(arr) < 2:
        return arr

    for number in range(len(str(max(arr)))):
        # for the length of the biggest number
        buckets = [[] for i in range(10)]
        for item in arr:
            single_num = item % (10 ** (number + 1))
            
            index = single_num // (10 ** number)
            # print(single_num)
            # print(index)
            buckets[index].append(item)
        result = []
        for bucket in buckets:
            for item in bucket:
                result.append(item)
        
    return result

# l = [5,4,77,56,67]
# print(radix_sort(l))