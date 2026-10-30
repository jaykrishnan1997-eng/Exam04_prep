# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    py_    print(constellation_mapper.py                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jkrishna <jkrishna@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/10/30 12:27:06 by jkrishna          #+#    #+#              #
#    Updated: 2026/10/30 12:40:39 by jkrishna         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def constellation_mapper(stars: list[tuple[int, int]], dim: int) -> list[str]:
    line = ''

    temp = []
    for r in range(0, dim):
        for c in range(0, dim):
            if (r,c) in stars:
                line += '*'
            else:
                line += '.'
        temp.append(line)
        line = ''

    return temp


if __name__ == "__main__":
    print(constellation_mapper([(0, 0), (1, 1), (2, 2)], 3))

    print(constellation_mapper([(1, 1), (0, 1), (2, 1), (1, 0), (1, 2)], 3))

    print(constellation_mapper([], 2))

    print(constellation_mapper([(0, 0), (0, 0), (1, 1)], 2))

    print(constellation_mapper([(0, 0), (5, 5)], 3))

    print(constellation_mapper([(1, 0), (1, 1), (1, 2)], 3))