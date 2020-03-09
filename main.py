# shift-f10 to run tests
# ctrl-alt-v/n  extract/inline variable
# shift-f6 rename
# f6 move
# ctrl-alt-m   extract method
# clrl-alt-l/o   auto lint. auto fix imports
# f2 to next error
# alt-enter   fix problem


from enum import Enum, auto

time_from_factory_to_b = 5
time_from_factory_to_port = 1
time_from_port_to_a = 3


class Destination(Enum):
    A = auto()
    B = auto()


A, B = Destination


class Transport(Enum):
    TRUCK = auto()
    BOAT = auto()


TRUCK, BOAT = Transport


def deliver(destinations):
    trucks = [TRUCK, TRUCK]
    boats = [BOAT]
    total_time = 0
    for destination in destinations:
        if destination == B:
            total_time += time_from_factory_to_b
            trucks.pop()
        if destination == A:
            total_time += time_from_factory_to_port + time_from_port_to_a
            trucks.pop()
            boats.pop()
    return total_time
    # if destinations == [B, B, B]:
    #     return time_from_factory_to_b * 3
    # if len(destinations) == 3:
    #     return time_from_factory_to_b + time_from_factory_to_port * 2
    # return time_from_factory_to_b
