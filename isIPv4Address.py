def isIPv4Address(s):
    try:
        nums = s.split(".")
        if len(nums) != 4:
            return False
        for n in nums:
            if len(str(int(n))) < len(n):
                return False
            elif int(n) < 0 or int(n) > 255:
                return False
        return True
    except ValueError:
        return False


s = "172.316.254.1"
print(isIPv4Address(s))
