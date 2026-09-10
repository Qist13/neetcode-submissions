class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        paren_map = {
            '}': '{',
            "]": '[',
            ")": "("
        }

        for ch in s:
            if ch in paren_map.values():
                stack.append(ch)
            elif ch in paren_map.keys():
                if not (stack and stack[-1] == paren_map[ch]):
                    return False

                stack.pop()

        return not bool(stack)