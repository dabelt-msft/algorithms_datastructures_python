def binary_search(nums, item):
    s_i = 0
    e_i = len(nums) - 1
    for _ in range(0, len(nums)):
        index = (s_i + e_i) // 2
        if nums[index] == item:
            return index
        elif nums[index] < item:
            s_i = index + 1
        else:
            e_i = index - 1
    return -1

print(binary_search([1,2,3,4,5,6,7,8],9))