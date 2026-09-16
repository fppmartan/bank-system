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

def transferencia(nome_origem, nome_destino, valor):
    if valor > 0:
        saldo_origem = dados.buscar_conta(nome_origem)
        saldo_destino = dados.buscar_conta(nome_destino)

        if saldo_origem is None:
            print("Conta de origem não encontrada.")

        elif saldo_destino is None:
            print("Conta de destino não encontrada.")

        elif saldo_origem < valor:
            print("Saldo insuficiente.")

        else:
            # Atualiza saldo da conta de origem
            dados.atualizar_saldo(nome_origem, saldo_origem - valor)

            # Atualiza saldo da conta de destino
            dados.atualizar_saldo(nome_destino, saldo_destino + valor)

    else:
        print("Valor de transferência inválido.")

def listar_contas():
    return dados.listar_todas_contas()