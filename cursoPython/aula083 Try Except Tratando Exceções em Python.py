
try:
    print(a)
except:
    pass
print('Foi')

try:
    a = 0
    try:
        a= 1/0
    except:
        print('Agora ficou loco')
except NameError as erro:
    print('Erro:', erro)
except (IndexError, KeyError) as erro:
    print('Erro:', erro)
except Exception as erro:
    print('Erro:', 'Ich, não faço ideia')
else:
    pass
finally:
    print('Tanto faz')
print ('Continuo assim mesmo')