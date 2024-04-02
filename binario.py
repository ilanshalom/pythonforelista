def binario_para_decimal(binario):
    decimal = 0
   
    binario = binario[::-1]
 
    for i in range(len(binario)):
        if binario[i] == '1':
            decimal += 2 ** i
    return decimal

def main():
    
    binario = input("Digite um número binário: ")
    
    
    decimal = binario_para_decimal(binario)
    

    print(f"O número binário {binario} é igual a {decimal} na base decimal.")


main()
