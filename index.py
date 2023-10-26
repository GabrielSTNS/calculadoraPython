numero1 = float(input("Digite um número: "))
numero2 = float(input("Digite outro número: "))
conta = input("Informe o tipo de conta (+, -, *, /, **): ")

if conta == "+":
    linha_1 = (f"A soma de {numero1:.2f} com {numero2:.2f} é: ")
    linha_2 = numero1 + numero2
    print(linha_1)
    print(f"{linha_2:.2f}")

if conta == "-":
    linha_1 = (f"A subtração de {numero1:.2f} com {numero2:.2f} é: ")
    linha_2 = numero1 - numero2
    print(linha_1)
    print(f"{linha_2:.2f}")

if conta == "*":
    linha_1 = (f"A multiplicação de {numero1:.2f} com {numero2:.2f} é: ")
    linha_2 = numero1 * numero2
    print(linha_1)
    print(f"{linha_2:.2f}")

if conta == "/":
    linha_1 = (f"A divisão de {numero1:.2f} com {numero2:.2f} é: ")
    linha_2 = numero1 / numero2
    print(linha_1)
    print(f"{linha_2:.2f}")

if conta == "**":
    linha_1 = (f"A exponenciação de {numero1:.2f} com {numero2:.2f} é: ")
    linha_2 = numero1**numero2
    print(linha_1)
    print(f"{linha_2:.2f}")
