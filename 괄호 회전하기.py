def solution(s):
    answer = 0
    list_s = []
    length = len(s)
    b_set = [["(", ")"], ["{", "}"], ["[", "]"]]
    
    for b in s:
        list_s.append(b)
        
    if len(s) % 2 != 0:
        return 0
    
    for i in range(length):
        stack = []
        for bracket in list_s:
            if bracket in '({[':
                stack.append(bracket)
                
            if len(stack) != 0:
                top = stack[len(stack) - 1]
                if [top, bracket] in b_set:
                    stack.pop()
                    
        if len(stack) == 0:
            answer += 1
            
        popped = list_s.pop(0)
        list_s.append(popped)

    return answer