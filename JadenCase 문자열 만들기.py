def solution(s):
    answer = ''
    before = ''
    for letter in s:
        if letter.isalpha and (before == '' or before == ' '):
            answer += letter.upper()
        else:
            answer += letter.lower()
        before = letter
    return answer