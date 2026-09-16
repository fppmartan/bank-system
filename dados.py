# Armazena o usuário cadastrado no inicio do programa.
conta_bancaria = {}


def salvar_nova_conta(nome):
    # Cria uma nova conta com saldo inicial de R$ 0.00
    conta_bancaria[nome] = 0.0

def buscar_conta(nome):
    # Retorna o saldo da conta se existir, ou None caso contrário
    if nome in conta_bancaria:
        return conta_bancaria[nome]
    return None

def atualizar_saldo(nome, novo_saldo):
    # Atualiza o valor numérico do saldo do usuário
    conta_bancaria[nome] = novo_saldo

def listar_todas_contas():
    # Retorna o dicionário completo
    return conta_bancaria