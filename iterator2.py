
class FlatIterator:

    def __init__(self, list_of_list):
        self.new_list = []
        self.actual_list = list_of_list
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter >= len(self.actual_list):
            if self.new_list:
                self.actual_list, self.counter = self.new_list.pop()
                return next(self)
            else:
                raise StopIteration

        item = self.actual_list[self.counter]
        self.counter += 1

        if type(item) is not list:
            return item
        else:
            # Запоминаем текущее состояние
            self.new_list.append((self.actual_list, self.counter))
            # Входим во вложенный список, он становится текущим списком
            self.actual_list = item
            self.counter = 0
            return next(self)

def test_3():
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']

    print(list(FlatIterator(list_of_lists_2)))

if __name__ == '__main__':
    test_3()