class Solution:
    def romanToInt(self, s: str) -> int:
        map_a = {'I' : 1, 'V': 5, 'X': 10, 'L': 50, 'C':100, 'D':500, 'M':1000}
        map_b = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
        count = 0
        # can only be one occurance
        for key in map_b.keys():
            if key in s:
                count += map_b[key]
                s = s.replace(key,'')
        # may have multiple occurances
        while len(s) > 0:
            for key in map_a.keys():
                if key in s:
                    count += s.count(key) * map_a[key]
                    s = s.replace(key,'')
        return count

    ## Much better, from discussion ##
    # Iterate L->R through str; if s[i] < s[i+1] then subtract!

def romanToInt(self, s):
    roman = {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
    z = 0
    for i in range(0, len(s) - 1):
        if roman[s[i]] < roman[s[i+1]]:
            z -= roman[s[i]]
        else:
            z += roman[s[i]]
    return z + roman[s[-1]]
