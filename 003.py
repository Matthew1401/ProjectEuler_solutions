num = 600851475143
divide = 2
result = 0
prime_factors = []

while num != 1:
    if num % divide == 0:
        num /= divide
        prime_factors.append(divide)
        divide = 2
    else:
        divide += 1

for i in prime_factors:
    if result < i:
        result = i

print(result)
