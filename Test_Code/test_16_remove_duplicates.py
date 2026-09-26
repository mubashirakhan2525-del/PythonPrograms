from importlib.machinery import SourceFileLoader

program = SourceFileLoader("remove_duplicates", "Code/16_remove_duplicates.py").load_module()


def test_remove_duplicates():
    assert program.remove_duplicates([1, 2, 2, 3, 3, 4]) == [1, 2, 3, 4]


def test_no_duplicates():
    assert program.remove_duplicates([1, 2, 3, 4]) == [1, 2, 3, 4]


def test_all_duplicates():
    assert program.remove_duplicates([5, 5, 5, 5]) == [5]


def test_empty_list():
    assert program.remove_duplicates([]) == []


def test_negative_numbers():
    assert program.remove_duplicates([-1, -1, 2, 2, 3]) == [-1, 2, 3]


print("All test cases passed.")
