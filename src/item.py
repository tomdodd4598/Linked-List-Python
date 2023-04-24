class Item:
    def __init__(self, value, next_):
        print(f'Creating item: {value}')
        self.value = value
        self.next_ = next_

    def __len__(self):
        item = self
        i = 0
        while item is not None:
            item = item.next_
            i += 1
        return i

    def __getitem__(self, n):
        item = self
        for i in range(n):
            item = item.next_
        return item

    def __iter__(self):
        class ItemIterator:
            def __init__(self, item):
                self.item = item

            def __next__(self):
                item = self.item
                if item is None:
                    raise StopIteration
                else:
                    self.item = self.item.next_
                    return item

        return ItemIterator(self)

    def print_get_next(self):
        print('{}{}'.format(self.value, '\n' if self.next_ is None else ', '), end='')
        return self.next_


def item_fold(f_some, f_last, f_empty, accumulator, item):
    if item is not None:
        next_ = item.next_
        if next_ is not None:
            return item_fold(f_some, f_last, f_empty, f_some(item, next_, accumulator), next_)
        else:
            return f_last(item, accumulator)
    else:
        return f_empty(accumulator)


def item_foldback(f_some, f_last, f_empty, generator, item):
    if item is not None:
        next_ = item.next_
        if next_ is not None:
            return item_foldback(
                f_some, f_last, f_empty, lambda inner_val: generator(f_some(item, next_, inner_val)), next_
            )
        else:
            return generator(f_last(item))
    else:
        return generator(f_empty())
