def is_operator(op):
    return op in "+-*/"

def to_infix(expression):
    stack = []
    for token in reversed(expression):
        if is_operator(token):
            operand1 = stack.pop()
            operand2 = stack.pop()
            stack.append(f"({operand1} {token} {operand2})")
        else:
            stack.append(token)

    return stack[0]

def to_postfix(infix):
    stack = []
    postfix = []
    
    operator_priority = {"+": 0, "-": 0, "*": 1, "/": 1}
    
    for token in infix:
        if token.isdigit():
            postfix.append(token)
        elif is_operator(token):
            while stack and is_operator(stack[-1]) and operator_priority[stack[-1]] >= operator_priority[token]:
                postfix.append(stack.pop())
            stack.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                postfix.append(stack.pop())
            stack.pop()
        
    while stack:
        postfix.append(stack.pop())
    
    return postfix

prefix_expression = ['*','1','+','3','*','-','5','+','*','7','9','2','+','-','4','6','8']
infix_expression = to_infix(prefix_expression)
print("Выражение в инфиксной форме:", infix_expression)
print("Выражение в постфиксной форме:", to_postfix(infix_expression))
print('\nМой вариант 9 в первом задании это вариант номер 7 во втором задании')
