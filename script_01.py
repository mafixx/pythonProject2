"""
Dicionários -> São estruturas que armazenam dados no formato chave: valor

Assim como as listas, dicionários são estruturas iteráveis, indexáveis, modificáveis
e que não permitem chaves duplicadas.

"""

if __name__ == "__main__":
    # Podemos criar dicionários de duas formas:
    cliente1 = {
        "nome": "Maria",
        "idade": 20}

    # Segunda forma:
    cliente2 = dict(
        nome="João",
        idade=30,
        sexo="M",
        setor="TI",
        cargo="Sênior"
        )

    print(cliente1)
    print(cliente2)

    # Como dicionários são iteráveis, podemos acessar os seus itens
    # de forma sequencial, dentro de um laço for.

    # Por padrão, os nomes das chaves são mostrados como itens do dicionário.
    # É a mesma coisa que fazer for item in cliente2.keys()
    for item in cliente2.keys():
        print(item)

    # Se quisermos mostrar os valores em um dicionário, utilizamos o método .values().
    for value in cliente2.values():
        print(value)
