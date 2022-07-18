#!/usr/bin/env python3

import sys
from random import randint

class Research:
    def __init__(self, path):
        self.path = path
    
    class Calculations:
        def __init__(self, data):
            self.data = data  
        
        def counts(self):
            lst = self.data
            heads = sum(l[0] for l in lst)
            tails = sum(l[1] for l in lst)
            return heads, tails
        
        def fractions(self, heads, tails):
            s = heads + tails
            if s == 0:
                return (0, 0)
            else:
                return heads/s * 100, tails/s * 100

    class Analytics(Calculations):
        def predict_random(self, num):
            if num <= 0:
                raise Exception('Wrong number')
            predict = []
            for i in range(num):
                predict.append([0,1]) if randint(0,1) == 0 else predict.append([1,0])
            return predict
        def predict_last(self):
            return self.data[-1]

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

def main():
    if len(sys.argv) != 2:
        raise Exception("Wrong number of arguments")
    path = sys.argv[1]
    f = Research(path)
    lst = f.file_reader(check_header(path))
    if validation(lst) == False:
        raise Exception("Invalid file structure")
    a = f.Analytics(lst)
    heads,tails = a.counts()
    p_heads, p_tails = a.fractions(heads,tails)
    print(lst)
    print(heads,tails)
    print(p_heads, p_tails)
    print(a.predict_random(3))
    print(a.predict_last())

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f'Error: {e}')