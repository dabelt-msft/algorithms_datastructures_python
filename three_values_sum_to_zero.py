def binary_search_util(nums, left, right, item):
    index = (left + right) // 2
    if left >= right:
        return -1
    elif nums[index] == item:
        return index
    elif nums[index] > item:
        return binary_search_util(nums, left, index, item)
    else:
        return binary_search_util(nums, index + 1, right, item)


def find_trips(nums):
    trips = set()
    l = 0
    r = len(nums) - 1
    while l < r:
        while r > (abs(l) / 2 + 1)//1:
            left = nums[l]
            right = nums[r]
            needed = 0 - (left + right)
            if left == 0 or right == 0:
                break
            if needed > left and needed < right and binary_search_util(nums, l + 1, r, needed) != -1:
                trips.add((left, needed, right))
            r -= 1
        r = len(nums) - 1
        l += 1
    return trips


print(find_trips([-5,-4,-3,-1,0,1,2,4,7]))


