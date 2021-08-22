def solution(n):
    answer = ''
    l = ['1', '2', '4']
    i = 0
    while n:
        for a in range(1, 4):
            if (n - (a * 3 ** i)) % (3 ** (i + 1)) == 0:
                answer += l[a-1]
                n -= (a * 3 ** i)
                break
        i += 1
    return answer[::-1]