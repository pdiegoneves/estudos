lista = [1, 10]
try:
  arquivo = open('teste.txt', 'r')
  texto = arquivo.read()
  divisao = 10 / 1
  numero = lista[1]
except ZeroDivisionError:
  print('Não é possível realizar uma divisão por zero')
except IndexError:
  print('Erro ao acessar um indicie inválido da lista')
except BaseException as ex:
  print('erro desconhecido. Erro: {}'.format(ex))
else:
  print('Executa quando não ocorre nenhuma exceção')
finally:
  print('Sempre executa')
  print('Fechando arquivo')
  arquivo.close()