"""Dutch National Flag Problem
Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.
You're not allowed to use any sorting function that Python provides.

Note: O(n) does not necessarily mean single-traversal. For e.g. if you traverse the array twice,
that would still be an O(n) solution but it will not count as single traversal.

Here is some boilerplate code and test cases to start with:
"""


def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    start = 0
    end = len(input_list) - 1
    for i, num in enumerate(input_list):
        if num == 0 and i > start:
            while 0 == input_list[start] and i > start:
                start += 1
            input_list[i], input_list[start] = input_list[start], input_list[i]
            start += 1
            if input_list[i] == 2 and i < end:
                while 2 == input_list[end] and i < end:
                    end -= 1
                input_list[i], input_list[end] = input_list[end], input_list[i]
                end -= 1
        elif num == 2 and i < end:
            while 2 == input_list[end] and i < end:
                end -= 1
            input_list[i], input_list[end] = input_list[end], input_list[i]
            end -= 1
            if input_list[i] == 0 and i > start:
                while 0 == input_list[start] and i > start:
                    start += 1
                input_list[i], input_list[start] = input_list[start], input_list[i]
                start += 1
    return input_list


def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 1])

test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
