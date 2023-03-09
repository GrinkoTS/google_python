import sys
import re
import os
import shutil

spisok1= []

for adress, dirs, files in os.walk('C:\\Users\Tamara\!Python_git\\babynames'):
    for j in files:
        if ('.html' in j) and ('.summary' not in j):
            spisok1.append(j)
    print(spisok1)

for spis in spisok1:
    print(os.path.abspath(spis))
    #p = os.path.abspath(spis)
    #print(filenames)



def extract_names(filename):
    babies = []
    f = open(filename, 'r')
    text = f.read()
    year = re.search(r'Popularity\sin\s(\d\d\d\d)', text)
    if not year:
        print('None this year')
    else:
        year1 = year.group(1)
        babies.append(year1)



    name_match = re.findall(r'<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>', text)

    boys = []
    girls = []

    for name in name_match:
        boy = name[1] + ' ' + name[0]
        boys.append(boy)
        girl = name[2] + ' ' + name[0]
        girls.append(girl)

    all_baby = boys + girls
    all_baby= sorted(all_baby)
    babies.extend(all_baby)
    #for baby in babies:
        #print(baby)


    sum_file = open(filename + '.summary', 'w')
    list_of_names = '\n'.join(babies)
    sum_file.write(list_of_names)
    sum_file.close()

    return babies
    return spisok1
    return girls
    return boys

for spis in spisok1:
    extract_names(spis)

    ###до данной точки все работает, дальше надо составить список имен и место их в файле

spisok2 = []
for adress, dirs, files in os.walk('C:\\Users\Tamara\!Python_git\\babynames'):
    for j in files:
        if ('.summary' in j):
            spisok2.append(j)
print(spisok2)

for spis2 in spisok2:
    rab = []
    with open(spis2) as text2:
        name_poisk = input()
        text2 = spis2.readline()
        for line in text2:
            if name_poisk in line:
                rab.append(line)
    print(rab)









