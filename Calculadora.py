menu = int(input("0. Sair;\n"
                 "1. Somar;\n"
                 "2. Subtrair;\n"
                 "3. Multiplicar;\n"
                 "4. Dividir;\n"
                 "5. Potencia;\n"
                 "6. Raiz quadrada inteira;\n"
                 "7. MMC;\n"
                 "8. MDC;\n"
                 "9. Fatorial;\n"
                 "10. Nominal;\n"))
while menu != 0 and menu <= 11:
    match menu:
        case 1:
            v1 = input("Digite um numero: ")
            v1 = float(v1.replace(",", "."))
            v2 = input("Digite outro numero: ")
            v2 = float(v2.replace(",", "."))
            v3 = v1 + v2
            print(f"valor final: {v3:.3f}")
            menu = int(input("0. Sair;\n"
                             "1. Somar;\n"
                             "2. Subtrair;\n"
                             "3. Multiplicar;\n"
                             "4. Dividir;\n"
                             "5. Potencia;\n"
                             "6. Raiz quadrada inteira;\n"
                             "7. MMC;\n"
                             "8. MDC;\n"
                             "9. Fatorial;\n"
                             "10. Nominal;\n"))
        case 2:
            v1 = input("Digite um numero: ")
            v1 = float(v1.replace(",", "."))
            v2 = input("Digite outro numero: ")
            v2 = float(v2.replace(",", "."))
            v3 = v1 - v2
            print(f"valor final: {v3:.3f}")
            menu = int(input("0. Sair;\n"
                             "1. Somar;\n"
                             "2. Subtrair;\n"
                             "3. Multiplicar;\n"
                             "4. Dividir;\n"
                             "5. Potencia;\n"
                             "6. Raiz quadrada inteira;\n"
                             "7. MMC;\n"
                             "8. MDC;\n"
                             "9. Fatorial;\n"
                             "10. Nominal;\n"))
        case 3:
            v1 = input("Digite um numero: ")
            v1 = float(v1.replace(",", "."))
            v2 = input("Digite outro numero: ")
            v2 = float(v2.replace(",", "."))
            v3 = v1 * v2
            print(f"valor final: {v3:.3f}")
            menu = int(input("0. Sair;\n"
                             "1. Somar;\n"
                             "2. Subtrair;\n"
                             "3. Multiplicar;\n"
                             "4. Dividir;\n"
                             "5. Potencia;\n"
                             "6. Raiz quadrada inteira;\n"
                             "7. MMC;\n"
                             "8. MDC;\n"
                             "9. Fatorial;\n"
                             "10. Nominal;\n"))
        case 4:
            v1 = input("Digite um numero: ")
            v1 = float(v1.replace(",", "."))
            v2 = input("Digite outro numero: ")
            v2 = float(v2.replace(",", "."))
            v3 = v1 / v2
            print(f"valor final: {v3:.3f}")
            menu = int(input("0. Sair;\n"
                             "1. Somar;\n"
                             "2. Subtrair;\n"
                             "3. Multiplicar;\n"
                             "4. Dividir;\n"
                             "5. Potencia;\n"
                             "6. Raiz quadrada inteira;\n"
                             "7. MMC;\n"
                             "8. MDC;\n"
                             "9. Fatorial;\n"
                             "10. Nominal;\n"))
        case 5:
            v1 = input("Digite um numero: ")
            v1 = float(v1.replace(",", "."))
            v2 = input("Digite outro numero: ")
            v2 = float(v2.replace(",", "."))
            v3 = v1 ** v2
            print(f"valor final: {v3:.3f}")
            menu = int(input("0. Sair;\n"
                             "1. Somar;\n"
                             "2. Subtrair;\n"
                             "3. Multiplicar;\n"
                             "4. Dividir;\n"
                             "5. Potencia;\n"
                             "6. Raiz quadrada inteira;\n"
                             "7. MMC;\n"
                             "8. MDC;\n"
                             "9. Fatorial;\n"
                             "10. Nominal;\n"))
        case 6:
            v1 = int(input("Digite um numero: "))
            v2 = v1 ** 0.5
            print(f"valor final: {v2:.3f}")
            menu = int(input("0. Sair;\n"
                             "1. Somar;\n"
                             "2. Subtrair;\n"
                             "3. Multiplicar;\n"
                             "4. Dividir;\n"
                             "5. Potencia;\n"
                             "6. Raiz quadrada inteira;\n"
                             "7. MMC;\n"
                             "8. MDC;\n"
                             "9. Fatorial;\n"
                             "10. Nominal;\n"))
        case 7:
            v1 = input("Digite um numero: ")
            v1 = float(v1.replace(",", "."))
            v2 = input("Digite outro numero: ")
            v2 = float(v2.replace(",", "."))
            v3 = v1 * v2
            print(f"valor final: {v3:.3f}")
            menu = int(input("0. Sair;\n"
                             "1. Somar;\n"
                             "2. Subtrair;\n"
                             "3. Multiplicar;\n"
                             "4. Dividir;\n"
                             "5. Potencia;\n"
                             "6. Raiz quadrada inteira;\n"
                             "7. MMC;\n"
                             "8. MDC;\n"
                             "9. Fatorial;\n"
                             "10. Nominal;\n"))
        case 8:
            v1 = input("Digite um numero: ")
            v1 = float(v1.replace(",", "."))
            v2 = input("Digite outro numero: ")
            v2 = float(v2.replace(",", "."))
            v3 = v1 // v2
            print(f"valor final: {v3:.3f}")
            menu = int(input("0. Sair;\n"
                             "1. Somar;\n"
                             "2. Subtrair;\n"
                             "3. Multiplicar;\n"
                             "4. Dividir;\n"
                             "5. Potencia;\n"
                             "6. Raiz quadrada inteira;\n"
                             "7. MMC;\n"
                             "8. MDC;\n"
                             "9. Fatorial;\n"
                             "10. Nominal;\n"))
        case 9:
            v1 = int(input("Digite um numero: "))
            v2 = 1
            for i in v1:
                v2 = v2 * v1
                v1 = v1 - 1
            print(f"valor final: {v2:.3f}")
            menu = int(input("0. Sair;\n"
                             "1. Somar;\n"
                             "2. Subtrair;\n"
                             "3. Multiplicar;\n"
                             "4. Dividir;\n"
                             "5. Potencia;\n"
                             "6. Raiz quadrada inteira;\n"
                             "7. MMC;\n"
                             "8. MDC;\n"
                             "9. Fatorial;\n"
                             "10. Nominal;\n"))
        case 10:
            v1 = int(input("Digite um numero: "))
            v1 = float(v1.replace(",", "."))
            v2 = 1
            for i in v1:
                v2 = v2 + v1
                v1 -= v1
            print(f"valor final: {v2:.3f}")
            menu = int(input("0. Sair;\n"
                             "1. Somar;\n"
                             "2. Subtrair;\n"
                             "3. Multiplicar;\n"
                             "4. Dividir;\n"
                             "5. Potencia;\n"
                             "6. Raiz quadrada inteira;\n"
                             "7. MMC;\n"
                             "8. MDC;\n"
                             "9. Fatorial;\n"
                             "10. Nominal;\n"))
print("Obrigado por usar está calculadora!")