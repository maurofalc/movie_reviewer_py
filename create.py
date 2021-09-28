from utils import open_file, close_file
from settings import movie

#create
def add_one():
  cont = 1
  file = open_file("append")
  busca = input("Procurar pelo filme: ")
  results = movie.search(busca)
  if results:
    for result in results:
      print(f"{cont} - {result['title']}")
      cont += 1
  else:
    print("Nenhuma correspondência encontrada!")
    return
  i = int(input("Digite o número do filme desejado: "))
  chosen = results[i - 1]
  print(f"> {chosen['title']} <")
  rating = int(input("Quantas estrelas? "))
  coment = input("Seus comentários sobre o filme: ")
  file.write(f"{chosen['id']}\n{chosen['title']}\n{rating}\n{coment}\n")
  close_file(file)
  print("Review adicionado com sucesso!!!")
