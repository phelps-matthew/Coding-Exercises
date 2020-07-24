# Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        # if negative, not palindrome
        # if first digit is zero, x must be zero
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        # get first half
        r = 0 # will form right have from end
        while x > r:
            # shift r a decimal place, add next digit of x
            r = r * 10 + x % 10
            x = x // 10
        # x == r (even length)
        # x == r//10 (odd length, discard middle number)
        return x == r or x == r//10
