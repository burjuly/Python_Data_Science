#!/usr/bin/env python3

import sys
import os

class Research:
    def __init__(self, path):
        self.path = path

    def file_reader(self):
        try:
            data_file = open(self.path, 'r')
            try:
                lines = data_file.read()
                return(lines)
            except:
                raise Exception("It is impossible to read the file")
        except:
            raise Exception("File could not be opened")

    def validation(self, data):
        tab = data.split('\n')
        header = tab[0].split(',')
        if len(header) == 2:
            if (header[0] == '') or (header[1] == ''):
                raise Exception("Empty field in the header")
        else:
            raise Exception("Wrong number of field in the header")
        i = 1
        while i < len(tab):
            if tab[i] == '0,1' or tab[i] == '1,0':
                i += 1
                continue
            else:
                raise Exception("The string should contain only '0,1' or '1,0'")

def parse_file():
    if len(sys.argv) == 2:
        path = os.path.abspath(sys.argv[1])
        data_file = Research(path)
        data = data_file.file_reader()
        data_file.validation(data)
        print(data)

if __name__ == '__main__':
    try:
        parse_file()
    except Exception as e:
        print(f'Error: {e}')   
        
