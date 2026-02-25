print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División real")
print("5. División entera")
print("6. Módulo")

op = int(input("Seleccione una opción: "))

a = float(input("Digite el primer número: "))
b = float(input("Digite el segundo número: "))

if op == 1:
    print("Resultado:", a + b)
elif op == 2:
    print("Resultado:", a - b)
elif op == 3:
    print("Resultado:", a * b)
elif op == 4:
    print("Resultado:", a / b)
elif op == 5:
    print("Resultado:", a // b)
elif op == 6:
    print("Resultado:", a % b)
else:
    print("Opción inválida")
