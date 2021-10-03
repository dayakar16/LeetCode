class Solution:
    def reverseWords(self, s: str) -> str:
        li = s.split(' ')
        for i,string in enumerate(li): 
            l = list(string)
            l[::] = l[::-1]
            li[i] = "".join(l)
            print(li[i])
        x = " ".join(li)
        return x
