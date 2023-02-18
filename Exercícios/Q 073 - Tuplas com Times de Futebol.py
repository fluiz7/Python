todos = ('Atlético-MG', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians',
         'Bragantino', 'Fluminense', 'América-MG', 'Atlético-GO', 'Santos',
         'Ceará SC', 'Internacional', 'São Paulo', 'Athletico-PR', 'Cuiabá',
         'Juventude', 'Grêmio', 'Bahia', 'Sport Recife', 'Chapecoense', )
print('--='*100)
print(f'Lista de times do Brasileirão: {todos}')
print('--='*100)
print(f'Os cinco primeiros são: {todos[0:5]}')
print('--='*32)
print(f'Os quatro últimos são: {todos[-4:]}')
print('--='*100)
print(f'Em ordem alfabética temos a lista: {sorted(todos)}')
print('--='*100)
print(f'O time da Chapecoense está na {todos.index("Chapecoense")+1}ª posição.')
