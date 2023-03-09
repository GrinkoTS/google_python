import os
import re

#os.startfile(r'C:\Users\Tamara\!Python_git\copyspecial\xyz__hello__.txt')

#filenames = os.listdir(r'C:\Users\Tamara\!Python_git\copyspecial')
#spisok = []
#for filename in filenames:
    #name_match = re.search(r'__(\w+)__', filename)
    #if name_match:
        #spisok.append(os.path.abspath(os.path.join(r'C:\Users\Tamara\!Python_git\copyspecial', filename)))
#print(spisok)


pathss = (r'C:\Users\Tamara\!Python_git\copyspecial')
filenames = os.listdir(pathss)
print(filenames)
for filename in filenames:
  name_match = re.search(r'__(\w+)__', filename)
  print(os.path.join(pathss, filename))
  print(os.path.abspath(filename))




def copy_to(pathss, dir2):
  filenames = os.listdir(dir)
  for filename in filenames:
    name_match = re.search(r'__(\w+)__', filename)
    if name_match:
      os.makedirs(r'C:\Users\Tamara\!Python_git\copyspecial\fooby')
      shutil.copyfile(r'C:\Users\Tamara\!Python_git\copyspecial', os.path.join(r'C:\Users\Tamara\!Python_git\copyspecial\fooby', filename))

pathss = (r'C:\\Users\\Tamara\\!Python_git\\copyspecial\\xyz__hello__.txt')
dir = (r'C:\Users\Tamara\!Python_git\copyspecial')
copy_to(pathss, dir)

