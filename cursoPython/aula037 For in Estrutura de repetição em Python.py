
frase = 'O rato roeu a roupa do rei de roma'
tamanho_frase = len(frase)
nova_string = ''
for letra in frase:
    if letra == 'r':
        nova_string += letra.upper()
    else:
        nova_string += letra
    print(nova_string)

for n in range(10, 20, 1):
    print(n)