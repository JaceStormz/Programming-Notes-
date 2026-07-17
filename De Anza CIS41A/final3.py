def count(*args, **kwargs):
    print(len(args) + len(kwargs))
    count(1, 2, 3)