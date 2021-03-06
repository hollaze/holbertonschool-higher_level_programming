#!/usr/bin/python3
''' MyList class '''


class MyList(list):
    """ inherit list

    Args:
        list (list)

    Methods:
        print_sorted - print sorted list
    """

    def print_sorted(self):
        print(sorted(self))
