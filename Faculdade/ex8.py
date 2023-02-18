st = str(input())
car = let = num = sim = 0
pal = st.replace("\\n",' ')
pal = len(pal.split())

for c in st:
    if c.isprintable():
        car += 1
    if c.isalpha():
        let += 1
    elif c.isdecimal():
        num += 1
    elif c.isascii():
        sim += 1
        
print(car, let, num, sim, pal)