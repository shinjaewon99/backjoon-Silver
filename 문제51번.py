def solution(n):
    answer = 0
    for i in range(n):
        if n % 2 == 0:
            answer.append(i)
   
    return answer