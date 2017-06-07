def product_of_ints_except_at_index(nums):
    prods = [None] * len(nums)
    product_so_far = 1

    if len(nums) < 2:
        raise IndexError("Need at least to integers")

    for i in range(0, len(nums)):
        prods[i] = product_so_far
        product_so_far *= nums[i]

    product_so_far = 1

    for i in range(len(nums)-1, -1, -1):
        prods[i] *= product_so_far
        product_so_far *= nums[i]

    return prods


nums = [1,2,6,5,9]

print(product_of_ints_except_at_index(nums))