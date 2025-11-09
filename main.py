from PathFinder import PathFinder


def main():
    print("Digite o tamanho da matriz (n x m): ")
    n = int(input("n: "))
    m = int(input("m: "))

    if n <= 0 or m <= 0:
        print("Tamanho inválido. n e m devem ser maiores que zero.")
        return
    
    matriz = []
    print("Digite os elementos da matriz:")
    valid = {"0", "1", "S", "E"}
    while True:
        matriz = []
        print("Digite os elementos da matriz:")
        for i in range(n):
            linha = []
            for j in range(m):
                while True:
                    valor = input(f"Elemento [{i}][{j}] (0, 1, S ou E): ").strip().upper()
                    if valor in valid:
                        linha.append(valor)
                        break
                    else:
                        print("Valor inválido. Digite apenas: 0, 1, S ou E.")
            matriz.append(linha)

        s_count = sum(1 for linha in matriz for cel in linha if cel == "S")
        e_count = sum(1 for linha in matriz for cel in linha if cel == "E")

        if s_count == 1 and e_count == 1:
            break
        print(f"Matriz inválida: encontrada(s) S={s_count}, E={e_count}. A matriz deve conter exatamente 1 S e 1 E. Digite a nova matriz.\n")

    print("Matriz digitada:")
    for linha in matriz:
        print(" ".join(linha))
    
    start_pos = None
    end_pos = None
    for i in range(n):
        for j in range(m):
            if matriz[i][j] == 'S':
                start_pos = (i, j)
            elif matriz[i][j] == 'E':
                end_pos = (i, j)
    
    finder = PathFinder(matriz)
    path = finder.find_path(start_pos, end_pos)
    
    # Exibe o resultado
    if path:
        print(f"\n✅ Caminho encontrado! Tamanho: {len(path)}")
        print("Caminho:", " → ".join([f"({x},{y})" for x, y in path]))
        
        # Mostra matriz com o caminho marcado
        matriz_visual = [linha[:] for linha in matriz]  # cópia
        for i, (x, y) in enumerate(path):
            if matriz_visual[x][y] not in ['S', 'E']:
                matriz_visual[x][y] = '*'
        
        print("\nMatriz com caminho marcado:")
        for linha in matriz_visual:
            print(" ".join(linha))
    else:
        print("\n❌ Nenhum caminho encontrado!")

if __name__ == "__main__":
    main()