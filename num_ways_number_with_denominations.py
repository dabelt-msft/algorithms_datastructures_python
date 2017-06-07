#number of ways to get a certain number with specific denominations provided


class Change:
    def __init__(self):
        self.memo = {}
        self.count = 0

    def change_possibilities_top_down(self, amount_left, denominations, current_index=0):

        # check our memo and short-circuit if we've already solved this one
        memo_key = str((amount_left, current_index))
        if memo_key in self.memo:
            print("grabbing memo{}".format(memo_key))
            return self.memo[memo_key]

        # base cases:
        # we hit the amount spot on. yes!
        if amount_left == 0:
            return 1

        # we overshot the amount left (used too many coins)
        if amount_left < 0:
            return 0

        # we're out of denominations
        if current_index >= len(denominations):
            return 0

        print("checking ways to make {} with {}".format(amount_left, denominations[current_index:]))

        # choose a current coin
        current_coin = denominations[current_index]

        # see how many possibilities we can get
        # for each number of times to use current_coin
        num_possibilities = 0
        while amount_left >= 0:
            print(self.count)
            num_possibilities += self.change_possibilities_top_down(amount_left, denominations, current_index + 1)
            self.count += 1
            # print(amount_left, current_coin)
            print(amount_left, " is amount left", current_index, " is current index")
            amount_left -= current_coin
            print("amount left after subtraction is ", amount_left)
            print(current_coin, "is current coin")


        # save the answer in our memo so we don't compute it again
        self.memo[memo_key] = num_possibilities
        return num_possibilities
nums = Change()
nums.change_possibilities_top_down(4, [1,2,3])

for key in nums.memo:
    print(key, nums.memo[key])