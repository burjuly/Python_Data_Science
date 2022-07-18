#!/usr/bin/env python3

class Research:
    def file_reader(self):
        try:
            with open('data.csv', 'r') as data_file:
                try:
                    lines = data_file.read()
                    return(lines)
                except:
                    print("It is impossible to read the file")
        except:
            print("File could not be opened")

def main():
    r = Research()
    data = r.file_reader()
    if data == None:
        return
    else:
        print(data)

if __name__ == '__main__':
    main()
    
