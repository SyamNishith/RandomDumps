import sys
# Divide and conquer solution to find the minimum and maximum number in a list
def findMinAndMax(nums, lower, higher, min=sys.maxsize, max=-sys.maxsize):
    # if the list contains only one element

    if lower ==higher:  # common comparison

        if min > nums[higher]:  # comparison 1
            min = nums[higher]

        if max < nums[lower]:  # comparison 2
            max = nums[lower]

        return min, max

    # if the list contains only two elements
    if higher - lower == 1:  # common comparison

        if nums[lower] < nums[higher]:  # comparison 1
            if min > nums[lower]:  # comparison 2
                min = nums[lower]

            if max < nums[higher]:  # comparison 3
                max = nums[higher]

        else:
            if min > nums[higher]:  # comparison 2
                min = nums[higher]

            if max < nums[lower]:  # comparison 3
                max = nums[lower]

        return min, max

    # find the middle element
    mid = (lower + higher) // 2

    # recur for the left sublist
    min, max = findMinAndMax(nums, lower, mid, min, max)

    # recur for the right sublist
    min, max = findMinAndMax(nums, mid + 1, higher, min, max)

    return min, max


if __name__ == '__main__':
    nums = [9]

    # initialize the minimum element by INFINITY and the
    # maximum element by -INFINITY
    (min, max) = findMinAndMax(nums, 0, len(nums) - 1)

    print("The minimum element in the list is", min)
    print("The maximum element in the list is", max)