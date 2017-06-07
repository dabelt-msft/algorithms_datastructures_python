import math

def largest_p_3(nums):
    h_p_3 = -math.inf
    l_p_2 = math.inf
    h_p_2 = -math.inf
    lowest = math.inf
    highest = -math.inf

    for i in range(0, len(nums)):

        if i >= 2:
            if nums[i] * l_p_2 > h_p_3:
                h_p_3 = nums[i] * l_p_2
            if nums[i] * h_p_2 > h_p_3:
                h_p_3 = nums[i] * h_p_2
        if i >= 1:
            if (nums[i] * lowest) < l_p_2:
                l_p_2 = nums[i] * lowest
            if (nums[i] * highest) < l_p_2:
                l_p_2 = nums[i] * highest
            if (nums[i] * lowest) > h_p_2:
                h_p_2 = nums[i] * lowest
            if (nums[i] * highest) > h_p_2:
                h_p_2 = nums[i] * highest
        if nums[i] < lowest:
            lowest = nums[i]
        if nums[i] > highest:
            highest = nums[i]

    return h_p_3

nums = [-2,2,-4,8,-10,9]

print(largest_p_3(nums))
