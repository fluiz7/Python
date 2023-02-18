# money = int(input('Quanto você deseja sacar? R$'))
# cin = money // 50
# vin = (money % 50) // 20
# dez = ((money % 50) % 20) // 10
# um = (((money % 50) % 20) % 10) // 1
# print(f'Total de {cin} cédulas de R$50\nTotal de {vin} cédulas de R$20\nTotal de {dez} cédulas de R$10')
# print(f'Total de {um} cédulas de R$1')
money = int(input('Quanto você deseja sacar? R$'))
total = money
ced = 50
totCed = 0
while True:
    if total >= ced:
        total -= ced
        totCed += 1
    else:
        if totCed > 0:
            print(f'Total de {totCed} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totCed = 0
        if total == 0:
            break
print('ENCERRANDO!!')
