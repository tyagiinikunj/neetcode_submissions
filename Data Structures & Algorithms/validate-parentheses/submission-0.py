class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        hashmap={")" : "(","}" : "{" ,"]" : "[" }
        for i in s:
            if i in hashmap:
                if st and st[-1] == hashmap[i]:
                    st.pop()
                else:
                    return False
            else:
                st.append(i)
        return True if not st else False
        
        