
import time
import unittest

def deco(func):

    print(f'Start time: {time.ctime()}')
    x = func(10)
    print(f'End time: {time.ctime()}')
    return x


@deco
def times2(x):
    return 2*x


def add(x):
    return x+1


unittest.TestCase.assertEqual(add(5), 6, 'yo')




