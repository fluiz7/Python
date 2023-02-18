# Método que encontra se tem Silva no nome, mas se for um derivado também dá True;

# nome = str(input('Digite seu nome completo: ')).strip()
# print("Seu nome tem Silva? ",'SILVA' in nome.upper())

# Método que encontra apenas se tiver Silva mesmo, nenhuma derivação funciona.

nome = str(input('Digite seu nome completo: ')).strip().upper().split()
print("Seu nome tem Silva? ", 'SILVA' in nome)
