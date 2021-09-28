import os
from utils import open_file, close_file, get_all, get_one

#delete
def del_all():
  os.remove("reviews.txt")

def del_one():
  films = get_all()
  list = get_one(films)
  i = int(input("Escolha o filme: "))
  replacement = ""
  retrieved = open_file("read")
  if retrieved == False:
    print("Você ainda não possui reviews")
    return
  lines = retrieved.readlines()
  for x in range(0, len(lines)-1, 4):
    if list[i-1] in lines[x]:
      replacement += ""
    else:
      replacement += lines[x] + lines[x+1] + lines[x+2] + lines[x+3]
  close_file(retrieved)

  new_file = open_file("write")
  new_file.write(replacement)
  close_file(new_file)
