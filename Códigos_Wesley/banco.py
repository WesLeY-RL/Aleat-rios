saldo = 0
limite = 500
extrato = ""
ns = 0
nd = 0
home = """
[d] depositar
[s] sacar
[e] extrato
[q] sair
"""
print(home)

while True:
    opcao = input("digite sua operação: ")
    if opcao == "d" :
        valor = float(input("digite o valor para depósito: "))
        if valor > 0:
            saldo = saldo + valor
            np = np + 1
        else:
            print("O depósito falhou tente novamente.")
            
    elif opcao == "s":
        valor = float(input("Digite o valor para saque: "))
        if valor > saldo :
            print(" O valor exedeu o saldo")
            
        elif valor > limite: 
            print("O limite para saque é 500 reais.")
        elif ns == 4 :
            print("o limite de números de saques se esgotou.")
        else:
            saldo = saldo - valor
            ns = ns + 1
    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print(f"\nNúmero de depósitos: {nd:.2f}")
        print(f"\nNúmero de saques: {ns:.2f}")
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")
    elif opcao == "q":
        break
    else:
        print("operação não encontrado")
        
            
                