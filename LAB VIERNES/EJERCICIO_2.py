# Inicializar la suma en cero
suma = 0

# Recorrer los números del 1 al 10 (puedes ajustar el rango según tus necesidades)
for num in range(1, 11):
    # Verificar si el número es impar
    if num % 2 != 0:
        suma += num

# Imprimir el resultado
print("La suma de los números impares es:", suma)