import pytest
from PathFinder import PathFinder

def test_um_caminho():
    matriz = [
        ['S','0','0','0','0'],
        ['1','1','1','1','0'],
        ['1','1','1','1','0'],
        ['1','1','1','1', 'E']
    ]
    coords = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4),
              (1, 4), (2, 4), (3, 4)]
              
    finder = PathFinder(matriz)
    path = finder.find_path((0, 0), (3, 4))

    assert path is not None, "Deveria encontrar um caminho"
    assert path == coords
    print("Sucesso teste de Matriz onde há um caminho possível")

def test_dois_caminhos():
    matriz = [
        ['S','0','0','0','0'],
        ['0','1','1','1','0'],
        ['0','0','0','1','0'],
        ['1','1','0','1', '0'],
        ['0','0','0','1','0'],
        ['0','1','1','1','0'],
        ['0','0','0','0', 'E']
    ]
    coords = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4),
              (1, 4), (2, 4), (3, 4), (4, 4), (5, 4), (6, 4)]
    finder = PathFinder(matriz)
    path = finder.find_path((0, 0), (6, 4))

    assert path is not None, "Deveria encontrar ao menos um dos caminhos possíveis"
    assert path == coords
    print("Sucesso teste de Matriz onde há dois caminhos possíveis")

def test_sem_caminho():
    matriz = [
        ['S','1','1'],
        ['1','1','1'],
        ['1','1', 'E']
    ]
    finder = PathFinder(matriz)
    path = finder.find_path((0, 0), (2, 2))

    assert path is None, "Não deveria haver caminho"
    print("Sucesso teste de Matriz onde não há caminhos possíveis")

if __name__ == "__main__":
    test_um_caminho()
    test_dois_caminhos()
    test_sem_caminho()