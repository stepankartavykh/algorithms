class TestIn:
    def __init__(self, elements=None):
        if elements is None:
            elements = []
        self.elements = elements

    def __contains__(self, item):
        print('test __contains__ method...')
        if item in self.elements:
            return True


# TODO time complexity of element in array
t = TestIn()
print(1 in t)

