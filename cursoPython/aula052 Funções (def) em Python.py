
def saudacao(msg='Olá', nome='cara'):
    print(msg, nome)
saudacao('Eu sou o ', 'Doutor')
variavel = saudacao('Eu sou o ', 'Doutor')
print(variavel)

def saudacao(msg='Olá', nome='cara'):
    print(msg, nome)
    return f'===> {msg} {nome}'
saudacao('Eu sou o ', 'Doutor')
variavel = saudacao('Eu sou o ', 'Doutor')
print(variavel)

def func(*args, **kwargs):
    print (args[0])
    print (args[-1])
    print (len(args))
    print (args)
    args = list(args)       # De trupla para lista
    print(args, kwargs)
    nome = kwargs.get('nome')
    sobrenome = kwargs.get('sobrenome')
    print('---------------------------------------------------------------')
func(1, 2, 3, 4, 5)
lista = [1, 2, 3, 4, 5]
print(*lista, sep='-')
func (lista, 6)
func (*lista, 6)
func (lista, nome='Doctor Who', sobrenome='Nine')