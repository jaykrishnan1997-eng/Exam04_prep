# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    py_sliding_window_maximum.py                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jkrishna <jkrishna@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/11/10 13:16:32 by jkrishna          #+#    #+#              #
#    Updated: 2026/11/10 13:30:37 by jkrishna         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def max_list(arr: list[int]):
    max_value = -9999999999
    for i in arr:
        if i > max_value:
            max_value = i
    return max_value

def sliding_window_maximum(nums: list[int], k: int) -> list[int]:
    i = 0
    result = []
    if k <= 0 or k > len(nums) or nums == []:
        return result
    for i in range(0, len(nums) - k + 1):
        win = []
        for j in range(i, i + k):
            win.append(nums[j])
        result.append(max_list(win))
    return result

if __name__ == "__main__":
    print(sliding_window_maximum([1, 3, -1, -3, 5, 3, 6, 7], 3))  # Expected: [3, 3, 5, 5, 6, 7]
    print(sliding_window_maximum([1, 2, 3, 4, 5], 2))  # Expected: [2, 3, 4, 5]
    print(sliding_window_maximum([5, 4, 3, 2, 1], 1))  # Expected: [5, 4, 3, 2, 1]
    print(sliding_window_maximum([1, 2, 3], 3))  # Expected: [3]
    print(sliding_window_maximum([1, 2, 3], 4))  # Expected: []
    print(sliding_window_maximum([], 2))  # Expected: []
    print(sliding_window_maximum([1, 2, 3], 0))  # Expected: []