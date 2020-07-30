def palindromeRearranging(inputString):
    # count the number of each individual character
    # can form a palindrome only if:
    #   at most one of the character counts is odd, all others must be even

    l = list(inputString)
    chars = set(l)
    counts = sum([l.count(x) % 2 for x in chars])
    return counts <= 1

a = "aabb"
print(palindromeRearranging(a))
