l = [1, 5, 10, 3, 7, 10]
n = len(l)
soma = 0

i = 0
while i < n:
    soma += l[i]
    i += 1
print(soma)

soma = 0
for numero in l:
    soma += numero
print(soma)
