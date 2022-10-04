# Stack Solution 
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        # Stack Solution 
        stack1 = []
        stack2 = []
        for char in s:
            if char =="#":
                if(len(stack1)==0):
                    continue
                else:
                    stack1.pop()
            else:
                stack1.append(char)
        for char in t:
            if char == "#":
                if(len(stack2)==0):
                    continue
                else:
                    stack2.pop()
            else:
                stack2.append(char)
        if stack1==stack2:
            return True
        else:
            return False
        