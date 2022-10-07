class Solution:
    
    def makeGood(self, s: str) -> str:
        stack = []
        output = ""
        for char in s:
            if len(stack)==0:
                stack.append(char)
            else:
                if abs(ord(stack[len(stack)-1])-ord(char))==32:
                    stack.pop()
                else:
                    stack.append(char)
        
        while(len(stack)!=0):
            output+=stack.pop()
        return output[::-1]
        