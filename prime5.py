import math

entiers = []
max_number = int(input("Nombre max : "))
max_number = max_number + 1
x = 3
entiers.append(x)
x = 5
entiers.append(x)
x = x + 2

while x < max_number:
    for i in range(2):
        entiers.append(x)
        x = x + 4
        entiers.append(x)
        x = x + 2
    entiers.append(x)
    x = x + 4
    entiers.append(x)
    x = x + 6
    entiers.append(x)
    x = x + 2
    entiers.append(x)
    x = x + 6

print("2")
print("3")
first_prime = 0
prime = 0
u = 1


while u < len(entiers):
    first_prime = entiers[u]
    prime = first_prime
    print(first_prime)
    if first_prime < math.sqrt(max_number):
        while prime < max_number:
            prime = prime + first_prime
            if prime in entiers:
                entiers.remove(prime)

    u = u + 1

print("Nombres premiers trouvés : ", len(entiers))

