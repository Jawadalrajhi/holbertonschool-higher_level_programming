class VerboseList(list):
    def append(self, item):
        super().append(item)
        print(f"Added {item} to the list.")

    def extend(self, iterable):
        super().extend(iterable)
        print(f"Extended the list with {len(iterable)} items.")

    def remove(self, item):
        print(f"Removed {item} from the list.")
        super().remove(item)

    def pop(self, index=None):
        if index is None:
            index = len(self) - 1
        item = self[index]
        print(f"Popped {item} from the list.")
        return super().pop(index)


verbose_list = VerboseList()

verbose_list.append(1)
verbose_list.extend([2, 3, 4])
verbose_list.remove(2)
verbose_list.pop()
