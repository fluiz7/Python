nome = input('Digite um nome completo: ')
maius = nome.upper()
minus = nome.lower()
total = len(nome.replace(" ", ''))
first = nome.split()

print('''Seu nome completo é: {}
Em maiúsculas é: {}
Em minúsculas fica: {}
Tem um total de {} letras:
Enquanto o primeiro nome possui {} letras.''' .format(nome, maius, minus, total, len(first[0])))
