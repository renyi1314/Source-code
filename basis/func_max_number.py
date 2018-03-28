def max_number(*args,**kwargs):
    a=list(args)
    a.sort()
    dict_number={"min_number":a[0],"max_number":a[len(a)-1]}
    print(dict_number.items())
max_number(5,5,1,2,6,7,22,11)

