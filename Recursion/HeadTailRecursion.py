# Head_Tail_Recursion 
# Programa para mostrar los tipos de recursion que existen:
# tail y head. Cambie el nombre de la funcion para llamar la
# que se desee.
# Miguel Angel Sanchez Mares mares112358@gmail.com

def tail(number):
    if(number == 0):
        return
    print('Llamada a la funcion tail con n = ' + str(number))
    #hacer alguna operacion
    print(number)
    tail(number - 1)

def head(number):
    if number == 0: 
        return
    print('Llamada a la funcion head con n = ' + str(number))
    head(number - 1)
    #hacer alguna operacion
    print(number)

tail(5)