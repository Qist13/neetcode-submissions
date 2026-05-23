class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        valid_operations = {"+", "-", "*", "/"}
        num_stack = []

        for token in tokens:
            if token in valid_operations:
                num1 = num_stack.pop()
                num2 = num_stack.pop()
                result = 0
                if token == "+":
                    result = num2 + num1
                elif token == "-":
                    result = num2 - num1
                elif token == "*":
                    result = num2 * num1
                elif token == "/":
                    result = int(num2 / num1)
                num_stack.append(result)
            else:
                num_stack.append(int(token))
        
        return num_stack[0]