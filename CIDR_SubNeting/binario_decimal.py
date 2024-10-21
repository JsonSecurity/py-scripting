def binario_a_decimal(binario):
    return int(binario, 2)

while True:
    numero_binario = input("[?] binario: ")
    if numero_binario.lower() == 'exit':
        break
    try:
        numero_decimal = binario_a_decimal(numero_binario)
        print(f"[+]: {numero_decimal}")
    except ValueError:
        print("[!] No valido.")
