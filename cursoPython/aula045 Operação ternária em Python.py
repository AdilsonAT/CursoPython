
logged_user = False
msg = 'Usuário logado.' if logged_user else 'Usuário precisa logar.'
print(msg)

idade = 18
e_de_maior = (idade >= 18)
msg = 'Pode acessar' if e_de_maior else 'Não pode acessar.'
print (msg)

idade = input('idade?')
if not idade.isnumeric():
    print('Não numerico')
else:
    idade = int(idade)
    e_de_maior = (idade >= 18)
    msg = 'Pode acessar' if e_de_maior else 'Não pode acessar.'
    print(msg)