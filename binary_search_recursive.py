def binary_search(nums, start, end, item):
    index = (start + end - 1)//2

    if end - start == 1:
        return index
    try:
        if nums[index] == item:
            return index
        elif nums[index] > item:
            return binary_search(nums, start, index, item)
        else:
            return binary_search(nums, index + 1, end, item)
    except:
        raise ValueError("Value not found")

nums = [1,2,3,4,5,6,7,8,9,10,11]

print(binary_search(nums, 0, len(nums), 10))
