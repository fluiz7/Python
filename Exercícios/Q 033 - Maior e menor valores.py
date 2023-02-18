pri = float(input('Primeiro valor: '))
seg = float(input('Segundo valor: '))
ter = float(input('Terceiro valor: '))
menor = pri
if pri > seg < ter:
    menor = seg
if pri > ter < seg:
    menor = ter
maior = pri
if pri < seg > ter:
    maior = seg
if pri < ter > seg:
    maior = ter
print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))
