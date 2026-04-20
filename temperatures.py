def temperatures_answer(temperatures):
    n = len(temperatures)
    answer = [0] * n
    for i in range(n):
        for j in range(i, n):
            if temperatures[j] > temperatures[i]:
                answer[i] = j - i
                break
    return answer
temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
print(temperatures_answer(temperatures))
