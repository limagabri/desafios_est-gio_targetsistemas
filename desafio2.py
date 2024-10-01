def sequencia_fibonacci(n):
    a, b = 0, 1
    fibonacci_list = [a, b]
    
    while b <= n:
        a, b = b, a + b
        fibonacci_list.append(b)
    
    return fibonacci_list

def is_in_fibonacci(n):
    fibonacci_list = sequencia_fibonacci(n)
    if n in fibonacci_list:
        return f"O número {n} pertence à sequência de Fibonacci."
    else:
        return f"O número {n} NÃO pertence à sequência de Fibonacci."

n = int(input("Informe um número: "))

print(is_in_fibonacci(n))
