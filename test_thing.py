# shift-f10 to run tests
# ctrl-alt-v/n  extract/inline variable
# shift-f6 rename
# f6 move
# ctrl-alt-m   extract method
# clrl-alt-l/o   auto lint. auto fix imports
# f2 to next error
# alt-enter   fix problem

from main import deliver, Destination

A = Destination.A
B = Destination.B


def test_deliver_one_a_package():
    destinations = [A]
    expected_time = 4
    actual = deliver(destinations)
    assert actual == expected_time

def test_deliver_one_b_package():
    destinations = [B]
    expected_time = 5
    actual = deliver(destinations)
    assert actual == expected_time

def test_deliver_one_b_package_with_class():
    destinations = [B]
    actual_time = Truck(destinations)

#
# def test_deliver_a_and_b_package():
#     destinations = [A, B]
#     expected_time = 5
#     actual = deliver(destinations)
#     assert actual == expected_time
#
#
# def test_deliver_a_and_b_and_b_package():
#     destinations = [A, B, B]
#     expected_time = 7
#     actual = deliver(destinations)
#     assert actual == expected_time
#
#
# def test_deliver_b_and_b_package():
#     destinations = [B, B]
#     expected_time = 5
#     actual = deliver(destinations)
#     assert actual == expected_time
#
#
# def test_deliver_b_b_b():
#     destinations = [B, B, B]
#     expected_time = 15
#     actual = deliver(destinations)
#     assert actual == expected_time
