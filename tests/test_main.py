# shift-f10 to run tests
# ctrl-alt-v/n  extract/inline variable
# shift-f6 rename
# f6 move
# ctrl-alt-m   extract method
# clrl-alt-l/o   auto lint. auto fix imports
# f2 to next error
# alt-enter   fix problem

from main.main import do_stuff


def test_thing():
    assert do_stuff() == 2
