"""

Implementar una función utilizando recursión para determinar si un número 
se encuentra o no en una lista de números. Alternativamente pueden utilizar una solución 
iterativa 

"""

def buscar_numero(lista_numeros, numero_buscado, indice = 0):
    if (lista_numeros == 0):
        return False
    elif indice >= len(lista_numeros) :
        return False
    elif lista_numeros[indice] == numero_buscado:
        return True
    else:
        return buscar_numero(lista_numeros, numero_buscado, indice + 1)
    
    
numero_buscado = int(input("ingrese el numero que quiere buscar: "))   
lista_numeros = [4, 7, 8, 14, 24, 21, 65, 378, 12441]
buscar = buscar_numero(lista_numeros, numero_buscado, indice = 0)


if buscar:
    print(f"El número {numero_buscado} está en la lista.")
else:
    print(f"El número {numero_buscado} NO está en la lista.")