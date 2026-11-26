#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   py_list_intersection_finder.py                       :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: jay-k <jay-k@student.42.fr>                  +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/10/30 12:51:17 by jkrishna            #+#    #+#            #
#   Updated: 2026/11/26 11:49:05 by jay-k              ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def sort(arr):
    i = 0
    while i < len(arr) - 1:
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
            i = 0
        else:
            i += 1
    return arr


def list_intersection_finder(lists: list[list[int]]) -> list[int]:
    if ([] in lists or len(lists) == 0):
        return []
    result = []
    lists[0] = sort(lists[0])
    for i in lists[0]:
        if all(i in unit for unit in lists) and i not in result:
            result.append(i)
    return result


# def sort(array) -> list:
#     for i in range(0, len(array) - 1):
#         if array[i] > array[i + 1]:
#             array[i], array[i + 1] = array[i + 1], array[i]
#     return array

# def list_intersection_finder(lists: list[list[int]]) -> list[int]:
#     flag = 1
#     result = []
#     if lists == []:
#         return []
#     first_list = lists[0]
#     for i in first_list:
#         for list in lists:
#             if i not in list:
#                 flag = 0
#         if flag == 1:
#             if i not in result:
#                 result.append(i)
#         flag = 1
#     return sort(result)


if __name__ == "__main__":
    print(list_intersection_finder([[1, 2, 3], [2, 3, 4], [2, 3, 5]]))  #  Expected: [2, 3]
    print(list_intersection_finder([[1, 2, 3, 4], [2, 4, 6, 8], [4, 8, 12]]))  #  Expected: [4]
    print(list_intersection_finder([[1, 1, 2, 3], [1, 2, 2, 3], [1, 2, 3, 3]]))   #  Expected: [1, 2, 3]
    print(list_intersection_finder([[1, 2, 3], [4, 5, 6]]))  # Expected: []
    print(list_intersection_finder([]))  # Expected: []
    print(list_intersection_finder([[1, 2, 3], []]))  # Expected: []
    print(list_intersection_finder([[5]]))  # Expected: [5]