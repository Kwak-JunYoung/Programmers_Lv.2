def solution(priorities, location):
    rank = 1
    while True:
        if location == 0:
            if priorities[location] == max(priorities):
                return rank
            location = len(priorities)
            priorities.append(priorities.pop(0))            

        elif priorities[0] == max(priorities):
            priorities.pop(0)
            rank += 1

        elif priorities[0] != max(priorities):
            priorities.append(priorities.pop(0))
            
        location -= 1