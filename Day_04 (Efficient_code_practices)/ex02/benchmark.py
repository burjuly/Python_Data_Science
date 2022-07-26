#!/usr/bin/env python3
import timeit
import sys

testcode_loop = '''
def list_loop(lst):
    new_list = []
    for i in lst:
        if i[-10::] == '@gmail.com':
            new_list.append(i)
    print(new_list)
    print('here')
    return(new_list)
'''

testcode_comp = '''
def list_comp(lst):
    new_list = [i for i in lst if i[-10::] == '@gmail.com']
    return(new_list)
'''

testcode_map = '''
def select(x):
    if x[-10::] == '@gmail.com':
        return x

def list_map(lst):
    new_list = list(map(select, lst))
    return(new_list)
'''

testcode_filter = '''
def list_filter(lst):
    new_list = list(filter(lambda x: x[-10::] == '@gmail.com', lst))
    print(new_list)
'''

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
    if len(sys.argv) == 3:
        func = ['loop', 'list_comprehension', 'map', 'filter']
        if sys.argv[1] in func and sys.argv[2].isdigit():
            name_func = sys.argv[1]
            num = int(sys.argv[2])
            lst = create_list()
            if name_func == 'loop':
                print(timeit.timeit(stmt=testcode_loop, number=num))
            elif name_func == 'list_comprehension':
                print(timeit.timeit(stmt=testcode_comp, number=num))
            elif name_func == 'map':
                print(timeit.timeit(stmt=testcode_map, number=num))
            else:
                print(timeit.timeit(stmt=testcode_filter, number=num))

if __name__ == '__main__':
    choose_var()
