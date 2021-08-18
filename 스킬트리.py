def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        stack = ''
        for my_skill in skill_tree:
            if my_skill in skill:
                stack += my_skill
        stack_size = len(stack)
        legit = True
        for i in range(stack_size):
            if stack[i] != skill[i]:
                legit = False
        if legit == True:
            answer += 1

    return answer