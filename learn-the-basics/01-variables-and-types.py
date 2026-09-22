# Exercício 01 — Variáveis e Tipos de Dados
#
# Parte A (sem rodar o código, responda em comentário):
# Qual o tipo e o valor final de cada variável abaixo? Explique os casos surpreendentes.
#
#   a = 7 / 2 - float , 3,5
#   b = 7 // 2 - integer , 3
#   c = -7 // 2 - integer, -4
#   d = 7 % -2 - integer, -1
#   e = 2 ** -1 - float, 2^-1 == 0,5
#   f = 0.1 + 0.2 == 0.3 - False, 0,3000000004
#   g = "3" * 3 - string, "333"
#   h = True + True = integer, 2
#   i = None - None
#   j = 1_000_000 - integer ,1000000
#

#
# Parte B:
# Escreva um programa que pede ao usuário nome, idade e altura (em metros)
# e imprime em UMA única linha, usando f-string:
#   "Olá, Davi! Você tem 25 anos e 1.80m de altura."
# A altura deve sempre aparecer com 2 casas decimais, mesmo que o usuário digite "1.8".
#
nome = input("Qual seu nome? ")
idade = int(input("Qual sua idade? "))
altura = float(input("Qual sua altura? (em metros)"))

print(f"Olá, {nome}! Você tem {idade} anos e {altura:.2f}m de altura.")
#
# Parte C:
# Troque o valor de duas variáveis `x` e `y` SEM usar uma variável auxiliar.
x = 2
y = 3
print(x, y)   # 2 3

x, y = y, x

print(x, y) # 3 2
