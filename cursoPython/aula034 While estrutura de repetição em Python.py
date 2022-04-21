
x = 0
while x < 10:
    if x == 3:
        break
    print(x)
    x += 1
print ('Acabou')


frase = 'O rato roeu a roupa do rei de roma'
tamanho_frase = len(frase)
contador = 0
nova_string = ''
while contador < tamanho_frase:
    if frase[contador] == 'r':
        nova_string += frase[contador].upper()
    else:
        nova_string += frase[contador]
    print(nova_string)
    contador += 1