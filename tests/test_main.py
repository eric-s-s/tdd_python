# shift-f10 to run tests
# ctrl-alt-v/n  extract/inline variable
# shift-f6 rename
# f6 move
# ctrl-alt-m   extract method
# clrl-alt-l/o   auto lint. auto fix imports
# f2 to next error
# alt-enter   fix problem
import pytest


def fizzbuzz(number):
    pass


@pytest.mark.parametrize("number,expected", [(5, "1,2,fizz,4,buzz")])
def test_thing(number, expected):
    assert fizzbuzz(number) == expected
