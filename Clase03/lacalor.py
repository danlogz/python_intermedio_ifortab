'''
Hacer un programa que te pida a cuantos grados centigrados estamos
Dependiendo el dato ingresado realizar las siguientes validaciones

si es mas de 35 grados mostrar: "ta juerte la calor"

si esta entre 25 a 30 grados mostrar: "se antoja un pozol"

si la temperatura es menor a 25 grados mostrar: "es hora de sacar el sueter cucarachiento"


utilizar el menor lineas de codigo posible

se evaluara:
legibilidad de codigo


"Simple es mejor que complejo"

'''

from zmq import EVENT_CLOSE_FAILED


grado = int(input("¿Cuantos centigrados estamos ahora?"))

if grado < 25:
    print (f'Ta juerte la calor {grado}')
elif grado >= 25 and grado <= 34:
    print(f'Se antoja un pozol {grado}')
elif grado > 35:
    print(f'Es hora de sacar el sueter cucarachiento {grado}')
else:
    print('Fin programa')