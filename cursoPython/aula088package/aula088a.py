
from aula088package.aula088formata import aula088real

def aumento(valor, percentagem, formata=False):
    r = valor+(valor*(percentagem/100))
    if formata:
        return aula088real.real(r)
    else:
        return r

def reducao(valor, percentagem, formata=False):
    r = valor-(valor*(percentagem/100))
    if formata:
        return aula088real.real(r)
    else:
        return r