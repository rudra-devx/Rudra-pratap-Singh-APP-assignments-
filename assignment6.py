def fibonacci(n):

    if n <= 0:
        return 0

    if n == 1:
        return 1

    a = 0
    b = 1

    for i in range(2, n + 1):
        a, b = b, a + b

    return b


n = int(input("Enter n: "))

print("Fibonacci number:", fibonacci(n))
