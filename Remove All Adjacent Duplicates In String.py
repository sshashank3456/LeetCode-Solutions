        for i in range(n):
            if not st:
                st.append(s[i])
             
                continue
            if st[-1]== s[i]:
                st.pop()
                continue
            else:
                st.append(s[i])
        while st:
            res.append(st[-1])
            st.pop()
        res.reverse()
        return ''.join(res)
