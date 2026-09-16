import dados

def deposito(nome_origem, valor):
    if valor > 0:
        saldo_atual = dados.atualizar_saldo(valor)

        if saldo_atual is not None:
            novo_saldo = saldo_atual + valor
            dados.atualizar_saldo(nome_origem, novo_saldo)

        else:
            print("Conta não encontrada.")

    else:
        print("Valor de deposito inválido.")
    
def saldo(nome_origem):
    return dados.buscar_conta(nome_origem)

def saque(nome_origem, valor):
    if valor > 0:
        saldo_atual = dados.buscar_conta(nome_origem)

        if saldo_atual is not None:
            novo_saldo = saldo_atual - valor
            dados.atualizar_saldo(nome_origem, novo_saldo)

        else: 
            print("Conta não encontrada.")

    else: 
        print("Valor de saque inválido.")

def transferência(nome_origem, nome_destino, valor):
    return

def listar_contas():
    return listar_contas()