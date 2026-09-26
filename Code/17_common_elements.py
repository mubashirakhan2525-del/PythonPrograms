def common_elements(list1, list2):
    common = []

    for number in list1:
        if number in list2 and number not in common:
            common.append(number)

    return common


if __name__ == "__main__":
    list1 = list(map(int, input("Enter first list numbers: ").split()))
    list2 = list(map(int, input("Enter second list numbers: ").split()))

    print("Common elements:", common_elements(list1, list2))