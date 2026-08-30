class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token not in {"+", "-", "*", "/"}:
                stack.append(int(token))
            else:
                right = stack.pop()
                left = stack.pop()

                if token == "+":
                    stack.append(left + right)
                elif token == "-":
                    stack.append(left - right)
                elif token == "*":
                    stack.append(left * right)
                else:
                    # Truncate toward zero
                    result = abs(left) // abs(right)

                    if (left < 0) != (right < 0):
                        result = -result

                    stack.append(result)

        return stack[-1]