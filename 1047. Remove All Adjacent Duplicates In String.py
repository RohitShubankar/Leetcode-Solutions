class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        output = ""
        for char in s:
            if (len(stack)==0):
                stack.append(char)
            elif(len(stack)!=0):
                if(char==stack[len(stack)-1]):
                    stack.pop()
                else:
                    stack.append(char)
        while(len(stack)!=0):
            output+=stack.pop()
        output = output[::-1]
        return output
    
                           