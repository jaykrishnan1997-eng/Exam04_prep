# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    py_array_rotation_detector.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jkrishna <jkrishna@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/10/30 12:11:36 by jkrishna          #+#    #+#              #
#    Updated: 2026/10/30 12:26:42 by jkrishna         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def swap(array: list) -> list:
    i = 0
    new_array = []
    for _ in range(0, len(array)):
        new_array.append(0)
    while(i < len(array)):
        new_array[i] = array[(i + 1)%len(array)]
        i += 1
    return new_array

def array_rotation_detector(arr1: list, arr2: list) -> bool:
    j = 0
    if arr1 == arr2:
        if arr1 == []:
            return True
        else:
            return False

    if len(arr1) != len(arr2):
        return False

    while(j < len(arr1)):
        if arr1 == arr2:
            return True
        else:
            arr2 = swap(arr2)
        j += 1
    return False

if __name__ == "__main__":
    print(array_rotation_detector([1, 2, 3, 4, 5], [4, 5, 1, 2, 3]))
    print(array_rotation_detector([1, 2, 3, 4, 5], [5, 1, 2, 3, 4]))
    print(array_rotation_detector([1, 2, 3], [3, 2, 1]))
    print(array_rotation_detector([1, 2], [1, 2, 3]))
    print(array_rotation_detector([], []))