
variavel = 'valor'
print(variavel)

def func():
    print('----->')
    variavel = 'outro valor'
    print (variavel)
    print('<-----')

def func2():
    print('=====>')
    global variavel
    print (variavel)
    variavel = 'um outro valor'
    print (variavel)
    print('<=====')

func()
print (variavel)

func2()
print (variavel)

