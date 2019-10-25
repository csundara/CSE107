# Fill in a correct implementation for each function.
# Define other functions if you think they make the
# assigned function easier to write or easier to read.


# This function returns the largest element in the given list.
def max(elements):
    largest = 0
    for ele in elements:
        if largest < ele:
            largest = ele
    return largest


# This function returns the smallest element in the given list.
def min(elements):
    smallest = elements[0]
    for ele in elements:
        if smallest > ele:
            smallest = ele
    return smallest


# This function returns the sum of the elements in the given list.
def sum(elements):
    summation = 0
    for ele in elements:
        summation = summation + ele
    return summation


# This function returns the mean of the elements in the given list.
def mean(elements):
    return sum(elements) / len(elements)


# This function returns the odd elements in the given list.
def odds(elements):
    rem = []
    for ele in elements:
        if ele % 2 == 0:
            rem.append(ele)
    for r in rem:
        elements.remove(r)
    return elements


# This function returns the even elements in the given list.
def evens(elements):
    rem = []
    for ele in elements:
        if ele % 2 == 1:
            rem.append(ele)
    for r in rem:
        elements.remove(r)
    return elements


# This function returns the every other element in the given list.
def every_other(elements):
    rem = []
    for i in range(len(elements)):
        if i % 2 == 1:
            rem.append(elements[i])
    for ele in rem:
        elements.remove(ele)
    return elements


# This function returns the every other odd element in the given list.
def every_other_odd(elements):
    elements = odds(elements)
    return every_other(elements)


# This function returns the every other even element in the given list.
def every_other_even(elements):
    elements = evens(elements)
    return every_other(elements)


def run_tests():
    """This function tests each function defined in this module."""

    # A single test is a tuple containing the function
    # which is being tested, a sample input, and the correct output.
    # Tests should be written using the unittest or pytest modules,
    # but, hopefully, this code is easier to understand.
    tests = [
        # This test will be used to check if `sum([1, 2, 3])` is `6`.
        (sum, [1, 2, 3], 6),
        (sum, [], 0),
        (sum, [-1, 0, 1], 0),
        (sum, [10000, 1000, 100, 10, 1], 11111),
        (max, [3, 2, 1, 2, 3], 3),
        (max, [-1, 4, -2, 10, 1, 5], 10),
        (min, [3, 2, 1, 2, 3], 1),
        (min, [-1, 4, -2, 10, 1, 5], -2),
        (odds, [1, 2, 3, 4], [1, 3]),
        (odds, [1, 100, 45, 23, 10, 2, 4, 13], [1, 45, 23, 13]),
        (odds, [], []),
        (evens, [1, 2, 3, 4], [2, 4]),
        (evens, [1, 100, 45, 23, 10, 2, 4, 13], [100, 10, 2, 4]),
        (evens, [], []),
        (every_other, [1, 2, 3, 4], [1, 3]),
        (every_other, [1, 100, 45, 23, 10, 2, 4, 13], [1, 45, 10, 4]),
        (every_other, [], []),
        (every_other_odd, [1, 2, 3, 4], [1]),
        (every_other_odd, [1, 100, 45, 23, 10, 2, 4, 13], [1, 23]),
        (every_other_odd, [], []),
        (every_other_even, [1, 2, 3, 4], [2]),
        (every_other_even, [1, 100, 45, 23, 10, 2, 4, 13], [100, 2]),
        (every_other_even, [], []),
    ]

    passed = 0
    failed = 0

    # Test each function.
    # Print a detailed error message whenever a function fails a test.
    for test in tests:
        f = (test[0])
        result = f(test[1])
        expected = test[2]
        if result == expected:
            passed += 1
        else:
            failed += 1

            # f.__name__ is the function's name
            # for example, evens.__name__ is the string "evens"
            print("Function '{}' given argument {}".format(f.__name__, test[1]))
            print("Expected {}, but returned {}".format(expected, result))
    print("\nPassed {} out of {} tests.".format(passed, passed + failed))


if __name__ == "__main__":
    run_tests()
