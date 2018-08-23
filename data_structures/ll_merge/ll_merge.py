from .linked_list import LinkedList

# def ll_merge(ll_1, ll_2):
#     cur1 = ll_1.head
#     cur2 = ll_2.head
#     ll_3 = LinkedList()
#     while cur1 and cur2:
#         if cur1._next:
#             ll_3.append(cur1.val)
#             cur1 = cur1._next

#         if cur2._next:
#             ll_3.append(cur1.val)
#             cur2 = cur2._next
#     return ll_3

def merge_lists(h1, h2):
    if h1 is None:
        return h2
    if h2 is None:
        return h1

    if (h1.value < h2.value):
        h1.next = merge_lists(h1.next, h2)
        return h1
    else:
        h2.next = merge_lists(h2.next, h1)
        return h2
