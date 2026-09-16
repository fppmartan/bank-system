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
    os.system("cls" if os.name == "nt" else "clear") 
    while True:
        print(f"\n> Bank • User: {usuario_logado}")
        print("1. Consultar Saldo")
        print("2. Depositar")
        print("3. Sacar")
        print("4. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            os.system("cls" if os.name == "nt" else "clear")
            valor_atual = negocio.saldo(usuario_logado)
            print(f"Seu saldo atual é: R$ {valor_atual:.2f}")
            
        elif opcao == '2':
            try:
                os.system("cls" if os.name == "nt" else "clear")
                valor = float(input("Digite o valor do depósito: R$ "))
                negocio.deposito(usuario_logado, valor)
                print("Operação finalizada.")
            except ValueError:
                print("Erro: Por favor, insira um valor numérico válido.")
                
        elif opcao == '3':
            try:
                os.system("cls" if os.name == "nt" else "clear")
                valor = float(input("Digite o valor do saque: R$ "))
                negocio.saque(usuario_logado, valor)
                print("Operação finalizada.")
            except ValueError:
                print("Erro: Por favor, insira um valor numérico válido.")
                
        elif opcao == '4':
            os.system("cls" if os.name == "nt" else "clear")
            print("Encerrando o sistema.")
            break
            
        else:
            print("Opção inválida! Tente novamente.")
            
        input("\nPressione Enter para voltar ao menu principal...")
        os.system("cls" if os.name == "nt" else "clear")

if __name__ == "__main__":
    # Limpa a tela
    os.system("cls" if os.name == "nt" else "clear") 
    # Inicia a aplicação chamando o menu inicial
    usuario = menu_inicial()
    # Passa o nome do usuário validado para o menu principal
    menu_principal(usuario)