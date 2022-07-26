#!/usr/bin/env python3
import timeit
import sys
from functools import reduce

def sq_loop(num):
    summ = 0
    for i in range(1, num + 1):
        summ = summ + i * i
    return(summ)

def sq_reduce(num):
    summ = reduce(lambda x, y: x + y ** 2, range(1, num + 1))
    return(summ)

def choose_function(func, num, count):
    if func == 'loop':
        print(timeit.timeit(lambda: sq_loop(num), number=count))
    else:
        print(timeit.timeit(lambda: sq_reduce(num), number=count))

def count_squares():
    if len(sys.argv) == 4:
        if sys.argv[1] in ['loop', 'reduce']:
            if sys.argv[2].isdigit() and sys.argv[3].isdigit():
                func = sys.argv[1]
                num = int(sys.argv[3])
                count = int(sys.argv[2])
                if num > 0 and count > 0:
                    choose_function(func, num, count)
            else:
                print('Value can be only number')
        else:
            print('Value can be only loop or reduce')
    else:
        print('Wrong number of arguments')

if __name__ == '__main__':
    count_squares()