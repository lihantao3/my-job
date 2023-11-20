#说明：素数指的是只能被1和自身整除的正整数（不包括1）。

list = []
for i in range(2, 100):
    is_prime = True
    for j in range(2, i):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        list.append(i)

print(list)
