# coding: utf-8
# a = 10
# b = 5
a = int(input('Entre com o primeiro valor: '))
b = int(input('Entre com o segundo valor: '))


soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b
resultado = ('Soma: {soma}\n'
      'Subtração: {sub}\n'
      'Multiplicação: {multi}\n'
      'Resto: {resto}\n'
      'Divisão: {div}'.format(soma=soma,
                               sub=subtracao,
                               multi=multiplicacao,
                               div=divisao,
                               resto=resto))

print(resultado)

# print('soma: ' + str(soma))
# print('sutracao: ' + str(subtracao))
# print(multiplicacao)
# print(divisao)
# print(int(divisao))
# print(resto)


# x = '1'
# soma2 = int(x) + 1
# print(soma2)
