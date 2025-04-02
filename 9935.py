string = input()
bomb = list(input())
len_bomb = len(bomb)

stack = []
len_stack = 0
for word in string:
    stack.append(word)
    len_stack += 1
    if len_stack >= len_bomb and stack[len_stack-len_bomb:] == bomb:
        for i in range(len_bomb):
            stack.pop()
        len_stack -= len_bomb

for word in stack:
    print(word, end='')
if stack == []:
    print("FRULA")