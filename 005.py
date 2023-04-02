num = 2520

is_loop = True
while is_loop:
    num += 17
    this_is_it = True
    for i in range(1, 20):
        if num % i != 0:
            this_is_it = False

    if this_is_it:
        break

    print(num)

print(num)
