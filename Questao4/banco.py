from agencia import Agencia

class Banco:
    def __init__(self, numero):
        self._numero = numero
        self._agencias = []  # Renomear para _agencias para consistência

    @property
    def saldo_total(self):
        return sum(agencia._saldo_total for agencia in self._agencias)

    def cadastrar_agencia(self, agencia):
        if isinstance(agencia, Agencia):
            self._agencias.append(agencia)
        else:
            raise TypeError("Deve ser uma instância de Agencia")

    def remover_agencia(self, numero):
        for i, agencia in enumerate(self._agencias):
            if agencia.numero == numero:
                self._agencias.pop(i)
                return True
        return False

    def __str__(self):
        return f"Banco {self._numero}: Agências = {len(self._agencias)}, Saldo Total = R$ {self.saldo_total:.2f}"