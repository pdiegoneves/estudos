a = int(input('Primeiro bimestre: '))
while a > 10 or a < 0:
    a = int(input('Você digitou errado. Primeiro Bimestre: '))
b = int(input('Segundo bimestre: '))
while b > 10 or b < 0:
    b = int(input('Você digitou errado. Segundo Bimestre: '))
c = int(input('Terceiro bimestre: '))
while c > 10 or c < 0:
    c = int(input('Você digitou errado. Teceiro Bimestre: '))
d = int(input('Quarto bimestre: '))
while d > 10 or d < 0:
    d = int(input('Você digitou errado. Quarto Bimestre: '))
media = (a + b + c + d) / 4
print('media: {}'.format(media))


# nota = int(input('Entre com a nota: '))
# while nota > 10:
#   nota = int(input('Nota inválida. Entre com a nota correta: '))
#   if nota <= 10:
#     print('Nota: {}'.format(nota))


# a = 0
# while a <= 10:
#   print(a)
#   a += 1

# a = int(input('Entre com um valor: '))
# for num in range(a+1):
#     div = 0
#     for x in range(1, num+1):
#         resto = num % x
#         # print(x, resto)
#         if resto == 0:
#             div += 1
#     if div == 2:
#         print(num)


# a = int(input('Entre com um número: '))

# div = 0
# for x in range(1, a+1):
#   resto = a % x
#   print(x, resto)
#   if(resto == 0):
#     div += 1

# if(div == 2):
#   print('número {} é primo'.format(a))
# else:
#   print('número {} não é primo'.format(a))


# for x in range(101):
#   print(x)
