                st.pop()

            elif not st:
                return False

            elif s[i] == ')' and st[-1] == '(':
            elif s[i] == '}' and st[-1] == '{':
                st.pop()

            elif s[i] == ']' and st[-1] == '[':
                st.pop()

            else:
                return False

        return not st