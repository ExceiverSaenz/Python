from NaturalMergeSorter import NaturalMergeSorter

class RunLengthTestCase:
    def __init__(self, lst, start, expected_return):
        self.lst = lst
        self.start = start
        self.expected_return = expected_return

    # Executes the test case. If the test case passes, a message that starts
    # with "PASS" is printed and true is returned. Otherwise a message that
    # starts with "FAIL" is printed and false is returned.
    def execute(self, test_feedback):
        user_sorter = NaturalMergeSorter()

        # Call the get_sorted_run_length() function with the test case parameters
        user_ret_val = user_sorter.get_sorted_run_length(self.lst, self.start)

        # The test passed only if the actual return value equals the
        # expected return value
        passed = user_ret_val == self.expected_return

        if user_ret_val == self.expected_return:
            print(f"""PASS: get_sorted_run_length()\n   List: {self.lst}""", file=test_feedback)
            print(f"""   Start index:           {self.start}""", file=test_feedback)
            print(f"""   Expected return value: {self.expected_return}""", file=test_feedback)
            print(f"""   Actual return value:   {user_ret_val}""", file=test_feedback)
            return True
        else:
            print(f"""FAIL: get_sorted_run_length()\n   List: {self.lst}""", file=test_feedback)
            print(f"""   Start index:           {self.start}""", file=test_feedback)
            print(f"""   Expected return value: {self.expected_return}""", file=test_feedback)
            print(f"""   Actual return value:   {user_ret_val}""", file=test_feedback)
            return False
