def exibir_menu_principal():
    print("""
          ************* MENU *************

          1 - DEPÓSITO
          2 - SAQUE
          3 - EXTRATO
          4 - SAIR

          ********************************
          """)

def exibir_menu_deposito():
    print("""
          ************* MENU *************

          1 - REALIZAR DEPÓSITO
          2 - VOLTAR

          ********************************
          """)
    
def exibir_menu_saque():
    print("""
          ************* MENU *************

          1 - REALIZAR SAQUE
          2 - VOLTAR

          ********************************
          """)

def realizar_deposito(saldo, depositos):
    deposito = float(input("Informe o valor do depósito: "))
    if deposito <= 0:
        print(f"Valor inválido.")
    else:
        saldo += deposito
        depositos.append(deposito)
        print(f"Depósito de R$ {deposito:.2f} realizado com sucesso.")
    return saldo

def realizar_saque(LIMITE_SAQUE, saldo, saque_diario, saques):
    if saque_diario >= LIMITE_SAQUE:
        print("Limite de saques diários atingido.")
        return saldo, saque_diario

    saque = float(input("Informe o valor do saque: "))
    if saldo < saque:
        print("Saldo insuficiente.")
        return saldo, saque_diario

    while saque > 500:
        print("Limite de R$ 500.00 por saque.")
        saque = float(input("Informe o valor do saque: "))

    if saque <= 0:
        print("Valor inválido.")
    else:
        saldo -= saque
        saque_diario += 1
        saques.append(saque)
        print(f"Saque de R$ {saque:.2f} realizado com sucesso.")
    return saldo, saque_diario

def exibir_extrato(saldo, saques, depositos):
    print("\n************* EXTRATO *************")
    if not depositos and not saques:
        print("         Não foram realizadas movimentações.")
    else:
        for i, deposito in enumerate(depositos, 1):
            print(f"        {i}º depósito: R$ {deposito:.2f}")

        for i, saque in enumerate(saques, 1):
            print(f"        {i}º saque: R$ {saque:.2f}")
    
    print(f"\n-----------------------------------\n        Saldo: R$ {saldo:.2f}\n")

def main():
    saldo = 1200
    saque_diario = 0
    depositos = []
    saques = []
    LIMITE_SAQUE = 3

    while True:
        exibir_menu_principal()
        opcao = int(input("Informe a operação desejada: "))

        if opcao == 1:
            exibir_menu_deposito()
            if int(input("Deseja realizar um depósito? ")) == 1:
                saldo = realizar_deposito(saldo, depositos)

        elif opcao == 2:
            exibir_menu_saque()
            if int(input("Deseja realizar um saque? ")) == 1:
                saldo, saque_diario = realizar_saque(LIMITE_SAQUE, saldo, saque_diario, saques)

        elif opcao == 3:
            exibir_extrato(saldo, saques, depositos)

        elif opcao == 4:
            print("\n***********************************\nFim do programa.\n***********************************")
            break

        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
