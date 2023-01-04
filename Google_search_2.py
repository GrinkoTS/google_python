lan = list()
n = int(input())
for i in range(n):
    a = input()
    lan.append(a)
n2 = int(input())
lan2 = []
counter = 0
for i in range(n2):
    slovo = input().lower()
    lan2.append(slovo)
lan3 = []
for num in lan:
    num1 = num.lower()
    for slovo2 in lan2:
        if slovo2 in num1:
            counter += 1
    if counter == n2:
        lan3.append(num)
    continue
print(lan3, sep='\n')
