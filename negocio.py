import dados

valorAtual = 0

def deposito(valor):
    if valor > 0:
        valorAtual += atualizar_saldo(valor)
    else:
        print("Valor de deposito inválido.")
    
def saldo():
    return buscar_conta(nome)

def saque(valor):
    if valor > 0:
        valorAtual -= atualizar_saldo(valor)
    else: 
        print("Valor de saque inválido.")

def transferência():
    return

def listar_contas():
    return listar_contas()