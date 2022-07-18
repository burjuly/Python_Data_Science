import sys

def check_string(str):
    for i in str:
        if ord(i) > 127:
            raise Exception('Not ASSCI symbol')

def validation(args):
    if args[1] == 'encode' or args[1] == 'decode':
        if args[3].isnumeric():
            check_string(args[2])
        else:
            raise Exception('Last argument must be numeric')
    else:
        raise Exception("First argument must be 'encode' or 'decode'")

def сaesar(type_code, str_code, shift):
    low_sym = 'abcdefghijklmnopqrstuvwxyz'
    up_sym = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_str = ''
    if type_code == 'encode':
        shift = -shift
    for i in str_code:
        if i in low_sym:
            new_index = low_sym.index(i) - shift % 26
            new_str += low_sym[new_index]
        elif i in up_sym:
            new_index = up_sym.index(i) - shift % 26
            new_str += up_sym[new_index]
        else:
            new_str += i
    print(new_str)    

if __name__ == '__main__':
    if len(sys.argv) != 4:
        raise Exception('Wrong number of arguments')
    validation(sys.argv)
    сaesar(sys.argv[1], sys.argv[2], int(sys.argv[3]))
