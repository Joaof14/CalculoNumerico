## Descrição

Este projeto implementa métodos numéricos para encontrar zeros de funções em Python, utilizando interface gráfica com Tkinter. Os métodos disponíveis são:

- Bissecção
- Falsa Posição
- Ponto Fixo
- Secante
- Newton

## Estrutura

- `Calc.py`: Implementação dos métodos numéricos e lógica principal.
- `C_N.py`: Interface gráfica (Tkinter) para entrada de dados e seleção de métodos.
- `resolução.txt`: Arquivo gerado com o histórico das iterações e resultados.
- `testes/`: Pasta com exemplos de funções, resoluções e gráficos gerados.

## Requisitos

- Python 3.x
- Bibliotecas: `sympy`, `tkinter`, `matplotlib` (backend para gráficos)

## Como usar

1. Execute o arquivo `C_N.py` para abrir a interface gráfica.
2. Preencha a função, intervalo, precisão e selecione o método desejado.
3. Para métodos que exigem chute inicial ou função de iteração, preencha os campos correspondentes.
4. Clique em "Gráfico" para visualizar o gráfico da função.
5. O resultado será exibido na interface e salvo em `resolução.txt`.

## Exemplos

Veja exemplos de uso e resoluções na pasta [`testes/`](CalcN1/testes/).

## Autor

Projeto acadêmico de
