# Implementação de Árvore Rubro-Negra em Python

## Visão Geral
Este projeto em Python implementa uma Árvore Rubro-Negra, um tipo de árvore binária de busca autoequilibrada. Cada nó da árvore possui um bit extra que denota a cor (vermelho ou preto), utilizado para garantir que a árvore permaneça aproximadamente balanceada durante inserções e remoções.

## Funcionalidades
- **Inserção de elementos**: Permite a inserção eficiente de novos nós enquanto mantém o balanceamento da árvore.
- **Remoção de elementos**: Remove nós mantendo as propriedades de autoequilíbrio da árvore.
- **Cálculo da altura da árvore**: Calcula a altura total da árvore para verificar seu balanceamento.
- **Impressão da árvore**: Representação visual da estrutura da árvore e das cores dos nós para fins de debug e ensino.

## Arquivos
- `Node.py`: Define a classe `Node`, responsável por representar cada nó da árvore.
- `RedBlackTree.py`: Contém a classe `RedBlackTree` que implementa as operações da árvore rubro-negra.
- `Main.py`: Demonstra o uso da classe `RedBlackTree` com operações de exemplo.

## Requisitos
- Python 3.8 ou superior.

## Observações
Eu, Matheus Delcor, fiz com o Python pois tenho mais conhecimento sobre com ele do que o Java, pois sou Data Engineer e trabalho somente com Python e SQL, por isso optei por usar o Python.

## Como Executar
Para executar o projeto, navegue até o diretório que contém os arquivos e utilize o seguinte comando:
```bash
python Main.py

Árvore Rubro-Negra/
│
├── Node.py              - Define a classe Node.
├── RedBlackTree.py      - Contém a classe RedBlackTree com todas as operações da árvore.
└── Main.py              - Demonstra o uso da árvore rubro-negra.
