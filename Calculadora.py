menu = int(input("0. Sair;"
                 "1. Somar;"
                 "2. Subtrair;"
                 "3. Multiplicar;"
                 "4. Dividir;"
                 "5. Potencia;"
                 "6. Raiz quadrada inteira;"
                 "7. MMC;"
                 "8. MDC;"
                 "9. Fatorial;"
                 "10. Nominal;"))
while menu != 0 or menu < 11:
    match menu:
        case 1:
            v1 = input("Digite um numero: ")
            v1 = float(v1.replace(",", "."))
            v2 = input("Digite outro numero: ")
            v2 = float(v2.replace(",", "."))
            v3 = v1 + v2
            print(f"valor final: {v3:.3f}")
            menu = int(input("0. Sair;"
                             "1. Somar;"
                             "2. Subtrair;"
                             "3. Multiplicar;"
                             "4. Dividir;"
                             "5. Potencia;"
                             "6. Raiz quadrada inteira;"
                             "7. MMC;"
                             "8. MDC;"
                             "9. Fatorial;"
                             "10. Nominal;"))
            break
