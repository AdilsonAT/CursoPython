
variavel = ['Doctor', 'Who', 'Nine']
for valor in variavel:
    print(valor)
    if valor.lower().startswith('j'):
        break
else:
    print('Não existe uma palavra que começa com j.')