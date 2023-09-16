import sys

from NaturalMergeSorter import NaturalMergeSorter
from RunLengthTestCase import RunLengthTestCase

def main():
    # Test case list: A completely sorted lst
    list1 = [15, 23, 23, 23, 31, 64, 77, 87, 88, 91]

    # Test case list: Sorted run of 3 followed by sorted run of 6
    list2 = [64, 88, 91, 12, 21, 34, 43, 56, 65]

    # Test case list: 5 elements in descending order, so 5 runs of length 1
    list3 = [-10, -20, -30, -40, -50]

    # Test case list: 8 equal elements, so 1 run of 8
    list4 = [-99, -99, -99, -99, -99, -99, -99, -99]

    test_cases = [
        # First test case uses an out-of-bounds starting index. remaining test
        # cases do not.
        RunLengthTestCase(list1, len(list1), 0),
        RunLengthTestCase(list1, 0, len(list1)),
        RunLengthTestCase(list1, 3, len(list1) - 3),
        RunLengthTestCase(list2, 0, 3),
        RunLengthTestCase(list2, 2, 1),
        RunLengthTestCase(list2, 3, 6),
        RunLengthTestCase(list3, 0, 1),
        RunLengthTestCase(list3, 3, 1),
        RunLengthTestCase(list4, 0, len(list4)),
        RunLengthTestCase(list4, 4, len(list4) - 4),
        RunLengthTestCase(list4, 5, len(list4) - 5),
    ]

    for test in (test_cases):
        # Execute the test case, printing messages to sys.stdout
        test.execute(sys.stdout)

    # Test case lst for sorting
    list5 = [87, 64, 53, 92, 81, 88, 70, 12, 45, 96, 72]


    list5_copy = list(list5)
    sorter = NaturalMergeSorter()
    sorter.natural_merge_sort(list5_copy)
    print(f"""
{'PASS' if list5_copy == sorted(list5) else 'FAIL'}: NaturalMergeSort()
   List before calling natural_merge_sort(): {list5}
   List after calling natural_merge_sort():  {list5_copy}""")

if __name__ == '__main__':  
    main()