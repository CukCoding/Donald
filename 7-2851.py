mushroom = []
score = 0
result = 0

for i in range(10):
    mushroom.append(int(input()))

for i in mushroom:
    score += i
    result = score
    if score >= 100:
        if abs(100 - score) > abs(100 - (score - i)):
            result = score - i
        break

print(result)