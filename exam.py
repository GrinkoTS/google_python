s = input().split('-')
if len(s) == 4 and s[0] == '7':
    s = s[1:]
if len(s) == 3:
    for i in range(len(s)):
        if i < 2:
            for j in s:
                if len(j) == 3 and j.isdigit:
                    continue
                else:
                    print('NO')
            if i == 2:
                if len(j) == 4 and j.isdigit:
                    print('NO')
                else:
                    print('NO')
else:
    print('NO')