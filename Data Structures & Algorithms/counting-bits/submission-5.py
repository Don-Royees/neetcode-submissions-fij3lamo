class Solution:
    def countBits(self, n: int) -> List[int]:
        nlist = []
        for i in range(n+1):
            i = list(str(bin(i)))
            i= i.count("1")
            nlist.append(i)
        return nlist 