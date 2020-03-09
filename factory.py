class Factory(object):

    def __init__(self):
        self.trucks = []
        self.goods = []

def test_init_empty_factory():
    factory = Factory()
    assert factory.trucks == []
    assert factory.goods == []