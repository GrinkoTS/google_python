import sys
import re
import os
import shutil


spisok2 = []
for adress, dirs, files in os.walk('C:\\Users\Tamara\!Python_git\\babynames'):
    for j in files:
        if ('.summary' in j):
            spisok2.append(j)
print(spisok2)

for spis2 in spisok2:
    rab = []
    f = open(spis2, 'r')
    text2 = f.read()
    name_match_find = re.search(input(), text2)
    if name_match_find:
        name1 = name_match_find.group(1)
        rab.append(name1)
    print(rab)