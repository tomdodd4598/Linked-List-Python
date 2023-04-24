from helpers import *

import re


def is_valid_string(string):
    return re.search('^(0|-?[1-9][0-9]*|[A-Za-z][0-9A-Z_a-z]*)$', string)


def is_number_string(string):
    return re.search('^-?[0-9]+$', string)


def insert_before(val, item):
    if is_number_string(val) and is_number_string(item.value):
        return int(val) <= int(item.value)
    else:
        return val <= item.value


def value_equals(item, val):
    return item.value == val


def main():
    start = None
    begin = True

    while True:
        if not begin:
            print()
        else:
            begin = False

        input_ = input('Awaiting input...\n')

        if len(input_) == 0:
            print('\nProgram terminated!')
            # start = remove_all(start)
            return

        elif input_[0] == '~':
            if len(input_) == 1:
                print('\nDeleting list...')
                start = remove_all(start)
            else:
                input_ = input_[1:]
                if is_valid_string(input_):
                    print('\nRemoving item...')
                    start = remove_item(start, input_, value_equals)
                else:
                    print('\nCould not parse input!')

        elif input_ == 'l':
            print('\nLoop print...')
            print_loop(start)

        elif input_ == 'i':
            print('\nIterator print...')
            print_iterator(start)

        elif input_ == 'a':
            print('\nArray print...')
            print_array(start)

        elif input_ == 'r':
            print('\nRecursive print...')
            print_recursive(start)

        elif input_ == 'f':
            print('\nFold print...')
            print_fold(start)

        elif input_ == 'b':
            print('\nFoldback print...')
            print_foldback(start)

        elif is_valid_string(input_):
            print('\nInserting item...')
            start = insert_item(start, input_, insert_before)

        else:
            print('\nCould not parse input!')


if __name__ == '__main__':
    main()
