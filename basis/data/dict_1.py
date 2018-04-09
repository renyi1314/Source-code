# employees = [
#     {"id": "0001", "name": "zs", "sex": "man", "age": "34"},
#     {"id": "0002", "name": "ls", "sex": "women", "age": "20"},
#     {"id": "0003", "name": "xs", "sex": "man", "age": "19"},
# ]
# print("id\tname\tsex\tage\t")
# for employee in employees:
#     print("%s\t%s\t%s\t%s" % (employee["id"], employee["name"], employee["sex"], employee["age"]))


# def intro(name, age, **kwargs):
#     print("name %s" % name)
#     print("age %s" % age)
#     # print("other", kwargs)
#     for i, j in kwargs.items():
#         print(i, j)
#
#
# intro(name="zs", age=29, sex=123, hehe=123)

# info3 = {"age": "20", "sex": "man", "name": "renyi3"}
# info2 = ("rneyi4","50","dsa")
#
#
# def foo(name, age, **kwargs):
#     print(name, age, kwargs)
#
# print(type(info2),type(info3))
# # foo(**info2)

name = input("input name")
age = input("input age")