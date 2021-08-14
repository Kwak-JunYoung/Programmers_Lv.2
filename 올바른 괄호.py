def solution(s):
    answer = True
    length = len(s)
    stack = []

    for i in range(length):
        if s[i] == '(':
            stack.append(s[i])
        else:
            if len(stack) != 0:
                stack.pop()
            else:
                answer = False

    if len(stack) != 0:
        answer = False
    return answer