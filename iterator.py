class numbers:
    def __init__(self):
        self.initial=1
    def __iter__(self):
        return self
    def __next__(self):
        if self.initial<=15:
            first=self.initial
            self.initial+=1
            return first
        else:
            raise StopIteration
values=numbers()
print(values.__next__())
for i in values:
    print(i)
    