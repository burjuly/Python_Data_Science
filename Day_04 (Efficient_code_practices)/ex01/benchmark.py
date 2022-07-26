#!/usr/bin/env python3
import timeit

def list_loop(lst):
    new_list = []
    for i in lst:
        if i[-10::] == '@gmail.com':
            new_list.append(i)
    return(new_list)

def list_comp(lst):
    new_list = [i for i in lst if i[-10::] == '@gmail.com']
    return(new_list)

def select(x):
    if x[-10::] == '@gmail.com':
        return x

def list_map(lst):
    new_list = list(map(select, lst))
    return(new_list)

def create_list():
    new_list = []
    emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com']
    i = 0
    while i < 5:
        for l in emails:
            new_list.append(l)
        i += 1
    return new_list

def arrange_time(time_loop, time_comp, time_map):
    d = {'loop': time_loop, 'list comprehension': time_map, 'map': time_map}
    list_d = list(d.items())
    list_d.sort(key=lambda i: i[1])
    return(list_d)

def choose_var():
    lst = create_list()
    time_loop = timeit.timeit(lambda: list_loop(lst), number=90000000)
    time_comp = timeit.timeit(lambda: list_comp(lst), number=90000000)
    time_map = timeit.timeit(lambda: list_map(lst), number=90000000)
    list_d = arrange_time(time_loop, time_comp, time_map)
    print(f"it is better to use a {list_d[0][0]}")
    print(f"{time_loop} vs {time_comp} vs {time_map}")

if __name__ == '__main__':
    choose_var()