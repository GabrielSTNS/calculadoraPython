numero1 = input("Digite um número: ")
numero2 = input("Digite outro número: ")
conta = input("Informe o tipo de conta (+, -, *, /, **): ")

conta_numero_1 = int(numero1)
conta_numero_2 = int(numero2)

if conta == "+":
    linha_1 = (f"A soma de {conta_numero_1:.2f} com {conta_numero_2:.2f} é: ")
    linha_2 = conta_numero_1 + conta_numero_2
    print(linha_1)
    print(f"{linha_2:.2f}")

if conta == "-":
    linha_1 = (f"A subtração de {conta_numero_1:.2f} com {conta_numero_2:.2f} é: ")
    linha_2 = conta_numero_1 - conta_numero_2
    print(linha_1)
    print(f"{linha_2:.2f}")
elif conta == "*":
    linha_1 = (f"A multiplicação de {conta_numero_1:.2f} com {conta_numero_2:.2f} é: ")
    linha_2 = conta_numero_1 * conta_numero_2
    print(linha_1)
    print(f"{linha_2:.2f}")
elif conta == "/":
    linha_1 = (f"A divisão de {conta_numero_1:.2f} com {conta_numero_2:.2f} é: ")
    linha_2 = conta_numero_1 / conta_numero_2
    print(linha_1)
    print(f"{linha_2:.2f}")
elif conta == "**":
    linha_1 = (f"A exponenciação de {conta_numero_1:.2f} com {conta_numero_2:.2f} é: ")
    linha_2 = conta_numero_1**conta_numero_2
    print(linha_1)
    print(f"{linha_2:.2f}")
