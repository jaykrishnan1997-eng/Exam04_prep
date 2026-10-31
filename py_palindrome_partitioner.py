# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    py_palindrome_partitioner.py                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jkrishna <jkrishna@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/10/31 12:07:34 by jkrishna          #+#    #+#              #
#    Updated: 2026/10/31 12:49:25 by jkrishna         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def rev_test(s):
    for i in range(0, len(s)):
        if s[i] != s[len(s) - 1 - i]:
            return False
    return True


def reverse(s):
    new_s = ''
    for i in s:
        new_s = i + new_s
    return new_s


def palindrome_partitioner(s: str) -> int:
    cuts = 0
    limit = len(s)
    list = []
    if rev_test(s):
        return 0
    while i < 0:
        if reverse(s[i:len(s) - 1 - i]) == s[:limit]:
            return cuts
        else:
            cuts += 1
            limit -= 1
    return cuts

if __name__ == "__main__":
    print(palindrome_partitioner("aab"))  # Expected: 1
    print(palindrome_partitioner("aba"))  # Expected: 0
    print(palindrome_partitioner("abc"))  # Expected: 2