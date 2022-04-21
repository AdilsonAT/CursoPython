# minha

from time import time
from time import sleep

def velocidade(funcao_demora):
    print('entrei velocidade')
    def interna(*args, **kwargs):
        print('entrei interna')
        start_time = time()
        resultado = funcao_demora(*args, **kwargs)
        end_time = time()
        tempo = (end_time - start_time) * 1000
        print(f'A função {funcao_demora.__name__} levou {tempo}ms para executar.')
        print('return resultado')
        return resultado

    print('return velocidade')
    return interna

@velocidade
def demora():
    print('entrei demora')
    for i in range(5):
        print(i)
        sleep(1)
    print('saida demora')

demora()