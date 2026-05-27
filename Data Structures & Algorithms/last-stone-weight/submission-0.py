class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        while len(stones) > 1:
            stones.sort(reverse=True)
            x = max(stones[0], stones[1])
            y = min(stones[0], stones[1])

            if x == y:
                stones = stones[2:]
            else:
                stones = stones[2:]
                stones.append(x - y)
        
        return stones[0] if stones else 0
        