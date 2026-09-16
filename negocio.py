import dados

def deposito(nome, valor):
    if valor > 0:
        saldo_atual = dados.atualizar_saldo(valor)

        if saldo_atual is not None:
            novo_saldo = saldo_atual + valor
            dados.atualizar_saldo(nome, novo_saldo)
        else:
            print("Conta não encontrada.")
    else:
        print("Valor de deposito inválido.")
    
def saldo(nome):
    return dados.buscar_conta(nome)

def saque(valor):
    if valor > 0:
        valorAtual -= atualizar_saldo(valor)
    else: 
        print("Valor de saque inválido.")

def transferência():
    return

def listar_contas():
    return listar_contas()