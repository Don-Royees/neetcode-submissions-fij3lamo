class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            rock1 = max(stones)
            stones.remove(rock1)
            rock2 = max(stones)
            stones.remove(rock2)
            leftover = abs(rock1 - rock2)
            stones.append(leftover)
        return stones[0] 