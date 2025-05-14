from conta import Corrente, Poupanca, Automatica


class Agencia:
    def __init__(self, numero):
        self._numero = numero
        self._contas = {}
        self._saldo_total = 0.0

    @property
    def numero(self):
        return self._numero

    def criar_conta(self, tipo, numero, saldo_inicial=0):
        tipos_validos = {
            "corrente": Corrente,
            "poupanca": Poupanca,
            "automatica": Automatica
        }

        tipo = tipo.strip().lower()

        if tipo not in tipos_validos:
            sugestoes = [t for t in tipos_validos.keys()
                         if t.startswith(tipo[:4])]
            sugestao = sugestoes[0] if sugestoes else None
            if sugestao:
                resposta = input(
                    f"Você quis dizer '{sugestao}'? (s/n): ").strip().lower()
                if resposta == "s":
                    tipo = sugestao
                else:
                    pass  # Não faz nada se o usuário disser não
            if tipo not in tipos_validos:  # Verifica novamente após a sugestão
                raise ValueError(f"Tipo de conta '{tipo}' inválido!")

        # Passa o saldo inicial corretamente
        if tipo == "automatica":
            nova_conta = tipos_validos[tipo](
                saldo_inicial)  # Não passa o número
        elif tipo == "corrente":
            taxa_padrao = 0.05  # Defina uma taxa padrão
            nova_conta = tipos_validos[tipo](
                numero, taxa_padrao, saldo_inicial)
        else:
            nova_conta = tipos_validos[tipo](numero, saldo_inicial)
        self._contas[numero] = nova_conta
        self._saldo_total += saldo_inicial
    
    def remover_conta(self, numero):
        if numero in self._contas:
            conta_removida = self._contas.pop(numero)
            self._saldo_total -= conta_removida.saldo
            return True
        return False

    def buscar_conta(self, numero_conta):
        return self._contas.get(numero_conta)
            
    def creditar(self, numero, valor):
        conta = self.buscar_conta(numero)
        if conta:
            conta.saldo = valor
            self._saldo_total += valor

    def debitar(self, numero, valor):
        conta = self.buscar_conta(numero)
        if conta:
            conta.saldo = -valor  # Setter fará o débito
            self._saldo_total -= valor

    def __add__(self, other):
        if isinstance(other, Agencia):
            saldo_total_self = sum(
                conta.saldo for conta in self._contas.values())
            saldo_total_other = sum(
                conta.saldo for conta in other._contas.values())
            return saldo_total_self + saldo_total_other
        raise TypeError("Operação inválida: Soma apenas entre agências.")

    def __str__(self):
        return f"Agencia {self.numero}, Saldo Total: R$ {self._saldo_total:.2f}, Contas: {len(self._contas)}"
    
    def aplicar_juros_poupanca(self, taxa):
        for conta in self._contas.values():
            if isinstance(conta, Poupanca):
                juros = conta.saldo * taxa
                conta.saldo = juros
                self._saldo_total += juros