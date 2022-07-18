def check_str(line):
    i = 0
    new_line = ''
    while i < len(line):
        if line[i] == '':
            new_line += '\t'
        elif line[i][0] == '"':
            while i < len(line) - 1 and (line[i] == '' or line[i][-1] != '"'):
                new_line = new_line + line[i] + ','
                i += 1
            new_line += line[i] + '\t'
        else:
            new_line += line[i] + '\t'
        i += 1
    return new_line[:-1]

def read_file():
    with open('ds.csv') as f:
        lines = f.readlines()[:-1]
    with open("ds.tsv", "w") as file_to_write:
        for line in lines:
            new = line.split(',')
            file_to_write.write(check_str(new))

if __name__ == '__main__':
    read_file()
