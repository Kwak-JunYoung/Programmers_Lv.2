import math
def solution(progresses, speeds):
    answer = []
    days = [math.ceil((100 - progresses[i]) / speeds[i]) for i in range(len(progresses))]
    pivot = 0
    count = 0
    for d in days:
        if days[pivot] >= d:
            count += 1
        else:
            answer.append(count)
            pivot = days.index(d)
            count = 1
    answer.append(count)
    return answer