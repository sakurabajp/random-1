import random

point = 4
Mpoint = 1000
countA = 0
countB = 0

for num in range(1000):
    Rnum = random.randint(1, Mpoint)
    if Rnum <= point:
        print("あたり！")
        countA = countA + 1
    elif Rnum != point:
        print("はずれ！")
        countB = countB + 1

probability = (point / Mpoint) * 100

print("確率→", probability, "\n出力回数→", num + 1)
print("アタリの出た数→", countA, "\nハズレの出た数→", countB)
print("確率結果→", (countA / (countA + countB)) * 100)
