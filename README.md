# Sistema Bancário

![CI](https://github.com/tatilimongi/DIO_NTTData_Bootcamp_Sistema_Bancario/actions/workflows/ci.yml/badge.svg?event=push)
![Coverage](https://codecov.io/gh/tatilimongi/DIO_NTTData_Bootcamp_Sistema_Bancario/branch/main/graph/badge.svg)
![Last Commit](https://img.shields.io/github/last-commit/tatilimongi/DIO_NTTData_Bootcamp_Sistema_Bancario)

![Commit Activity](https://img.shields.io/github/commit-activity/m/tatilimongi/DIO_NTTData_Bootcamp_Sistema_Bancario)
![Release](https://img.shields.io/github/v/release/tatilimongi/DIO_NTTData_Bootcamp_Sistema_Bancario)
![License](https://img.shields.io/github/license/tatilimongi/DIO_NTTData_Bootcamp_Sistema_Bancario?style=flat-square)

## Descrição

Este projeto é um desafio do bootcamp oferecido pela NTT Data na plataforma DIO, desenvolvido em Python. O objetivo é implementar um sistema bancário simples com funcionalidades de saque, depósito e visualização de extrato.

## Funcionalidades

- **Depositar**: Permite ao usuário depositar valores na conta. Todos os depósitos são armazenados em uma variável e exibidos na operação de extrato.
  
- **Sacar**: Permite ao usuário realizar saques com as seguintes regras:
  - Limite de 3 saques diários.
  - Limite máximo de R$ 500,00 por saque.
  - Se o saldo for insuficiente, uma mensagem informativa é exibida.

- **Extrato**: Exibe um extrato de todas as operações realizadas na conta, incluindo depósitos e saques. 
  - O extrato lista todas as transações realizadas.
  - No final do extrato, é exibido o saldo atual da conta.
  - Se não houver movimentações, uma mensagem "Não foram realizadas movimentações" é exibida.
  
## Regras de Negócio

1. **Limite de Saques**: O usuário pode realizar até 3 saques por dia, com um valor máximo de R$ 500,00 por saque.

2. **Saldo Insuficiente**: Se o saldo for menor que o valor do saque solicitado, o sistema exibirá uma mensagem de erro e o saque não será realizado.

3. **Formato dos Valores**: Todos os valores monetários são exibidos no formato R$ xxx.xx. Exemplo: R$ 1500.45.

## Como Executar

1. Clone este repositório:
    ```bash
    git clone https://github.com/seu-usuario/DIO_NTTData_Bootcamp_Sistema_Bancario.git
    ```

2. Navegue até o diretório do projeto:
    ```bash
    cd DIO_NTTData_Bootcamp_Sistema_Bancario
    ```

3. Execute o script Python:
    ```bash
    python sistema_bancario.py
    ```

## Exemplo de Uso

1. **Depósito**:
    - O usuário pode depositar qualquer valor na conta.
    - Exemplo: Depósito de R$ 200,00.

2. **Saque**:
    - O usuário solicita um saque de R$ 300,00.
    - Se o saldo for suficiente e o limite de saques diários não tiver sido excedido, o saque é realizado.

3. **Extrato**:
    - O sistema exibe todos os depósitos e saques realizados, além do saldo final.
    - Se não houver transações, exibe a mensagem "Não foram realizadas movimentações".

## Tecnologias Utilizadas

- **Python**: Linguagem principal utilizada para o desenvolvimento do sistema.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e enviar pull requests.

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---
