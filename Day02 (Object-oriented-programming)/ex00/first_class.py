#!/usr/bin/env python3

class Must_read:
    try:
        with open('data.csv') as f:
            try:
                lines = f.read()
                print(lines)
            except:
                print("It is impossible to read the file")
    except: 
        print("File could not be opened")

if __name__ == '__main__':
    Must_read()
