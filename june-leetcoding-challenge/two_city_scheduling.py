class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        minimum = 0
        costs.sort(key=lambda x: x[0] - x[1], reverse=True)
        costs_len = len(costs)
        for idx in range(costs_len):
            if idx < costs_len//2:
                minimum += costs[idx][1]
            else:
                minimum += costs[idx][0]
        return minimum