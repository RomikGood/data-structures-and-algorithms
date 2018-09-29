def selection(lst):
    length = len(lst)
    for i in range(0, length-1):
        cur_min_ind = i
        for j in range(i+1, length):
            if lst[j] < lst[cur_min_ind]:
                cur_min_ind = j
        lst[i], lst[cur_min_ind] = lst[cur_min_ind], lst[i]
    return lst
               



