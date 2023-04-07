class reverse_iter:
    def __init__(self, iterible):
        self.iterible = list(iterible)
        self.idx = len(iterible) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if 0 > self.idx or self.idx > len(self.iterible) - 1:
            raise StopIteration
        value_to_return = self.iterible[self.idx]
        self.idx -= 1
        return value_to_return


class reverse_iter2:
    def __init__(self, iterible):
        self.iterible = reversed(list(iterible))

    def __iter__(self):
        return iter(self.iterible)




reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)

print('-------------------')

reversed_list = reverse_iter2([1, 2, 3, 4])
for item in reversed_list:
    print(item)
