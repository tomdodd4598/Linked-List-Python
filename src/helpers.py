from item import *


def insert_item(start, val, insert_before):
    print(f'Creating item: {val}')
    current = start
    previous = None

    while current is not None and not insert_before(val, current):
        previous = current
        current = current.next_

    item = Item(val, current)

    if previous is None:
        start = item
    else:
        previous.next_ = item

    return start


def remove_item(start, val, value_equals):
    current = start
    previous = None

    while current is not None and not value_equals(current, val):
        previous = current
        current = current.next_

    if current is None:
        print(f'Item {val} does not exist!')
    else:
        if previous is None:
            start = current.next_
        else:
            previous.next_ = current.next_

        print(f'Removed item: {val}')

    return start


def remove_all(_start):
    return None


def print_list(start):
    while start is not None:
        start = start.print_get_next()


def print_iterator(start):
    if start is not None:
        for item in start:
            item.print_get_next()


def print_array(start):
    item = start
    i = 0
    while item is not None:
        item = start[i].print_get_next()
        i += 1


def print_recursive(start):
    if start is not None:
        print_recursive(start.print_get_next())


def print_fold(start):
    def f_some(current, _next, accumulator):
        return f'{accumulator}{current.value}, '

    def f_last(current, accumulator):
        return f'{accumulator}{current.value}\n'

    def f_empty(accumulator):
        return accumulator

    print(item_fold(f_some, f_last, f_empty, '', start), end='')


def print_foldback(start):
    def f_some(current, _next, inner_val):
        return f'{current.value}, {inner_val}'

    def f_last(current):
        return f'{current.value}\n'

    def f_empty():
        return ''

    print(item_foldback(f_some, f_last, f_empty, lambda x: x, start), end='')
