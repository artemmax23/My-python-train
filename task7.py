def merge_sorted_lists(lst1: list, lst2: list) -> list:
    i = j = 0
    merge_list = []
    list_length1 = len(lst1)
    list_length2 = len(lst2)
    
    while (i < list_length1) and (j < list_length2):
         if (lst1[i] <= lst2[j]):
             merge_list.append(lst1[i])
             i += 1
         else:
             merge_list.append(lst2[j])
             j += 1
     
    merge_list.extend(lst1[i:])
    merge_list.extend(lst2[j:])
              
    return merge_list
         
print(merge_sorted_lists([1, 3, 5], [2, 4, 6]))  # [1, 2, 3, 4, 5, 6]
print(merge_sorted_lists([1, 2, 3], []))         # [1, 2, 3]
print(merge_sorted_lists([], []))                # []