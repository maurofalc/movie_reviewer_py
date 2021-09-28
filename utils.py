import os

def open_file(mode):
  if mode == "read":
    if os.path.exists("reviews.txt"):
      file = open("reviews.txt", "r", encoding="utf-8")
    else:
      file = False
  elif mode == "append":
    file = open("reviews.txt", "a", encoding="utf-8")
  elif mode == "write":
    file = open("reviews.txt", "w", encoding="utf-8")
  return file

def close_file(file):
  file.close()

def get_all():
  aux = 0
  films = {}
  retrieved = open_file("read")
  if retrieved == False:
    return films
  lines = retrieved.readlines()
  while aux < len(lines) - 1:
    films[lines[aux].strip()] = [
      lines[aux+1].strip(),
      lines[aux+2].strip(),
      lines[aux+3].strip()
    ]
    aux += 4
  close_file(retrieved)
  return films

def get_one(films):
  cont = 1
  aux = []
  for key, value in films.items():
    print(f"{cont} - {value[0]}")
    aux.append(key)
    cont += 1
  return aux

def scoring(stars):
  return stars * '⭐️'

def clear():
  os.system("clear")
