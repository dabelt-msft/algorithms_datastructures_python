def find_kth(nums, start, end, kth):
    i = sort_pivot(nums, start, end)
    try:
        if i + 1 == kth:
            return nums[i]
        elif i + 1 < kth:
            return find_kth(nums, i + 1, end, kth)
        else:
            return find_kth(nums, start, i, kth)
    except:
        raise ValueError("There are {} numbers in the list and you're looking for the position {}.".format(len(nums), kth))

def sort_pivot(nums, start, end):
    pivot = nums[start]
    p_i = start
    for index in range(start, end):
        if pivot > nums[index]:
            temp = nums[p_i]
            for sub_i in range(p_i, index + 1):
                if sub_i == p_i:
                    nums[sub_i] = nums[index]
                else:
                    temp, nums[sub_i], = nums[sub_i], temp
            p_i += 1
    return nums, p_i

nums = [5, 3, 6, 4, 7, 2, 9]

print(find_kth(nums, 0, len(nums), 9))
print(find_kth(nums, 0, len(nums), 1))
