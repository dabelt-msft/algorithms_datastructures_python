import sys

class largest_sum_of_ints:
    def __init__(self):
        self.total = 0
        self.multiple = 1
        self.largest = -sys.maxsize
        self.num = False


    def add_to_largest_and_reset_util(self):
        if self.total > self.largest:
            self.largest = self.total
        self.total = 0
        self.multiple = 1
        return self.largest


    def calculate_largest(self, str):
        for i in range(0, len(str)):
            if str[i].isdigit():
                self.num = True
            else:
                self.num = False
            if self.num:
                self.total *= self.multiple
                self.total += int(str[i])
                if self.multiple == 1:
                    self.multiple *= 10
                if i == len(str) - 1:
                  self.add_to_largest_and_reset_util()
            elif self.total != 0:
                self.add_to_largest_and_reset_util()
        return self.largest

largest = largest_sum_of_ints()
print(largest.calculate_largest("asdf131231cae323423423432"))