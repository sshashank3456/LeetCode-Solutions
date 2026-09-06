class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res= [-1] * n
        st= []
        for i in range(2* n-1, -1, -1):
            if i < n:
            st.append(nums[i %n])
                if st:
                    res[i] = st[-1]
                st.pop()
            while st and st[-1] <= nums[i % n]:
        return res