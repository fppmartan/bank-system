# Armazena o usuário cadastrado no inicio do programa.
conta_bancaria = {}


def salvar_nova_conta(nome):
    # Cria uma nova conta com saldo inicial de R$ 0.00
    if nome not in conta_bancaria:
        conta_bancaria[nome] = 0.0

def buscar_conta(nome):
    # Retorna o saldo da conta se existir, ou None caso contrário
    return conta_bancaria.get(nome)

def atualizar_saldo(nome, novo_saldo):
    # Atualiza o valor numérico do saldo do usuário
    if nome in conta_bancaria:
        conta_bancaria[nome] = novo_saldo

def listar_todas_contas():
    # Retorna o dicionário completo
    return conta_bancaria