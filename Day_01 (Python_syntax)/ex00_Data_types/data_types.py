def data_types():
    i = int()
    s = str()
    f = float()
    b = bool()
    l = list()
    d = dict()
    t = tuple()
    st = set()

    print(f"[{type(i).__name__}, {type(s).__name__},", end=' ')
    print(f"{type(f).__name__}, {type(b).__name__},", end=' ')
    print(f"{type(l).__name__}, {type(d).__name__},", end=' ')
    print(f"{type(t).__name__}, {type(st).__name__}]")

if __name__ == '__main__':
    data_types()