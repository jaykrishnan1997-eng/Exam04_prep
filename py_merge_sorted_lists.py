# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    py_merge_sorted_lists.py                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jkrishna <jkrishna@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/10/31 11:52:28 by jkrishna          #+#    #+#              #
#    Updated: 2026/10/31 12:02:25 by jkrishna         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def sort(list):
    for _ in range(0, len(list)):
        for i in range(0, len(list) - 1):
            if list[i] > list[i + 1]:
                list[i], list[i + 1] = list[i + 1], list[i]
    return list


def merge_sorted_lists(lists: list[list[int]]) -> list[int]:
    result = []
    for list in lists:
        if len(lists) == 1:
            return list
        for i in list:
            # if i not in result:
            result.append(i)

    return sort(result)


if __name__ == "__main__":
    print(merge_sorted_lists([[1, 3, 5], [2, 4, 6]]))  # Expected: [1, 2, 3, 4, 5, 6]
    print(merge_sorted_lists([[1, 5, 9], [2, 3, 8], [4, 6, 7]]))  # Expected: [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(merge_sorted_lists([[5], [1, 3], [2, 4]]))  # Expected: [1, 2, 3, 4, 5]
    print(merge_sorted_lists([[1, 1, 2], [2, 3, 3]]))  # Expected: [1, 1, 2, 2, 3, 3]
    print(merge_sorted_lists([[], [1, 2, 3]]))  # Expected: [1, 2, 3]
    print(merge_sorted_lists([[]]))  # Expected: []
    print(merge_sorted_lists([[-5, -1, 0], [-3, 2, 4]]))  # Expected: [-5, -3, -1, 0, 2, 4]
    print(merge_sorted_lists([[10], [10], [10]]))  # Expected: [10, 10, 10]