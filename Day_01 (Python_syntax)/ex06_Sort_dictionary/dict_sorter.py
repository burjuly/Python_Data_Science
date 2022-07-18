import sys

def sorted_country():
    list_of_tuples = [
        ('Russia', '25'),
        ('France', '132'),
        ('Germany', '132'),
        ('Spain', '178'),
        ('Italy', '162'),
        ('Portugal', '17'),
        ('Finland', '3'),
        ('Hungary', '2'),
        ('The Netherlands', '28'),
        ('The USA', '610'),
        ('The United Kingdom', '95'),
        ('China', '83'),
        ('Iran', '76'),
        ('Turkey', '65'),
        ('Belgium', '34'),
        ('Canada', '28'),
        ('Switzerland', '26'),
        ('Brazil', '25'),
        ('Austria', '14'),
        ('Israel', '12')
    ]
    d = {}
    for i in list_of_tuples:
        d.update({i[0]: i[1]})

    sort_dict = dict(sorted(d.items(), key =lambda item: (-int(item[1]), item[0])))
    for key in sort_dict.keys():
        print(key)

if __name__ == '__main__':
    sorted_country()