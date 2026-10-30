# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    py_list_intersection_finder.py                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jkrishna <jkrishna@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/10/30 12:51:17 by jkrishna          #+#    #+#              #
#    Updated: 2026/10/30 13:09:38 by jkrishna         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def sort(array) -> list:
    for i in range(0, len(array) - 1):
        if array[i] > array[i + 1]:
            array[i], array[i + 1] = array[i + 1], array[i]
    return array

def list_intersection_finder(lists: list[list[int]]) -> list[int]:
    flag = 1
    result = []
    if lists == []:
        return []
    first_list = lists[0]
    for i in first_list:
        for list in lists:
            if i not in list:
                flag = 0
        if flag == 1:
            if i not in result:
                result.append(i)
        flag = 1
    return sort(result)


if __name__ == "__main__":
    print(list_intersection_finder([[1, 2, 3], [2, 3, 4], [2, 3, 5]]))  # Expected: [2, 3]
    print(list_intersection_finder([[1, 2, 3, 4], [2, 4, 6, 8], [4, 8, 12]]))  # Expected: [4]
    print(list_intersection_finder([[1, 1, 2, 3], [1, 2, 2, 3], [1, 2, 3, 3]]))  # Expected: [1, 2, 3]
    print(list_intersection_finder([[1, 2, 3], [4, 5, 6]]))  # Expected: []
    print(list_intersection_finder([]))  # Expected: []
    print(list_intersection_finder([[1, 2, 3], []]))  # Expected: []
    print(list_intersection_finder([[5]]))  # Expected: [5]