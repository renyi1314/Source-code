class foo:
    def __str__(self):
        # print("Hello,world")
        return "hello,world"

    def __unicode__(self):
        return "hello,unicode"

    def __repr__(self):
        return "hello,repr"
a=foo()
print(a)
