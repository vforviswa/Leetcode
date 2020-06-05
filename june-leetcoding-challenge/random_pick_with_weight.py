class Solution:

    def __init__(self, w: List[int]):
        for i in range(1, len(w)):
            w[i] += w[i-1]
        self.weights = w

    def pickIndex(self) -> int:
        target = random.randint(1, self.weights[-1])
        left, right = 0, len(self.weights) - 1
        while(left < right):
            mid = left + (right-left)//2
            if target > self.weights[mid]:
                left = mid + 1
            else:
                right = mid
        return left


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()