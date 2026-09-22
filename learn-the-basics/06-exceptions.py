# Exercício 06 — Exceções
#
# Parte A — Entrada segura:
# Escreva uma função `ler_inteiro(mensagem)` que pede um número ao usuário e
# continua pedindo até receber um inteiro válido. Deve tratar ValueError.
#
# Parte B — Divisão segura:
# Escreva `dividir(a, b)` que:
#   - retorna a / b
#   - trata ZeroDivisionError imprimindo uma mensagem amigável e retornando None
#   - trata TypeError (ex.: dividir("10", 2))
#   - usa `else` para imprimir "Divisão feita com sucesso"
#   - usa `finally` para imprimir "Fim da operação"
# Explique em comentário quando cada bloco (try/except/else/finally) executa.
#
# Parte C — Exceção própria:
# Crie uma exceção `SaldoInsuficienteError` (herdando de Exception).
# Escreva `sacar(saldo, valor)` que levanta (`raise`) essa exceção quando
# valor > saldo e ValueError quando valor <= 0. Chame a função num try/except
# que trata os dois casos de forma diferente.
#
# Pergunta conceitual (responda em comentário):
# Por que `except:` (sem tipo) ou `except Exception:` genérico é considerado
# má prática na maioria dos casos?

