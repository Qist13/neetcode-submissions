class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        paren_map = {')': '(', ']': '[', '}': '{'}

        for ch in s:
            if ch in paren_map:
                if stack and stack[-1] == paren_map[ch]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)

        return not stack