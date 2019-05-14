# Iterative solution
# Recursive solution
# Note: We need to be able to handle a scenario where a number won't be happy
# and will loop endlessly since the sum will never equal 1 (we could limit this
# to a timeout of maybe 50 loops max or something)
# Brainstorming:
class Solution:
    def sumSquaresOfDigits(self, num):
        temp = str(num)
        sum = 0
        for digit in temp:
            digit_val = int(digit)
            sum += digit_val ** 2
        print(sum)
        return sum

    def isHappy(self, n: int) -> bool:
        isHappyNum = False
        num_sum = self.sumSquaresOfDigits(n)
        timeout = 0
        while isHappyNum != True:
            if num_sum == 1:
                return True
            elif timeout == 50:
                return False
            else:
                num_sum = self.sumSquaresOfDigits(num_sum)
                timeout += 1
