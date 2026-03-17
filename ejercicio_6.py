# sentencias
temperatura = int(input("Indica la temperatura: "))
if temperatura > 22:
    print("Esta haciendo calor")
else:
    print("Hace frio")

if temperatura > 28:
    print("Esta haciendo calor")
elif temperatura > 20:
    print("Es un dia agradable")
elif temperatura > 10:
    print("Hace un poco de frio")
else:
    print("Hace frio, brrrr")

print("Proceso concluido")
