"""
Tuplas e sets -> juntos com listas e dicionários são, os tipos de dados em python
que são tratados como sequências
"""

from random import randint

if __name__ == "__main__":

    tupla1 = (1, 2, 3)
    print(tupla1)

    # Tuplas são bem parecidas com as listas,
    # a diferença entre elas mais significante é que as tuplas não permitem
    # alteração dos seus valores (imutável). A linha abaixo causará um erro.
    # tupla1[2] = 10

    # Caso seja muito necessário alterar o valor de uma tupla,
    # podemos convertê-la para lista, fazer a alteração e converter novamente para tupla.
    lista1 = list(tupla1)
    lista1[2] = 10
    tupla1 = tuple(lista1)
    print(tupla1)

    # sets(conjuntos) são outros tipos de sequência em Python.
    # Podem ser entendidos como representação dos conjuntos matemáticos na linguagem.
    # Um detalhe importante é que os sets não permitem valores repetidos.

    # Criar lista de 100 itens, com valores randômicos entre 1 e 20
    lista_numeros = []
    for _ in range(100):
        lista_numeros.append(randint(1, 20))

    print(lista_numeros)
    lista_numeros.clear()

    # Podemos fazer a mesma coisa utilizando list comprehension
    lista_numeros = [randint(1, 20) for _ in range(100)]
    print(lista_numeros)

    # Devemos remover os itens repetidos da lista
    lista_numeros = set(lista_numeros)
    print(lista_numeros)

    # Utilizar o lista_numeros.sort() também



