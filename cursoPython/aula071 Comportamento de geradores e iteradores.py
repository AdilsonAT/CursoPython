
# list, tuples, str -> squences -> itéravel

nome = 'É um nome qualquer'
for letra in nome:
    print(letra)

iterador = iter(nome)
for x in iterador:
    print(next(iterador))
