from utils import open_file, close_file, get_all, get_one

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