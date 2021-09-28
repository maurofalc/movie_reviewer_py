from utils import get_all, get_one, scoring

#read
def list_all():
  films = get_all()
  if len(films) == 0:
    print("\nVocê ainda não possui reviews\n")
  for key, value in films.items():
    print("\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n")
    print(f"{value[0]}\n{scoring(int(value[1]))}\n{value[2]}")
    print("\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n")

def list_one():
  films = get_all()
  list = get_one(films)
  print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n")
  i = int(input("\nEscolha o filme: "))
  print("\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n")
  print(f"{films[list[i-1]][0]}\n{scoring(int(films[list[i-1]][1]))}\n{films[list[i-1]][2]}")
  print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n")
