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
