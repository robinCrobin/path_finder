
def main():
    print("Digite o tamanho da matriz (n x m): ")
    n = int(input("n: "))
    m = int(input("m: "))

    if n <= 0 or m <= 0:
        print("Tamanho inválido. n e m devem ser maiores que zero.")
        return
    
    matriz = []
    print("Digite os elementos da matriz:")
    valid = {"O", "1", "S", "E"}
    for i in range(n):
        linha = []
        for j in range(m):
            while True:
                valor = input(f"Elemento [{i}][{j}] (O, 1, S ou E): ").strip().upper()
                if valor in valid:
                    linha.append(valor)
                    break
                else:
                    print("Valor inválido. Digite apenas: O, 1, S ou E.")
        matriz.append(linha)
    
    print("Matriz digitada:")
    for linha in matriz:
        print(" ".join(linha))

if __name__ == "__main__":
    main()