class NaturalMergeSorter:
    def __init__(self):
        return

    def get_sorted_run_length(self, integer_list, start_index):
        if start_index > len(integer_list)-1:
            return 0

        counter = 0

        for i in range(start_index, len(integer_list)-1):
            if integer_list[i] <= integer_list[i+1]:
                counter += 1
            else:
                break
        return counter+1

    def natural_merge_sort(self, integer_list):
        i = 0
        while True:
            start_idx = i
            len1 = self.get_sorted_run_length(integer_list, start_idx)
            if len1 == len(integer_list):
                return
            if (len1 + start_idx) == (len(integer_list)):
                i = 0
            else:
                start = len1 + start_idx
                len2 = self.get_sorted_run_length(integer_list, start)
                end = len2 + start_idx + len1

                self.merge_sort(integer_list, start_idx, end - 1)
                if end == len(integer_list):
                    i = 0
                else:
                    i = end
        return

    def merge_sort(self, numbers, i, k):
        j = 0

        if i < k:
            j = (i + k) // 2  # Find the midpoint in the partition

            # Recursively sort left and right partitions
            self.merge_sort(numbers, i, j)
            self.merge_sort(numbers, j + 1, k)

            # Merge left and right partition in sorted order
            self.merge(numbers, i, j, k)

    def merge(self, numbers, left_first, left_last, right_last):
        merged_size = right_last - left_first + 1

        merged_numbers = [None] * merged_size
        merge_pos = 0
        left_pos = left_first
        right_pos = left_last + 1

        # Add smallest element from left or right partition to merged numbers
        while left_pos <= left_last and right_pos <= right_last:
            if numbers[left_pos] <= numbers[right_pos]:
                merged_numbers[merge_pos] = numbers[left_pos]
                left_pos += 1
            else:
                merged_numbers[merge_pos] = numbers[right_pos]
                right_pos += 1

            merge_pos += 1

        # If left partition isn't empty, add remaining elements to merged_numbers
        while left_pos <= left_last:
            merged_numbers[merge_pos] = numbers[left_pos]
            left_pos += 1
            merge_pos += 1

        # If right partition isn't empty, add remaining elements to merged_numbers
        while right_pos <= right_last:
            merged_numbers[merge_pos] = numbers[right_pos]
            right_pos += 1
            merge_pos += 1

        # Copy merged numbers back to numbers
        for merge_pos in range(merged_size):
            numbers[left_first + merge_pos] = merged_numbers[merge_pos]
