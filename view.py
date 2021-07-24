from controller import PessoaController
while True:
    decisao = int(input('digite 1 para salvar pessoa ou digite 2 para ver a pessoa salva e 3 para sair'))
    if decisao == 3:
        break
    if decisao == 1:
        nome = input('digite seu nome:')
        idade = int(input('digite sua idade: '))
        cpf = input('digite seu cpf:')
        if PessoaController.Cadastrar(nome, idade, cpf):
            print('usuario cadastrado')
        else:
            print('digite valores válidos')
    if decisao == 2:
        print()