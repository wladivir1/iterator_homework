import types

# функция для решения задачи №4
def flat_generator(list_of_lists):
    for item in list_of_lists:
        if isinstance(item, list):
            for el in flat_generator(item):
                yield el
        else:
            yield item


def test_4():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']

    assert isinstance(flat_generator(list_of_lists_2), types.GeneratorType)

# для проверки кода
list_of_lists_2 = [
    [['a'], ['b', 'c']],
    ['d', 'e', [['f'], 'h'], False],
    [1, 2, None, [[[[['!']]]]], []]
]

# вспомогательная функция для проверки правильности решения задачи №4
def check_flat_list_from_task_4(lst):
    for el in flat_generator(lst):
        print(el, end=' ')

if __name__ == '__main__':
    test_4()

    check_flat_list_from_task_4(list_of_lists_2)