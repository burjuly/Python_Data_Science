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

def create_list():
    new_list = []
    emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com']
    i = 0
    while i < 5:
        for l in emails:
            new_list.append(l)
        i += 1
    return new_list

def choose_var():
    lst = create_list()
    time_loop = timeit.timeit(lambda: list_loop(lst), number=90000000)
    time_comp = timeit.timeit(lambda: list_comp(lst), number=90000000)
    if time_comp < time_loop:
        print('it is better to use a list comprehension')
    else:
        print('it is better to use a loop')
    print(f"{time_loop} vs {time_comp}")

if __name__ == '__main__':
    choose_var()