palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS',
            'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR',
            'FUTURO')
for c in palavras:
    print(f'\nNa palavra {c} temos as vogais:', end=' ')
    for pos in range(0, len(c)):
        if c[pos] in 'AaEeIiOoUu':
            print(c[pos].lower(), end=' ')
# for c in palavras:
#     print(f'\nNa palavra {c} temos as vogais:', end=' ')
#     for pos in c:
#         if pos in 'AaEeIiOoUu':
#             print(pos.lower(), end=' ')
