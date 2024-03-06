class P:
    def __init__(self, nome, valor) -> None:
        self.nome = nome
        self.valor = valor

class X(P):
    def __init__(self, nome, valor, agencia) -> None:
        # super().__init__(nome, valor)
        self.nome = nome
        self.valor = valor
        self.agencia = agencia



a = P('caio', 35)
print(a.nome, a.valor)

b = X('fabio', 45, 1475)
print(b.nome, b.valor, b.agencia)
print()
print(a.nome, a.valor)