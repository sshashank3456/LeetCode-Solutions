class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        n=len(arr)
        nodel= arr[0]
        onedel= float('-inf')
        res= arr[0]
        for i in range(1, n):
            prevnodel= nodel
            prevonedel= onedel
            nodel= max(nodel + arr[i], arr[i])
            v2= prevonedel + arr[i]
            onedel= max(v2, prevnodel)
            res= max(res, onedel, nodel)
        return res