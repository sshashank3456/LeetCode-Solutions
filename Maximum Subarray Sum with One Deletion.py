    def maximumSum(self, arr: List[int]) -> int:
        nodelete = arr[0]
        onedelete = float('-inf')
        res = arr[0]
        for i in range(1, len(arr)):
            prevnodelete = nodelete
            prevonedelete = onedelete
            nodelete = max(nodelete + arr[i], arr[i])
            v2 = prevonedelete + arr[i]
            onedelete = max(v2, prevnodelete)
            res = max(res, nodelete, onedelete)
        return res
class Solution: