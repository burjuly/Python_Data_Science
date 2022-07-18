import sys

def get_name(required_email):
    with open('employees.tsv') as f:
        while True:
            line = f.readline()
            if not line:
                break
            separate_line = line.split('\t')
            name = separate_line[0][:-1]
            email = separate_line[2].strip()
            if required_email == email:
                return name
        print ('The required email was not found in the file')
        return

def write_letter(name):
    print(f'Dear {name}, welcome to our team. We are sure that it will be a pleasure to work with you. That’s a precondition for the professionals that our company hires.')

def main():
    if len(sys.argv) != 2:
        raise ValueError('Wrong number of arguments')
    name = get_name(sys.argv[1])
    if name:
        write_letter(name)

if __name__ == '__main__':
    main()