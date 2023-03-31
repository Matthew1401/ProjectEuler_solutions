fibonacci = 1
fibonacci_before = 1
result = 0

while fibonacci < 4_000_000:
    temporary = fibonacci
    fibonacci += fibonacci_before
    fibonacci_before = temporary
    if fibonacci % 2 == 0:
        result += fibonacci

print(result)

