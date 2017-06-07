def new_gen(iterable):
    counter = -1
    for item in iterable:
        if item > 6:
            return
        counter += 1
        if counter % 2 != 0:
            continue
        else:
            yield item


def run_new_gen(iterable):
    for item in new_gen(iterable):
        print(item)

# run_new_gen([0,1,2,3,4,5,6])

def avg(list):
    return sum(list)/len(list)

print(avg(list(x*x for x in range(1,100000) if x <= 3)))


def take(count, iterable):
    counter = 0
    for item in iterable:
        if counter == count:
            return
        counter += 1
        yield item


def run_take_when_needed(items):
    count = 0
    for item in take(7, items):
        if count % 2 == 0:
            print(item)
        count += 1


def run_take(items):
    for item in take(3, items):
        print(item)


def distinct(iterable):
    seen = set()
    for item in iterable:
        if item in seen:
            continue
        yield item
        seen.add(item)


def run_distinct(iterable):
    for item in distinct(iterable):
        print(item)


def run_pipeline(iterable):
    for item in take(3, distinct(iterable)):
        print(item)


if __name__ == '__main__':
    # run_take([1,2,3,4,5])
    # run_take([1,2,3,4])
    # run_distinct([1,2,1,1,1])
    run_pipeline([1,1,1,2,2,2,2,2,2,3,4,5])
