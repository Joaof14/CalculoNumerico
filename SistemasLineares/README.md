# Sistemas Lineares - CalcN2

Este projeto implementa métodos numéricos para resolução de sistemas lineares e interpolação em Python.

## Métodos Implementados

### Resolução de Sistemas Lineares
- Eliminação de Gauss
- Fatoração LU
- Gauss-Seidel
- Gauss-Jacobi

### Interpolação
- Interpolação de Lagrange
- Interpolação de Newton
- Interpolação por sistema linear

## Estrutura do Projeto

- `GUI.py`: Interface gráfica para entrada de dados e seleção de métodos.
- `Metodos.py`: Implementação dos algoritmos numéricos.
- `TesteSistLinear.txt`: Exemplos de sistemas testados.
- `resultados/`: Resultados das resoluções.
- `Resultados Testes/`: Resultados dos testes dos métodos.

## Requisitos

- Python 3.x
- Bibliotecas: `numpy`, `sympy`, `warnings`, `matplotlib`

## Como Usar

1. Execute o arquivo `GUI.py` para abrir a interface gráfica.
2. Insira os dados do sistema linear ou pontos para interpolação. 
3. Selecione o método desejado e execute.
4. Os resultados serão exibidos na interface e salvos na pasta `resultados/`.

## Exemplos

Veja exemplos de sistemas e resoluções em [`TesteSistLinear.txt`](TesteSistLinear.txt) e na pasta [`Resultados Testes/`](Resultados%20Testes/).

## Autor

Projeto acadêmico
