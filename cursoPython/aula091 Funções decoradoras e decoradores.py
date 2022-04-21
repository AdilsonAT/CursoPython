
def fala_oi():
    print('Oi')
variavel = fala_oi
variavel()
print(type(variavel))

print('--------------------------------------------------------------------------------')

def master():
    def slave():
        print('Oi')
    return slave
variavel = master()
variavel()
print(type(variavel))

print('--------------------------------------------------------------------------------')

def master(funcao):
    def slave():
        print('Agora estou decorada')
        funcao()
    return slave
def fala_oi():
    print('Oi')
variavel = master(fala_oi)
variavel()
fala_oi()
@master
def fala_oi():
    print('Oi')
fala_oi()

print('--------------------------------------------------------------------------------')

from time import time
from time import sleep

def velocidade(funcao):
    print('entrei velocidade')
    def interna(*args, **kwargs):
        print('entrei interna')
        start_time = time()
        resultado = funcao(*args, **kwargs)
        end_time = time()
        tempo = (end_time - start_time) * 1000
        print(f'A função {funcao.__name__} levou {tempo}ms para executar.')
        return resultado
    return interna

@velocidade
def demora():
    for i in range(5):
        print(i)
        sleep(1)

demora()