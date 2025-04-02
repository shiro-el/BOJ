Infix = input()

Oper = {}
Oper['+'] = 2
Oper['-'] = 2
Oper['*'] = 1
Oper['/'] = 1
Oper['('] = 3

OpStack = []
Postfix = []

for token in Infix:
    if token in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        Postfix.append(token)

    elif token == '(':
        OpStack.append('(')

    elif token == ')':
        while OpStack[-1] != '(':
            Postfix.append(OpStack.pop())
        OpStack.pop()

    else:
        while OpStack != [] and Oper[OpStack[-1]] <= Oper[token]:
            Postfix.append(OpStack.pop())
        OpStack.append(token)

for i in range(len(OpStack)):
    Postfix.append(OpStack.pop())

print(*Postfix, sep='')