#Find lexicographically next greater permutation of numbers
    def nextPermutation(num):
        f_L=len(num)-1
        m_L=f_L
        while m_L>0:
            if num[m_L-1]<num[m_L]:
                break
            m_L-=1
        
        if m_L==0:
            num.reverse()
        else:
            for n in range(f_L,m_L-1,-1):
                if num[n]>num[m_L-1]:
                    break
            num[n],num[m_L-1]=num[m_L-1],num[n]
            
            num[m_L:]=reversed(num[m_L:])
        return num