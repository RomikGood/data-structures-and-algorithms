from .stack import Stack


def multi_bracket_validation(input):
    stack = Stack()
    for char in input:
        if char in ('{', '[', '(', ')', ']', '}'):
            for bracket in input:
                if bracket == ')':
                    if stack.length == 0 or stack.pop() != '(':
                        return False
                elif bracket == '}':
                    if stack.length == 0 or stack.pop() != '{':
                        return False
                elif bracket == ']':
                    if stack.length == 0 or stack.pop() != '[':
                        return False
                else:
                    stack.push(bracket)
                    return stack.length == 0


multi_bracket_validation('(5)')
