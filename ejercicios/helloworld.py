# funciones

def menoresQueDiez(listaConNumeros):
    contador = 0
    for i in listaConNumeros:
        if(i==10):
            contador = contador + 1
    print(contador)
                    

notasCurso=[10,2,10,4,10,10,3,5,67,4]

menoresQueDiez(notasCurso)



