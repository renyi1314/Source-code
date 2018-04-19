def hello(*args):
    print(args)
    print("hello")

HelloWorld = type("HiWorld",(object,),{'fn_hello':hello})

print(HelloWorld)
print(HelloWorld.__name__)
print(HelloWorld.__class__)
print(HelloWorld.__dict__)

a= HelloWorld()
a.fn_hello()