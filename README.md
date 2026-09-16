# Sistema Bancário - Arquitetura em Camadas

## 📄 Sobre o Projeto

Este é um sistema bancário simples desenvolvido em Python, executado via terminal de linha de comando (CLI). O projeto foi construído aplicando os conceitos de **Arquitetura em Três Camadas**, visando manter o código organizado, modular, escalável e de fácil manutenção. O armazenamento das informações bancárias é realizado em memória durante a execução do programa.

### Estrutura das Camadas

* **`main.py` (Camada de Apresentação):** Responsável por exibir os menus interativos, processar os inputs do usuário e apresentar os resultados das operações.
* **`negocio.py` (Camada de Regras de Negócio):** Contém toda a lógica de validação do sistema, garantindo a integridade das transações (ex: bloqueio de saque com saldo insuficiente, depósitos negativos, etc.).
* **`dados.py` (Camada de Dados):** Gerencia o armazenamento e a manipulação direta dos dados estruturados em memória (Dicionários), isolando essa responsabilidade do restante da aplicação.

## ⚙️ Pré-requisitos

Para rodar este projeto, você precisará apenas do interpretador Python instalado em sua máquina:
* [Python 3.x](https://www.python.org/downloads/) 

## 🚀 Como Executar

1. Clone o repositório para o seu ambiente local ou faça o download dos arquivos.
2. Abra o terminal (ou prompt de comando) e navegue até a raiz do diretório do projeto.
3. Inicie o sistema executando o arquivo principal:

```bash
python main.py
```
*(Nota: Dependendo da configuração do seu sistema operacional, pode ser necessário usar o comando `python3 main.py`)*

## 👥 Equipe de Desenvolvimento (Alunos)

Este projeto foi desenvolvido como parte de uma avaliação acadêmica pelos seguintes alunos:

* Davi Monteiro Cardoso                RA: 1262524674
* Felippe Martan Berto de Miranda      RA: 1262523044
* Vitor dos Santos Ferreira            RA: 1262523019
* Diego Gomes de Araujo                RA: 1262526385
