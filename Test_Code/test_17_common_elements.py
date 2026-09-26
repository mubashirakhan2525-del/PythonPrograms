from importlib.machinery import SourceFileLoader

program = SourceFileLoader("common_elements", "Code/17_common_elements.py").load_module()


def test_common_elements():
    assert program.common_elements([1, 2, 3, 4], [3, 4, 5, 6]) == [3, 4]


def test_no_common_elements():
    assert program.common_elements([1, 2, 3], [4, 5, 6]) == []


def test_all_common_elements():
    assert program.common_elements([1, 2, 3], [1, 2, 3]) == [1, 2, 3]


def test_repeated_elements():
    assert program.common_elements([1, 2, 2, 3], [2, 2, 4]) == [2]


def test_negative_numbers():
    assert program.common_elements([-1, -2, 3], [-2, 3, 5]) == [-2, 3]


print("All test cases passed.")
