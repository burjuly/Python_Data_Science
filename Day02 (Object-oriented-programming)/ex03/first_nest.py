#!/usr/bin/env python3

import sys
import os

class Research:
    def __init__(self, path):
        self.path = path
    
    class Calculations:
        def counts(lst):
            heads = sum(l[0] for l in lst)
            tails = sum(l[1] for l in lst)
            return heads, tails
        
        def fractions(heads, tails):
            s = heads + tails
            if s == 0:
                return (0, 0)
            else:
                return heads/s * 100, tails/s * 100

    def str_to_list(lines, has_header):
        tab = lines.split('\n')
        if has_header == True:
            tab = tab[1::]
        lst = [list(map(int, l.split(','))) for l in tab]
        return(lst)

    def file_reader(self, has_header = True):
        try:
            with open(self.path, 'r') as f:
                try:
                    lines = f.read()
                    return(Research.str_to_list(lines, has_header))
                except:
                    raise Exception("It is impossible to read the file")
        except:
            raise Exception("File could not be opened")

def check_header(path):
    try:
        with open(path, 'r') as f:
            try:
                lines = f.read()
                tab = lines.split('\n')
                if tab[0] == 'head,tail':
                    return True
                else:
                    return False
            except:
                raise Exception("It is impossible to read the file")
    except:
        raise Exception("File could not be opened")

def validation(data):
    for i in data:
        if i in [[0,1],[1,0]]:
            continue
        else:
            return False
    return True

def parse_file():
    if len(sys.argv) != 2:
        raise Exception("Wrong number of arguments")
    path = os.path.abspath(sys.argv[1])
    f = Research(path)
    lst = f.file_reader(check_header(path))
    if validation(lst) == False:
        raise Exception("Invalid file structure")
    heads,tails = f.Calculations.counts(lst)
    p_heads, p_tails = f.Calculations.fractions(heads,tails)
    print(lst)
    print(heads,tails)
    print(p_heads, p_tails)

if __name__ == '__main__':
    try:
        parse_file()
    except Exception as e:
        print(f'Error: {e}')