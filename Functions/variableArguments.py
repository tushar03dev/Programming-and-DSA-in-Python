def sum_all(*args):
    print(args)
    for arg in args:
        print(arg)
    return sum(args)
print(sum_all(1, 2, 3))