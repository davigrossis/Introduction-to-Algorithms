# Exercício 13 — Desafio Final (integra todo o bloco)
#
# Crie um sistema simples de controle de notas no terminal com um menu em loop:
#
#   1 - Cadastrar aluno (nome + notas separadas por vírgula)
#   2 - Listar alunos com média e situação
#   3 - Buscar aluno por nome
#   4 - Estatísticas da turma
#   0 - Sair
#
# Requisitos:
#   - Armazene os dados em um dicionário {nome: [notas]}
#   - Cada funcionalidade deve ser uma função separada
#   - Situação: média >= 7 "Aprovado", 5 <= média < 7 "Recuperação", < 5 "Reprovado"
#   - Não deixe o programa quebrar com entrada inválida (letras nas notas,
#     notas fora de 0-10, opção de menu inexistente, nome duplicado)
#   - Nomes devem ser tratados sem diferenciar maiúsculas/minúsculas
#     e sem espaços extras nas pontas
#   - Estatísticas: média geral da turma, melhor aluno, pior aluno e
#     quantidade de alunos em cada situação
#   - Saída formatada com f-strings (médias com 1 casa decimal, colunas alinhadas)
#   - Use pelo menos uma list comprehension e uma dict comprehension
#   - Use `if __name__ == "__main__":` para iniciar o programa
#
# Pergunta conceitual (responda em comentário):
# Para que serve o `if __name__ == "__main__":`?

