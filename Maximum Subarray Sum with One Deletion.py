class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        nodelete= arr[0]
        onedelete= float('-inf')
        for i in range(1, len(arr)):
            prevnodelete= nodelete
            prevonedelete= onedelete
            nodelete= max(nodelete + arr[i], arr[i])
            v2= prevonedelete+ arr[i]
            onedelete= max(prevnodelete, v2)
            res= max(res, max(onedelete, nodelete))
        return res
        res=arr[0]
