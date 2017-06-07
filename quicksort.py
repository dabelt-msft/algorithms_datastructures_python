def quick_sort(nums, start, end):


def sort_pivot(nums, start, end):
    pivot = nums[start]
    p_i = start
    for cur_i in range(start, end):
        if pivot > nums[cur_i]:
            temp = pivot
            for s_i in range(p_i, cur_i + 1):
                if s_i == p_i:
                    nums[s_i] = nums[cur_i]
                else:
                    temp, nums[s_i] = nums[s_i], temp
            p_i += 1
    return nums, p_i, nums[p_i]

nums = [5, 3, 6, 4, 7, 2, 9]

print(sort_pivot(nums, 0, len(nums)))
print(sort_pivot(nums, 0, len(nums)))


