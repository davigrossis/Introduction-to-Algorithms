# Exercício 12 — Dicionários
#
# Parte A — CRUD:
# Crie um dicionário `aluno` com nome, idade e cursos (lista).
#   - acesse a idade com [] e com .get()
#   - tente acessar uma chave inexistente das duas formas; explique a diferença
#   - adicione a chave "email"
#   - adicione um curso à lista de cursos
#   - remova "idade" com pop
#   - percorra imprimindo chave e valor com .items()
#
# Parte B — Contador de palavras:
# Dado um texto, retorne um dicionário {palavra: quantidade}.
# Faça de duas formas: 1) com dict e .get()  2) com collections.Counter
# Depois imprima as 3 palavras mais frequentes.
#
# Parte C — Agrupamento:
# Dada a lista de palavras:
#   ["python", "java", "pascal", "javascript", "go", "perl", "c"]
# Agrupe pela primeira letra:
#   {"p": ["python", "pascal", "perl"], "j": ["java", "javascript"], ...}
# Faça com .setdefault() ou collections.defaultdict.
#
# Parte D — Dict comprehension:
#   1. {n: n**2} para n de 1 a 5
#   2. Inverter chaves e valores de {"a": 1, "b": 2, "c": 3}
#   3. Filtrar de `precos = {"arroz": 25, "feijão": 8, "carne": 45, "sal": 3}`
#      apenas os itens com preço acima de 10
#
# Parte E — Estrutura aninhada:
# Represente uma agenda de contatos (nome -> {telefone, email, cidade}).
# Escreva funções para adicionar contato, buscar por nome (tratando o caso
# de não existir) e listar todos os contatos de uma cidade.
#
# Pergunta conceitual (responda em comentário):
# Que tipos podem ser chave de um dicionário? Por quê?

