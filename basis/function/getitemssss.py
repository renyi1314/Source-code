class Item:
    name = "renyi"
    age = 25

    def __getitem__(self, item):
        if hasattr(self, item):
            return getattr(self, item)


p = Item()
print(p["name"])
print(p["age"])
print(p["test"])
