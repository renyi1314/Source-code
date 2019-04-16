def fn(self, name="world"):
    print("Hello, {}".format(name))


Hello = type('Hello', (object,), {"say_heelo": fn})

hello = Hello()
hello.say_heelo()
