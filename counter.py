""" A program that stores and updates a counter using a Python pickle file"""

import os.path
import sys
#from pickle import dump, load
import pickle
from pathlib import Path

def update_counter(file_name, reset=False):
    """ Updates a counter stored in the file 'file_name'

    A new counter will be created and initialized to 1 if none exists or if
    the reset flag is True.

    If the counter already exists and reset is False, the counter's value will
    be incremented.

    file_name: the file that stores the counter to be incremented.  If the file
    doesn't exist, a counter is created and initialized to 1.
    reset: True if the counter in the file should be rest.
    returns: the new counter value

    >>> update_counter('blah.pickle',True)
    1
    >>> update_counter('blah.pickle')
    2
    >>> update_counter('blah2.pickle',True)
    1
    >>> update_counter('blah.pickle')
    3
    >>> update_counter('blah2.pickle')
    2
    """
    my_file = Path(file_name)
    if (reset or not(my_file.is_file())):
        counter = 0
    else:
        counter = pickle.load( open(file_name, "rb"))
    counter += 1
    pickle.dump(counter, open(file_name, "wb"))
    print(counter)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        import doctest
        doctest.testmod()
        update_counter('blah.pickle') #proof that it works
    else:
        print("new value is " + str(update_counter(sys.argv[1])))
