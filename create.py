from utils import open_file, close_file
from settings import movie

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
