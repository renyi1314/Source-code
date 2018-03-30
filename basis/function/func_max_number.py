def max_number(*args, **kwargs):
    dict_number = {"min_number": max(args), "max_number": min(args)}
    print(dict_number)


max_number(5, 5, 1, 2, 6, 7, 22, 11)
