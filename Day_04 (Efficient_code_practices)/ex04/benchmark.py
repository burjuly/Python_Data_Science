#!/usr/bin/env python3
import timeit
import random
from collections import Counter

def create_dict(lst):
    dic = {}
    for i in lst:
        if i in dic:
            dic[i] = dic[i] + 1
        else:
            dic.update({i: 1})
    return (dic)

def dic_counter(lst):
    dic = dict(Counter(lst))
    return(dic)

def select_top(lst):
    dic = {}
    new_dic = {}
    dic = create_dict(lst)
    list_d = list(dic.items())
    list_d.sort(key=lambda i: i[1])
    list_top = list_d[-10::]
    for n in list_top:
        new_dic.update({n[0] : n[1]})
    return(new_dic)

def select_top_counter(lst):
    top = dict(Counter(lst).most_common(10))
    return(top)

def choose_counter():
    lst = [random.randint(0, 100) for i in range(0, 1000000)]
    time_my_function = timeit.timeit(lambda: create_dict(lst))
    time_counter = timeit.timeit(lambda: dic_counter(lst))
    time_my_top = timeit.timeit(lambda: select_top(lst))
    time_counters_top = timeit.timeit(lambda: select_top_counter(lst))
    print(f'my function: {time_my_function}')
    print(f'Counter:  {time_counter}')
    print(f'my top:  {time_my_top}' )
    print(f'Counter\'s top: {time_counters_top}')

if __name__ == '__main__':
    choose_counter()