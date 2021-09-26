"""
def my_min(nums):
    result = nums[0]
    for num in nums:
        if num < result:
            result = num
    return result

my_min(4, 5, 6, 7, 2)
"""


def my_min(*args):
    result = args[0]
    for num in args:
        if num < result:
            result = num
    return result

my_min(4, 5, 6, 7, 2)
