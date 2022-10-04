class Solution:
    def calPoints(self, operations: List[str]) -> int:
        s = []
        for i in range(len(operations)):
            if operations[i]=='C':
                s.pop()
            elif operations[i]=='D':
                s.append(2*s[len(s)-1])
            elif operations[i]=='+':
                a = s[len(s)-1]
                b= s[len(s)-2]
                s.append(a+b)
            else:
                s.append(int(operations[i]))
        return sum(s)
    