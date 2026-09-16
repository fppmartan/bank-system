import os
import negocio

def menu_inicial():
    while True:
        # Menu para cadastro inicial, solicitando apenas o nome do usuário
        print("> Bank System")
        user = input("Digite o nome do usuário: ")
        
        # Verifica se o usuário digitou algum texto
        if user != "":
            negocio.salvar_conta(user)
            print(f"Usuário '{user}' cadastrado com sucesso!")
            return user
                
        # Se o nome estiver vazio, ele pula o if e avisa o usuário, repetindo o loop
        print("Erro: O nome não pode estar vazio. Tente novamente.")
    
def menu_principal(usuario_logado):
    # Menu interativo principal para realizar as transações bancárias.
    os.system("cls") 
    while True:
        print(f"\n> Bank • User: {usuario_logado}")
        print("1. Consultar Saldo")
        print("2. Depositar")
        print("3. Sacar")
        print("4. Transferir")
        print("5. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            valor_atual = negocio.saldo(usuario_logado)
            print(f"Seu saldo atual é: R$ {valor_atual:.2f}")
            
        elif opcao == '2':
            try:
                valor = float(input("Digite o valor do depósito: R$ "))
                negocio.deposito(usuario_logado, valor)
                print("Operação finalizada.")
            except ValueError:
                print("Erro: Por favor, insira um valor numérico válido.")
                
        elif opcao == '3':
            try:
                valor = float(input("Digite o valor do saque: R$ "))
                negocio.saque(usuario_logado, valor)
                print("Operação finalizada.")
            except ValueError:
                print("Erro: Por favor, insira um valor numérico válido.")
                
        elif opcao == '4':
            destino = input("Digite o nome do usuário de destino: ")
            try:
                valor = float(input("Digite o valor da transferência: R$ "))
                negocio.transferência(usuario_logado, destino, valor)
                print("Operação finalizada.")
            except ValueError:
                print("Erro: Por favor, insira um valor numérico válido.")
                
        elif opcao == '5':
            print("Encerrando o sistema.")
            break
            
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    # Limpa a tela
    os.system("cls") 
    # Inicia a aplicação chamando o menu inicial
    usuario = menu_inicial()
    # Passa o nome do usuário validado para o menu principal
    menu_principal(usuario)