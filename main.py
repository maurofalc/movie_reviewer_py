from tmdbv3api import TMDb, Movie
import os

#TMDb settings
tmdb = TMDb()
tmdb.api_key = "f4bba9678e3e06682db882a5dcbbeb51"
tmdb.language = 'pt'
movie = Movie()

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
  if len(films) == 0:
    print("Você ainda não possui reviews")
  print("\n/=======================\\")
  print("Seus reviews:\n")
  for key, value in films.items():
    print(f"{cont} - {value[0]}")
    aux.append(key)
    cont += 1
  return aux

#create
def add_one():
  file = open_file("append")
  busca = input("Procurar pelo filme: ")
  results = movie.search(busca)
  if results:
    result = results[0]
  else:
    print("Nenhuma correspondência encontrada!")
    return
  print(result)
  rating = int(input("Quantas estrelas? "))
  coment = input("Seus comentários sobre o filme: ")
  file.write(f"{result['id']}\n{result['title']}\n{rating}\n{coment}\n")
  close_file(file)

#read
def list_all():
  films = get_all()
  if len(films) == 0:
    print("Você ainda não possui reviews")
  for key, value in films.items():
    print("\n/=======================\\")
    print(f"{value[0]}\n{value[1]} estrelas\n{value[2]}")
    print("/=======================\\\n")

def list_one():
  films = get_all()
  list = get_one(films)
  print("/=======================\\\n")
  i = int(input("Escolha o filme: "))
  print("\n/=======================\\")
  print(f"{films[list[i-1]][0]}\n{films[list[i-1]][1]} estrelas\n{films[list[i-1]][2]}")
  print("/=======================\\\n")

def rewrite():
  replacement = ""
  retrieved = open_file("read")
  if retrieved == False:
    print("Você ainda não possui reviews")
    return

#update
def update_one():
  films = get_all()
  list = get_one(films)
  i = int(input("Escolha o filme: "))
  new_rating = input("Novas estrelas? ")
  new_coment = input("Novos comentários sobre o filme: ")
  retrieved = open_file("read")
  replacement = ""
  if retrieved == False:
    print("Você ainda não possui reviews")
    return
  lines = retrieved.readlines()
  for x in range(0, len(lines)-1, 4):
    if list[i-1] in lines[x]:
      replacement += lines[x] + lines[x+1] + new_rating + "\n" + new_coment + "\n"
    else:
      replacement += lines[x] + lines[x+1] + lines[x+2] + lines[x+3]
  close_file(retrieved)

  new_file = open_file("write")
  new_file.write(replacement)
  close_file(new_file)

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

def show_menu():
  print("1 - Adicionar um review")
  print("2 - Listar todos os reviews")
  print("3 - Exibir review de um filme")
  print("4 - Atualizar um review")
  print("5 - Deletar todos os reviews")
  print("6 - Deletar um review")
  print("Outro - Encerrar programa")

def main():
  show_menu()
  stop = False
  while (not stop):
    opt = int(input("\nSelecione a opção desejada: "))
    if opt < 1 or opt > 6:
      print("Encerrando...")
      stop = True
    else:
      if opt == 1:
        add_one()
      elif opt == 2:
        list_all()
      elif opt == 3:
        list_one()
      elif opt == 4:
        update_one()
      elif opt == 5:
        del_all()
      elif opt == 6:
        del_one()

main()
