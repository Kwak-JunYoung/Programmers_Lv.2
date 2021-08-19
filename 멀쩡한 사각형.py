import math
def solution(w,h):
    answer = w * h
    # 잘린 종이가 없다는 가정하에 초기화
    comdi = math.gcd(w, h)
    # 수행 시간을 줄이기 위해 최대공약수를 따로 구해놓음
    impossible = 0
    # 사용 불가능한 종이의 개수    
    
    mov = h / w
    # w가 한 칸 이동할 때 h가 움직이는 거리
    limit = w // comdi + 1
    # 최대공약수로 나누어 그 연산 시간을 줄임. 후에 곱셈 한번으로 올바른 답을 찾을 수 있음
    
    if w == 1 or h == 1:
        return 0
    elif w == h:
        return w * (h - 1)
    
    for i in range(1, limit):
        impossible += (math.ceil(mov * i) - math.floor(mov * (i - 1)))
        
    impossible *= comdi
    return answer - impossible