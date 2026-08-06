class Solution:
    def countBits(self, n: int) -> List[int]:
        nlist = [0]
        for i in range(1,n+1):
            i = list(str(bin(i)))
            i= i.count("1")
            nlist.append(i)
        return nlist 