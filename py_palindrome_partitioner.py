#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   py_palindrome_partitioner.py                         :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: jay-k <jay-k@student.42.fr>                  +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/10/31 12:07:34 by jkrishna            #+#    #+#            #
#   Updated: 2026/11/28 11:38:14 by jay-k              ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def _rev(arr):
    i = 0
    while i < len(arr) // 2:
        if arr[i] != arr[len(arr) - 1 - i]:
            return False
        i += 1
    return True


def palindrome_partitioner(s: str) -> int:
    l = len(s)
    if _rev(s) == 0:
        return 0
    df = [float('inf')] * (l + 1)
    df[0] = -1

    for i in range(0, l + 1):
        for j in range(j):
            if _rev(s[j:i]):
                if df[i] > df[j] + 1:
                    df[i] = df[j] + 1
 
    return df[l]



# def rev_test(s):
#     i = 0
#     while i < len(s) // 2:
#         if s[i] != s[len(s) - 1 - i]:
#             return False
#         i += 1
#     return True


# def palindrome_partitioner(s: str) -> int:

#     leng = len(s)

#     if rev_test(s):
#         return 0
#     # dp is minimum cuts required for first i characters
#     dp = [float('inf')] * (leng + 1)
#     dp[0] = -1

#     for i in range(1, leng + 1):
#         for j in range(i):
#             if rev_test(s[j:i]):
#                 if (dp[j] + 1) < dp[i]:
#                     dp[i] = dp[j] + 1
#     return dp[leng]


# def reverse(s):
#     new_s = ''
#     for i in s:
#         new_s = i + new_s
#     return new_s


# def palindrome_partitioner(s: str) -> int:
#     start = 0
#     stop = 1
#     leng = len(s)
#     accepted_list = []
#     temp = ""
#     if rev_test(s):
#         return 0

#     while start < leng:
#         while stop <= leng:
#             if rev_test(s[start:stop]):
#                 # print(s[start:stop])
#                 if len(temp) < len(s[start:stop]):
#                     temp = s[start:stop]
#             stop += 1
#         accepted_list.append(temp)
#         # breakpoint()
#         start += (len(temp))
#         if start >= leng:
#             break
#         stop = start + 1
#         temp = ""
#     return (len(accepted_list) - 1)


if __name__ == "__main__":
    # print(rev_test("aba"))
    print(palindrome_partitioner("aab"))  # Expected: 1
    print(palindrome_partitioner("aba"))  # Expected: 0
    print(palindrome_partitioner("abc"))  # Expected: 2
    print(palindrome_partitioner("aaba"))  # Expected: 1
    print(palindrome_partitioner("aabcc")) # 2