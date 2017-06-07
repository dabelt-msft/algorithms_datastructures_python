# def find_two_nums_equal_sum(nums, sum):
#     items = dict()
#     for index in range(0, len(nums)):
#         if nums[index] in items:
#             return nums[index], nums[items[nums[index]]]
#         else:
#             items[16 - nums[index]] = index

def nom_sum(nums, left, right):
    return nums[left] + nums[right]


def find_two_nums_optimized(nums, sum):
    sorted = nums.sort()
    l_i = 0
    r_i = -1
    while nom_sum(nums, l_i, r_i) != sum:
        if nom_sum(nums, l_i, r_i) < sum:
            l_i += 1
        else:
            r_i -= 1
    return nums[l_i], nums[r_i]


nums = [7,2,3,4,6,9]

# print(find_two_nums_equal_sum(nums, 16))
print(find_two_nums_optimized(nums, 16))