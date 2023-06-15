#1)Un algoritmo que resuelva el problema asumiendo que la máquina en donde va a correrse el
#programa tiene recursos infinitos, que el tiempo de ejecución no importa y que lo más
#importante es realizar el desarrollo en el menor tiempo posible.

def encontrarSuma_En_(suma,lista):
    encontrado=False
    for i in range(len(lista)):     
        for j in range(i+1,len(lista)): 
            if(lista[i]+lista[j]==suma):
                encontrado=True
    return encontrado
#2)Un algoritmo que resuelva el problema asumiendo que los recursos son un bien preciado,
#que el tiempo de ejecución si importa y que el tiempo de desarrollo no es importante.

def encontrarSuma_En_Eficiente(suma, lista):
    encontrado=False
    numerosVistos = set()
    for numero in lista: ##En esta funcion recorro la lista una sola vez, por lo tanto baja la complejidad.
        complemento = suma - numero  #calculo el complemento restando numero de suma para determinar que numero se necesita para que la suma sea igual a suma.
        if complemento in numerosVistos:
            encontrado=True
        numerosVistos.add(numero)
    return encontrado

#Ejemplos de prueba:
listaDePrueba=[1,2,3,5]
print(encontrarSuma_En_(1,listaDePrueba))
print(encontrarSuma_En_Eficiente(1,listaDePrueba))