
import csv

with open('clientes.csv', 'r') as arquivo:
    dados = csv.reader(arquivo)     # retorna formato de lista
    print(dados)    # iterador
    next(dados)     # pula cabeçalho
    for dado in dados:
        print(dado)

print('-----------------------------------------------------------------------------------------------')

with open('clientes.csv', 'r') as arquivo:
    dados = csv.DictReader(arquivo)     # retorna formato de dicionario
    print(dados)    # iterador
    for dado in dados:
        print(dado)
        print(dado['Nome'], dado['Sobrenome'], dado['E-mail'], dado['Telefone'])

print('-----------------------------------------------------------------------------------------------')

with open('clientes.csv', 'r') as arquivo:
    dados = [x for x in csv.DictReader(arquivo)]    # converte em lista
for dado in dados:
    print(dado)
with open('cliente2.csv', 'w') as arquivo:
    escreve = csv.writer(
        arquivo,
        delimiter = ',',
        quotechar = '"',
        quoting = csv.QUOTE_ALL
    )
    chaves = dados[0].keys()
    print(chaves)
    chaves = list(chaves)
    print(chaves)
    escreve.writerow(
        [
            chaves[0],
            chaves[1],
            chaves[2],
            chaves[3]
        ]
    )
    for dado in dados:
        escreve.writerow(
            [
                dado['Nome'],
                dado['Sobrenome'],
                dado['E-mail'],
                dado['Telefone']
            ]
        )
