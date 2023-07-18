menu = '''

[s] Sacar
[d] Depositar
[e] Extrato
[q] Sair

=> '''

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d": 
        valor = float(input("Informe o valor do deposito: "))

        if valor > 0 :
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou, o valor informado é invalido!")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo 

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou, Você não tem saldo suficiente")

        elif excedeu_limite:
            print("Operação falhou, o valor do saque passa o limite maximo de saque!")

        elif excedeu_saques:
            print("Operação falhou, quantidade de saques já bateu o limite!")
        
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R${valor:.2f}\n"
            numero_saques += 1

        else: 
            print("Operação falhou, o Valor informado é invalido.")

    elif opcao == "e":
        print("\n===========EXTRATO===========")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\n Saldo: R$ {saldo:.2f}")
        print("===============================")

    elif opcao == "q":
        break

    else:
        print("Operação invalida, por favor selecione novamente o serviço desejado!s")