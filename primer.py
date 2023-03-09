import os
import re
import shutil


## Example pulls filenames from a dir, prints their relative and absolute paths
#def printdir(dir):
  #filenames = os.listdir(dir)
  #for filename in filenames:
    #print(filename)  ## foo.txt
    #print(os.path.join(dir, filename)) ## dir/foo.txt (relative to current dir)
    #print(os.path.abspath(os.path.join(dir, filename))) ## /home/nick/dir/foo.txt

#printdir(input())



def get_special_paths(dir):
  spisok = []
  filenames = os.listdir(dir)
  for filename in filenames:
    name_match = re.search(r'__(\w+)__', filename)
    if name_match:
      spisok.append(os.path.abspath(os.path.join(dir, filename)))
  print(spisok)

  return spisok

get_special_paths(r'C:\Users\Tamara\!Python_git\copyspecial')

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

