# We have two special characters. The first character can be represented by one bit 0. The second character can be represented by two bits (10 or 11).

# Now given a string represented by several bits. Return whether the last character must be a one-bit character or not. The given string will always end with a zero.

class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i = 0
        # iterating backward, if bits[i]=1, skip next number
        # [a,..,x,y,z] minimal scenarios below
        #   for i=index(x), if x=1 then i->index(z) True
        #   for i=index(y), if y=1 then i->index(z)+1 False
        #   for i=index(y), if y=0 then i->index(z) True
        while i < len(bits)-1:
            if bits[i]:
                i += 2
            else:
                i += 1
        return i == len(bits) - 1
    # we could combine conditional statement into i += bits[i] + 1

