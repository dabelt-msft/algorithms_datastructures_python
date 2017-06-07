def find_single_in_dups(nums, start, end):
    index = (start + end -1)//2
    if end - start == 1:
        return index
    if index % 2 == 0:
        #check right
        if nums[index] == nums[index + 1]:
            return find_single_in_dups(nums, index + 2, end)
        elif nums[index] == nums[index - 1]:
            return find_single_in_dups(nums, start, index - 2)
        else:
            return index
    else:
        if nums[index] == nums[index - 1]:
            return find_single_in_dups(nums, index + 1, end)
        else:
            return find_single_in_dups(nums, start, index)

nums = [1,2,2,3,3,4,4,5,5]

print(find_single_in_dups(nums, 0, len(nums)))
