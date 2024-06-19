from bd import *
from conexaobd import conexao
from datetime import datetime, date

conbd = conexao()

def Menu():
    print('')
    print('Olá, Seja bem Vindo ao nosso menu! ')
    print('')
    print('Selecione a operação desejada: ')
    print('')
    print('0. Sair')
    print('1. Cadastrar Produtos')
    print('2. Cadastrar Clientes')
    print('3. Cadastrar Fornecedores')
    print('4. Cadastrar Funcionarios')
    print('5. Cadastrar Promoções')
    print('6. Deletar Produtos')
    print('7. Deletar Clientes')
    print('8. Deletar Fornecedores')
    print('9. Deletar Funcionario')
    print('10.Deletar Promoção')
    print('11.Atualizar Produto')
    print('12.Atualizar Cliente')
    print('13.Atualizar Fornecedor')
    print('14.Atualizar Funcionario')
    print('15.Atualizar Promoção')
    print('16.Listar produtos')
    print('17.Listar clientes')
    print('18.Listar fornecedores')
    print('19.Listar funcionarios')
    print('20.Listar promoções')
    print('21.Cadastrar pedido')
    



def opcaobd():
    while True:
        option = input('\nOpção: ')
        if option == '0':
            print ('Programa finalizado!')
            break
        elif option == '1':
            nome =  input ('Digite o nome do produto: ')
            descricao = input ('Digite a descrição do produto: ')
            preco = float(input('Digite o preço do produto: '))
            quantidade = input('Digite a quantidade do produto: ')
            cadastrarProdutos(conbd, nome, descricao, preco,quantidade)
        elif option == '2':
            nome =  input ('Digite o nome do cliente: ')
            sobrenome = input ('Digite o sobrenome do cliente: ')
            endereco = input ('Digite o endereco do cliente: ')
            cidade = input ('Digite a cidade do cliente: ')
            codigopostal = input('Digite o código-postal do cliente: ')
            cadastrarClientes(conbd, nome, sobrenome, endereco, cidade, codigopostal)
        elif option == '3':
            nome =  input ('Digite o nome do Fornecedor: ')
            contato = input ('Digite o contato do Fornecedor: ')
            endereco = input ('Digite o endereço do Fornecedor: ')
            cadastrarFornecedores(conbd, nome, contato, endereco)
        elif option == '4':
            nome =  input ('Digite o nome do Funcionario : ')
            cargo = input ('Digite o cargo: ')
            departamento = input ('Digite o departamento: ')
            cadastrarFuncionarios(conbd, nome, cargo, departamento)
        elif option == '5':
            nome =  input ('Digite a promoção: ')
            descricao = input('Digite a Descrição da promoção: ')
            DataInicio = input('Digite a data inicial: ')
            DataInicio = datetime.strptime(DataInicio, '%d-%m-%Y').strftime('%Y-%m-%d')
            DataFim = input('Digite a data final: ')
            DataFim = datetime.strptime(DataFim, '%d-%m-%Y').strftime('%Y-%m-%d')
            cadastrarPromocoes(conbd, nome, descricao, DataInicio, DataFim)
        elif option == '6':
            idprot = input ('Digite o ID do produto para remove-lo: ')
            deletarProdutos(conbd, idprot)
        elif option == '7':
            ID_Cliente = input ('Digite o ID do cliente para remove-lo: ')
            deletarClientes(conbd, ID_Cliente)
        elif option == '8':
            ID_Fornecedor = input ('Digite o ID do Fornecedor para remove-lo: ')
            deletarFornecedores(conbd, ID_Fornecedor)
        elif option == '9':
            ID_Funcionario = input ('Digite o ID do Funcionario para remove-lo: ')
            deletarFuncionarios(conbd, ID_Funcionario)
        elif option == '10':
            ID_Promocao = input ('Digite o ID da Promoção para deletar: ')
            deletarPromocoes(conbd, ID_Promocao)
        elif option == '11':
            ID_Produto = int (input ('Digite o ID do Produto: '))
            Nome = input ('Digite o novo nome do produto: ')
            Descricao = input ('Digite a nova Descrição: ')
            Preco = float(input ('Digite o novo preço: '))
            atualizarProdutos(conbd, Nome, Descricao, Preco, ID_Produto)
        elif option == '12':
            ID_Cliente = int (input ('Digite o ID do Cliente: '))
            Nome = input ('Digite o novo nome: ')
            Sobrenome = input ('Digite o novo sobrenome: ')
            Endereco = input ('Digite o novo endereço: ')
            Cidade = input ('Digite a nova cidade: ')
            CodigoPostal = input ('Digite o novo Código Postal: ')
            atualizarClientes(conbd, Nome,Sobrenome,Endereco,Cidade,CodigoPostal,ID_Cliente)
        elif option == '13':
            ID_Fornecedor = int (input ('Digite o ID do Fornecedor: '))
            Nome = input ('Digite o novo nome do fornecedor: ')
            Contato = input ('Digite o novo contato: ')
            Endereco = input ('Digite o novo endereço do fornecedor: ')
            atualizarFornecedores(conbd, Nome,Contato,Endereco, ID_Fornecedor)
        elif option == '14':
            ID_Funcionario = int (input ('Digite o ID do Funcionario: '))
            Nome = input ('Digite o novo nome do funcionario: ')
            Cargo = input ('Digite o novo cargo: ')
            Departamento = input ('Digite o novo endereço do funcionario: ')
            atualizarFuncionarios(conbd,Nome,Cargo,Departamento, ID_Funcionario)
        elif option == '15':
            ID_Promocao = int (input ('Digite o ID da Promoção: '))
            Nome = input ('Digite o novo nome do funcionario: ')
            Descricao = input ('Digite a Descrição da promoção: ')
            DataInicio = input ('Digite a data que começa a promoção: ')
            DataInicio = datetime.strptime(DataInicio, '%d-%m-%Y').strftime('%Y-%m-%d')
            DataFim = input ('Digite a data que termina a promoção: ')
            DataFim = datetime.strptime(DataFim, '%d-%m-%Y').strftime('%Y-%m-%d')
            atualizarPromocoes(conbd,Nome,Descricao,DataInicio,DataFim, ID_Promocao)
        elif option == '16':
            listarProdutos(conbd,)
        elif option == '17':
            listarClientes(conbd,)
        elif option == '18':
            listarFornecedores(conbd,)
        elif option == '19':
            listarFuncionarios(conbd,)
        elif option == '20':
            listarPromocoes(conbd,)
        elif option == '21':
            nome = input('Digite seu nome: ')
            sobrenome = input('Digite seu sobrenome: ') 
            produt = input('Qual produto você deseja? : ')
            quantidade = int (input ('Quantas peças? :'))
            data = date.today()
            formpag = input ('Qual a forma de pagamento? : \n1.Cartão de Crédito \n2.Boleto Bancário \n3.Cartão de Débito  \n: ')
            cadastrarPedidos(conbd,nome,sobrenome,produt,quantidade,formpag,data)