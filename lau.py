def estaenlista(n,l):
    return n in l
def cargarLista(l):
    num=int(input('Ingresar numeros, o 0 (cero ) para terminar\n'))
    while num!=0:
        while num>0 and not estaenlista(num,l):
            l.append(num)
            num=int(input())
        while estaenlista(num,l) or num<0:
            if num<0:
                num=int(input('Error, numero NO positivo.'))
            if estaenlista(num,l):
                num=int(input('Error, número repetido.'))
def cargarConjuntos(l1,l2):
    cargarLista(l1)
    cargarLista(l2)
def union(l1,l2):
    ls=[]
    for x in l1:
        ls.append(x)
    for x in l2:
        if x not in ls:
            ls.append(x)
    return ls
def interseccion(l1,l2):
    ls=[]
    for x in l1:
        if x in l2:
            ls.append(x)
    return ls
def diferencia(l1,l2):
    ls=[]
    for x in l1:
        if x not in l2:
            ls.append(x)
    return ls
def diferenciaSimetrica(l1,l2):
    ls=[]
    for x in l1:
        if x not in l2:
            ls.append(x)
    for x in l2:
        if x not in l1:
            ls.append(x)
    return ls
def main():
    lis1=[] ; lis2=[]
    print('1. CARGAR CONJUNTOS\n2. UNION\n3. INTERSECCION\n4. DIFERENCIA (A-B)\n5. DIFERENCIA SIMÉTRICA\n6. SALIR')
    op=int(input('Ingrese el valor de la opción: '))
    while op!=6:
        while op<1 or op>6:
            op=int(input('Opción inexistente. Ingrese el valor de la opción: '))
        if op==1:
            lis1=[] ; lis2=[]
            cargarConjuntos(lis1,lis2)
            print(lis1)
            print(lis2)
            op=int(input('Ingrese el valor de la opción: '))
        if op==2:
            print(union(lis1,lis2))
            op=int(input('Ingrese el valor de la opción: '))
        if op==3:
            print(interseccion(lis1,lis2))
            op=int(input('Ingrese el valor de la opción: '))
        if op==4:
            print(diferencia(lis1,lis2))
            op=int(input('Ingrese el valor de la opción: '))
        if op==5:
            print(diferenciaSimetrica(lis1,lis2))
            op=int(input('Ingrese el valor de la opción: '))
main()
