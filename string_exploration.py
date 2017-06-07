from collections import deque

def reverse(text):
    items = deque()
    for item in text:
        items.appendleft(item)

    return ''.join(items)

print(reverse("asdfadsf"))

def is_unique(text):
    sort = ''.join(sorted(text))
    i = 0
    j = i + 1
    l = sort[i]
    r = sort[j]
    while j < len(sort):
        if l == r:
            return False
        i += 1
        j += 1
    return type(sort)

def is_unique_optimized_for_time(text):
    items = set()
    for chr in text:
        if chr in items:
            return False
        else:
            items.add(chr)
    return True

print(is_unique_optimized_for_time("asfd"))

arr = [1,2,3,4,5,6]

def swap_in_place(arr):
    for i in range(0, (len(arr)-1)//2 + 1):
        arr[len(arr) -1 -i], arr[i] = arr[i], arr[len(arr) -1 -i]
    return arr

def count_chars_util(text):
    count = {}
    for chr in text:
        if chr in count:
            count[chr] += 1
        else:
            count[chr] = 1
    return count

def perm(text1, text2):
    first = count_chars_util(text1)
    second = count_chars_util(text2)

    for key, value in first.items():
        if second[key] != value:
            return False
    return True

# print(swap_in_place(arr))

print(perm("asdfasdf","asdfasdf"))

def perm_pal(text):

    count = {}
    odd = 0

    for chr in text:
        if chr in count:
            count[chr] += 1
        else:
            count[chr] = 1

    for key in count:
        if count[key] % 2 != 0:
            odd += 1
        if odd > 1:
            return False
    return True

print(perm_pal("a"))



