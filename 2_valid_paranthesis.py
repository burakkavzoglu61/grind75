class Solution:
    def is_matched(self,first, second):
        if first == "(" and second ==")":
            return True
        elif first == "{" and second =="}":
            return True
        if first == "[" and second =="]":
            return True
        return False
    def isValid(self, s: str) -> bool:
        stack = []

        for elem in s:
            if len(stack) == 0:
                stack.append(elem)
                continue
            if self.is_matched(stack[len(stack)-1], elem):
                stack.pop()
            else:
                stack.append(elem)
        return len(stack) == 0