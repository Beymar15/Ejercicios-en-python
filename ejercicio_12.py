# diccionario -> almacen de pares de clave-valor
mi_diccionario = {'nombre':'Bruno Diaz','edad':25,'Ciudad':'La paz'}
print(mi_diccionario)

#Acceder a un valor
print(mi_diccionario['nombre'])
print(mi_diccionario['Ciudad'])

#agregar elementos
mi_diccionario['profesion'] = 'Ingeniero'
print(mi_diccionario)

#eliminar un elemento
del mi_diccionario['Ciudad']
print(mi_diccionario)

#Obtener claves del diccionaro
print(mi_diccionario.values())

#Verificar si una clave existe
if 'Ciudad' in mi_diccionario:
    print("Clave encontrada")

# Recorridp de un diccionario
for clave, valor in mi_diccionario.items():
    print("Clave: ",clave,"Valor: ",valor)
