print("Кол-во сотрудников:", )
kolvo = int(input())

print("Расстояния до дома каждого сотрудника вводите через пробел: ")
a = input()
s = a.split()
i=0
dist = []
while i<len(s):
    j = int(s[i])
    dist.append(j)
    i+=1

print("Тарифы каждого таксиста вводите через пробел: ")
a = input()
s = a.split()
tarif = []
i=0
while i<len(s):
    j = int(s[i])
    tarif.append(j)
    i+=1

otvet=[]
i=0
while i<kolvo:
    otvet.append(0)
    i+=1
i=0
while i<kolvo:
    maxd = max(dist)
    num_human = dist.index(maxd)
    mint = min(tarif)
    num_taxi = tarif.index(mint)
    otvet[num_human] = num_taxi + 1
    dist[num_human] = -1
    tarif[num_taxi] = 10001
    i+=1

print("Распределение по машинам: ")
i=0
while i<len(otvet):
    print('Сотрудник номер', i+1, 'должен сесть в такси номер', otvet[i])
    i+=1