class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        # return bin(n).count('1') == 1 -> Alternate version
        return not (n & (n-1))