# Exercício 07 — Funções
#
# Parte A — Parâmetros:
# Escreva `saudacao(nome, saudacao="Olá", pontuacao="!")` que retorna a
# frase montada. Chame a função de 3 formas: só posicional, com argumento
# nomeado fora de ordem, e usando o valor padrão.
#
# Parte B — *args e **kwargs:
# Escreva `media(*numeros)` que aceita qualquer quantidade de números e
# retorna a média (retorne 0 se nenhum número for passado).
# Escreva `descrever(**dados)` que imprime cada chave e valor recebidos.
# Depois, chame `media` passando uma lista já existente (desempacotando com *).
#
# Parte C — Retorno múltiplo:
# Escreva `min_max(lista)` que retorna o menor e o maior valor SEM usar
# min() e max(). Receba o retorno em duas variáveis.
#
# Parte D — lambda e funções como argumento:
# Dada a lista:
#   pessoas = [("Ana", 30), ("Bruno", 25), ("Carla", 35)]
# Ordene por idade usando sorted() com key=lambda.
# Use map() para gerar uma lista só com os nomes e filter() para as pessoas
# com mais de 28 anos.
#
# Parte E — Armadilha clássica (responda em comentário):
# O que este código imprime? Por quê? Como corrigir?
#
#   def adicionar(item, lista=[]):
#       lista.append(item)
#       return lista
#
#   print(adicionar(1))
#   print(adicionar(2))
#
# Parte F — Escopo (responda em comentário):
# O que acontece aqui? Qual palavra-chave resolveria (e por que evitá-la)?
#
#   contador = 0
#   def incrementar():
#       contador += 1
#   incrementar()

