counter = 0
s = input()
s = s.lower()
s = s.split()
x1 = s.count('a')
x2 = s.count('an')
x3 = s.count('the')
print('Общее количество артиклей:', x1 + x2 + x3)