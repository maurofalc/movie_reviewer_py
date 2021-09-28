from utils import get_all, get_one, scoring

#read
def list_all():
  films = get_all()
  if len(films) == 0:
    print("Você ainda não possui reviews")
  for key, value in films.items():
    print("\n/=======================\\")
    print(f"{value[0]}\n{scoring(int(value[1]))}\n{value[2]}")
    print("/=======================\\\n")

def list_one():
  films = get_all()
  list = get_one(films)
  print("/=======================\\\n")
  i = int(input("Escolha o filme: "))
  print("\n/=======================\\")
  print(f"{films[list[i-1]][0]}\n{films[list[i-1]][1]} estrelas\n{films[list[i-1]][2]}")
  print("/=======================\\\n")
