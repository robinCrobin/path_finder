# Trabalho PathFinder
## Descrição do projeto
Este projeto implementa o algoritmo de busca de caminho A*, em Python, para encontrar a rota mais curta entre um ponto inicial "S" e um ponto final "E" dentro de um labirinto 2D. O labirinto pode conter obstáculos (representados pelo número "1") que o algoritmo deve desviar. Este algoritmo combina o custo do caminho já percorrido e uma estimativa da distância até o ponto final para encontrar a solução de modo eficiente.

## Introdução sobre o problema
O problema central é guiar um robô de resgate através de um labirinto, representado por uma matriz 2D. O robô precisa encontrar o menor caminho possível partindo de um ponto inicial "S" até um ponto final "E".

O labirinto é composto por:
- 0: células livres, por onde é permitido o robô passar.
- 1: obstáculos, onde não é permitido o robô passar.
- S: ponto inicial.
- E: ponto final.

O robô só pode se mover nas direções adjacentes, desde que ela não seja um obstáculo, ou seja, tenha o valor 1, e cada movimento tem um custo de 1. O desafio é encontrar a rota ótima (mais curta) de forma eficiente, o que é solucionado pelo algoritmo A*.

## Instruções para executar o projeto
### Pré-requisitos:
Ter o Python instalado. Nenhuma biblioteca externa é necessária, pois o projeto utiliza apenas módulos nativos do Python.

### Execução:
1. Clone este repositório.
2. Abra seu terminal e navegue até a pasta do projeto.
3. Execute o arquivo `main.py`:

    No Windows execute:
   
    ```python main.py```
    
    No macOS ou Linux execute:
   
    ```python3 main.py```

## Funcionamento do Algoritmo A*
O A* é um algoritmo de busca heurístico muito eficiente. Ele encontra o caminho mais curto ao combinar o custo real para chegar a um ponto com uma estimativa inteligente do custo restante. Assim, para decidir qual célula explorar em seguida, ele calcula uma pontuação f(n) para cada célula (nó) candidata.

Essa pontuação é a soma de dois valores: `f(n) = g(n) + h(n)`, em que g(n) é o custo real do caminho percorrido desde o início ('S') até o nó atual (n). Neste caso, como cada passo custa 1, g(n) é o número de passos dados para chegar até o nó atual; h(n) é a estimativa de custo do nó atual (n) até o destino ('E'). Neste projeto, foi usado a Distância de Manhattan, que é indicada para o caso em que não se pode mover nas diagonais. E f(n) é o custo total, ou seja, a pontuação final daquele nó.

O algoritmo A* usa uma fila de prioridade para manter uma lista de nós a serem explorados, e ele sempre escolhe explorar o nó que tem o menor custo "f". Essa combinação garante que o A* não perca tempo explorando caminhos ruins (graças à heurística h) e que, ao mesmo tempo, encontre o caminho mais curto (graças ao custo real g).

## Exemplo de entrada e saída com caminho encontrado
1. Entrada:

    Matriz digitada:
   
    <img width="77" height="92" alt="image" src="https://github.com/user-attachments/assets/d15bc9bc-cd0f-4efb-93c6-d3c0474432f2" />


3. Saída:
   
    ✅ Caminho encontrado! Tamanho: 7
    
    Caminho: (0,0) → (1,0) → (1,1) → (2,1) → (3,1) → (3,2) → (3,3)
    
    Matriz com caminho marcado:
    
   <img width="81" height="90" alt="image" src="https://github.com/user-attachments/assets/6d7ab9f9-aed7-4de6-8215-56d595242dbe" />


## Exemplo de entrada e saída sem caminho
1. Entrada:
   
    Matriz digitada:

    <img width="62" height="72" alt="image" src="https://github.com/user-attachments/assets/652ada6e-04c3-49aa-baa1-68df7a729b86" />


3. Saída:
   
    ❌ Nenhum caminho encontrado!
