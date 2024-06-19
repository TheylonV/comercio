def cadastrarProdutos(conbd, Nome, Descricao, Preco, Quantidade):
    mycursor = conbd.cursor()
    sql ='INSERT INTO produtos (Nome, Descricao, Preco) VALUES (%s,%s,%s)'
    val = (Nome, Descricao, Preco)
    mycursor.execute(sql,val)
    ID_Produto = mycursor.lastrowid
    sql1 = 'INSERT INTO estoque (ID_Produto, Quantidade) VALUES (%s,%s)'
    val1 = (ID_Produto, Quantidade)
    mycursor.execute(sql1, val1)
    conbd.commit()
    print('Produto Cadastrado com Sucesso! ')
    mycursor.close()

def cadastrarClientes(conbd, Nome, Sobrenome, Endereco, Cidade, Codigopostal):
    mycursor = conbd.cursor()
    sql ='INSERT INTO clientes (Nome, Sobrenome, Endereco, Cidade, Codigopostal) VALUES (%s,%s,%s,%s,%s)'
    val = (Nome, Sobrenome, Endereco, Cidade, Codigopostal)
    mycursor.execute(sql, val)
    conbd.commit()
    print('\nCliente Cadastrado com Sucesso!')
    mycursor.close()

def cadastrarFornecedores(conbd, Nome, Contato, Endereco):
    mycursor = conbd.cursor()
    sql ='INSERT INTO fornecedores (Nome, Contato, Endereco) VALUES (%s,%s,%s)'
    val = (Nome, Contato, Endereco)
    mycursor.execute(sql, val)
    conbd.commit()
    print('\nFornecedor Cadastrado com Sucesso!')
    mycursor.close()

def cadastrarFuncionarios(conbd, Nome, Cargo, Departamento):
    mycursor = conbd.cursor()
    sql ='INSERT INTO funcionarios (Nome, Cargo, Departamento) VALUES (%s,%s,%s)'
    val = (Nome, Cargo, Departamento)
    mycursor.execute(sql, val)
    conbd.commit()
    print('\nFuncionario Cadastrado com Sucesso!')
    mycursor.close()

def cadastrarPromocoes(conbd, Nome, Descricao, DataInicio, DataFim):
    mycursor = conbd.cursor()
    sql ='INSERT INTO promocoes (Nome, Descricao, DataInicio, DataFim) VALUES (%s,%s,%s,%s)'
    val = (Nome, Descricao, DataInicio, DataFim)
    mycursor.execute(sql, val)
    conbd.commit()
    print('\nPromoção Cadastrada com Sucesso!')
    mycursor.close()

def deletarProdutos(conbd, idprot):
    mycursor = conbd.cursor()
    sql ='DELETE FROM produtos WHERE ID_Produto = %s'
    val = (idprot,)
    mycursor.execute(sql, val)
    conbd.commit()
    print('\nProduto Deletado!')
    mycursor.close()

def deletarClientes(conbd, ID_Cliente):
    mycursor = conbd.cursor()
    sql ='DELETE FROM clientes WHERE ID_Cliente = %s'
    val = (ID_Cliente,)
    mycursor.execute(sql, val)
    conbd.commit()
    print('\nCliente Deletado!')
    mycursor.close()

def deletarFornecedores(conbd, ID_Fornecedor):
    mycursor = conbd.cursor()
    sql ='DELETE FROM fornecedores WHERE ID_Fornecedor = %s'
    val = (ID_Fornecedor,)
    mycursor.execute(sql, val)
    conbd.commit()
    print('\nFornecedor Deletado!')
    mycursor.close()
    
def deletarFuncionarios(conbd, ID_Funcionario):
    mycursor = conbd.cursor()
    sql ='DELETE FROM funcionarios WHERE ID_Funcionario = %s'
    val = (ID_Funcionario,)
    mycursor.execute(sql, val)
    conbd.commit()
    print('\nFuncionario Deletado!')
    mycursor.close()

def deletarPromocoes(conbd, ID_Promocao):
    mycursor = conbd.cursor()
    sql ='DELETE FROM promocoes WHERE ID_Promocao = %s'
    val = (ID_Promocao,)
    mycursor.execute(sql, val)
    conbd.commit()
    print('\nPromoção Deletada!')
    mycursor.close()

def atualizarProdutos(conbd, Nome, Descricao, Preco, ID_Produto):
    mycursor = conbd.cursor()
    sql ='UPDATE produtos SET Nome = %s, Descricao = %s, Preco = %s WHERE ID_Produto = %s'
    val = (Nome,Descricao,Preco, ID_Produto)
    mycursor.execute(sql, val)
    conbd.commit()
    print('\n Produto atualizado!')
    mycursor.close()

def atualizarClientes(conbd, Nome, Sobrenome, Endereco, Cidade, CodigoPostal, ID_Cliente):
    mycursor = conbd.cursor()
    sql ='UPDATE clientes SET Nome = %s, Sobrenome = %s, Endereco = %s, Cidade = %s, CodigoPostal = %s WHERE ID_Cliente = %s'
    val = (Nome,Sobrenome,Endereco,Cidade,CodigoPostal,ID_Cliente)
    mycursor.execute(sql, val)
    conbd.commit()
    print('\n Cliente atualizado!')
    mycursor.close()

def atualizarFornecedores(conbd, Nome,Contato,Endereco, ID_Fornecedor):
    mycursor = conbd.cursor()
    sql ='UPDATE fornecedores SET Nome = %s, Contato = %s, Endereco = %s WHERE ID_Fornecedor = %s'
    val = (Nome,Contato,Endereco, ID_Fornecedor)
    mycursor.execute(sql, val)
    conbd.commit()
    print('\n Fornecedor atualizado!')
    mycursor.close()

def atualizarFuncionarios(conbd, Nome,Cargo,Departamento, ID_Funcionario):
    mycursor = conbd.cursor()
    sql ='UPDATE funcionarios SET Nome = %s, Cargo = %s, Departamento = %s WHERE ID_Funcionario = %s'
    val = (Nome,Cargo,Departamento, ID_Funcionario)
    mycursor.execute(sql, val)
    conbd.commit()
    print('\n Funcionario atualizado!')
    mycursor.close()

def atualizarPromocoes(conbd, Nome,Descricao,DataInicio,DataFim, ID_Promocao):
    mycursor = conbd.cursor()
    sql ='UPDATE promocoes SET Nome = %s, Descricao = %s, DataInicio = %s, DataFim = %s WHERE ID_Promocao = %s'
    val = (Nome,Descricao,DataInicio,DataFim, ID_Promocao)
    mycursor.execute(sql, val)
    conbd.commit()
    print('\n Promoção atualizada!')
    mycursor.close()

def listarProdutos(conbd,):
    mycursor = conbd.cursor()
    sql ='SELECT * FROM produtos'
    listagem = mycursor.execute(sql)
    listagem = mycursor.fetchall()
    for i in listagem:
        print(i)
    mycursor.close()

def listarClientes(conbd,):
    mycursor = conbd.cursor()
    sql ='SELECT * FROM clientes'
    listagem = mycursor.execute(sql)
    listagem = mycursor.fetchall()
    for i in listagem:
        print(i)
    mycursor.close()

def listarFornecedores(conbd,):
    mycursor = conbd.cursor()
    sql ='SELECT * FROM fornecedores'
    listagem = mycursor.execute(sql)
    listagem = mycursor.fetchall()
    for i in listagem:
        print(i)
    mycursor.close()

def listarFuncionarios(conbd,):
    mycursor = conbd.cursor()
    sql ='SELECT * FROM funcionarios'
    listagem = mycursor.execute(sql)
    listagem = mycursor.fetchall()
    for i in listagem:
        print(i)
    mycursor.close()

def listarPromocoes(conbd,):
    mycursor = conbd.cursor()
    sql ='SELECT * FROM promocoes'
    listagem = mycursor.execute(sql)
    listagem = mycursor.fetchall()
    for i in listagem:
        print(i)
    mycursor.close()

def cadastrarPedidos(conbd, nome,sobrenome,produt,quantidade,formpag,data):
    mycursor = conbd.cursor()
    sql = 'SELECT ID_Cliente FROM clientes WHERE Nome = %s AND Sobrenome = %s'
    val = (nome,sobrenome)
    mycursor.execute(sql,val)
    ID_Cliente = int (mycursor.fetchone()[0])
    sql = 'SELECT ID_Produto FROM produtos WHERE Nome = %s'
    val = (produt,)
    mycursor.execute(sql,val)
    ID_Produto = int (mycursor.fetchone()[0])
    sql = 'SELECT Preco FROM produtos WHERE ID_Produto = %s'
    val = (ID_Produto,)
    mycursor.execute(sql,val)
    Preco = float(mycursor.fetchone()[0])
    sql = 'INSERT INTO pedidos (Data_Pedido,ID_Cliente,Total) VALUES (%s,%s,%s)'
    val = (data, ID_Cliente, (Preco * quantidade))
    mycursor.execute(sql,val)
    sql = 'UPDATE estoque SET Quantidade = %s' #UPDATE promocoes SET Nome = %s,
    val = (quantidade,)
    mycursor.execute(sql,val)
    sql = 'INSERT INTO vendas (ID_Venda) VALUES (%s)' #INSERT INTO estoque (ID_Produto, Quantidade) VALUES (%s,%s)'
    val = (formpag,)
    mycursor.execute(sql,val)
    conbd.commit()
    print('\n Pedido feito com sucesso !')
    mycursor.close()


    #mycursor = conbd.cursor()
    #sql ='INSERT INTO produtos (Nome, Descricao, Preco) VALUES (%s,%s,%s)'
    #val = (Nome, Descricao, Preco)
    #mycursor.execute(sql,val)
    #ID_Produto = mycursor.lastrowid
    #sql1 = 'INSERT INTO estoque (ID_Produto, Quantidade) VALUES (%s,%s)'
    #val1 = (ID_Produto, Quantidade)
    #mycursor.execute(sql1, val1)
    #conbd.commit()
    #print('Produto Cadastrado com Sucesso! ')
    #mycursor.close()

    