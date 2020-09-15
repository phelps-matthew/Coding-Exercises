# Does not quite work. Returns RuntimeError from set changing size during iteration
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def permute_recur(k, S, U):
            try:
                for e in U:
                    S.append(e)
                    U.remove(e)
                    if k==1:
                        print(S)
                        return
                    else:
                        permute_recur(k-1, S, U)
                    U.add(S.pop())
            except RuntimeError:
                pass
        return permute_recur(len(nums), [], set(nums))
