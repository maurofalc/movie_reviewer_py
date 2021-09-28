from create import add_one
from read import list_all, list_one
from update import update_one
from delete import del_all, del_one

print("1 - Adicionar um review")
print("2 - Listar todos os reviews")
print("3 - Exibir review de um filme")
print("4 - Atualizar um review")
print("5 - Deletar todos os reviews")
print("6 - Deletar um review")
print("Outro - Encerrar programa")

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