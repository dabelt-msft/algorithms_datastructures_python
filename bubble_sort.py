def swap(nums, cur_i):
    nums[cur_i], nums[cur_i + 1] = nums[cur_i + 1], nums[cur_i]

def bubble_sort(n, nums):
    swap_count = 0
    count = 0

    for i in range(0, len(nums)):
        for j in range(0, len(nums) - 1 - count):
            if nums[j] > nums[j+1]:
                swap(nums, j)
                swap_count += 1
        count+=1
    return "Array is sorted in {0} swaps.\n" \
           "First Element: {1}\n" \
           "Last Element: {2}\n".format(swap_count, nums[0], nums[-1])

def main():
    n = int(input().strip())
    a = list(map(int, input().strip().split(' ')))
    print(bubble_sort(n, a))
if __name__ == "__main__":
    main()


