class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n=len(temperatures)
        st= []
        res= [0] * n
        res[n-1]= 0
        st.append(n-1)
        for i in range(n-2, -1, -1):
            while st and temperatures[st[-1]] <= temperatures[i]:
            if not st:
                st.pop()
                res[i] = 0
            else:
                res[i] = st[-1] - i
            st.append(i)
        return res
