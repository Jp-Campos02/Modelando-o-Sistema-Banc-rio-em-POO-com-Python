import textwrap

def menu():
    opcoes = """
    ================ MENU ================
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nc] Nova conta
    [lc] Listar contas
    [nu] Novo usuário
    [q] Sair
    => """
    return input(textwrap.dedent(opcoes))

def depositar(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito: R$ {valor:.2f}")
        print("\n=== Depósito realizado com sucesso! ===")
    else:
        print("\n@@@ Operação falhou! Valor inválido. @@@")
    return saldo

def sacar(saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor <= 0:
        print("\n@@@ Operação falhou! Valor inválido. @@@")
    elif valor > saldo:
        print("\n@@@ Saldo insuficiente. @@@")
    elif valor > limite:
        print("\n@@@ Valor do saque excede o limite. @@@")
    elif numero_saques >= limite_saques:
        print("\n@@@ Limite de saques diários atingido. @@@")
    else:
        saldo -= valor
        extrato.append(f"Saque: R$ {valor:.2f}")
        numero_saques += 1
        print("\n=== Saque realizado com sucesso! ===")
    return saldo, numero_saques

def exibir_extrato(saldo, extrato):
    print("\n================ EXTRATO ================")
    print("\n".join(extrato) if extrato else "Nenhuma movimentação realizada.")
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    if any(usuario['cpf'] == cpf for usuario in usuarios):
        print("\n@@@ CPF já cadastrado! @@@")
        return
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/UF): ")
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("\n=== Usuário criado com sucesso! ===")

def criar_conta(agencia, numero_conta, usuarios, contas):
    cpf = input("Informe o CPF do titular: ")
    usuario = next((u for u in usuarios if u['cpf'] == cpf), None)
    if usuario:
        conta = {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
        contas.append(conta)
        print("\n=== Conta criada com sucesso! ===")
    else:
        print("\n@@@ Usuário não encontrado. @@@")

def listar_contas(contas):
    for conta in contas:
        print("=" * 40)
        print(f"Agência: {conta['agencia']}\nConta: {conta['numero_conta']}\nTitular: {conta['usuario']['nome']}")
        print("=" * 40)

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    saldo = 0
    limite = 500
    extrato = []
    numero_saques = 0
    usuarios = []
    contas = []
    while True:
        opcao = menu()
        if opcao == "d":
            saldo = depositar(saldo, float(input("Valor do depósito: ")), extrato)
        elif opcao == "s":
            saldo, numero_saques = sacar(saldo, float(input("Valor do saque: ")), extrato, limite, numero_saques, LIMITE_SAQUES)
        elif opcao == "e":
            exibir_extrato(saldo, extrato)
        elif opcao == "nu":
            criar_usuario(usuarios)
        elif opcao == "nc":
            criar_conta(AGENCIA, len(contas) + 1, usuarios, contas)
        elif opcao == "lc":
            listar_contas(contas)
        elif opcao == "q":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
