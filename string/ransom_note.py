#Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

#Each letter in the magazine string can only be used once in your ransom note.

from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        return not Counter(ransomNote) - Counter(magazine)
        
        ## ORGINAL - Required edge case testing, better to use set subtraction
        ## any magazine can create ransom note
        #if not ransomNote:
        #    return True
        #if not magazine:
        #    return False
        #m = Counter(magazine)
        #r = Counter(ransomNote)
        # chars in ransomNote and not in magazine will be negative after mag_cnt.subtract(ran_cnt)
        #m.subtract(r)
        #return min(m.values()) >= 0
