
def decimal_a_binario(decimal):
    return bin(int(decimal))[2:]

while True:
    numero_decimal = input("\n[?] Decimal: ")
    try:
        numero_binario = decimal_a_binario(numero_decimal)
        print(f"[+]: {numero_binario}")
        print("[+] len:", len(numero_binario))
    except ValueError:
        print("\n[!] No válido.")
