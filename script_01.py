"""
Dicionários
Dicionários são estruturas que armazenam dados no formato chave: valor
Dicionários são estruturas iteráveis, indexáveis, modificáveis e que não permitem
chaves duplicadas
"""

if __name__ == "__main__":

    # Podemos criar dicionários de 2 maneiras
    cliente1 = {
        # chave: valor
        # key: value
        "nome": "Maria",
        "idade": 20,
        "sexo": "F",
        "setor": "TI",
        "cargo": "Especialista"
    }

    cliente2 = dict(
        nome="João",
        idade=30,
        sexo="M",
        setor="TI",
        cargo="Especialista"
    )

    print(cliente1)
    print(cliente2)

    # Como dicionários são iteráveis, podemos acessar os seus itens de forma sequencial
    # dentro de um laço for

    # Por padrão, os nomes das chaves são mostrados como itens do dicionário
    # É a mesma coisa que fazer for item in cliente2.keys()
    for item in cliente2:
        print(item)

    print('-'*30)
    # Se quisermos mostrar os valores em um dicionário, utilizamos o método .values()
    for value in cliente2.values():
        print(value)

    print('-'*30)
    # Se quisermos mostrar tanto a chave quanto o valor, utilizamos o método .items()
    for chave, valor in cliente2.items():
        print(f"{chave} = {valor}")

    print(f"{'-'*5} acessando e alterando itens e adicionando itens de um dicionário {'-'*5}")

    # Para acessar um valor, podemos utilizar diretamente o nome da chave
    # ou através do método get().
    # A chave "nome" deverá existir no dicionário.
    # Se não existir, o programa vai gerar uma exceção do tipo KeyError.
    print(cliente2["nome"])

    # Utilizando o método get, se a chave não existir, retorna "none". Opcionalmente,
    # podemos definir um valor de retorno, caso a chave não exista.
    print(cliente2.get("idade")) # Retorna o valor '30'
    print(cliente2.get("historico")) # Retorna 'none'
    print(cliente2.get("qi", "a chave qi não existe")) # Retorna a frase

    cliente2["idade"] = 28
    # O método update recebe um dicionário como argumento.
    # Se a chave passada existir, o valor do dicionário é alterado.
    # Se não existir, essa nova chave é criada no dicionário.
    cliente2.update({
        "cargo": "Pleno",
        "promocao": True
    })
    print(cliente2)

    print(f"{'-' * 5} remover itens de um dicionário {'-' * 5}")

    # Podemos remover itens de um dicionário de 4 maneiras distinas.

    # 1- Método pop()
    valor_removido = cliente2.pop("promocao")
    print(f"Valor removido: {valor_removido}")
    print(cliente2)

    # 2- Método popitem()
    valor_removido = cliente2.popitem()
    print(f"Valor removido: {valor_removido}")
    print(cliente2)

    # 3- Método del (remove objetos)
    del cliente2["sexo"]
    print(cliente2)

    # 4- O método clear()
    cliente2.clear()
    print(cliente2)

    # Caso queira copiar um dicionário em outro, devemos lembrar que
    # eles possuem o mesmo detalhe das listas: são referências a valores na memória.
    # Assim como nas listas, devemos utilizar o método copy()
    # para copiar os valores de um dicionário em outro.
    cliente3 = cliente2.copy()
