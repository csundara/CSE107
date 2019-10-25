def is_ele(first_ele, lst):
    """ checks given list lst and any additional sublists for element
    first_ele """
    rtn = False

    if isinstance(lst, list):
        for e in lst:
            if isinstance(e, list):
                rtn = is_ele(first_ele, e)
            elif e == first_ele:
                rtn = True
        return rtn
    elif lst == first_ele:
        return True
    else:
        return False


def element_of(lst):
    """ checks sublists for first element of main list """
    first = lst[0]

    for e in lst:
        if isinstance(e, list):
            return is_ele(first, e)
    return False


def filter_by_depth(dep, lst):
    """ takes in a depth dep and a list lst and removes any sublists nested
    deeper then dep """
    new_list = []

    if int(dep) > 0:
        for e in lst:
            if isinstance(e, list):
                elem = filter_by_depth(dep - 1, e)
                if elem != []:
                    new_list.append(elem)
            else:
                new_list.append(e)

    return new_list


def main():
    if element_of([5, [1, 2, 3, 4, 5, 6, 7]]):
        print('sucess')
    else:
        print('first test failed')
        print(element_of([5, [1, 2, 3, 4, 5, 6, 7]]))

    if element_of([7, [1, 2, [3, 4, [5, 6]], [7]]]):
        print('sucess')
    else:
        print('second test failed')
        print(element_of([7, [1, 2, [3, 4, [5, 6]], [7]]]))

    if element_of([77, [1, 2, [3, 4, [5, 6]], [7]]]):
        print('third test failed')
        print(element_of([77, [1, 2, [3, 4, [5, 6]], [7]]]))
    else:
        print('sucess')

    if filter_by_depth(0, [1, 2, 3]) == []:
        print('sucess')
    else:
        print('fourth test failed')
        print(filter_by_depth(0, [1, 2, 3]))

    if filter_by_depth(1, [1, 2, 3]) == [1, 2, 3]:
        print('sucess')
    else:
        print('fifth test failed')
        print(filter_by_depth(1, [1, 2, 3]))

    if filter_by_depth(5, [1, 2, 3]) == [1, 2, 3]:
        print('sucess')
    else:
        print('sixth test failed')
        print(filter_by_depth(5, [1, 2, 3]))

    if filter_by_depth(2, [1, 2, [3, 4, [5, 6]], [7]]) == [1, 2, [3, 4], [7]]:
        print('sucess')
    else:
        print('seventh test failed')
        print(filter_by_depth(2, [1, 2, [3, 4, [5, 6]], [7]]))


if __name__ == "__main__":
    main()
