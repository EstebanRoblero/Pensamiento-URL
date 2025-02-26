num = int(input("ingrese numero de 5 digitos: "))
if num < 99999 and num > 10000:
    a = num // 10000 %10
    b = num // 1000 % 10
    c = num // 100 % 10
    d = num // 10 % 10
    e = num % 10
    print (a)
    print (b)
    print (c)
    print (d)
    print (e)

    if a > b:
        a, b = b, a
    if b > c:
        b, c = c, b
    if c > d:
        c, d = d, c
    if d > e:
        d, e = e, d
    if a > b:
        a, b = b, a
    if b > c:
        b, c = c, b
    if c > d:
        c, d = d, c
    if a > b:
        a, b = b, a
    if b > c:
        b, c = c, b
    if a > b:
        a, b = b, a


    
    if a < b:
        a, b = b, a
    if b < c:
        b, c = c, b
    if c < d:
        c, d = d, c
    if d < e:
        d, e = e, d
    if a < b:
        a, b = b, a
    if b < c:
        b, c = c, b
    if c < d:
        c, d = d, c
    if a < b:
        a, b = b, a
    if b < c:
        b, c = c, b
    if a < b:
        a, b = b, a
        
print("lista ordenada de numeros ascendiente: ", a,b,c,d,e)
print("lista ordenada de numeros descendiente: ", e,d,c,b,a)