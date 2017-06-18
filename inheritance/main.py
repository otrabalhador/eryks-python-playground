class MyDict(object):
    def __init__(self):
        self.dictionary = dict()

    def add(self, key, value):
        self.dictionary[key] = value

    def __str__(self):
        return str(self.dictionary)


a = MyDict
a.add("1",2)
print(a)
