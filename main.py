
def main():
    print("Digite o tamanho da matriz (n x m): ")
    n = int(input("n: "))
    m = int(input("m: "))

    if n <= 0 or m <= 0:
        print("Tamanho inválido. n e m devem ser maiores que zero.")
        return
    
    matriz = []
    print("Digite os elementos da matriz:")
    for i in range(n):
        linha = []
        for j in range(m):
            elemento = int(input(f"Elemento [{i}][{j}]: "))
            linha.append(elemento)
        matriz.append(linha)
    
    print("Matriz digitada:")
    for linha in matriz:
        print(" ".join(map(str, linha)))

if __name__ == "__main__":
    main()