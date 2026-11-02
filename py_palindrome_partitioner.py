# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    py_palindrome_partitioner.py                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jkrishna <jkrishna@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/10/31 12:07:34 by jkrishna          #+#    #+#              #
#    Updated: 2026/11/02 10:14:28 by jkrishna         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def rev_test(s):
    i = 0
    while i < len(s) // 2:
        if s[i] != s[len(s) - 1 - i]:
            return False
        i += 1
    return True


def palindrome_partitioner(s: str) -> int:

    leng = len(s)

    if rev_test(s):
        return 0
    # dp is minimum cuts required for first i characters
    dp = [float('inf')] * (leng + 1)
    dp[0] = -1

    for i in range(1, leng + 1):
        for j in range(i):
            if rev_test(s[j:i]):
                if (dp[j] + 1) < dp[i]:
                    dp[i] = dp[j] + 1
    return dp[leng]


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