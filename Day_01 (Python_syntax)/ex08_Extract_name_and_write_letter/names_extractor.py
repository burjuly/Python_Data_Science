import sys

def extract_name(path):
    with open(path, 'r') as file_to_read:
        with open('employees.tsv', 'w') as file_to_write :
            file_to_write.write(f'Name\tSurname\tE-mail\n')
            while True:
                line = file_to_read.readline()
                if not line:
                    break
                line_all = line.split('.')
                email = line_all[0] + '.' + line_all[1] + '.' + line_all[2]
                name = line_all[0].capitalize()
                surname = line_all[1].split('@')[0].capitalize()
                file_to_write.write(f'{name} \t{surname}\t{email}')
                
def main():
    if len(sys.argv) != 2:
        raise ValueError('Wrong number of arguments')
    extract_name(sys.argv[1])

if __name__ == '__main__':
    main()