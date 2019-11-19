# shift-f10 to run tests
# ctrl-alt-v/n  extract/inline variable
# shift-f6 rename
# f6 move
# ctrl-alt-m   extract method
# clrl-alt-l/o   auto lint. auto fix imports
# f2 to next error
# alt-enter   fix problem

from main import do_stuff
import pytest


def calculate_winner(param, param1):
    param = [get_number(c) for c in param.split(" ")]
    param1 = [get_number(c) for c in param1.split(" ")]

    if max(param) < max(param1):
        return 2
    else:
        return 1


def get_number(param):
    param = convert_face_cards(param)
    number = int(param[:-1])
    return number


def convert_face_cards(param):
    param = param.replace('J', '11')
    param = param.replace('Q', '12')
    param = param.replace('K', '13')
    param = param.replace('A', '14')
    return param


def test_get_number():
    assert get_number('10H') == 10


@pytest.mark.parametrize('face_answer', zip('JQKA', range(11, 15)))
def test_get_number_face_card(face_answer):
    face, answer = face_answer
    assert get_number(f'{face}H') == answer


def test_basic_winner_player_1_suits():
    assert calculate_winner('3D', '2H') == 1


def test_basic_winner_player_2_suits():
    assert calculate_winner('2H', '3D') == 2


def test_basic_winner_player_2_has_10():
    assert calculate_winner('2H', '10D') == 2


def test_face_card_player_1():
    assert calculate_winner('QH', 'JD') == 1


def test_face_card_player_1_king():
    assert calculate_winner('KH', 'AD') == 2


@pytest.mark.parametrize('c', range(1, 11))
def test_face_card_with_number(c):
    param = f'{c}H'
    assert calculate_winner(param, 'AS') == 2


def test_pair_high_card_is_first():
    assert calculate_winner('10H 2D', '8S') == 1


def test_pair_high_card_is_second():
    assert calculate_winner('1H 20D', '8S') == 1
