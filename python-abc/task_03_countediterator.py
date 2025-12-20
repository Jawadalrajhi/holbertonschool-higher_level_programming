class CountedIterator:
    def __init__(self, iterable):
        self.iterator = iter(iterable)
        self.counter = 0

    def get_count(self):
        return self.counter

    def __next__(self):
        try:
            item = next(self.iterator)
            self.counter += 1
            return item
        except StopIteration:
            raise StopIteration("No more items to iterate")


iterable = [1, 2, 3, 4, 5]
counted_iter = CountedIterator(iterable)

try:
    while True:
        item = next(counted_iter)
        print("Item:", item)
        print("Count:", counted_iter.get_count())
except StopIteration as e:
    print(e)
