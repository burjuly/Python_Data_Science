#!/usr/bin/env python3

import sys
import resource

def read_file(path):
    lines = []
    with open(path, 'r') as f:
        lines = f.readlines()
    return(lines)

def main():
    if len(sys.argv) != 2:
        raise Exception("Wrong number of arguments")
    path = sys.argv[1]
    lines = read_file(path)
    for line in lines:
        pass

    usage = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024 / 1024 / 1024
    usage_r = round(usage, 3)
    user_time = resource.getrusage(resource.RUSAGE_SELF).ru_utime
    system_time = resource.getrusage(resource.RUSAGE_SELF).ru_stime
    total_time = round(user_time + system_time, 3)

    print(f'Peak Memory Usage = {usage_r} GB')
    print(f'User Mode Time + System Mode Time = {total_time}')

if __name__ == '__main__':
    main()