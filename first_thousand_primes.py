
from itertools import islice, count
from math import sqrt

#islice allows for lazy slicing
#range requires bounds but count doesn't
#count() provides an open ended version of range



def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(sqrt(x) + 1)):
        if x % i == 0:
            return False
    return True

test = islice((x for x in count() if is_prime(x)), 1000)
print(len(list(test)))

items = [1,2,3,4,5]

def lazy_slice(items):
    for item in items:
        yield item



print(list(islice(lazy_slice(items),5)))

print(any([False, False, False, True, False]))

print(all([True, True, False]))

for x in list(x for x in range(1,100) if is_prime(x)):
    print(x)

print(any(is_prime(x) for x in range(1,100)))