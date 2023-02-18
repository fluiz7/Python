# cid = str(input('Em que cidade você nasceu? ')).strip()
# low = cid.lower()
# print('santo' in low)

cid = str(input('Em que cidade você nasceu? ')).strip()
print(cid[:5].lower() == 'santo')