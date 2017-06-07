#Reverse a stack using only one other stack and a temp variable

def rev_stack(nums):
    temp = None
    s_s = list()
    for i in range(0, len(nums)):
        temp = nums.pop()
        while len(nums) > i:
            s_s.append(nums.pop())
        nums.append(temp)
        while s_s:
            nums.append(s_s.pop())
    return nums

nums = []
nums.append(5)
nums.append(4)
nums.append(3)
nums.append(2)
nums.append(1)
print(nums)
print(rev_stack(nums))