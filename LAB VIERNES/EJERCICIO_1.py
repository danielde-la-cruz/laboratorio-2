def fibonacci(n):
    fib_series = [0, 1]
    while len(fib_series) < n:
        next_fib = fib_series[-1] + fib_series[-2]
        fib_series.append(next_fib)
    return fib_series


n = int(input("Ingrese el valor de n para calcular la serie de Fibonacci: "))
if n <= 0:
    print("El valor de n debe ser mayor que cero.")
else:
    fib_series = fibonacci(n)
    print(f"Serie de Fibonacci hasta el término {n}: {fib_series}")
